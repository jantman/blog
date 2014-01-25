Title: Parsing Nagios status.dat in PHP
Date: 2010-02-21 22:42
Author: admin
Category: Monitoring
Tags: Nagios, PHP, xml
Slug: parsing-nagios-status-dat-in-php

**If you're just looking for the script or PHP module**, you can get
them at:
[http://github.com/jantman/php-nagios-xml](http://github.com/jantman/php-nagios-xml).

A while ago (back in late 2008), I wrote a PHP script that parses the
Nagios status.dat file into an associative array. My original use was to
output XML which was then read by another script on another server and
used for a small custom GUI. It's a very simple PHP script that just
takes the path of the status.dat file (which, obviously, must be
readable by the user running the script).

At that time, I was using Nagios v2. Since then, I've moved to Nagios
v3, and have updated the script to include the ability to parse v3
status.dat files, as well as a function to detect the version of a
status file. I also refactored the code so that the parsing functions
are all contained in a single file (statusXML.php.inc) which is safe to
include in other scripts. The actual statusXML.php file now just
includes examples of how to call all of the functions and output XML
(though it is equally useful to output the serialized array, or use it
directly).

Since I posted my script online, two people have been kind enough to
send back their modifications:

-   [Artur Krzywański](http://www.krzywanski.net/) modified the original
    ([r4](https://github.com/jantman/php-nagios-xml/blob/9926602ef4868a898661b6ea0f430ff8ccba4dd3/parseNagiosXML.php))
    version of
    [statusXML.php](https://github.com/jantman/php-nagios-xml/blob/master/statusXML.php)
    to allow selection of the keys to be returned.
-   Whitham D. Reeve II of [General Communication,
    Inc.](http://www.gci.com), who needed higher performance for a very
    large status file, rewrote my script in C as a PHP module.

Both of these generous contributions have been included in my [Github
repository](https://github.com/jantman/php-nagios-xml) as of the current
commit. Unfortunately, due to my delay in putting my Nagios3 code into
svn, both of these contributions are **Nagios v2** only.

As time permits, I plan on merging Artur's changes into the current
version of statusXML.php.inc. Unfortunately, C isn't one of my strong
points, but I plan on also updating Whitham's PHP module code to work
with Nagios3 as soon as possible.

Stay tuned for updates, and thanks to both gentlemen for contributing
their work. I'm always interested in hearing how people are using my
code, and how they are making it better.

**Also:** While I added this project to [Nagios
Exchange](http://exchange.nagios.org/), and plan on adding it to
[Monitoring Exchange](http://www.monitoringexchange.org/), I don't
always keep those sites up to date (I can't access Nagios Exchange right
now, and who knows if I'll have time to update it tomorrow). I
*strongly* recommend directly checking out from Git at
[https://github.com/jantman/php-nagios-xml](https://github.com/jantman/php-nagios-xml).
