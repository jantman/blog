Title: New server, and looking for work
Date: 2011-09-27 19:35
Author: admin
Category: Miscellaneous
Tags: linode, move, rack, servers
Slug: new-server-and-looking-for-work

First off, I've moved this blog from a server in my basement to
[Linode](http://www.linode.com) virtual hosting, in preparation for my
move from New Jersey to an apartment in Georgia. This will mark the
first time since 2001 (when I was 14) that I didn't have at least a
publicly-accessible Linux server in my home. It also means that, as sad
as it is, the rack will probably all be either going in Ebay or to scrap
(after a good [Guttmann
wipe](http://en.wikipedia.org/wiki/Gutmann_method), of course).

![server rack](/GFX/rack_2011-09-27_small.jpg)

I'm a bit sad to give up hosting DNS myself and having my beautiful
per-zone, per-domain, hourly DNS statistics, but that was my first move,
and Linode's web-based DNS manager is much nicer than my collection of
PHP scripts, MySQL backend, and rndc reload wrapper (and I no longer
need BIND split-horizon since the hosting is remote). Mail was next, and
I've got one web server moved and the other on the way. The biggest
disappointment is losing my testbed for all the fun stuff I can't do (or
doesn't make sense) with a virtualized hosting provider -
[Puppet](http://puppetlabs.com/), real ISC DHCP, BIND9, Cisco CatOS and
IOS devices, [Bacula](http://www.bacula.org), running my own edge
router, etc. There's at least a handful of current production Rutgers
services and tools that got their start here as projects in my spare
time. But I'm sure I'll make up somehow, and I'm planning on putting
aside some money for a massive new desktop to run a slew of VMs.

On a second note, the one thing holding back my move to Georgia is,
well, my lack of a job there. I'm really just starting to look around,
and am very much hoping to find something comparable to my current
position at Rutgers - a group supporting diverse services, doing mainly
architecture and implementation of new services, a good dose of
automation and custom tool development, and hopefully also some work
with performance and availability monitoring (think
[Nagios](http://www.nagios.org) and [Cacti](http://www.cacti.net/)),
logging, etc. And, of course, something that's network-focused, whether
wireless or wired. Maintaining some data center space/physical
infrastructure and occasionally working with my hands is fun too. So, if
you know anyone who's hiring a Linux/open source dude in the general
vicinity of Athens, GA (including Atlanta and the surrounding area),
please give me a heads-up, or pass them along to
[resume.jasonantman.com](http://resume.jasonantman.com).
