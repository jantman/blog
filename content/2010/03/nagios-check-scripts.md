Title: Nagios check scripts
Date: 2010-03-16 22:33
Author: admin
Category: Monitoring
Tags: 1-wire, asterisk, bacula, DOCSIS, Nagios, snmp, syslog, ubiquiti
Slug: nagios-check-scripts

Last week I added some of my Nagios check scripts to my [nagios-scripts
GitHub repository](https://github.com/jantman/nagios-scripts). Perhaps
they'll be of some use to some other people...

-   [check\_1wire\_temps.php](https://github.com/jantman/nagios-scripts/blob/master/check_1wire_temps.php)
    - quick and dirty, built for one specific application, but a good
    starting place for checking Dallas 1-wire temperatures via OWFS.
-   [check\_802dot11.php](https://github.com/jantman/nagios-scripts/blob/master/check_802dot11.php)
    - A script to check various things in the IEEE-802DOT11 MIB, written
    for Ubiquiti APs (SNMP).
-   [check\_frogfoot.php](https://github.com/jantman/nagios-scripts/blob/master/check_frogfoot.php)
    - A script to check some stuff from FROGFOOT-MIB, also written for
    Ubiquiti APs (SNMP).
-   [check\_asterisk\_iaxpeers](https://github.com/jantman/nagios-scripts/blob/master/check_asterisk_iaxpeers)
    - a Python check script to parse the output of rasterisk for IAX
    peer status and latency (includes perf data output).
-   [check\_bacula\_job.php](https://github.com/jantman/nagios-scripts/blob/master/check_bacula_job.php)
    - A script to connect to the Bacula database and make sure a
    specified job terminated OK and was run on schedule.
-   [check\_docsis](https://github.com/jantman/nagios-scripts/blob/master/check_docsis)
    - A script to check status and various metrics for cable modems
    implementing the DOCSIS MIB (SNMP). Works with (at least) the
    Motorola SurfBoard modems used by Cablevision (which use
    192.168.100.1 on the LAN side).
-   [check\_syslog\_age.php](https://github.com/jantman/nagios-scripts/blob/master/check_syslog_age.php)
    - A PHP script which checks (recursively) that the newest file under
    a directory is no more than X seconds old. I use this for checking
    my centralized syslog server, which has logs separated out in
    `/var/log/HOSTS/hostname`.

**Update 2011-01-31** - the
[check\_syslog\_age.php](https://github.com/jantman/nagios-scripts/blob/master/check_syslog_age.php)
script was updated today to handle an error condition where stat() calls
in PHP fail on files larger than 2GB on 32-bit systems.
