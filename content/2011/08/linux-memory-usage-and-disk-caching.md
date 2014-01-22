Title: Linux Memory Usage and Disk Caching
Date: 2011-08-23 08:17
Author: admin
Category: Tech HowTos
Tags: linux, memory, rsyslog, syslog
Slug: linux-memory-usage-and-disk-caching

I recently added some [Cacti][]-based graphing to a number of
Linux-based servers prior to rolling out a new service. When I was
looking over the performance graphs of the initial testing, I noticed
that memory usage on our [rsyslog][] server was near 98%. Looking at
`top(1)`, I saw numbers that agreed, though processor usage was around
99% idle, and no process appeared to be using more than 1% of memory. It
took me a minute or two to open my eyes and see past the panic of memory
usage, and finally look at the complete output from `free(1)`:

~~~~{.bash}
             total       used       free     shared    buffers     cached
Mem:       8171508    8032632     138876          0     162084    7253716
-/+ buffers/cache:     616832    7554676
Swap:      4192956        152    4192804
~~~~

The pertinent part is the last column: "cached". It slipped my mind that
while rsyslog is writing vast amounts of data to disk, which may or may
not ever be read back, the kernel is using free memory to cache as much
of that as it reliably can. Hence the difference between what the kernel
and userland tools call "free", and what most human beings (or at least
sysadmins) would consider "free" - or, more correctly, "available for
use".

When I get a chance, maybe I'll submit patches to the Cacti Memory Usage
Percent (SNMP) template to either graph cache separately, or remove it
from the total.

Interestingly, I also found a somewhat cute page entitled "Help! Linux
ate my RAM!" at [http://www.linuxatemyram.com/][].

  [Cacti]: http://www.cacti.net
  [rsyslog]: http://www.rsyslog.com
  [http://www.linuxatemyram.com/]: http://www.linuxatemyram.com/
