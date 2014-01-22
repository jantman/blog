Title: Documentation generation for web apps - PHP and JavaScript
Date: 2010-08-26 08:10
Author: admin
Category: Tech HowTos
Tags: documentation, javascript, PHP, web programming
Slug: documentation-generation-for-web-apps-php-and-javascript

Recently I've been making some changes to a relatively complex ePCR
(electronic patient care report) program that I wrote for the [ambulance
corps][]. It's a web application (available only on our LAN, of course)
written in PHP, with a relatively large chunk of custom javascript to
provide Ajax/DHTML functions. Most of the PHP code was already
documented and processed with [phpDocumentor][] (phpdoc) to generate API
documentation. However, since so much of the functionality is
DHTML-based, there was a lot of looking back to the JavaScript source to
figure out what was called where.

My search for a true multi-language documentation generator was
relatively fruitless. There's [doxygen][] but that needed a Perl helper
script for javascript files. Since virtually all of the code, both PHP
and JavaScript, is purely procedural, I was really only concerned about
docblocks and the functions they precede.

Luckily, it occurred to me that JavaScript is pretty close in syntax to
PHP, and I tend to write them with exactly the same style. A little
research showed that phpdoc can more or less handle javascript code,
with a few caveats:

-   The code needs to parse as PHP, so things like inline functions mess
    it up.
-   The default phpDocumentor ini file doesn't recognize files with
    `.js` extensions.
-   The files need to have a <?php at the top.

Noting this, I wrote a small script that iterates through a directory of
`.js` files, parses them line by line, pulls out only the function
declarations (which, hopefully, don't also have code on the same line)
and docblocks, and writes the output (with a <?php at the top) to a
same-named file in a different directory.

The script obviously requires phpdoc to be installed, and also requires
you to edit the phpDocumentor.ini file (installed with PEAR on my system
at `/usr/share/php5/PEAR/data/PhpDocumentor/phpDocumentor.ini`) and add
a "js" line to the `[_phpDocumentor_phpfile_exts]` section to get phpdoc
to recognize `*.js` files.

I was easily able to integrate this with a Makefile rule and create a
single set of cross-linked phpdoc API docs including both JS and PHP
files. I also added explicit package names (like "-PHP" and "-JS") to
keep things separated a little.

The script can be found at:
[http://svn.jasonantman.com/misc-scripts/js2phpdoc.php][]. It's
(obviously) free for any use, provided that you follow the license terms
(leave copyrights intact, send modifications back to me, and update the
changelog if you modify it).

My Makefile rule (which uses a temp directory to both keep the generated
files separate from the source and keep the file paths as seen by phpdoc
the same as the actual source):  
` .PHONY: docs`

docs:  
mkdir -p temp/js  
bin/js2phpdoc.php js/ temp/js/  
cp -r inc temp/  
cp \*.php temp/  
phpdoc -c docs/default.ini  
rm -Rf temp  
</code>

  [ambulance corps]: http://www.midlandparkambulance.com
  [phpDocumentor]: http://www.phpdoc.org/
  [doxygen]: http://www.stack.nl/~dimitri/doxygen/
  [http://svn.jasonantman.com/misc-scripts/js2phpdoc.php]: http://svn.jasonantman.com/misc-scripts/js2phpdoc.php
