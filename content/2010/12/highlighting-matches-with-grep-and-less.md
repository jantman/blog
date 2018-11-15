Title: Highlighting matches with grep and less
Date: 2010-12-09 09:08
Author: admin
Category: Miscellaneous
Tags: color, grep, less, terminal
Slug: highlighting-matches-with-grep-and-less

Yes, I haven't posted much lately. Just a quick little tip, since it
came in handy today.

Grep accepts a `--color` argument which highlights matches in color
(assuming your terminal supports it). Passing grep `--color=always` and
piping the output into `less -R` will allow you to scroll through the
colorized output with less. Very handy if you're grepping through source
code with long lines or SQL statements.
