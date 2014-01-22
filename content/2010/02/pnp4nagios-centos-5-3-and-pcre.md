Title: pnp4nagios, CentOS 5.3 and pcre
Date: 2010-02-11 15:20
Author: admin
Category: Monitoring
Tags: centos, graphing, monitoring, Nagios, pnp4nagios, rpm
Slug: pnp4nagios-centos-5-3-and-pcre

I started testing out the [pnp4nagios][] tool to incorporate graphs of
performance data into [Nagios][]. Despite what [Klein and Sellens][]
suggest (p. 57), I really don't want separate tools for monitoring and
trending. [Cacti][]already handles UPS metrics, switch ports, router
traffic, etc. For everything else - system load, etc. - I see no reason
to have two checks run rather than just one (Nagios).

There was a CentOS package for the older pnp4nagios 0.4.x, but I opted
to build and install the new 0.6.x from source. Unfortunately, I hit one
snag - it requires PCRE compiled with support for Unicode properties,
and I couldn't find any package for CentOS compiled with that option.
So, with a simple edit of the %configure macro in the SPEC file, I built
one. Unfortunately, I wasn't working in a real build environment - just
on one of my web servers - so I only built the .i386 version, but you
can feel free to build from the source rpm.

-   [pcre-6.6-2.7.i386.rpm][]
-   [pcre-devel-6.6-2.7.i386.rpm][]
-   [pcre-6.6-2.7.src.rpm][]

  [pnp4nagios]: http://www.pnp4nagios.org/
  [Nagios]: http://www.nagios.org
  [Klein and Sellens]: http://www.sage.org/pubs/20_numbers/
  [Cacti]: http://www.cacti.net
  [pcre-6.6-2.7.i386.rpm]: http://repo.jasonantman.com/centos/5/local/i386/RPMS/pcre-6.6-2.7.i386.rpm
  [pcre-devel-6.6-2.7.i386.rpm]: http://repo.jasonantman.com/centos/5/local/i386/RPMS/pcre-devel-6.6-2.7.i386.rpm
  [pcre-6.6-2.7.src.rpm]: http://repo.jasonantman.com/centos/5/local/SRPMS/pcre-6.6-2.7.src.rpm
