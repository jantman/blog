Title: Readable Nagios Log Timestamps
Date: 2012-10-17 05:00
Author: admin
Category: Software
Tags: icinga, Nagios, perl, timestamp
Slug: readable-nagios-log-timestamps

If you're like me and most humans, the Nagios logfile timestamp (a unix
timestamp) isn't terribly useful when trying to grep through the logs
and correlate events:  

~~~~{.console}
# head -2 nagios.log
[1350360000] LOG ROTATION: DAILY
[1350360000] LOG VERSION: 2.0
~~~~

Here's a nifty Perl one-liner that you can pipe your logs through:  

~~~~{.perl}
perl -pe 's/(\\d+)/localtime($1)/e'  
~~~~

to get nicer output like:  

~~~~{.perl}
# head -2 nagios.log
[Tue Oct 16 00:00:00 2012] LOG ROTATION: DAILY
[Tue Oct 16 00:00:00 2012] LOG VERSION: 2.0
~~~~
