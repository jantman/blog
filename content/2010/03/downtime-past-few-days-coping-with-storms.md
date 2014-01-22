Title: Downtime past few days, coping with storms
Date: 2010-03-17 22:27
Author: admin
Category: Miscellaneous
Tags: availability, power, reliability, UPS, uptime
Slug: downtime-past-few-days-coping-with-storms

As far as I can see from [Google Analytics][], though I'm now up to
about 4,000 visitors per month for this blog, it seems like most are
one-time visitors. So hopefully the few hiccups of the past few days
weren't noticed (except by me, and my mailserver...). As many of you in
the US may know, New Jersey was hit by a pretty big nor'easter last
weekend and my area was [especially][] [hard][] [hit][]. I lost power
for about five hours Saturday night (the 13th) and again for an hour or
so the next morning. Needless to say, these were both much longer than
my small UPSes could cope with (the smaller of the two has a mere 12
minutes of runtime with brand new batteries). While I do have a small
(2500W) gas generator, it was buried in the back of the garage. The time
it would take to dig it out and string extension cords from the UPSes to
a relatively dry area outside would probably be more than 12 minutes -
not to mention that as first lieutenant (second-in-command) of the
town's volunteer [ambulance corps][], I was running in the opposite
direction once things got bad.

Luckily, the problems caused or uncovered by the power loss were
relatively minor:

1.  The batteries in my smaller UPS lasted about 90 seconds. I'd noticed
    the bad battery light a few weeks ago, but put it off (hey, it's my
    home setup, I don't exactly have a budget). [RefurbUPS][], where I
    got the two APC SU1000NET's, got me a replacement RBC6 (aftermarket,
    not original APC) in two days, for around $73. Unfortunately, my
    Tripp Lite SMART2200RMXL2U (unfortunately without the external
    battery pack) also just had its orange light pop on, so there goes
    another $90.
2.  The battery replacement caused another short (\~5 minute) downtime
    tonight, including my router. Unfortunately the router is plugged
    into the smaller of the two UPSes, and none of my current boxes have
    more than one power supply. Mistake. Especially considering my
    limited resources. On the positive side, I took the opportunity to
    move all of the equipment onto [Liebert MicroPOD][]s.
3.  The external SATA disk for my desktop used to store media is dead.
    I'm getting incessant read errors, followed by offlining the disk,
    on two USB adapters and internal SATA. I guess I should have a
    better surge protector for the desktop.
4.  A few of my boxes didn't come up clean, mainly due to entropy in the
    configs, or services that were never `chkconfig`'ed. Well, I don't
    use any configuration management at home.
5.  One of the disks in my storage server (RAID 1+0 of 6x 36.4Gb 10k RPM
    SCSI disks) died - actually a few days before the power outage. I
    was able to find a new replacement on Ebay, with warranty, for about
    $40.
6.  Many of my internal services - including a lot of the [Nagios][]
    checks - use a separate gigabit management network, run off of an
    older GigE aggregation switch. This was on the smaller UPS, so it
    went down quick. As both this and my main switch are of the same
    series, perhaps an RPS unit would be worth the money.

Plans for the future:

-   Get [Puppet][] working at home. As part of this, buy a spare server
    so I can migrate services one at a time to a puppet-ized version,
    test, and then rebuild (while the production machine is still
    running).
-   In the future, given my limited infrastructure, purchasing dual
    power supply machines - and putting the PSes on separate UPSes -
    would be a good thing.
-   Configure the Tripp Lite UPS to do load shedding.
-   Setup UPS management software to bring down boxes in a logical
    order.
-   Power savings is also important - so I'm thinking about rebuilding
    things using [Xen][], and using live migration to both distribute
    load logically under normal circumstances, and to move around loads
    in the event of power failure (kill non-critical/internal-only
    stuff, consolidate the rest).

  [Google Analytics]: http://www.google.com/analytics/
  [especially]: http://www.northjersey.com/news/bergen/87665172_Weekend_storm_thrashes_Wyckoff.html
  [hard]: http://www.northjersey.com/news/87704777_Ridgewood_power_outages_could_last_for_days.html
  [hit]: http://www.northjersey.com/news/87852727_Downed_trees__power_lines_bring_Glen_Rock_to_a_near_standstill.html
  [ambulance corps]: http://www.midlandparkambulance.com/
  [RefurbUPS]: http://www.refurbups.com
  [Liebert MicroPOD]: http://www.liebert.com/product_pages/Product.aspx?id=6&hz=60
  [Nagios]: http://www.nagios.org
  [Puppet]: http://reductivelabs.com/products/puppet/
  [Xen]: http://www.xen.org/
