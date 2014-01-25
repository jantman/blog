Title: Emacs Mode Variable for HTML
Date: 2012-06-26 08:43
Author: admin
Category: Tech HowTos
Tags: emacs, html. php
Slug: emacs-mode-variable-for-html

Unfortunately, I often find myself editing files that are mixed PHP and
HTML, and ending with a ".php" extension. For most smaller
projects/tasks, I use [emacs](http://www.gnu.org/software/emacs/) at the
command line (nox) and my .emacs settings for
[php-mode](http://php-mode.sourceforge.net/) will latch onto the ".php"
extension and open it with PHP mode. Unfortunately, PHP mode really
doesn't like embedded HTML (let alone mostly HTML with some inline PHP),
and the indentation gets very messy, among other problems.

The simple solution is to add the following (XHTML 1.0
Transitional-compliant) comment to the first line of the file, which
tells emacs to load html-mode:

~~~~{.html}
~~~~

You can also get emacs to do this for you, as per the [Specifying File
Variables](http://www.gnu.org/software/emacs/manual/html_node/emacs/Specifying-File-Variables.html)
documentation page. Once in html-mode, simply <tt>M-x
add-file-local-variable-prop-line</a>, enter "mode" for the variable
name and use the default of the current mode.
