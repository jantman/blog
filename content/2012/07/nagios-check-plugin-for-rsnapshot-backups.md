Title: Nagios Check Plugin for Rsnapshot Backups
Date: 2012-07-07 06:34
Author: admin
Category: Monitoring
Tags: backups, monitoring, Nagios, rsnapshot, rsync
Slug: nagios-check-plugin-for-rsnapshot-backups

In a previous post, I described how I do [Secure rsnapshot backups over
the WAN via
SSH](/2012/01/secure-rsnapshot-backups-over-the-wan-via-ssh/). While my
layout of rsnapshot configuration files, data, and log files is a bit
esoteric, I monitor all this with a Nagios check plugin that runs on my
backup host. It Assumes that the output of
[rsnapshot](http://rsnapshot.org/) is written to a text log file, one
file per host, at a path that matches
`/path_to_log_directory/log_HOSTNAME_YYYYMMDD-HHMMSS.log` where
`HOSTNAME` is the name of the host, and `YYYYMMDD-HHMMSS` is a datestamp
(actually, the script just finds the newest file matching
`log_HOSTNAME_*.log` in that directory). In order to obtain correct
timing of the runs, which rsnapshot doesn't offer, it assumes that you
trigger rsnapshot through a wrapper script, which runs it once per host
(inside a loop?) with per-host log files and some logging information
added, like:

~~~~{.bash}
for h in 
do
    LOGFILE="/mnt/backup/rsnapshot/logs/log_${h}_`date +%Y%m%d-%H%M%S`.txt"
    echo "# Starting backup at `date` (`date +%s`)" >> "$LOGFILE"
    /usr/bin/rsnapshot -c /etc/rsnapshot-$h.conf daily &>> "$LOGFILE"
    echo "# Finished backup at `date` (`date +%s`)" >> "$LOGFILE"
done
~~~~

The `check_rsnapshot.pl` plugin uses `utils.pm` from Nagios, as well as
[Getopt::Long](http://search.cpan.org/~jv/Getopt-Long-2.38/lib/Getopt/Long.pm),
[File::stat](http://search.cpan.org/~makoto/File-Stat-0.01/Stat.pm),
[File::Basename](http://search.cpan.org/~flora/perl-5.14.2/lib/File/Basename.pm),
[File::Spec](http://search.cpan.org/~smueller/PathTools-3.33/lib/File/Spec.pm)
and
[Number::Bytes::Human](http://search.cpan.org/~ferreira/Number-Bytes-Human-0.07/Human.pm).
This was one of my first Perl plugins, but seems to be rather
acceptable. It makes the following checks based on the rsnapshot log:

1.  Backup run in the last X seconds (warning and crit thresholds)
2.  Maximum time from start to finish (warning and crit thresholds)
3.  Minimum size of backup (warning and crit thresholds)
4.  Minimum number of files in backup (warning and crit thresholds)

In addition to `check_file_age` checks on a number of files that are
included in backups and I know are modified before each backup run, this
seems to handle monitoring quite well for me. I certainly preferred
running [Bacula](http://www.bacula.org/) and using my MySQL-based
[check\_bacula\_job.php](https://github.com/jantman/nagios-scripts/blob/master/check_bacula_job.php),
but as I'm now backing up 4 machines to my desktop, I no longer have a
need for Bacula (or tapes).

The script itself can be found at
[github](https://github.com/jantman/nagios-scripts/blob/master/check_rsnapshot.pl).
