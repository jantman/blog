Title: Vyatta VC5 - Snort alerts to syslog
Date: 2011-01-30 19:54
Author: admin
Category: Software
Tags: security, snort, syslog, vyatta
Slug: vyatta-vc5-snort-alerts-to-syslog

I'm running a [Vyatta](http://www.vyatta.org) vyatta router at home - in
my opinion it's pretty near "enterprise grade", and I'm running the
Community/Core (read: no-cost and almost all Free) on commodity hardware
with great performance. Granted, I'm still on the older version (5 as
opposed to the current 6) since an upgrade will require total downtime
and a spare set of SCSI disks for the machine it's on, but it still
works quite well. Today I decided to enable the
[Snort](http://www.snort.org) IDS on the box. It actually worked quite
well (albeit stuck at older rules until I upgrade to Vyatta VC6) and
didn't put much more load on the box. For the time being I decided to
just have it alert on problems and not drop anything, as I'm getting
pretty high false positives and the older Vyatta version doesn't seem to
have a way to disregard rules.

My biggest complaint was that Vyatta didn't see fit to allow alerts by
syslog. I'm not a big fan of keeping information like IDS logs stuck on
the router - I don't like logging in to it any more than I have to, it
doesn't have much storage, and I'd also like to keep stuff like this in
a more secure location. Through a bit of digging, I found the
`/opt/vyatta/share/perl5/VyattaSnortConfig.pm` Perl module which
generates the Snort config file from Vyatta's CLI stuff. Looking through
the Perl code, I found the definition of the snort.conf output
statements:

~~~~{.perl}
my $output_def =<<EOD;
  output alert_unified: alert, limit $log_limit
  output log_null
EOD
~~~~

I simply added a line `output alert_syslog: log_local3 log_notice` after the `output alert_unified` line.

~~~~{.perl}
my $output_def =<<EOD;
  output alert_unified: alert, limit $log_limit
  output alert_syslog: log_local3 log_notice
  output log_null
EOD
~~~~

I then went into Vyatta configuration and changed a rule from alert to pass, committed,
changed back, committed, and `/etc/snort/snort.conf` now had my syslog lines. I'm now 
getting snort alerts to local3 in syslog, which is fed to my centralized log server. My
next project is to find or write something which will parse these logs, generate a daily
summary email, and maybe check them hourly and alert on any big changes. I also might just
cron an emailing of the output from Vyatta's show ips summary command. So far I have over 11,000 events logged in about 12 hours.
