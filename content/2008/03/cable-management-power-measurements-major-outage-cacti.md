Title: Cable Management, Power Measurements, Major Outage, Cacti
Date: 2008-03-06 01:02
Author: admin
Category: Projects
Tags: apc, cable management, cacti, disaster, monitoring, power distribution, power failure, rack, UPS
Slug: cable-management-power-measurements-major-outage-cacti

So, once again, still really busy. But a few new things.

First, my racks both at home and at the apartment are atrocious. They
have no cable management at all. Both started with 1-3 machines, and no
real plans for upgrades (since they're just my personal/development
machines). Unfortunately, the "rack" (a metal workshop shelving unit) at
home now has 8 machines and a host of ancillary equipment. The one at
the apartment - an actual 42U rack - has 5 plus a few switches,
rackmount KMM, etc. They're both a jumble of wires in the back.
Unfortunately, it seems like cable management hardware is \*epxensive\*.
$30 for a 2U metal blank with a few plastic split D-rings, or almost $40
for a 2-meter vertical hunk of plastic channel with slits in the sides?
So, I've been vaguely considering what it will take to fabricate some
cable management hardware of my own. Probably just building something
out of rack blanks for the horizontal off of the switches, and buying
some sort of vertical channel for power and networking/KVM. Man, those
KVM cables sure do take up a lot of space. Also at the moment, at home
my power is all coming directly out of two UPSs, whereas at the
apartment it's straight from mains off of a surge suppressor. I's like
to buy another UPS for the apartment from RefurbUPS.com, where I got the
ones from home, and also add a PDU at home and a vertical power strip at
the apartment.

Also, at the apartment, the roommates and I have had some discussion
lately about how much power the machines draw. This mainly stemmed from
our plans to move this June, into a rented house with two more people.
This seems to be falling through, so I don't have to worry about moving
and re-cabling everything, but I'm still interested in finding out how
much power is being drawn. Granted, my UPSs at home give me a
more-or-less good idea of power consumption, but I'd like to know in
detail. The ideal solution would be a clamp ammeter around the mains
line to the equipment - one with a serial interface. Unfortunately, I
can't seem to find such a thing, short of a digital multimeter left on
all the time. So, I guess I'll be looking around, and if I can't find
anything specific, maybe I'll work on a microcontroller that can read
1-200mV in 1mV increments, and use it with an inductive clamp ammeter
(usual output for them is 1mV per A).

So, on Monday I got into work and couldn't access my mailserver. Weird.
I never even got any Nagios alerts. I checked Nagios and... nothing. As
in no connection. I SSH'd home and pinged both boxes, but nothing. The
switch showed the mail server totally offline, and the Nagios box
plugged connected but ZERO data out. I reset the counters and waited.
Still nothing. After an hour or so of poking around, I determined that
both devices were on the same 6-port group on the switch, and nothing
else there was up too. So, after five long hours, I got someone back
home to switch the cables. Still nothing. On a hunch, I asked to have
her check the mail server (the "new" Sun Blade 150) and, sure enough, it
wasn't powered on. A click of the power button, and the mail server was
back online. Along with an ominous last email from Nagios, stating that
the UPS running my switch lost power, and 6 minutes later, was going
down hard. Then quiet.

I don't usually have power outages. So I'll admit, when I added some of
the new machines, I committed a high sin - I "never got around" to
setting up everything power-wise. I also have the switch running off of
an old BackUPS 500VA unit, USB, without automatic self-tests. As a
result of all this:

1.  The little UPS powering the switch only held out for 6-7 minutes. As
    a result, once that died, the bigger units didn't even matter, as
    all hope was lost. This needs to be on a bigger UPS - maybe one of
    the 1000VA's until it gets its' own.
2.  APCupsd requires a network to initiate shutdown, so the rest of the
    machines came down hard (as confirmed by looking through log files).
3.  The SunBlade was never setup to power on after power interruption,
    so it just sat there like a brick.

Most disturbingly, while my Nagios/monitoring box is up (according to
the switch, power draw figures from the UPS, and the lights, as
confirmed by someone on-site), it's dead. No ping, nothing out. I'll
have to look into it, but it made me realize that this really is my only
way of analyzing problems. That needs to stop.

Maybe one day I'll have the money for a nice [SmartUPS RT][] or even a
[Symmetra][] - though getting 208V into my basement is even more of a
dream than spending $4000 on a UPS.

Also, I decided (after all this) to setup graphing of UPS data (load,
voltage in and out, temp, capacity, run time, etc.). While I haven't
gotten around to setting up [Zenoss][] yet, I did a quick (well, 4 hours
later I'm done configuring it) [Cacti][]installation on my web server (I
should already have it running on the monitoring box, but who knows what
that will look like when I get home). I also dropped a [Cacti host
template in CVS][] for the [AP9605 PowerNet SNMP card][] in my UPSs.

  [SmartUPS RT]: http://www.apc.com/products/family/index.cfm?id=223
  [Symmetra]: http://www.apc.com/products/family/index.cfm?id=189
  [Zenoss]: http://www.zenoss.com/
  [Cacti]: http://www.cacti.net/
  [Cacti host template in CVS]: http://cvs.jasonantman.com/cvs/misc-scripts/cacti_host_template_apc_powernet_ap9605.xml?view=log
  [AP9605 PowerNet SNMP card]: http://www.jasonantman.com/blog/2007/03/apc-ap9605-powernet-snmp-card.html
