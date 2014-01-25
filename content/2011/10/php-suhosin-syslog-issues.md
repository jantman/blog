Title: php-suhosin syslog issues
Date: 2011-10-21 10:24
Author: admin
Category: Tech HowTos
Tags: centos, logging, PHP, security, suhosin, syslog
Slug: php-suhosin-syslog-issues

I just installed php-[suhosin](http://www.hardened-php.net/suhosin/)
0.9.29 from EPEL on a CentOS 5.6 box. I'm running a whole bunch of
name-based vhosts in Apache, and have a bunch of web apps, so I opted to
run suhosin in simulation mode (don't actually block anything, but log
errors) and have it log via syslog to a single file. Unfortunately, when
I configured this, the syslog messages started showing up in the wrong
place, apparently with the wrong facility *and* priority. After some
roundabout debugging (at first assuming syslogd to be the problem), I
determined that, for whatever really strange reason (perhaps an
incorrect syslog.h on the EPEL box that built the suhosin package?) the
LOG\_\* constants were incorrect. I looked up the correct integer values
in `/usr/include/sys/syslog.h` and the following configuration
directives accomplished the task correctly:

~~~~{.ini}
suhosin.log.syslog.facility = 128
; 128 = LOG_LOCAL0

suhosin.log.syslog.priority = 5
; 5 = LOG_NOTICE
~~~~

This one line puts suhosin into simulation mode, where it only logs
errors instead of enforcing on them:

~~~~{.ini}
suhosin.simulation = On
~~~~
