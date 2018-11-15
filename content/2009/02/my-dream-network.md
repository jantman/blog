Title: My Dream Network
Date: 2009-02-07 01:15
Author: admin
Category: Miscellaneous
Tags: configuration, dream network, ideal network, management
Slug: my-dream-network

On the same thread as the [last
post](/2009/02/community-datacenter/), some
thoughts on my ideal network, or the hosts on that network:

-   One "gold master" installation/kickstart file of a single chosen
    distro, with a base set of packages, including site-specific
    packages. (or something like this implemented in a configuration
    management system)
-   All new installations performed over the network in an automated
    fashion, and from a local repository.
-   Software updates are automated (either through a configuration
    management tool or something like the behemoth I talked about
    [here](/2008/10/my-biggest-problem-with-linux/))
    and pulled from a local repository (perhaps one which mirrors the
    mainline repos, but only downloads a package the first time it's
    requested?).
-   [Puppet](http://reductivelabs.com/trac/puppet) or
    [CFengine](http://www.cfengine.org/) on each machine. Better than
    just having them is having each machine automatically added when
    it's created. Even better yet would be to have Puppet or CFengine
    combined with something like
    [Cobbler](https://fedorahosted.org/cobbler/), so I can define a new
    machine in {puppet|cfengine}, list its' MAC address, then netboot
    the box and come back in a few hours to have an OS installed,
    packages installed and the machine configured, monitored in Nagios,
    monitored for security and backed up.
-   [Tripwire](http://www.tripwire.com/) or some other sort of security
    software, as well as centralized logging and auditing, on every box.
-   A small number of additional "package groups" to add to the "gold
    master" via config management - something like "web server"
    (Apache2, PHP, MySQL, log analysis for them, etc.), "development
    server" (CVS, debuggers, etc.). These would also update the backup
    system to include appropriate directories, update Nagios configs,
    etc.
-   A good way - if even a human making notes in a per-machine text file
    - of tracking the "little stuff" like that one cron script that
    makes everything work right, the location of that hacked-together
    Python script, etc. A way to easily remember the things needed to
    recreate a box which aren't found in `rpm -qa` or any obvious
    overviews.
-   [Bacula](http://www.bacula.org) or [AMANDA](http://www.amanda.org/)
    setup to backup every box, perhaps with some sort of template system
    for server types - every machine gets `/root` and `/etc` backed up,
    but web servers get `/srv/www` and mail servers get `/var/mail`.
-   Nagios setup to monitor everything logical on every box. Perhaps
    this would use a configuration management engine to handle Nagios
    configs, so that for example if any Proliant hardware is used,
    {config management program} will figure this out, install the HPASM
    packages, put the appropriate check scripts on the box, and update
    the Nagios configs. Likewise, adding Apache to a machine should
    cause it to be monitored in the Nagios configs.

Unfortunately, as I'm not independently wealthy, I don't have the time
to quit my job, wipe every machine I own, and start from scratch. But it
sure would be nice to be able to, one day, start a server farm from
scratch and be able to implement some of these cool things...
