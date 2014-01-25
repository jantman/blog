Title: Switch Shopping; the Law of Gross Tonnage
Date: 2008-04-02 16:25
Author: admin
Category: Miscellaneous
Tags: driving, gigabit, switch
Slug: switch-shopping-the-law-of-gross-tonnage

<p>
Well, I'm shopping for a new switch. But first, a small aside:  

> I drive a [Ford
> F-250](http://www.jasonantman.com/wiki/index.php/Image:TruckMed.jpg).
> It's a pretty big truck. And every once in a while, someone cuts me
> off in something like a [Honda
> Fit](http://automobiles.honda.com/fit/). It really makes me stop and
> wonder - how stupid are they? I'll admit that after two and a half
> years of driving a 13,000 pound
> [ambulance](http://www.midlandparkambulance.com/albums/The%20New%20588.php)
> in my spare time, I know a bit about the maneuverability problems of
> large vehicles. But I have to assume that the average driver, when
> confronted with something like my truck - 6500 pounds empty, 21 feet
> long and tall enough that the hood is at the level of the roof of most
> passenger cars - they'd think twice about doing something stupid. I
> won't even mention the people who cut off or tailgate dump trucks and
> semi's.
>
> </p>
> I've spent a bit of time on the water throughout my life. Piloting a
> boat isn't especially difficult, but there are a few things you learn
> about navigation. One of them is affectionately known as [The Law of
> Gross Tonnage](http://www.auxguidanceskills.info/press/bigger.html).
> It's really simple. Big things take a long time to stop, and can't
> maneuver very well. So stay out of their way. So I have to wonder, why
> don't they include this in driver's manuals? Sure, people do stupid
> things. Some people just have to, it's part of their nature. But if
> they're going to, why can't they be smart, and choose to do it in
> front (or behind) of a vehicle that actually has a chance of stopping?

In other news, I'm starting to shop for a new switch. At the moment, my
network at home (hosting this blog/site and everything else) is running
on a single, ancient, Rutgers University surplus [Bay Networks BaySTack
450-24T](http://www.jasonantman.com/wiki/index.php/BayStack_450-24T).
It's served me well (and it server Rutgers well before me) but it's time
for an upgrade. While it's a manageable switch, it's only capable of
100Base-TX. And streaming a few gigs of backups over it every night
isn't fun, not to mention attempting a network install of a full OS.

So, it's time to shop for a new switch. Depending on budget, I've
identified two possible configurations:

1.  Get a new 10/100 manageable switch for the main network, and buy a
    desktop 8- to 12-port Gigabit Ethernet switch for a dedicated backup
    LAN.
2.  Bite the bullet and buy a Gigabit manageable switch.

If possible, I'm leaning towards the second option. My budget puts me in
the market for what are normally considered edge switches, and Gigabit
is just arriving in that land (heck, the dictionary in my browser
doesn't even know it's a word). The bottom line is that it's going to be
a long time before anything faster than Gigabit makes it to most
desktops. So, I'm distinctly aware of the possibility of needing a
manageable switch and eventually implementing 802.1ad link aggregation
to increase bandwidth to the backup server and other key machines.

The major features I'm interested in:

-   19" rack mount form factor, at least 16 ports (24 would be good) all
    at Gigabit speeds.
-   Something from a good manufacturer, not a white-box or house brand.
    Good support.
-   Extensive manageability - at a minimum, SNMP and Telnet. Hopefully
    RMON.
-   802.1Q VLANS
-   Good options for firmware upgrades, and not anything that requires a
    service contract (i.e. Cisco).
-   802.3ad Link Aggregation (at a minimum, supporting 3 systems with
    2-4 links each).
-   Port mirroring.
-   Support for QoS/CoS - at a minimum, 802.1p.
-   Acceptable MTBF.

Some added bonuses that I'd really like:

-   Support for syslog to a separate machine.
-   SFP slots so I can move to a faster backbone switch in the future,
    or move key systems to fiber or a faster standard.
-   Even more management - SSH would be nice, as would RADIUS or TATACS
    authentication.
-   A good switch fabric capacity - 32Gbps or higher for a 24-port.
-   802.3af Power over Ethernet. (Well, I could always use injectors)
-   MAC filtering, ACLs, and/or 802.1x NAC.
-   802.1ab LLDP.

I'll keep looking around and pricing things out. My hard budget is $500,
but it would take a lot to get me to spend that much. I'm probably
looking for something closer to the $300 range, probably lightly used or
refurbished. If anyone happens to see this and has a suggestion, feel
free to share!
