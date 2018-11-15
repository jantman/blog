Title: SunFire Information
Date: 2008-08-08 14:45
Author: admin
Category: Hardware
Tags: sun, sunfire
Slug: sunfire-information

Ok, an update is a long time coming, and I'll post one this weekend with
status of a lot of my projects, as well as some new information.

For now, I'm installing two beautiful SunFire x4150's at work, and
here's a little bit of information on how to use these great boxes:

**RAID Configuration** is
accomplished by a normal startup prompt Ctrl+ (C? I don't remember) key
sequence, as they're x64 machines and it's a standard RAID controller.

**Serial Management** is great -
just connect (in [Kermit](http://www.columbia.edu/kermit/ck80.html) I
just had to set speed to 9600 and carrier-watch off) and you get a
prompt that looks like `SUNSP001E682F6311 login:`. The numbers are the
MAC address of the management interface (SP). The default login is
root:changeme, as per Sun doc 819-1155-16. When you login, you'll see
the current firmware version (4.0.06 as my box shipped).

**Getting a System Console** - on
the x4100, at the iLOM prompt, `cd /SP/console`, `start /SYS` to boot
the system, and then `start` to get the console. On the x4150, we must
start `/SP/AgentInfo/Console`, and use `Esc+Shift+9` to get away from
the console.
