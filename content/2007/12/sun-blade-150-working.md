Title: Sun Blade 150 working!
Date: 2007-12-14 02:44
Author: admin
Category: Tech HowTos
Tags: nvram, openboot, password, smc, solaris, sun, sunblade
Slug: sun-blade-150-working

Yes, it's 3 AM here, and I've been working since about 6 PM on this. But
I finally got one of my two surplus (and fully locked down in NVRAM) Sun
Blade 150 workstations up and running. I encountered a few problems
along the way, but managed to solve them - more or less.

## Problem 1 - NVRAM password set, impossible to install an OS.

I did a *lot* of googling, and asking for advice. Eventually, I came
by a forum post expressing success with a procedure of pulling out and
then re-inserting the NVRAM \*while\* the system is powered on. This
left my system un-bootable. I pulled the chip again, and found two pins
bent. I straightened them, re-inserted, and rebooted using the Stop+N
Equivalent Functionality (after powering on the system, once you hear
the POST beep, click the power button twice quickly). This temporarily
resets the NVRAM to default settings. I found that the password was
gone, and was able to issue the "set-defaults" command at the "ok\>"
prompt. I then popped in the Solaris 10 install CD, issued the
"reset-all" command to reboot, and used Stop+A at boot to bring up a
boot menu, and told it to boot from CDROM ("boot cdrom"). Installation
then started.

## Problem 2 - Invalid NVRAM

After the above procedure, when booting, I got a message following the
Sun banner stating that there was a problem with the IDprom checksum.
When the install CD booted, I also got messages stating "Invalid format
code in IDprom", "Warning: IDprom checksum error", and "os-io Invalid
format code in IDprom". After another five hours of work, I found that
it's essentially something I have to live with. While OpenBoot previous
to version 4 allowed use of the "mkp" and "mkpl" commands to directly
write the IDprom, version 4 and above allows no access to this. The
IDprom was reporting an ethernet (mac) address of all zeros.
Unfortunately, there seems to be no way to correct this as far as I've
found. However, it didn't effect my OS installation... much.

\*There may be a way to access the IDprom through OpenBoot 4.x, but I
couldn't find any reference to it online, and couldn't figure out the
FORTH commands from the reference docs.

Some helpful links for the above problems include the OpenBoot 4.x
Command Reference Manual, currently found
[here](http://dlc.sun.com/pdf/816-1177-10/816-1177-10.pdf), as well as
the Sun Blade 150 Service Manual (from
[docs.sun.com](http://docs.sun.com/)), document 816-4379-10, currently
indexed with the Sun Blade 150 docs
[here](http://docs.sun.com/app/docs/coll/sb150). It was also
interesting, in my search for help, to look at the OpenBoot 3.x Command
Manual, and see how easy it was to re-write the IDprom on older Sun
Blade workstations.

Pleaese note that the advice given in the [Unofficial SunBlade 100
FAQ](http://040.digital-bless.com/texts/Unofficial_Sun_Blade_100_FAQ.htm)
and the [squirrel.com Sun NVRAM
FAQ](http://www.squirrel.com/sun-nvram-hostid.faq.html) doesn't seem to
work on the 150 with OpenBoot 4.x. From what I can tell, all of that
advice applies only to OpenBoot 3.x!

Some other helpful links included an ITworld.com article on [Sun NVRAM
passwords](http://open.itworld.com/5040/nlsunixfirmware070111/page_1.html),
[this](http://forum.java.sun.com/thread.jspa?threadID=5093819&messageID=9329080)
Sun Developer Forum post, and
[this](http://forum.java.sun.com/thread.jspa?threadID=5093819&messageID=9329080)
post on password recovery.

## Problem 3 - MAC / Ethernet address is 00:00:00:00:00:00

When booting Solaris, I found that I couldn't get DHCP. When I finally
got the OS running and logged in as root, I realized something
interesting - I couldn't access or ping anything past the one switch I
was connected to. But everything on that switch was fine, pinging both
from and to the Solaris box. I ping'ed from my laptop, and then thought
to run "arp -a". It showed a MAC address of 00:00:00:00:00:00! Running
"ifconfig -a" on the Solaris box confirmed this. Luckily, the first time
I booted this box, I wrote down the ethernet address and hostID as shown
on the banner. I ran a quick ifconfig to setup the correct MAC, like
"ifconfig eri0 ether xx:xx:xx:xx:xx:xx". Networking now worked
perfectly, and I could get to everything on the LAN as well as browse
the web. It would be good to somehow reset this in NVRAM, but for now
I'm just going to add it to the startup scripts somewhere. One forum
post that I found suggested adding the previous ifconfig command to the
top of /etc/rc.c/init.d/network, which I've done and will see how it
works at the next boot.

## Problem 4 - Can't login to SMC (Solaris Management Console)

My next task after getting the system up and running, and getting
networking working, as to give myself a user account. I was logged in
using the Java Desktop System, so I opened a terminal and ran "smc &".
After the usual initialization wait, I loaded the toolboxes for the
local machine, and connected. When I clicked on the "users" module and
entered my root password, I got an invalid password / login failed
message. I tried again and again, even checking against the post-it that
I wrote the password on until I memorize it. Nothing. Searching the
forums, I came by this
[post](http://forum.java.sun.com/thread.jspa?threadID=5104081&messageID=9354742),
but the value in /etc/security/policy.conf was correctly set to "
CRYPT\_DEFAULT=\_\_unix\_\_". So, on a wild hunch, I used "passwd" to
reset my password to a shorter one, which I use on a few other
(unimportant) workstations. Magic!

I now have, after two days of work, a working Solaris box. Now that I
have a good OS install, in order to get the other box working, I
\*should\* just be able to swap HDDs, boot, login as root, and use the
"eeprom" command to set "security-mode" to "none", bypassing all of this
bull\*\*\*\*.
