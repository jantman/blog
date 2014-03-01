Title: Script to Chart Intervals Between Problem and Recovery from Nagios/Icinga Log Files
Date: 2012-05-31 13:54
Author: admin
Category: Ops
Tags: chart, icinga, monitoring, Nagios, perl
Slug: script-to-chart-intervals-between-problem-and-recovery-from-nagiosicinga-log-files

At work, we use [Icinga](http://www.icinga.org) (a fork of
[Nagios](http://nagios.org/)) for monitoring. We have a few services
which are restarted or otherwise poked by event handlers, but the
recovery takes a while - so we often get paged for problems which
recover in a few minutes. I wrote a small perl script that greps through
the archived log files for a given regex (service and/or host name) and
then calculates the time from problem to recovery and graphs those
times.

The script is called `nagios_log_problem_interval.pl` and can be
downloaded from [my
github](https://github.com/jantman/nagios-scripts/blob/master/nagios_log_problem_interval.pl).
Below is some sample output, the number of minutes from problem to
recovery are along the Y axis and the count is along the X axis:

~~~~{.console}
> nagios_log_problem_interval.pl --archivedir=/var/icinga/archive --match=myhost --backtrack=10 myhost;HTTP
Count
1:########(8)
2:##(2)
3:#(1)
4:##(2)
5:#######(7)
6:(0)
7:(0)
8:#(1)
9:(0)
10:(0)
11:#(1)
12:(0)
13:#(1)
14:(0)
15:(0)
16-29:(0)
30-59:(0)
60+:(0)
~~~~
