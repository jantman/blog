Title: Vyatta - Showing ISC dhcpd fixed-address leases
Date: 2011-12-24 14:42
Author: admin
Category: Tech HowTos
Tags: dhcpd, rsyslog, vyatta
Slug: vyatta-showing-isc-dhcpd-fixed-address-leases

ISC [dhcpd](http://www.isc.org/software/dhcp) has the ability to always
give a specific MAC address the same IP address "lease" using the
fixed-address configuration option. This is configured in
[Vyatta](http://www.vyatta.org) using the `static-mapping` configuration
statement. Unfortunately, since dhcpd doesn't store fixed-address leases
in the `dhcpd.leases` file, the Vyatta `show dhcp leases` command
doesn't show anything about them - which makes it difficult to debug
anything dhcp-related if all of the hosts on your network are setup for
fixed addresses. I found a mention of this on the [vyatta
forum](http://www.vyatta.org/forum/viewtopic.php?p=121558), and also an
[open bug (1990)](https://bugzilla.vyatta.com/show_bug.cgi?id=1990) to
fix it, but no proposed resolution. Since I came across this problem and
happen to know a bit about ISC dhcpd, I developed both a workaround for
users (including a perl script) and a possible solution for the Vyatta
developers to implement.

**Workaround for Users:**

There's no way to get dhcpd to store fixed-address hosts in the
dhcpd.leases file (though it's been discussed on the dhcpd-users mailing
list a few times). There is, however, a way to get dhcpd to log every
time it sends an ACK to a client. The following Vyatta configuration
commands will get dhcpd to log all transactions to syslog, will have
[rsyslog](http://rsyslog.com/) put that in `/var/log/user/dhcpd`. Since
this log can fill up very quickly on a busy server, the latter two
commands will tell [logrotate](https://fedorahosted.org/logrotate/) to
rotate the log file when it reaches 3000k in size, and keep 5 copies
(feel free to adjust to your needs):

~~~~{.console}
# set service dhcp-server global-parameters "log-facility local2;"
# set system syslog file dhcpd facility local2 level debug
# set system syslog file dhcpd archive files 5
# set system syslog file dhcpd archive size 3000
~~~~

Once this is done, you can `tail -f /var/log/user/dhcpd` to watch DHCP
discover/request/offer/ack in realtime, or grep through the log file for
a specific IP or MAC. If you want an easier method, I've written a perl
script (latest version will always live in [my subversion
repo](http://svn.jasonantman.com/misc-scripts/show_dhcp_fixed_ACKs.pl))
to grep through `/var/log/user/dhcpd` and show the most recent DHCPACK
for each IP address, sorted by IP. Here's the code of the simple script,
which is more than half comments. To use it, after performing the above
steps, all you need to do is login to your Vyatta box,
`wget http://svn.jasonantman.com/misc-scripts/show_dhcp_fixed_ACKs.pl`
and then `perl show_dhcp_fixed_ACKs.pl`.

~~~~{.perl}
#!/usr/bin/perl

#
# show_dhcp_fixed_ACKs.pl - script to show the most recent DHCP ACKs per IP address for ISC DHCPd,
#   from a log file. Originally written for Vyatta routers that just show the dynamic leases.
#
# To use this, you need to have dhcpd logging to syslog, and your syslog server putting the log file at
# /var/log/user/dhcpd (or a file path specified by the $logfile variable below.
#
# To accomplish this on Vyatta 6.3, run:
# set service dhcp-server global-parameters "log-facility local2;"
# set system syslog file dhcpd facility local2 level debug
# set system syslog file dhcpd archive files 5
# set system syslog file dhcpd archive size 3000
# commit
#
# Copyright 2011 Jason Antman  All Rights Reserved.
# This script is free for use by anyone anywhere, provided that you comply with the following terms:
# 1) Keep this notice and copyright statement intact.
# 2) Send any substantial changes, improvements or bog fixes back to me at the above address.
# 3) If you include this in a product or redistribute it, you notify me, and include my name in the credits or changelog.
#
# The following URL always points to the newest version of this script. If you obtained it from another source, you should
# check here:
# $HeadURL$
# $LastChangedRevision$
#
# CHANGELOG:
# 2011-12-24 jason@jasonantman.com:
#    initial version of script
#
#

use strict;
use warnings;

my $logfile = "/var/log/user/dhcpd";

my %data = ();

open DF, $logfile or die $!;
while ( my $line =  ) {
    if ( $line !~ m/dhcpd: DHCPACK/) { next;}
    $line =~ m/([A-Za-z]+ [0-9]+ [0-9]{1,2}:[0-9]{2}:[0-9]{2}) [^\/x]+ dhcpd: DHCPACK on (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) to ((?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}) via (.+)/;
    #print "$1==$2==$3==$4==\n" ;
    $data{"$2"}->{'mac'} = "$3";
    $data{"$2"}->{'date'} = "$1";
    $data{"$2"}->{'if'} = "$4";
    $data{"$2"}->{'ip'} = "$2";    
}

printf("%-18s %-20s %-18s %-10s\n", "IP Address", "Hardware Address", "Date", "Interface");
printf("%-18s %-20s %-18s %-10s\n", "----------", "----------------", "----", "---------");

# begin sort by IP address
my @keys =
  map  substr($_, 4) =>
  sort
  map  pack('C4' =>
    /(\d+)\.(\d+)\.(\d+)\.(\d+)/)
    . $_ => (keys %data);
# end sort by IP address

foreach my $key (@keys) {
    printf("%-18s %-20s %-18s %-10s\n", $data{$key}{'ip'}, $data{$key}{'mac'}, $data{$key}{'date'}, $data{$key}{'if'});
}
~~~~

**A solution for Vyatta:**

I suggested this to Vyatta in a reply to [bug
1990](https://bugzilla.vyatta.com/show_bug.cgi?id=1990). Since they
already use [rsyslog](http://rsyslog.com/) which has very powerful
processing capabilities, it would be easy to have rsyslog parse the
DHCPACK messages in real time and update some data store (flat files or
a simple database) with the information. While how to store this would
be up to the Vyatta guys, I have some rsyslog configuration to parse
DHCPACK messages and update a MySQL database (with two tables; one for
most recent ACK per IP address and one for most recent ACK per MAC
address) that might be of some use:

~~~~{.text}
$template DHCPACKonIP, "INSERT INTO dhcplog_ip   
       SET   
       server_ip=inet_aton('%fromhost-ip%'),   
       msg_type='DHCPACK',   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,6,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'   
       ON DUPLICATE KEY UPDATE   
       server_ip=inet_aton('%fromhost-ip%'),   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       gateway='%msg:R,ERE,6,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'  
",SQL

$template DHCPACKonMAC, "INSERT INTO dhcplog_mac   
       SET   
       server_ip=inet_aton('%fromhost-ip%'),   
       msg_type='DHCPACK',   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,6,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'   
       ON DUPLICATE KEY UPDATE   
       server_ip=inet_aton('%fromhost-ip%'),   
       date='%timereported:::date-mysql%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,6,BLANK:DHCPACK on ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) to (([0-9a-f]{2}:){5}[0-9a-f]{2})( \(([^)]+)\))? via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'  
",SQL

$template DHCPACKtoIP, "INSERT INTO dhcplog_ip   
       SET   
       server_ip=inet_aton('%fromhost-ip%'),   
       msg_type='DHCPACK',   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,4,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'   
       ON DUPLICATE KEY UPDATE   
       server_ip=inet_aton('%fromhost-ip%'),   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       gateway='%msg:R,ERE,4,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'  
",SQL

$template DHCPACKtoMAC, "INSERT INTO dhcplog_mac   
       SET   
       server_ip=inet_aton('%fromhost-ip%'),   
       msg_type='DHCPACK',   
       date='%timereported:::date-mysql%',   
       mac_addr='%msg:R,ERE,2,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,4,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'   
       ON DUPLICATE KEY UPDATE   
       server_ip=inet_aton('%fromhost-ip%'),   
       date='%timereported:::date-mysql%',   
       client_ip=inet_aton('%msg:R,ERE,1,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%'),   
       gateway='%msg:R,ERE,4,BLANK:DHCPACK to ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) \((([0-9a-f]{2}:){5}[0-9a-f]{2})\) via (([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|eth0)--end%',   
       fullmsg='%msg%'  
",SQL

:msg, startswith, " DHCPACK on" :ommysql:hostname,database,dbuser,dbpass;DHCPACKonIP
& :ommysql:hostname,database,dbuser,dbpass;DHCPACKonMAC
& ~ ### DISCARD

if $msg startswith ' DHCPACK to' and ( not ( $msg contains 'no client hardware address' ) )   
then :ommysql:hostname,database,dbuser,dbpass;DHCPACKtoMAC
& :ommysql:hostname,database,dbuser,dbpass;DHCPACKtoIP
& ~ ### DISCARD
~~~~
