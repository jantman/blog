Title: Solaris Update, Hardware Photos, SMF Manifests, Nagios Plugins
Date: 2008-01-02 02:06
Author: admin
Category: Projects
Slug: solaris-update-hardware-photos-smf-manifests-nagios-plugins

So in the past weekend, I had my first real experience with Solaris in
production. I finally setup my Sun Blade 150 running Solaris 10 as my
new mailserver, replacing a (!!!) vintage 1998 Gateway Pentium II 350MHz
desktop. Quite an upgrade, even to the still-not-new Sun workstation.
Maybe sometime in the future I'll even upgrade some of my other old
desktops with my spare Dell PowerEdge 2550.

Anyway, the whole process, from fresh Solaris install to working
mailserver, probably took me around 24 work hours. That being said, I've
never really administered Solaris before, so that also included horribly
long stretches of doc reading and figuring out SMF, package and service
administration, etc.

I've detailed the entire process on my
[wiki](http://www.jasonantman.com/wiki/index.php/Solaris_Mailserver) in
excruciating detail. The Solaris package repository any pkg-get systems
from [blastwave.org](http://www.blastwave.org/) were immensely helpful,
as were a number of [Ben Rockwood's](http://cuddletech.com/blog/) blog
posts. The entire operation involved installing and configuring Dovecot
with IMAPS, Postfix with TLS and SASL to authenticate to my ISP's
mailserver (which I use to relay outgoing mail, given my dynamic IP),
Procmail, Fetchmail and SpamAssassin. I also had to setup the machine to
relay mail for other hosts on the LAN. Rounding it out, I setup
monitoring with Nagios and backups of the system and mail through
Bacula. During the process, I also had to modify some Service Management
Facility (SMF) manifests for Fetchmail, Postfix, and Dovecot.

I still have a few things to do - namely create
[Nagios](http://www.nagios.org/) check scripts for processors,
temperatures, and fans (using the prtdiag command) and hard drive
status/errors (using iostat -Exn, given that I haven't been able to find
a SMART tool that supports IDE under Solaris). For everything else, I
just checked the [NagiosExchange](http://www.nagios-exchange.org/)
plugin repository, using check\_by\_ssh for everything. The only problem
I had was that NagiosExchange didn't appear to have working default
Nagios plugins for Solaris 10. Luckily, though, Blastwave had a
"nagiosp" plugin package.

I'll probably update this blog with my check plugins as I develop them,
but for now I have a little
[page](http://www.jasonantman.com/wiki/index.php/Solaris_Nagios_Checks)
on my [wiki](http://www.jasonantman.com/wiki/)about using Nagios with
Solaris.

Also, I uploaded [a few
photos](http://www.jasonantman.com/wiki/index.php/Jasonantman.com_Hardware)
of the equipment that runs this blog and the rest of my site and
development network - all on a "beautiful" Sears shop shelf in my
basement. Nothing wonderful, but it gets the job done. I'll admit that I
could have done a better job stitching the photos together, but the
space is so tight that I can't get a wide shot of the whole rack.

The rack, in all its glory:  
[![image](http://www.jasonantman.com/wiki/images/0/0a/Tall1_sm.jpg)](http://www.jasonantman.com/wiki/images/c/c3/Tall1.jpg)

A closer view of (most of) the hardware:  
[![image](http://www.jasonantman.com/wiki/images/5/57/Tall3_sm.jpg)](http://www.jasonantman.com/wiki/images/7/77/Tall3.jpg)

Happy New Year!
