Title: Project Announcement - PHPsa
Date: 2009-09-29 15:36
Author: admin
Category: Projects
Tags: bind, cacti, dns, Nagios, PHPsa, Projects, puppet, rsyslog, sysadmin, syslog
Slug: project-announcement-phpsa

So, here's the "official" scoop on the new project that I'm
planning/starting to work on. I'm calling it PHPsa for now, and it's
going to (hopefully) be an integrated dashboard/portal for SysAdmins.
While there are a number of tools that fit into this general category
(perhaps with [OSSIM](http://www.alienvault.com/home.php?section=News)
being the closest, though it's security-minded), I feel that there's a
real gap in terms of tool integration. My daily workflow, which includes
multiple trips to and correlation among Nagios, Cacti, DNS, DHCP,
Puppet, logs, and other tools really leaves something to be desired. So,
I'm setting out to create a modular SysAdmin dashboard that unifies many
of the common SysAdmin-related tools into a modular dashboard.

The first overall design goals that I've set are:

1.  A modular, plugin-based architecture that allows admins to select
    which features/tools they want, and allows easy development of new
    modules.
2.  Design with legacy tools in mind - easy ways to tie in to tools that
    weren't written with PHPsa in mind, both in terms of linking to
    information and gathering/unifying information.
3.  RBAC, including per-module rules and the possibility for a limited
    read-only view (client/user mode).
4.  Use of data sources, specifically web-based/REST APIs where
    available, and databases otherwise, from existing tools with as
    little modification as possible.
5.  Support for database abstraction, though I'll be using MySQL.
6.  Eventually, implement RSS feeds of pertinent information.
7.  Balance Ajax/DHTML with the desire for important things to have
    canonical, static, bookmark-able URLs.

So, here are some of the things that I'm planning on integrating, with
obvious bias towards getting my own projects done before I integrate
pre-existing tools:

-   [MultiBindAdmin](http://multibindadmin.jasonantman.com), my DNS and
    DHCP administration tool (specifically geared towards split-view DNS
    with the inside view behind NAT).
-   [RackMan](http://rackman.jasonantman.com/), my tool for mapping
    devices' physical locations in racks (and tacking patching).
-   My simple config tool for
    [Puppet](http://reductivelabs.com/products/puppet/).
-   [Nagios](http://nagios.org/).
-   [Cacti](http://www.cacti.net/).
-   Nathan Hubbard's [MachDB](http://www.machdb.org/).
-   [Bacula](http://www.bacula.org/en/) (monitoring/status only).
-   Syslog via [rsyslog](http://www.rsyslog.com/) (or any other
    syslog-to-SQL solution).
-   Possibly a front-end to [Google
    Analytics](http://www.google.com/analytics/).
-   Some of my custom scripts for graphing SpamAssassin, DNS queries,
    etc.
-   Some sort of Apache log analysis, like
    [Webalizer](http://www.mrunix.net/webalizer/).
-   Mail log analysis, possibly
    [AWstats](http://awstats.sourceforge.net/).

So, the first big issues that I'm going to tackle:

1.  General layout. Specifically, how to handle a more-or-less
    consistent layout while integrating tools that weren't designed for
    PHPsa. I'll probably end up using iFrames (or even a frameset) for
    tools that don't integrate well.
2.  How to correlate data/objects between different tools (i.e. how to
    display information from Nagios, Cacti, MultiBindAdmin and MachDB
    for a given host?).
3.  Do I want to use a templating engine like
    [Smarty](http://www.smarty.net/) or hand-code all of the HTML?
4.  How will I handle plugins?
5.  How much code do I want to re-write and how much can I use as-is
    from other tools? And, on a related note, how much existing data can
    I access easily from other tools, vs having to use grabber scripts
    that dump data in MySQL?

**Update 2010-02-03**: I think this may become a semi-official project
for me at $work, which means that I'll be able to dedicate quite a bit
more time to it. Unfortunately, it also means that I will, most likely,
have to give up Nathan Hubbard's [MachDB](http://www.machdb.org/) in
favor of [OCS Inventory NG](http://www.ocsinventory-ng.org/), a more
mature project that already includes inventory support for Linux,
Windows and Mac.
