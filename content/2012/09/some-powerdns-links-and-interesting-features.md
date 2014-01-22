Title: Some PowerDNS Links and Interesting Features
Date: 2012-09-05 05:00
Author: admin
Category: SysAdmin
Tags: bind, dns, multibindadmin, powerdns
Slug: some-powerdns-links-and-interesting-features

At $WORK we lost a disk in the RAID1 of one of our external nameservers,
and it rekindled an occasional discussion of migration from <a>ISC
BIND</a> to [PowerDNS][]. PowerDNS has separate authoritative and
recursive servers, and doesn't seem to natively support views or
split-horizon the way BIND does, but it has some really cool features
including very mature database backends, load balancing, Lua scripting
support to modify how recursive queries are answered, and geolocation or
IP-range based query results.

While this project is still just casual research, I thought I'd share
some of the useful links and information I've found:

PowerDNS Front-ends:

-   [JPowerAdmin][] - One of the two most popular, a GPLv3 Java (JBoss
    SEAM) based web UI with a RESTful API, with support for "multiple"
    database backends. Sponsored by Nicmus, Inc. [Online demo][]
    (demo:demo). Looks nice, simple UI, but no support for
    split-horizon.
-   [PowerAdmin][] - the other most popular, though it seems to be
    undergoing a large overhaul at the moment. Has full support for most
    of PowerDNS's features, written in PHP, supports "large" databases,
    fine-grained user permissions, RFC validation, zone templates.
    [Online demo][1] (demo:demo). I don't really like that it manages
    the SOAs as full text (without any templating, dropdowns or default
    values), and that it doesn't prepopulate default values for TTL in
    the new record form, but it looks like a good starting place for
    someone (like me) who's handy with PHP.
-   [pdns-gui - PowerDNS GUI - Google Project Hosting][] - PHP/MySQL
    GUI. [Online demo][2]. Handles templates nicely but won't scale to
    too many of them. Window-based UI is visually pleasing but will
    probably be a problem for big zones.
-   [powerdns-webinterface - PowerDNS Webinterface - Google Project
    Hosting][] - A nice but relatively simplistic UI written in PHP. It
    has some nice features like multi-user authentication (and logging,
    though I haven't looked into how detailed it is), automatic SOA
    serial update, automatic PTR creation, etc. Unfortunately not geared
    towards people with lots of domains and multiple records; it has
    only one template for new domains (and no way to update domains
    created from a template), no easy filtering, and still treats SOA
    like a single text record.
-   [ZoneAdmin | SourceForge.net][] and <a>Project website</a> - Maybe
    not the fastest tool to use in bulk, but a nice, relatively
    intuitive and full-featured admin tool. [Online demo][3]
    (demo:demo).

Some links on PowerDNS split-horizon

-   [Old Nabble - PowerDNS - Split Horizon Scripts][]

It looks to me that split-horizon is going to be the hardest part for
us, at least to also have a web UI to manage it. It looks like with
PowerDNS, the most common way to run split horizon DNS (views) is to run
two separate sets of servers or instances, either on different boxes or
multi-homed; one for internal and one for external. While that sounds
like quite a bit of overhead beyond what BIND does, the real problem is
finding a web UI that supports it; I don't care if it's in two separate
databases, but what I want is a logical (web UI) view that has zones
made up of resource names (i.e. the leftmost column in a zone file) with
one or two RRs (type, ttl, priority, value) - one for each view. That's
the real catch - all of our machines are in private IP space behind a
firewall, so I need to be able to manage the internal and external
records on one screen. While it's not exactly scalable, and the code
stagnated quite a bit once I got it to a point that was usable for me,
this was the main goal of my [MultiBIND Admin][] project.

  [PowerDNS]: http://powerdns.com/content/products.html
  [JPowerAdmin]: http://www.nicmus.com/community.html
  [Online demo]: http://www.nicmus.com/JPowerAdmin
  [PowerAdmin]: https://www.poweradmin.org
  [1]: http://demo.poweradmin.org/
  [pdns-gui - PowerDNS GUI - Google Project Hosting]: http://code.google.com/p/pdns-gui/
  [2]: http://www.powerdns-gui.org/
  [powerdns-webinterface - PowerDNS Webinterface - Google Project
  Hosting]: http://code.google.com/p/powerdns-webinterface/
  [ZoneAdmin | SourceForge.net]: http://sourceforge.net/projects/zoneadmin/
  [3]: http://open.megabit.net/demos/ZoneAdmin/
  [Old Nabble - PowerDNS - Split Horizon Scripts]: http://old.nabble.com/Split-Horizon-Scripts-td32843045.html
  [MultiBIND Admin]: http://multibindadmin.jasonantman.com/
