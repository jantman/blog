Title: Downtime Last Night; Coping with outages on a shoestring budget
Date: 2011-01-10 09:22
Author: admin
Category: Projects
Tags: disaster recovery, downtime, failover, redundancy
Slug: downtime-last-night-coping-with-outages-on-a-shoestring-budget

Anyone who tried to visit any of my sites last night, or send me email,
probably noticed that I dropped off the face of the earth. I take my
uptime pretty seriously - even with virtually no budget, about 10
minutes of UPS time, and everything hosted out of my basement. I've only
had about a [6-hour block of
downtime](/2010/03/downtime-past-few-days-coping-with-storms/) in the
past 21 months, aside from that nothing externally visible except a few
sub-3-minute hiccups. And the 6 hours was due to a major power outage
that quickly overwhelmed my UPS. Without a generator, I can't really
blame anyone for that. Anyway, last night into this morning I had
partial to full outages for about 12 hours. By far the most I've had
since I literally ripped apart my entire infrastructure, moved it from
shelves to a rack, and put it back together on the fly.

I'd like to apologize to the few people whose web sites or other
services I host out of my house. On one hand, I think those few people
are getting their money's worth from their free hosting :) On the other
hand I know how frustrating it can be, especially when you can't even
resolve DNS and my email is down. Rest assured that this situation
deeply bothers me, and I'm already hard at work on plans to at least
keep people (both the people I do hosting for and their visitors)
informed if something like this should happen in the future.

**The Story:**

Well, yesterday afternoon as I was at my father's house about an hour
away, I started to get a slew of [Nagios](http://www.nagios.org)
notification SMSes (well, email to SMS). They started at 14:22 and
stopped after a few minutes, but since I was driving, I didn't check
them. When I got home, I found a scenario I hadn't really anticipated -
the TV worked fine, but I had virtually no connectivity on my cable
Internet line. I got home around 16:22 and had spotty-at-best
connectivity. I could get some DNS in and out, but it was pretty much
impossible to load a web page on my desktop. I was getting Nagios alerts
out in bursts, and the postfix queue was pretty full. A cursory
inspection showed both routers (mine and Optimum's) online with link,
the Modem had link and was blinking away, but I was passing < 100 Kbps
of data. My DOCSIS-MIB checks on the cable modem were spitting back all
sorts of bad values. Not good. I checked coax connections, rebooted the
modem and router, and went outside to inspect the aerials and the
splitters on the outside of the house. Nothing visibly wrong, and no
positive change after the reboot. Now the modem wasn't showing link at
all, and I couldn't even ping its LAN IP.

I called Optimum at 17:12 and went through the initial troubleshooting
with the technical support guy. I told him I'd already power-cycled the
modem, and gave him a rundown of the status lights. He confirmed that
they couldn't even see the modem on the WAN side, and would have to send
a tech out. The big plus to Optimum Business is that, despite it being
after 5 PM on a Sunday night, I was given an ETA of 2-4 hours. After
about 15 minutes, I power-cycled the modem again, and was able to get
link. I was seeing some data pushed through the routers, but only about
50Kbps. I called Optimum back, spoke with another tech, and was told
that they couldn't even get diagnostics back from the modem, and were
seeing 94% packet loss on ping. Time to wait for the tech.

The field tech arrived at 17:53. Utterly amazing... about 30 minutes
after I got off the phone with tech support. I don't know if they keep
their better techs waiting around for business customers, but this guy -
Jason - was one of the most knowledgeable and experienced that I've ever
met. He poked around the modem a bit, re-did some of the shoddy work
that the original installers left, and then climbed the pole to figure
out what was going on. About half an hour later, he came back with the
bad news. His test scope wouldn't even lock on to the 609MHz carrier
used for the cable modem, so there was something definitely wrong, and
it was past the pole in front of the house. He told me they'd need to
escalate the problem to the outside plant engineers, but since I was a
business customer, I could expect some update or fix in 6-18 hours. He
left around 18:30. Well, I was bummed, but I used the time to get other
stuff done and start planning for at least minimal DR plans for the
future.

According to my off-site Nagios, I at least got some mail out and SSH in
from 19:55 to 20:44, and then had another total loss of connectivity.
Everything came back around 02:20 today, meaning a full 12 hours of
downtime.

**Analysis and Future Plans:**

Well for the foreseeable future I'm just working my day job and probably
not doing much (paid) consulting, so purchasing a backup connection is
out of the question - especially since FiOS charges almost twice what
Optimum does for static IP service. There's really no way I could've
prevented this outage, and it turns out that the problem wasn't even on
my property, so it's not anything I could have fixed myself (or
prevented by convincing Optimum to let me purchase a spare modem to keep
on hand). Once again, for something that isn't directly money-making for
me, it's not really worth it to try and get hosting as a backup, since
I've got all sorts of complex postfix configurations, BIND master/slave
replication, etc. Within my budget, I can't really say there's anything
I could do to solve this problem, or to get even half of my services
back up. My offsite Nagios is behind a dynamic residential cable
connection, so that won't really fix any problems either.

My plan for the short-term is to find a static IP somewhere that I can
run a box behind, add it as a NS record, and at the minimum setup a
caching Postfix server, a catch-all Apache server with a "we know about
it, we're coming back soon" page, and hacked BIND zone files that point
everything at this one box (albeit with a low TTL).

If anyone out there happens to read this, any comments on how to deal
with a total loss of connectivity on a budget of, say, $15/month above
the cost of my Optimum connection??
