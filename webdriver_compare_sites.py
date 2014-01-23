#!/usr/bin/env python
"""
Script using selenium/webdriver (pip install selenium) to automate
using two Firefox windows to compare identical paths on two different
domains - specifically, to compare your local Pelican paths running
on localhost to the WordPress installation they came from.

This uses a dict that's written on every change (so you can safely
Ctrl+C) to automate keeping track of which paths have been seen,
and which need further review.

"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import remote

import anyjson

import time
import os
import optparse
import sys
import re

# help when running through screen
if 'DISPLAY' not in os.environ:
    os.environ['DISPLAY'] = ":0"

def loadPages(browser, windows, one, two):
    """
    load pages, one in each window
    """
    browser.switch_to_window(windows[0])
    browser.get(one)
    browser.switch_to_window(windows[1])
    browser.get(two)
    return True

def check_path(path, pdict, old, new, browser, windows):
    """
    Interactively check a path
    """
    pdict['seen'] = True
    one = old + path
    two = new + path
    loadPages(browser, windows, one, two)
    # prompt for status
    resp = ""
    while resp not in ['s', 'r', 'o', 'm']:
        resp = raw_input("Page Decision: [s=skip, r=review, o=ok, m=markup fix] ").strip()
    if resp == 'r':
        pdict['review'] = True
        note = raw_input("Notes: ").strip()
        if note != "":
            pdict['note'] = note
    if resp == 'm':
        pdict['markup'] = True
        note = raw_input("Notes: ").strip()
        if note != "":
            pdict['note'] = note
    elif resp == 's':
        pdict['seen'] = False
    return pdict

def get_all_paths(dname):
    """
    Get all paths under dname that map to WP post URLs;
    i.e. all directories that contain "index.html"

    Don't include generated pages, only posts.

    :rtype: list of paths
    """
    paths = []
    for root, subdirs, files in os.walk(dname):
        for f in files:
            if f == "index.html":
                path = os.path.join(root, f)
                if path.startswith(dname):
                    path = path[len(dname):]
                path = os.path.dirname(path) + '/'
                path = re.sub('/+', '/', path)
                paths.append(path)
    return paths

def make_path_dict(paths):
    """
    Make a path_dict with the right keys
    """
    pdict = {}
    elem = {'seen': False, 'review': False, 'note': "", 'markup': False}
    for p in paths:
        pdict[p] = elem
    return pdict

def print_report(json_path, url_base):
    """
    Print a report on the json savefile contents
    """
    with open(json_path, 'r') as fh:
        j = anyjson.deserialize(fh.read())
    seen = 0
    review = 0
    markup = 0
    for path in j:
        s = ""
        if j[path]['seen'] is True:
            seen = seen + 1
        if j[path]['review'] is True:
            s = " review"
            review = review + 1
        if j[path]['markup'] is True:
            s = s + " markup"
            markup = markup + 1
        if s != "":
            print("%s\t%s%s" % (s, url_base, path))
            if j[path]['note'].strip() != "":
                print("\t%s" % j[path]['note'])
    print("==============================")
    print("Seen:   %d" % seen)
    print("Review: %d" % review)
    print("Markup: %d" % markup)
    print("Unseen: %d" % (len(j) - seen))
    print("=================")
    print("Total: %d" % len(j))

def parse_opts(argv):
    """
    Parse command-line options.

    :param argv: sys.argv or similar list
    :rtype: optparse.Values
    """
    parser = optparse.OptionParser()

    parser.add_option('-o', '--old', dest='old', action='store', type='string',
                      help='old path prefix, i.e. "http://blog.example.com"')

    parser.add_option('-n', '--new', dest='new', action='store', type='string', default='http://localhost:8000',
                      help='new path prefix, default: http://localhost:8000')

    parser.add_option('-d', '--output-dir', dest='htmldir', action='store', type='string', default='output',
                      help='Pelican output directory, default: output')

    parser.add_option('-s', '--savefile', dest='savefile', action='store', type='string', default='webdriver_compare.json',
                      help='path to JSON savefile, default: webdriver_compare.json')

    parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False,
                      help='verbose output')

    parser.add_option('-r', '--report', dest='report', action='store_true', default=False,
                      help='dont run, but report on savefile')

    options, args = parser.parse_args(argv)

    if not options.old or not options.new:
        sys.stderr.write("ERROR: you must specify -o|--old and -n|--new\n")
        sys.exit(1)

    return options

def main():
    """
    Main method
    """
    opts = parse_opts(sys.argv[1:])

    path_dict = {}

    if opts.report:
        if not os.path.exists(opts.savefile):
            sys.stderr.write("ERROR: savefile %s does not exist." % opts.savefile)
            sys.exit(1)
        print_report(opts.savefile, opts.new)
        sys.exit(0)

    if opts.savefile and os.path.exists(opts.savefile):
        # read the savefile instead of parsing URLs
        try:
            with open(opts.savefile, 'r') as fh:
                path_dict = anyjson.deserialize(fh.read())
        except ValueError:
            sys.stderr.write("ERROR: could not deserialize JSON savefile %s\n" % opts.savefile)
            return False
    else:
        paths = get_all_paths(opts.htmldir)
        path_dict = make_path_dict(paths)
        if opts.verbose:
            print("+ Found %d paths" % len(path_dict))
        with open(opts.savefile, "w") as fh:
            fh.write(anyjson.serialize(path_dict))
            fh.flush()
            os.fsync(fh.fileno())
    # we now have path_dict

    # setup the WebDriver stuff
    browser = webdriver.Firefox() # Get local session of firefox

    # open another window, which requires a loaded document/page
    browser.get("http://www.google.com")
    temp = browser.find_element_by_tag_name('body')
    temp.send_keys(Keys.CONTROL, 'n')
    windows = browser.window_handles

    for p in path_dict:
        if path_dict[p]['seen'] is True and path_dict[p]['review'] is False:
            continue
        if path_dict[p]['review'] is True:
            print("Reopening %s for review" % p)
            if path_dict[p]['note'] != "":
                print("\tPrevious Note: %s" % path_dict[p]['note'])
        path_dict[p] = check_path(p, path_dict[p], opts.old, opts.new, browser, windows)
        # write the JSON out and flush
        with open(opts.savefile, "w") as fh:
            fh.write(anyjson.serialize(path_dict))
            fh.flush()
            os.fsync(fh.fileno())
    print("Print a report about the paths...")

if __name__ == "__main__":
    main()
