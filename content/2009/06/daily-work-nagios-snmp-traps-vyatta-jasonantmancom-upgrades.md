Title: Daily Work - Nagios SNMP traps, Vyatta, JasonAntman.com upgrades
Date: 2009-06-27 01:03
Author: admin
Category: Miscellaneous
Tags: apc, bluesocket, Nagios, snmp, vyatta
Slug: daily-work-nagios-snmp-traps-vyatta-jasonantmancom-upgrades

So it's been a very busy day. I was up until 5 AM or so working on
implementing [Puppet](http://reductivelabs.com/trac/puppet/) at home.
I'm building two new boxes - a storage (centralized home
directory)/syslog (to MySQL) server and a second web server (possibly
also to handle Nagios) - and I decided that they'll be totally built by
Puppet. The only thing I had to give up on was setting up the NFS share
for my home directory on the new storage box and installing and testing
[rsyslog](http://www.rsyslog.com/) on it.

This afternoon around 7, I started on my weekend projects for [the
ambulance corps](http://www.midlandparkambulance.com) - setting up
[Nagios](http://www.nagios.org) to receive SNMP traps from the APC UPS
and moving over to the new [Vyatta](http://www.vyatta.org)-based router
(from [m0n0wall](http://m0n0.ch/wall/)). I'd attempted the router
before, but had to rollback - I'm using an old
[BlueSocket](http://www.bluesocket.com/) controller for hardware - it's
just a nice black 1U enclosure with a stock Intel motherboard, 20GB HDD,
512MB RAM and three 10/100 NICs. The first time, I was unable to get
link on either of the two NICs I was using, so I decided to rollback.

**Nagios SNMP Traps**

I found a good starting point for Nagios SNMP traps on the [OpsView
blog](http://altinity.blogs.com/dotorg/2006/03/lessons_in_snmp.html). I
setup \`snmptrapd\` on the Nagios server and hacked together a little
Python script to just write all of the traps to a file. After some
testing with \`snmptrap\` on my laptop, I did a test by pulling the
power plug of the UPS, waiting about 30 seconds, and then plugging it
back in. Sure enough, the little old [AP9605 PowerNet SNMP
card](/2007/03/apc-ap9605-powernet-snmp-card/)
generated two SNMP traps - one for power loss and one for power regained
- both of which showed up in the test file

The next step will be deciding how to get the traps into Nagios -
specifically whether I want to go with something heavy-weight, like
[SNMPtt](http://snmptt.sourceforge.net/) that can handle other devices,
or whether I want to code a simple script myself just to deal with the
APC cards.

**Router**

The main reason why I wanted to make the switch from m0n0 to Vyatta was
to ease the setup and maintenance of an IPsec tunnel from the ambulance
HQ to my house, so I could push backups (relatively small) over the WAN
to my infrastructure (or, rather, have Bacula pull the backups). Another
big bonus was finally having a way of configuring and checking things
through SSH without having to port-forward a web GUI. Another bonus of
having a real Linux system under the router is the ability to make
custom Nagios check scripts and easily execute them. Something I hadn't
thought of - but became obvious during the switchover - is the ability
to run full-fledged \`tcpdump\` on the router itself.

After building the new config myself, and confirming that the system ran
in isolation, I moved it over to production. The first issue was a bit
of a thinko on my part - the interfaces on the BSC are actually arranged
on the back of the box like eth0-----eth2-----eth1, so I originally had
the LAN uplink in the wrong interface. After correcting that and waiting
for the network to stabilize, I noticed a total external connectivity
failure. After some troubleshooting - thanks to tcpdump on the router -
it occurred to me that the (ancient) cable modem needs to be rebooted
when the router MAC changes.

I honestly don't remember the other problems that I ran into, but
eventually I ended up getting almost-full functionality - and then a
total network outage. A tcpdump on my laptop showed some really really
weird BOOTP traffic with addresses of 255.255.255.255. After doing some
troubleshooting and monitoring port counters on the switch, I narrowed
it down to coming from a single Windows box and the wireless access
point. After shutting off both ports, things seemed to stabilize. I also
had some "martian address" issues with one of the boxes, but decided to
roll the box and that solved it.

Over the next day or so, I'll be reconfiguring Nagios both at home and
at the ambulance corps to cope with the changes and add in the requisite
monitoring, and keep an eye on things. Assuming all goes well, I'll
power down the old router on Sunday.

On the home front, I've moved over from my old storage machine to the
old one - essentially just the NFS mount, and moved over a tarball of
everything else. I also added a 1000Base-SX card to the new box, though
it appears that I'm out of fiber patch cords. The old storage box was
brought down for the first time in about 3 years (aside from brief
outages for hardware upgrades or array rebuilds). Assuming I got
everything off of it, it will be relegated to the spares pile.

I'm going to make a serious effort to post on a daily basis, if only for
my own future reference. I should have the demo of
[RackMan](http://rackman.jasonantman.com) out soon, and I'm also about
to start on integrating it with Nathan Hubbard's
[MachDB](http://www.machdb.org/) as well as a PHP script I wrote to pull
port names and MACs from Cisco switches and associate them with NICs in
machines. Hopefully I'll also have some interesting Puppet stuff out
soon.
