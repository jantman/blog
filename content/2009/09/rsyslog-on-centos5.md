Title: rsyslog on CentOS5
Date: 2009-09-17 15:45
Author: admin
Category: Tech HowTos
Tags: centos, logging, rsyslog, syslog
Slug: rsyslog-on-centos5

**Update July 2011** - We've been using rsyslog for our centralized
syslog infrastructure at [work][] (site being redesigned at the moment)
for about a year now. As a result, our colleagues at [Rutgers University
Open System Solutions][] have been nice enough to include rsyslog in
their [koji][] build system. Updated packages of rsyslog for CentOS 5
x86 and x86\_64 are available [here][]. Please be aware that they have
some dependencies of specific RU versions. It's probably best if you
download the source RPM and build it yourself using rpmbuild. The
current [5.6.2 source package][] includes a CentOS 5 spec file and other
related scripts. This RPM repository is only open to the public as a
courtesy, so please download once at most and distribute it to your
servers yourself.

Having finally setup my storage server (I know it's not much, but for me
starting with 1TB is wonderful), I actually got around to redoing my
centralized logging infrastructure. Here's a small summary of what I
have to handle:

-   logs from 15 hosts at 2 locations, including Cisco devices and a mix
    of syslog and syslog-ng Linux boxen.
-   Remote location logs forwarded to one server at remote location,
    then to centralized log server via SSH port forwarding.
-   48-hour retention of full iptables border firewall logs (\~
    3GB/day).
-   Future plans to have all logs stored in MySQL.

I'd previously had most of the boxes logging to an older host with low
disk space, but had to discontinue this due to lack of storage. Having
assessed the options, and with definite plans to log to a database, I
decided to go with [rsyslog][] for the centralized host.

Unfortunately, stable rsyslog is up to 4.4.x, with 5.x in development,
and the newest package I could find for CentOS was 2.something. So, I
set about building it from source. It was a \*very\* difficult build on
my machine (CentOS 5.3, 2.6.18-128.el5 \#1 SMP i686). Unfortunately, I
don't have an RPM build environment setup, but here's how I accomplished
it:

1.  I f not already done, <span style="font-family: courier new;">yum
    install rpmforge-release</span>
2.  <span style="font-family: courier new;">yum install gnutls-devel
    gnutls libatomic\_ops-devel gcc43 java-1.6.0-openjdk-devel</span>
3.  Download [rsyslog-4.5.2][] (currently Beta). Extract, cd into the
    directory.
4.  To test the performance difference from MySQL,
    <span style="font-family: courier new;">yum install php-pgsql
    postgresql postgresql-devel postgresql-libs postgresql-server</span>
5.  Edit the "configure" script, add
    <span style="font-family: courier new;">-DHAVE\_ATOMIC\_BUILTINS</span>
    to the <span style="font-family: courier new;">DEFS</span> line
    (28936 in this version).
6.  <span style="font-family: courier new;">export
    CC=/usr/bin/gcc43</span>
7.  <span style="font-family: courier new;">export
    CCDEPMODE="depmode=gcc4"</span>
8.  <span style="font-family: courier new;">export CFLAGS="-O3
    -march=i686"</span>
9.  <span style="font-family: courier new;">./configure --enable-mysql
    --enable-omtemplate --enable-gnutls --enable-pgsql</span>
10. <span style="font-family: courier new;">make && make install</span>

For my system, I used the
<span style="font-family: courier new;">/etc/sysconfig/rsyslog</span>
and <span style="font-family: courier new;">/etc/init.d/rsyslog</span>
from the 2.x rsyslog RPMs, with some modifications as follows:

<span style="font-family: courier new;">/etc/sysconfig/rsyslog</span>
*(comments have been removed to save space)*:

~~~~{.bash}
# -c4   version 4 compatibility mode
# -x     disable DNS for remote messages (don't want it to hang if DNS is down
# -4     IPv4 only
SYSLOGD_OPTIONS="-c4 -x -4"
~~~~

<span style="font-family: courier new;">/etc/init.d/rsyslog</span>
*(comments have been removed to save space)*:

~~~~{.bash}
#!/bin/bash
#
# rsyslog        Starts rsyslogd.
#
#
# chkconfig: - 12 88
# description: Syslog is the facility by which many daemons use to log   
# messages to various system log files.  It is a good idea to always   
# run rsyslog.
### BEGIN INIT INFO
# Provides: $syslog
# Required-Start: $local_fs $network $remote_fs
# Required-Stop: $local_fs $network $remote_fs
# Default-Stop: 0 1 2 3 4 5 6
# Short-Description: Enhanced system logging and kernel message trapping daemons
# Description: Rsyslog is an enhanced multi-threaded syslogd supporting,
#              among others, MySQL, syslog/tcp, RFC 3195, permitted
#              sender lists, filtering on any message part, and fine
#              grain output format control.
### END INIT INFO

# Source function library.
. /etc/init.d/functions

RETVAL=0

start() {
        [ -x /sbin/rsyslogd ] || exit 5

        # Do not start rsyslog when sysklogd is running
        if [ -e /var/run/syslogd.pid ] ; then
                echo $"Shut down sysklogd before you run rsyslog";
                exit 1;
        fi

        # Source config
        if [ -f /etc/sysconfig/rsyslog ] ; then
                . /etc/sysconfig/rsyslog
        else
                SYSLOGD_OPTIONS="-m 0"
        fi

        if [ -z "$SYSLOG_UMASK" ] ; then
              SYSLOG_UMASK=077;
        fi
        umask $SYSLOG_UMASK

        echo -n $"Starting system logger: "
        daemon rsyslogd $SYSLOGD_OPTIONS
        RETVAL=$?
        echo
        [ $RETVAL -eq 0 ] && touch /var/lock/subsys/rsyslog
        return $RETVAL
}
stop() {
        echo -n $"Shutting down system logger: "
        killproc rsyslogd
        RETVAL=$?
        echo
        [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/rsyslog
        return $RETVAL
}
reload()  {
    RETVAL=1
    syslog=`cat /var/run/rsyslogd.pid 2>/dev/null`
    echo -n "Reloading system logger..."
    if [ -n "${syslog}" ] && [ -e /proc/"${syslog}" ]; then
        kill -HUP "$syslog";
        RETVAL=$?
    fi
    if [ $RETVAL -ne 0 ]; then
        failure
    else
        success
    fi
    echo
    return $RETVAL
}
rhstatus() {
        status rsyslogd
}
restart() {
        stop
        start
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        restart
        ;;
  reload|force-reload)
        reload
        ;;
  status)
        rhstatus
        ;;
  condrestart)
        [ -f /var/lock/subsys/rsyslog ] && restart || :
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|force-reload|condrestart}"
        exit 2
esac

exit $?
~~~~

**My rsyslog.conf file**:

~~~~{.text only}
# uncomment next line for debugging, use graphvis to see the graph
#$GenerateConfigGraph /root/rsyslog-graph.dot
$ModLoad imklog
$ModLoad imtcp
$ModLoad imudp
$ModLoad imuxsock

# template
$template RemoteHost,"/var/log/HOSTS/%HOSTNAME%/%$YEAR%/%$MONTH%/%$DAY%/%syslogfacility-text%.log"
# used for Cisco, vanilla syslog when we can't parse host name
$template RemoteFromHost,"/var/log/HOSTS/%FROMHOST%/%$YEAR%/%$MONTH%/%$DAY%/%syslogfacility-text%.log"

# NOTE - we can't bind UDP to a ruleset, so it enters the local RuleSet
#   and has to be dealt with here

$RuleSet local

# for cisco, vyatta - doesn't send hostname, need to use IP manually
:fromhost, isequal, "192.168.0.99" ?RemoteFromHost
:fromhost, isequal, "192.168.0.99" ~
:fromhost, isequal, "192.168.0.103" ?RemoteFromHost
:fromhost, isequal, "192.168.0.103" ~
:fromhost, isequal, "192.168.0.97" ?RemoteFromHost
:fromhost, isequal, "192.168.0.97" ~
:fromhost, isequal, "192.168.0.111" ?RemoteFromHost
:fromhost, isequal, "192.168.0.111" ~
# anything from a remote host gets logged as such
:source, isequal, "" ?RemoteHost
:source, isequal, "" ~

#
# LOCAL LOGGING
#

kern.*                                                 /var/log/messages
*.info;mail.none;authpriv.none;cron.none                /var/log/messages
authpriv.*                                              /var/log/secure
mail.*                                                  -/var/log/maillog
cron.*                                                  /var/log/cron
*.emerg                                                 *
uucp,news.crit                                          /var/log/spooler
local7.*                                                /var/log/boot.log

# use the local RuleSet as default
$DefaultRuleset local

#
# BEGIN centralized logging stuff added 2009-09-16 by jantman
#

# define ruleset for remote logging
$RuleSet remote

*.* ?RemoteHost

# bind ruleset to tcp listener
$InputTCPServerBindRuleset remote
# and activate it:
$InputTCPServerRun 5000

$UDPServerRun 514
$UDPServerRun 5000

#
# END remote logging
#
~~~~

  [work]: http://services.rutgers.edu/
  [Rutgers University Open System Solutions]: http://oss.rutgers.edu
  [koji]: http://koji.rutgers.edu
  [here]: http://koji.rutgers.edu/koji/buildinfo?buildID=2140
  [5.6.2 source package]: http://koji.rutgers.edu/koji/rpminfo?rpmID=14051
  [rsyslog]: http://www.rsyslog.com
  [rsyslog-4.5.2]: http://rsyslog.com/Downloads-index-req-viewdownload-cid-1-orderby-dateD.phtml
