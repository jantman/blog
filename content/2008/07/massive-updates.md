Title: Massive Updates
Date: 2008-07-17 12:28
Author: admin
Category: Projects
Tags: access point, alix, BlackLabAuth, mythtv, Nagios, pc engines, soekris, tuxostat, WifiDog, wireless
Slug: massive-updates

I know I've been quite for a while. I've been quite busy. Unfortunately,
due to changing priorities, there are a lot of projects I've been
working on, but few of them have gotten finished. A sampling, in no
specific order:

-   Migrating my network/service monitoring to Nagios 3, *totally*
    re-writing my config files to make use of the new features, and
    making one coherent list of all the services that should be in it
    and aren't.
-   Planning to totally re-wire all networking at the [ambulance corps
    building][] to eliminate some problems. This includes *building* an
    8U wall-mount rack, and also trying a [PC Engines ALIX.2c1][] board
    as a router (still undecided on WAN/LAN/DMZ or WAN/LAN/WLAN). It
    also means a long day of work at some point in the future, and lots
    of cable drops.
-   [tuxOstat][], the linux-controlled thermostat, is pretty much on the
    back burner. It's a stable beta with severely reduced functionality,
    but has been handling my cooling needs without any major bugs in the
    past month or so. It still only has a basic CLI interface and a very
    simple kludge of a web GUI, but it works. Other modes (heating, fan
    only), predictive temperature calculation, other temperature/zone
    calculation modes, and physical controls (buttons, menu on LCD) are
    still to come, as well as the move from PC to Soekris (if I can ever
    figure it out, and get one with USB). I now feel that an ALIX board
    might be a better shot, as they take CF (more space than the
    Soekris), have a slightly faster processor, and also support USB at
    about half the price point.
-   I'm considering moving my main web site to a CMS, and letting the
    [wiki][] serve more as a knowledge base.
-   I'm working on patching together a new access point for the
    ambulance corps, based on [Pyramid Linux][]. I needed something
    which would run on the Soekris net4526, had at least WEP, and
    supported some sort of captive portal. Pyramid has [WifiDog][], but
    that only wants to do local authentication or RADIUS, and I wanted
    direct auth to LDAP and MySQL logging. On the positive side, it just
    uses some PHP pages hosted under Apache to handle authentication -
    the WAP redirects the user to a login page on a (separate) web
    server, the user does their stuff, and then the WAP makes a request
    to the server to determine whether it should open up the firewall,
    keep the user locked down, or totally kick them. So, once I figure
    out some routing issues, I'll get back to working on the new project
    - [BlackLabAuth][], a re-write of the WifiDog auth server software
    that's geared towards a closed-access network (i.e. only people
    and/or MACs already listed in LDAP can login) with full logging to
    MySQL. I already have some code [in CVS][], but some issues with my
    development Soekris board have slowed the project for the time
    being. When finished, I'll have not only the new auth server
    available for download (with documentation) but also a ready-to-run
    (well, some configuration time needed, but minor and scripted) image
    for the net4526.
-   My desktop that I use for [MythTV][] filled up its' disk. Totally. I
    ordered a cheap Syba SATA card (PCI) from NewEgg, along with a 500GB
    WD SATA-150 disk, but no luck. Though the card (Syba / Initio 1622
    chipset, shows up as Class 0106: 1101:1622 (rev 02)) said it was
    supported under Linux, the driver CD mentioned nothing about it.
    Some investigation on the Syba website turned up a zipped archive.
    After extraction, I found a readme that gave (poor) instructions on
    how to re-compile a kernel, and warned that you MUST have 2.6.15. Oh
    well, I wasn't going to give up 2.6.16.27 (the newest RPM'd kernel
    for OpenSuSE 10.1). The standard drivers for it didn't appear until
    2.6.25 or so. So... after many debates with myself as to whether I
    should blow away my whole MythTV installation and upgrade from the
    now-ancient 10.1, I decided that I'll only be in my apartment for
    another year, I should make it last. Some investigation turned up a
    $24 Silicon Image-based card that should work fine, and it's now in
    the mail...

I'm sure I missed something big, but I'll update as needed, and attempt
to make it a daily habit to post something interesting or, at the very
least, hard-to-find. After all, I'm sure that I use this blog and my
wiki as an informational resource (my bad memory) more than anyone else
would...

  [ambulance corps building]: http://www.midlandparkambulance.com
  [PC Engines ALIX.2c1]: http://www.pcengines.ch/alix2c1.htm
  [tuxOstat]: http://tuxostat.jasonantman.com
  [wiki]: http://www.jasonantman.com/wiki/
  [Pyramid Linux]: http://pyramid.metrix.net/
  [WifiDog]: http://dev.wifidog.org/
  [BlackLabAuth]: http://blacklabauth.jasonantman.com/
  [in CVS]: http://cvs.jasonantman.com/BlackLabAuth
  [MythTV]: http://www.mythtv.org/
