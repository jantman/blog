Title: Update
Date: 2008-06-15 11:03
Author: admin
Category: Miscellaneous
Tags: ieilogd, linux, php ems tools, tuxostat
Slug: update-2

I've been incredibly busy lately. But I have 2 quick updates-

\1) tuxOstat, my thermostat project, isn't totally finished, but is up
and running. There's still some work to do, but the code is largely
complete, and in [CVS](http://cvs.jasonantman.com/tuxostat). There's
also a [web interface](http://701rh.dyndns.org:10080/) with temperature
graphs, system status, and a (horrible) webcam view of the LCD control
panel. I'll probably be finishing up a first version this week,
finishing the documentation next week, and releasing what I have soon.

I got an e-mail today about one of my older projects, [PHP EMS
Tools](http://www.php-ems-tools.com), a PHP/MySQL based application for
fire/EMS agencies to handle scheduling, membership rosters, equipment
checks, etc. The potential user was asking about running the software on
Windows - which, of course, I have no experience with. I'm pretty sure
there aren't many, if any, Unix-specific calls hidden in the code, and
advised him to try XAMPP (Apache/MySQL on Windows). But I did take a
moment to comment on why I chose Linux. My pilot installation of PHP EMS
Tools, at the Midland Park Volunteer Ambulance Corps, where I've been a
member since 2005, has been handling our scheduling, roster, and
equipment checks since June 2006. It's running on a generation 1 Compaq
Proliant DL380, running dual Pentium III 733MHz processors and 1GB
memory - and even with a number of other programs on it, including
[ieilogd](http://cvs.jasonantman.com/ieilogd/) which is reading from the
serial port 24x7 - the load average has never passed 1.2 and the memory
usage is well under 50%. More importantly, the system has been up for
442 days without a hiccup!
