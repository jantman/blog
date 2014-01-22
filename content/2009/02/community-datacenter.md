Title: Community Datacenter
Date: 2009-02-07 00:50
Author: admin
Category: Ideas and Rants
Tags: community, datacenter
Slug: community-datacenter

I've been planning a lot of administrative work lately... I have a few
machines that need OS upgrades, my backup system is barely functional
(it needs both a new, large disk and a configuration overhaul), and I'm
planning a switch to static IP service - which means not only a new
[router/firewall][] to design, configure and monitor, as well as moving
some services previously run by [IPcop][] over to a dedicated box, but
also finally adding three IPsec VPNs, monitoring them and tunneling all
sorts of stuff over them, and reconfiguring all of my DNS, finding any
hard-coded URLs, and a slew of other projects.

So this got me thinking. While there are a number of reasons why I run
such a complex network at home (mainly including maintaining my presence
on the web and my email, providing temporary hosting for freelance work,
the convenience of file access from anywhere, the breadth of
administrative experience it gives me, and a way to test new
technologies) there are some parts of it that I just don't like dealing
with. I've never been a really network-centric guy, and the idea of
having to setup a router/firewall (I'm going with [Vyatta][] as it seems
to be the *only* thing that will deal with the complex configuration I
want) for all this just to get 5 static IPs seems a bit much. Not to
mention there's just too much running on all those boxen (8 at home, 2
at school, plus 3 others at 2 other locations) for me to keep a handle
on all of it and still be a full-time student, work 30 hours/week, and
do freelance work. Something's always bound to get ignored - sometimes
backups stop for a week, sometimes Nagios goes haywire, and sometimes
Cacti stops graphing for a month before I notice it.

The biggest thing I learned from running all of these systems for
personal use is to start everything consistently and with a plan. My
oldest box in semi-production is running SuSE 9.3, installed somewhere
between April and October of 2005. It was ignored for so long (a period
when it wasn't being used for much) that I now can't even perform
updates, as the update sequence is virtually impossible to accomplish.
Then again, re-purposed desktops shouldn't be in "production" for 4
years. Anyway, perhaps the biggest lesson in trying to deal with all of
this is the importance of consistency. Not just attempting to
standardize on one distribution, but also making a local image that
includes the standard packages, configurations, and other important
stuff - like the Nagios user account and local plugins and maybe even
the public SSH key of the Nagios box. Even better would be a
configuration management system like [Puppet][] or [CFengine][], or even
manually keeping all of the distros updated to a common version.

But, I digress. The real point of this post was supposed to be a simple
idea: I have all of this running at home, and I know quite a few IT
people who have a similar setup at home or at work, or have considerable
resources at a hosting/colo facility. So, why not start a "community
datacenter" project? At home I have to do everything from backups to
firewall and router administration to security. I'd be much happier just
handling network/service monitoring, log analysis, and some tool and web
scripting. I know a few Cisco-heads who run their "home" LANs on chassis
switches, but find it such a pain to reconfigure Apache or run a
monitoring app. I'm sure someone's thought of this in the past, and
probably tried it, but why don't some guys (who can be trusted) get
together, find some colo space (or anywhere with power and connectivity)
and start, essentially, a co-op data center? Assuming you could find a
large enough circle of trusted friends, I'm sure you could find someone
willing to volunteer every service needed - from network engineering to
backups, monitoring, and security - in exchange for some rack space and
connectivity, or even a virtual host. I know I'd opt in any second - or
even let someone throw a box in my basement in exchange for someone to
help read through logs or setup a HTTPS VPN, if it weren't for the
archaic equipment I'm running.

Just a thought...

  [router/firewall]: http://www.vyatta.com/
  [IPcop]: http://www.ipcop.org/
  [Vyatta]: http://www.vyatta.com
  [Puppet]: http://reductivelabs.com/trac/puppet
  [CFengine]: http://www.cfengine.org/
