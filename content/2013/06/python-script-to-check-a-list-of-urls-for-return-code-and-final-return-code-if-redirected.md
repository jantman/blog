Title: Python script to check a list of URLs for return code, and final return code if redirected
Date: 2013-06-10 06:00
Author: admin
Category: SysAdmin
Tags: http, python, redirect, urllib
Slug: python-script-to-check-a-list-of-urls-for-return-code-and-final-return-code-if-redirected

Every once in a while I need to add a bunch of redirects in Apache.
Here's a handy, dead simple Python script which takes a list of URLs on
STDIN, and for each one prints out either the response code, or, if the
response is a redirect, the response code of what is redirected to.
Pretty useful when you've just added a bunch of redirects and want to
make sure none of them 404.

The latest source of this script lives at
[https://github.com/jantman/misc-scripts/blob/master/check\_url\_list.py](https://github.com/jantman/misc-scripts/blob/master/check_url_list.py).

~~~~{.python}
#!/usr/bin/env python
"""
Script to check a list of URLs (passed on stdin) for response code, and for response code of the final path in a series of redirects.
Outputs (to stdout) a list of count of a given URL, response code, and if redirected, the final URL and its response code

Optionally, with verbose flag, report on all URL checks on STDERR

Copyright 2013 Jason Antman  all rights reserved
This script is distributed under the terms of the GPLv3, as per the
LICENSE file in this repository.

The canonical version of this script can be found at:

"""

import sys
import urllib2

def get_url_nofollow(url):
    try:
        response = urllib2.urlopen(url)
        code = response.getcode()
        return code
    except urllib2.HTTPError as e:
        return e.code
    except:
        return 0

def main():
    urls = {}

    for line in sys.stdin.readlines():
        line = line.strip()
        if line not in urls:
            sys.stderr.write("+ checking URL: %s\n" % line)
            urls[line] = {'code': get_url_nofollow(line), 'count': 1}
            sys.stderr.write("++ %s\n" % str(urls[line]))
        else:
            urls[line]['count'] = urls[line]['count'] + 1

    for url in urls:
        if urls[url]['code'] != 200:
            print "%d\t%d\t%s" % (urls[url]['count'], urls[url]['code'], url)

if __name__ == "__main__":
    main()
~~~~
