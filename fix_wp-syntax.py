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
into proper syntax hilighting markup. It CHANGES FILES IN-PLACE.

REQUIREMENTS:

"""

import os
import sys
import re

files = sys.argv[1:]

"""
translation of GeSHi identifiers to Pygments identifiers,
for identifiers not supported by both
"""
geshi_to_pygments = {}

def translate_identifier(i):
    """
    Translate a wp-syntax/GeSHi language identifier to
    a Pygments identifier.
    """
    return geshi_to_pygments.get(i, i)

lang_re = re.compile(r'^~~~~ {lang="([^"]+)"')

for f in files:
    content = ""
    inpre = False
    count = 0
    with open(f, "r") as fh:
        for line in fh:
            m = lang_re.match(line)
            if m is not None:
                content = content + "        " + ":::" + translate_identifier(m.group(1)) + "\n"
                inpre = True
                count = count + 1
            elif inpre and line.strip() == "~~~~":
                inpre = False
                content = content + "\n"
            elif inpre:
                content = content + "        " + line
            else:
                content = content + line
    with open(f, "w") as fh:
        fh.write(content)
        fh.flush()
        os.fsync(fh.fileno())
    print("fix_wp-syntax.py: fixed %d blocks in %s" % (count, f))
# done

