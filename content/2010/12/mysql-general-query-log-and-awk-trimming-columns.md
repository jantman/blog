Title: MySQL General Query Log and Awk Trimming Columns
Date: 2010-12-21 11:45
Author: admin
Category: Tech HowTos
Tags: awk, database, logging, mysql
Slug: mysql-general-query-log-and-awk-trimming-columns

So today I started to implement a number of complex regex-based rules
and templates to get [rsyslog](http://www.rsyslog.com) to parse ISC
DHCPd logs in realtime. Unfortunately one of my templates must have been
wrong, because I started seeing some errors about a field that cannot be
blank in `/var/log/messages`. Unfortunately, rsyslog doesn't log the
query that raised the error, or the name of the template, or anything
else useful - just that there was a database error. With over a dozen
new templates, this didn't help much. But the following technique did:

MySQLd has a [General Query
Log](http://dev.mysql.com/doc/refman/5.1/en/query-log.html) that can be
activated by addling a line like:  
  
~~~~{.text}
log=/tmp/query.log`
~~~~

to `/etc/my.cnf` under the `[mysqld]` section. This will log \*all\*
queries to the specified log file, even if they resulted in an error or
did not manipulate data.

I couldn't find documentation on the log file format, but I observed
that each line appeared to begin with some whitespace, then a number
(perhaps a connection or section number, or maybe some sort of query
ordering number), then the word "Query", then the query. The following
awk expression prints everything from the third column on, dropping the
first two columns (the number and "Query"):  

~~~~{.bash}
awk '{ for (i=2; i<=NF; i++) printf "%s ", $i; printf "\n"; }'
~~~~
  
For easy analysis, the output of that can be piped into `sort` and then
`uniq`.
