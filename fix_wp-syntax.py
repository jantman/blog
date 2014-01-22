#!/usr/bin/env python
"""
Script to fix hilighted code blocks from WordPress wp-syntax plugin.

WordPress wp-syntax plugin (http://wordpress.org/extend/plugins/wp-syntax/)
uses a "lang" attr on pre tags to define the syntax hilighting, like:

    <pre lang="bash">
    something="foo"
    </pre>

When pelican-import runs this through Pandoc to produce MarkDown, it comes out
as a weird and meaningless block like:

    ~~~~ {lang="bash"}
    something="foo"
    ~~~~

This script takes file path(s) as arguments, and converts this junk
into proper MarkDown notation. It CHANGES FILES IN-PLACE.

REQUIREMENTS:

"""

import os
import sys
import re

from pygments import lexers

files = sys.argv[1:]

"""
translation of GeSHi identifiers to Pygments identifiers,
for GeSHi identifiers not supported by Pygments
"""
overrides = {}

def translate_identifier(lexers, overrides, i):
    """
    Translate a wp-syntax/GeSHi language identifier to
    a Pygments identifier.
    """
    if i in lexers:
        return lexers[i]
    if i in overrides:
        return overrides[i]
    sys.stderr.write("Unknown lexer, leaving as-is: %s" % i)
    return i

def get_lexers_list():
    """ get a list of all pygments lexers """
    d = {}
    ls = lexers.get_all_lexers()
    for l in ls:
        d[l[0]] = l[0]
        for n in l[1]:
            d[n] = l[0]
    return d

lang_re = re.compile(r'^~~~~ {lang="([^"]+)"}$')

lexers = get_lexers_list()

for f in files:
    content = ""
    inpre = False
    count = 0
    with open(f, "r") as fh:
        for line in fh:
            m = lang_re.match(line)
            if m is not None:
                line = ("~~~~{.%s}\n" % translate_identifier(lexers, overrides, m.group(1)))
                inpre = True
                count = count + 1
            elif inpre and line.strip() == "~~~~":
                inpre = False
            content = content + line
    with open(f, "w") as fh:
        fh.write(content)
        fh.flush()
        os.fsync(fh.fileno())
    print("fix_wp-syntax.py: fixed %d blocks in %s" % (count, f))
# done

