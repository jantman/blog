Title: Big Plans - Major Infrastructure Upgrades
Date: 2008-02-05 01:36
Author: admin
Category: Projects
Slug: big-plans-major-infrastructure-upgrades

Well, some more news. I've got some pay coming to me, and I also
realized that I have literally a *pile* of Dell server rack rails, cable
management parts, and front bezels/panels (that I got from [Rutgers
Unversity Surplus](http://www.material.rutgers.edu/surplussales.shtml))
to sell on [EBay](http://myworld.ebay.com/jason-antman/). So, aside from
expenses (like $45/month for Verizon data service on my wonderful [Treo
700p](http://www.palm.com/us/products/smartphones/treo700p/)) and
savings, I decided that I should make some infrastructure upgrades to
jasonantman.com.

Just figuring out what to do was a task. I'll admit that my
administration techniques haven't really scaled with the network, so I
clicked into my [Nagios](http://www.nagios.org/) installation, and
remembered that I'm monitoring 17 hosts (and 165 services), I realized
that this will end up being a big project, both in terms of
infrastructure/hardware and software. The first decision was that I
wouldn't do anything with the hosts at the [ambulance
corps](http://www.midlandparkambulance.com/) or my apartment (the
apartment is all non-mission-critical), so that narrowed it down to the
main seven systems at home.

Figuring out what I have running was also a major task, and highlighted
some real problems. I found [a Perl script that gathers hardware
information on Linux-based
systems](http://www.dracoware.com/ppl/rtwomey/inventory.shtml) from
[Ryan Twomey](http://www.dracoware.com/ppl/rtwomey/index.html)
(*everything* is running some version of
[OpenSuSE](http://www.opensuse.org/) 10.x except for the mailserver,
which runs [Sun Solaris 10](http://www.sun.com/software/solaris/)). I
had to scp the script and its' two perl modules to five machines (not
counting the one I was working on), SSH into them an run it, and then
SCP the results back. Well, that's something to worry about later. For
Solaris, I just ran some commands and gathered the information
manually.  

# The Results:

## Needs Replacing:

1.  Router/Firewall - Old gateway mini-tower system, 400MHz Celeron,
    192MB RAM, 6 GB IDE disk.
2.  SSH gateway and temporary storage for SFTP'd files - Old Gateway
    G6-350, 350MHz Pentium-II, 128MB RAM (**!!!**), 40GB IDE disk.
3.  Disk storage for backups - Old Dell tower, 500MHz Pentium-II, 256MB
    RAM, 250GB IDE disk for storage.

## Still has a ways to go:

1.  Web Server - Compaq Proliant DL360-G1, 2x 1GHz Pentium-III, 1GB RAM,
    2x 18GB SCSI disks, RAID-1.
2.  Backup Director (and mirrored disk storage for critical backups) -
    Compaq Proliant ML370-G1, 2x 750MHz Pentium-III, 2GB RAM, 4x 18GB
    SCSI disks in a 3-disk RAID5 with one hot spare.
3.  Monitoring (Nagios) box - Compaq Proliant DL320-G1, single
    Pentium-III 1GHz, 512MB RAM, single 18GB SCSI disk.

The one unfortunate about these (for me, "new") machines is that they
all have 10/100 Mb/s NICs, so an upgrade to gigabit will mean hardware
changes.

And the rest falls somewhere in the middle. One option, if budget is an
issue, is to move an older machine down to the apartment to use as a
print server for [print
accounting](http://www.jasonantman.com/blog/2007/11/print-accounting.html),
which is currently running in a Xen VM as the *only* load on a beautiful
1U Dell PowerEdge 650 (Pentium-4 2.4GHz, 762MB RAM, 2x 36GB SCSI disks,
3com 10/100 NIC and Intel Pro Dual-Gigabit NIC).  

## Other acquisitions on the list:

1.  New switch to replace the aged [BayStack 450-24T
    switch](http://www.jasonantman.com/wiki/index.php/BayStack_450-24T)
    that *everything* is running on now. I'm looking for something good,
    managed, with Telnet (or SSH) and SNMP for monitoring, as well as
    the easy ability to do a span port. The important thing is that I
    \*never\* have to be on-site to manage it. Maybe a Cisco if I can
    choose a model and get the cash together.
2.  A gigabit (even unmanaged, though SNMP monitoring and MRTG/Cacti
    would be nice) switch for a dedicated backup network, to move that
    load off of the little 100Mbps main switch.
3.  Right now, I just have everything [crammed onto a Sears metal shop
    shelf
    unit](http://www.jasonantman.com/wiki/index.php/Jasonantman.com_Hardware).
    I'd really like to replace that with a nice little 24U (low ceilings
    in the basement) rack, especially since most of my stuff is
    rack-mount.
4.  I don't have rack rails for any of the Proliants - none of them came
    with them, and they were all purchased before I had anything rack
    mounted (at the apartment).

# Software Needs:

1.  Obviously, some better way of handling administration. Right now,
    software updates (via YaST/YOU) are run as cron jobs, and I have no
    easy way of distributing files or running commands on multiple
    systems without manually scp/ssh'ing to all of them
2.  I'm going to start testing some other [Network
    Monitoring](http://www.jasonantman.com/blog/2008/01/network-monitoring.html)
    packages at the apartment. Since I'm going to have some scheduled
    downtime for all of this (especially with a router/firewall
    replacement), I might as well plan a move to a new monitoring
    system.
3.  At the moment, all of my web presence is on one Generation-1 (G-I)
    Compaq Proliant server. While it seems to have a lot of life left
    (especially under its' current low load), I don't like that.
    Especially given that I'm only home every other weekend, so even
    with nightly backups, if it gives up the ghost I'm down for a while.
    I'm going to think about mirroring this to a box at the apartment
    (see both items below), but there are still some technical issues to
    be dealt with:  
   1.  Both home and the apartment are on residential high-bandwidth
        connections ([Verizon FiOS](http://www.verizon.com/fios) and
        [Optimum Online](http://www.optimum.com/), respectively) using
        [DynDNS.org](http://www.dyndns.org/) with dynamic IPs. I still
        haven't been able to get [IPcop](http://ipcop.org/) to VPN
        between the two (either with the built-in VPN or Zerina). If I
        wanted to mirror to the apartment, it would surely be easier to
        copy everything over a VPN, and not worry as much about
        security.
    2.  I use DynDNS and [GoDaddy](http://www.godaddy.com/) (yes, this
        years' Super Bowl commercial was a letdown) Domain Forwarding.
        As a result, I don't have any control over DNS at all, so I'm
        not quite sure how I'd do a failover from home to the apartment
        automatically. It would be possible, however, to do the manual
        failover from home to the apartment, just for the downtime, if I
        mirrored the home server to a box at the apartment.

    While I don't want to give up my email on my Treo, it is tempting
    that Verizon FiOS is now listing [a business-class FiOS connection
    at 3Mbps down/768Kbps
    up](http://www22.verizon.com/content/businessdsl/popups/bdsl+speeds+and+package+features/bdsl+speeds+and+package+features.htm)
    at $80/month with *static IP*. We're paying $30-40/month now, so
    dropping the data plan would cover it. I'd be getting slightly lower
    speed, but there would be so many fewer headaches with a static IP,
    not to mention that I could finally get my site on port 80 without
    nasty redirection, and get a real mailserver without relaying.
    Something to think about...
4.  At the moment, I'm using IPcop's builtin DNS cache for local DNS.
    That means I'm bound to a simple hostname<-\>IP pairing. I'd really
    like a real DNS server, so that I can have both hostnames and
    functional names. It would also help with VPN.

The biggest problem with all of this is that I'm only home 2 weekends a
month, so I'll probably have to have everything shipped here (to the
apartment at school), do the installation and configuration here, and
then bring it home and drop it in place (and perform final
configuration).

I'll keep everyone posted as work progresses.
