Title: Petit for Log Analysis
Date: 2012-02-21 11:57
Author: admin
Category: Miscellaneous
Tags: analysis, log, logging, petit, syslog
Slug: petit-for-log-analysis

I recently discovered the
[petit](http://crunchtools.com/software/petit/) program for log
analysis. It's a simple tool to pull out useful information from syslog
logs in a variety of ways. I've only used it a few times so far, mainly
on logs from problems I've already solved but didn't know the cause of
at first. So far, it's proven quite useful. Here are a few examples:

-   `petit --wordcount /var/log/messages` - displays ordered count of
    words appearing in the log. My first step, especially if "warning",
    "error" or "fatal" shows up near the top...
-   `petit --hash --fingerprint /var/log/messages` - hashes the log,
    removes filters (such as numerics, datestamp), and displays count of
    matching lines. Absolutely wonderful for web error logs, as it
    removes client IP addresses, line numbers, etc.
-   `petit --mgraph /var/log/messages` - graph messages per minute for
    the first hour of the log (ASCII of course)
-   `petit --hgraph /var/log/messages` - same as above, but messages per
    hour for the first day
-   Petit will also read from stdin with the --Xgraph options, so you
    can `cat logfile | grep word | petit --mgraph`

Just one note - this tool appears to work only on standard syslog
formatted logs. If some non-datestamped lines managed to work their way
into the log (i.e. someone used echo \>\> logfile instead of `logger`),
it will choke.

Many thanks to Scott McCarty for this wonderful tool!</a>
