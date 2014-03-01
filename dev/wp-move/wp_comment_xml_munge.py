#!/usr/bin/env python
"""
Script to munge a WordPress XML export before importing in Disqus

- adds `dsq:thread_identifier` field to all posts, using `wp:post_name` as its content

requirements (pip install these):
lxml
"""

from lxml import etree
import optparse
import sys
import re
import os
import codecs
import tempfile

def disqusify_wp_xml(infile, outfile, verbose=False):
    """
    disqus-ify wordpress XML export

    :param infile: path to input wordpress XML export file
    :type infile: string
    :param outfile: path to write output XML file at
    :type outfile: string
    :param verbose: enable verbose/debug output
    :type verbose: boolean
    """
    namespaces = {
        'wp': 'http://wordpress.org/export/1.1/',
        'dsq': 'http://www.disqus.com/',
    }
    etree.register_namespace('dsq', 'http://www.disqus.com/')
    etree.register_namespace('wp', 'http://wordpress.org/export/1.1/')

    if not os.path.exists(infile):
        sys.stderr.write("ERROR: file does not exist: %s\n" % infile)
        return False

    # we need to add the Disqus namespace.
    # due to https://bugs.launchpad.net/lxml/+bug/555602, lxml can't
    # add to xmlns attributes, so we need to string-munge them, but because
    # of lxml issues, this has to be read from a file...
    with codecs.open(infile, encoding='utf-8') as fh:
        data_in = fh.read()
    fh, fname = tempfile.mkstemp()
    data_in = data_in.replace(u'xmlns:wp="http://wordpress.org/export/1.1/"', u'xmlns:wp="http://wordpress.org/export/1.1/" xmlns:dsq="http://www.disqus.com/"')
    data_in = data_in.encode('utf-8')
    os.write(fh, data_in)
    os.close(fh)

    try:
        tree = etree.parse(fname)
    except IOError as e:
        sys.stderr.write("%s\n" % e)
        os.remove(fname)
        return False
    os.remove(fname)

    root = tree.getroot()

    item_count = 0
    item_withcomm_count = 0
    for element in root.iter("item"):
        guid = str(element.find("guid").text)
        link = str(element.find("link").text)
        name = str(element.find("wp:post_name", namespaces=namespaces).text)
        item_count = item_count + 1
        if len(element.findall("wp:comment", namespaces=namespaces)) < 1:
            if verbose:
                print("Skipping post with no comments: guid=%s name=%s" % (guid, name))
            continue
        item_withcomm_count = item_withcomm_count + 1
        print("Found post with comments: guid=%s name=%s" % (guid, name))
        identifier = etree.Element('{http://www.disqus.com/}thread_identifier')
        identifier.text = name
        element.append(identifier)
    if verbose:
        print("Found %d items, %d items with comments." % (item_count, item_withcomm_count))
    ser = etree.tostring(root, xml_declaration=True, pretty_print=True)
    with open(outfile, 'w') as fh:
        fh.write(ser)
    print("Output written to: %s" % outfile)
    return True

def parse_options(argv):
    """ parse command line options """
    parser = optparse.OptionParser()

    parser.add_option('-o', '--outfile', dest='outfile', action='store', type='string', default="",
                      help='output filename. defaults to input file name, s/\.xml$/_disqus\.xml/')

    parser.add_option('-i', '--infile', dest='infile', action='store', type='string',
                      help='input WordPress XML export file')

    parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False,
                      help='verbose output')

    options, args = parser.parse_args(argv)

    if not options.infile:
        sys.stderr.write("ERROR: you must specify -i|--infile\n")
        sys.exit(1)

    if not options.infile.endswith(".xml"):
        sys.stderr.write("ERROR: -i|--infile must match '\.xml$'\n")
        sys.exit(1)

    if options.outfile == "":
        options.outfile = re.sub(r'\.xml$', '_disqus.xml', options.infile)

    return options

if __name__ == "__main__":
    opts = parse_options(sys.argv)
    disqusify_wp_xml(opts.infile, opts.outfile, opts.verbose)
