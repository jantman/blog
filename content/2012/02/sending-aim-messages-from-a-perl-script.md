Title: Sending AOL Instant Messenger (AIM) Messages from a Perl Script
Date: 2012-02-28 18:33
Author: admin
Category: Monitoring
Tags: aim, aol, icinga, instant messenger, Nagios, notifications, perl
Slug: sending-aim-messages-from-a-perl-script

I've been doing some work on [icinga](http://www.icinga.org) (a Nagios
fork) and wanted to implement notification via AOL Instant Messenger
(AIM), since I'm almost always signed on when I'm at a computer.
Unfortunately, most of the
[scripts](http://vuksan.com/linux/nagios_scripts.html#send_aim_messages)
that I could find use
[Net::AIM::TOC](http://search.cpan.org/~friffin/Net-AIM-TOC-0.97/TOC.pm)
which implements a now-defunct protocol. So, I found Perl's
[Net::OSCAR](http://search.cpan.org/~toddr/Net-OSCAR-1.928/lib/Net/OSCAR.pm)
and [James Nonnemaker's script](http://moo.net/code/aim.html), and
decided to rework them into something a bit more full-featured.

The below script sends a single IM to a single contact via the command
line (using a specified AIM username and password). It's intended to be
a Nagios notification script (using the configurations shown below), but
could be used for any purpose. The most up-to-date version of the script
will be available at:
[github.com/jantman/public-nagios/master/send\_aim.pl](https://github.com/jantman/nagios-scripts/blob/master/send_aim.pl)

~~~~{.perl}
#!/usr/bin/perl

#
# Script to send AIM messages from the command line
#
# Copyright 2012 Jason Antman  
# based on the simple version (C) 2008 James Nonnemaker / james[at]ustelcom[dot]net 
#    found at: 
#
# The canonical, up-to-date version of this script can be found at:
#  
#
# For updates, news, etc., see:
#  
#
# $HeadURL$
# $LastChangedRevision$
#

use strict;
use warnings;
use Net::OSCAR qw(:standard);
use Getopt::Long;

my ($screenname, $passwd, $ToSn, $Msg);
my $VERSION = "r17";

my $result = GetOptions ("screenname=s" => \$screenname,
              "password=s"   => \$passwd,
              "to=s"         => \$ToSn);

if(! $screenname || ! $passwd || ! $ToSn) {
    print "send_aim.pl $VERSION by Jason Antman \n\n";
    print "USAGE: send_aim.pl --screenname= --password= --to=\n\n";
}

# slurp message from STDIN
my $holdTerminator = $/;
undef $/;
$Msg = ;
$/ = $holdTerminator;
my @lines = split /$holdTerminator/, $Msg;
$Msg = "init";
$Msg = join $holdTerminator, @lines;

my $oscar = Net::OSCAR->new();
$oscar->loglevel(0);
$oscar->signon($screenname, $passwd);

$oscar->set_callback_snac_unknown(\&snac_unknown);
$oscar->set_callback_im_ok (\&log_out);
$oscar->set_callback_signon_done (\&do_it);

while (1) {
    $oscar->do_one_loop();
}

sub do_it {
    $oscar->send_im($ToSn, $Msg);
}

sub log_out {
    $oscar->signoff;
    exit;
}

sub snac_unknown {
    my($oscar, $connection, $snac, $data) = @_;
    # just use this to override the default snac_unknown handler, which prints a data dump of the packet
}
~~~~

The command line usage is pretty simple - it takes the message to send
on stdin and parameters for the sender's screen name and password, and
the recipient's screen name, like:

~~~~{.bash}
echo -e "Hello\nworld\n" | send_aim.pl --screenname=mySN --password=myPass --to=recipientSN
~~~~

The Icinga configs that I used for this are as follows. I just used the
default Icinga 1.6 notify by email commands, since AIM should handle the
full length fine.

~~~~{.text}
# host notification command
define command{
        command_name    notify-host-by-aim
        command_line    /usr/bin/printf "%b" "***** Icinga *****\n\nNotification Type: $NOTIFICATIONTYPE$\nHost: $HOSTNAME$\nState: $HOSTSTATE$\nAddress: $HOSTADDRESS$\nInfo: $HOSTOUTPUT$\n\nDate/Time: $LONGDATETIME$\n" | /usr/lib/nagios/plugins/notification/send_aim.pl --screenname=mySN --password=myPass --to=$CONTACTADDRESS1$
}

# service notification command
define command{
        command_name    notify-service-by-aim
        command_line    /usr/bin/printf "%b" "***** Icinga *****\n\nNotification Type: $NOTIFICATIONTYPE$\n\nService: $SERVICEDESC$\nHost: $HOSTALIAS$\nAddress: $HOSTADDRESS$\nState: $SERVICESTATE$\n\nDate/Time: $LONGDATETIME$\n\nAdditional Info:\n\n$SERVICEOUTPUT$\n" | /usr/lib/nagios/plugins/notification/send_aim.pl --screenname=mySN --password=myPass --to=$CONTACTADDRESS1$
}

# example contact
define contact{
        contact_name                    joeadmin
        alias                           Joe Admin
        use                             generic-with-AIM-contact
        email                           joeadmin@example.com
        pager                           5555555555@vtext.com
        address1                        joeAdminSN ; AIM screen name
}
~~~~
