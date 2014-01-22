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
overrides = {'none': 'text', 'lisp': 'common-lisp', 'html4strict': 'html'}
overrides['xorg'] = 'text'
overrides['nagios'] = 'text'

"""
Mapping of WP categories to new blog categories, for any that change.
"""
categories = {}
categories['android'] = 'Android'
categories['EMS, Non-Technical Commentary'] = 'Miscellaneous'
categories['EMS, Personal'] = 'Miscellaneous'
categories['EMS, Projects'] = 'Miscellaneous'
categories['Higher Education'] = 'Miscellaneous'
categories['Higher Education, Ideas and Rants'] = 'Miscellaneous'
categories['History'] = 'Miscellaneous'
categories['Ideas and Rants'] = 'Ideas and Rants'
categories['Ideas and Rants, Miscellaneous Geek Stuff, Non-Technical Commentary'] = 'Miscellaneous'
categories['Ideas and Rants, Projects, Reviews'] = 'Ideas and Rants'
categories['Interesting Links and Resources'] = 'Links'
categories['Interesting Links and Resources, SysAdmin'] = 'Links'
categories['Miscellaneous Geek Stuff'] = 'Miscellaneous'
categories['Miscellaneous Geek Stuff, SysAdmin'] = 'SysAdmin'
categories['Miscellaneous Geek Stuff, Uncategorized'] = 'Miscellaneous'
categories['Non-Technical Commentary'] = 'Miscellaneous'
categories['opensource'] = 'Miscellaneous'
categories['Personal'] = 'Miscellaneous'
categories['Personal, Projects'] = 'Projects'
categories['PHP EMS Tools'] = 'Projects'
categories['PHPsa, Projects'] = 'Projects'
categories['Projects'] = 'Projects'
categories['Projects, Reviews'] = 'Projects'
categories['Projects, Reviews, Uncategorized'] = 'Projects'
categories['Projects, SysAdmin, Uncategorized'] = 'Projects'
categories['Projects, Tech HowTos'] = 'Tech HowTos'
categories['Puppet'] = 'Puppet'
categories['Puppet, SysAdmin'] = 'Puppet'
categories['Reviews'] = 'Reviews'
categories['SysAdmin, Tech HowTos'] = 'Tech HowTos'
categories['SysAdmin, Uncategorized'] = 'SysAdmin'
categories['Tech News'] = 'Miscellaneous'
categories['Uncategorized'] = 'Miscellaneous'
categories['Vehicles'] = 'Miscellaneous'

def translate_identifier(lexers, overrides, i, fname=None):
    """
    Translate a wp-syntax/GeSHi language identifier to
    a Pygments identifier.
    """
    if i in lexers:
        return lexers[i].lower()
    if i in overrides:
        return overrides[i]
    sys.stderr.write("Unknown lexer, leaving as-is: %s" % i)
    if fname is not None:
        sys.stderr.write(" in file %s" % fname)
    sys.stderr.write("\n")
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

def translate_category(i):
    """ translate a category name """
    if i in categories:
        return categories[i]
    return i

lang_re = re.compile(r'^~~~~ {lang="([^"]+)"}$')
cat_re = re.compile(r'^Category: (.+)$')

lexers = get_lexers_list()

for f in files:
    content = ""
    inpre = False
    count = 0
    with open(f, "r") as fh:
        for line in fh:
            m = cat_re.match(line)
            if m is not None:
                line = ("Category: %s\n" % translate_category(m.group(1).strip()))
                content = content + line
                continue
            m = lang_re.match(line)
            if m is not None:
                line = ("~~~~{.%s}\n" % translate_identifier(lexers, overrides, m.group(1), fname=f))
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

