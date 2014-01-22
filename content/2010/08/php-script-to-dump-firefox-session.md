Title: PHP Script to Dump Firefox Session
Date: 2010-08-17 21:17
Author: admin
Category: Miscellaneous
Tags: firefox, PHP
Slug: php-script-to-dump-firefox-session

If you're anything like me, you often find yourself working on multiple
computers. Today I left a few tabs open in Firefox on my work laptop,
and wanted to continue reading from my desktop. Normally I'd just grab
the laptop, or RDP into it if it was my work desktop that had the open
tabs, but at the moment my girlfriend is neck-deep in WoW on the
MacBook. Having had this problem before (getting tabs back remotely, not
a laptop occupied with WoW), I started thinking about a solution.

I *could* have closed my local firefox session, moved the
sessionstore.js somewhere else, copied the one from the laptop over,
re-opened firefox, ... well, you get the idea.

But that sounds like a really sub-optimal solution. So I started looking
around a bit. It seems that sessionstore.js is *almost* JSON, but as per
[Mozilla bug 407110][], it's not quite standards-compliant. Luckily, it
seems that PHP's JSON module is quite tolerant, so once I stripped off
the leading and trailing parens from the file contents, it parsed quite
nicely.

I've written a small `dumpFirefoxSession.php` script that reads the
sessionstore.js file (in cwd or a specified path), unserializes the JSON
as an array, and then dumps the tabs. It dumps as either plain text or
HTML (currently just elements inside the body, not a full HTML file).
The HTML will include `ol`s for each window listing the tabs, links to
the current content (sessionstore.js also holds history for each tab,
but I don't need this), and it shows which tab is currently selected.

You can grab the script from subversion at:
[http://svn.jasonantman.com/misc-scripts/dumpFirefoxSession.php][]. The
current version is 3. You'll need PHP (probably 5) with JSON support.

  [Mozilla bug 407110]: https://bugzilla.mozilla.org/show_bug.cgi?id=407110#c2
  [http://svn.jasonantman.com/misc-scripts/dumpFirefoxSession.php]: http://svn.jasonantman.com/misc-scripts/dumpFirefoxSession.php
