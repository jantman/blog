Title: MediaWiki - Preformatted Text within Lists
Date: 2012-03-15 18:10
Author: admin
Category: Software
Tags: formatting, mediawiki, wiki
Slug: mediawiki-preformatted-text-within-lists

As I discovered this morning, with [MediaWiki](http://www.mediawiki.org)
1.5.7+, if you attempt to put a `<pre>` wraped block of code within a
numbered list, the indentation breaks and the numbering starts over
after the `<pre>` block. This was pretty annoying, as I was trying to
document a procedure including the commands to be run and their
explanation. It took a few minutes, but I found the solution in the
[wikimedia Help:Editing
FAQ](http://meta.wikimedia.org/wiki/Help:Editing_FAQ#Q:_Can_I_put_preformatted_text_inside_a_numbered_list.3F)
page, thanks to [Ulf Rompe](http://meta.wikimedia.org/wiki/User:Rompe):

~~~~{.text}
# one
# two
#:
#:here are a couple lines
#:of preformatted text
#:
# and the numbering
# continues
~~~~

The code lines are indented a bit more than what looks right, but it
works.
