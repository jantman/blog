Title: Puppet facter facts for syslog daemon type and version, symantec netbackup
Date: 2012-08-25 11:33
Author: admin
Category: Software
Tags: facter, nbu, netbackup, puppet, rsyslog, syslog
Slug: puppet-facter-facts-for-syslog-daemon-type-and-version-symantec-netbackup

I have a few more custom facts that I've added to my
[puppet-facter-facts](https://github.com/jantman/puppet-facter-facts)
github repository:

-   [syslog\_bin](https://github.com/jantman/puppet-facter-facts/blob/master/syslog_bin.rb),
    [syslog\_type](https://github.com/jantman/puppet-facter-facts/blob/master/syslog_type.rb),
    and
    [syslog\_version](https://github.com/jantman/puppet-facter-facts/blob/master/syslog_version.rb)
    - tell the absolute path to the *running* syslog binary, its short
    name (basename), and its version as a string. Currently only know
    about `/sbin/syslogd` and `/sbin/rsyslogd`.
-   [has\_netbackup](https://github.com/jantman/puppet-facter-facts/blob/master/has_netbackup.rb)
    - tests for presence of the `/usr/openv/netbackup/bin` directory,
    created by installation of [Symantec
    Netbackup](http://www.symantec.com/netbackup). Useful for making
    generation of include/exclude files conditional on having NetBackup
    installed.

Hopefully some of these will be of use to someone else as well.
