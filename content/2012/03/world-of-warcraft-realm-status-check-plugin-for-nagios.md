Title: World of Warcraft Realm Status Check Plugin for Nagios
Date: 2012-03-16 07:40
Author: admin
Category: Miscellaneous
Tags: blizzard, check plugin, monitoring, Nagios, warcraft, wow
Slug: world-of-warcraft-realm-status-check-plugin-for-nagios

My wife [Jackie](http://www.jackieantman.com/)
([Syrilia](http://us.battle.net/wow/en/character/Arthas/Syrilia/simple))
is an avid [World of
Warcraft](http://en.wikipedia.org/wiki/World_of_Warcraft) player (it's a
[MMORPG](http://en.wikipedia.org/wiki/Massively_multiplayer_online_role-playing_game)
with over 10 million players). They have weekly server
maintenance/update windows every Tuesday morning - total downtime. The
length is never really fixed, so I looked around to see if there was a
logical way to notify when the servers came back up.

I managed to find a [World of Warcraft Realm status check
plugin](http://exchange.nagios.org/directory/Plugins/Games/World-of-Warcraft-Realm-status/details)
on Nagios Exchange, but it was written to a now-discontinued API. It was
also last modified in 2008, and I can't seem to get in contact with the
author, Scott A'Hearn (webmaster@scottahearn.com) - that email returns
undeliverable, there's no email link on the site that his domain now
redirects to, and the domain scottahearn.com is a (eek) private
registration in WHOIS, so I don't really have any way of finding contact
information. Regardless, I've modified the script to use the [new
Blizzard REST API](http://blizzard.github.com/api-wow-docs/#id3381933)
and it's now working. Of course, this is pulling from Blizzard's data
feed, not doing any actual monitoring itself, and be warned that they
impose query limits (at the moment, their
[docs](http://blizzard.github.com/api-wow-docs/#id3379836) say 3,000
requests per day for anonymous access; to be nice to them, I only check
on Tuesdays from 3am-4pm, when I'm most concerned about it). The updated
source code is shown below, but the most up-to-date version will always
live at  

[https://github.com/jantman/nagios-scripts/blob/master/check\_wow.pl](https://github.com/jantman/nagios-scripts/blob/master/check_wow.pl).
If you want, you can also see a diff of my changes to Scott's original
version on
[github](https://github.com/jantman/nagios-scripts/commit/f84eede5256aa6621812e91f0b3b73e91f3b11e8#check_wow.pl).

~~~~{.perl}
#!/usr/bin/perl -w
#
# World of Warcraft Realm detector plugin for Nagios
#
# Written by Scott A'Hearn (webmaster@scottahearn.com), version 1.2, Last Modified: 07-21-2008
#
# Modified by Jason Antman  02-22-2012, to cope with the change from
# the deprecated worldofwarcraft.com XML feed to the BattleNet JSON API.
#
# Usage: ./check_wow -r 
#
# Description:
#
# This plugin will check the status of a World of Warcraft realm, based 
# on input from the battle.net JSON realm status API.
#
# Output:
#
# If the realm is up, the plugin will
# return an OK state with a message containing the status of the realm as well 
# as some extended information such as type (PvP, PvE, etc) and population.  
# If the realm is down, the plugin will return a CRITICAL state with a message
# containing the status of the realm as well as any available extended 
# information such as type (PvP, PvE, etc) and population. If the realm is
# shown as currently having a queue, a WARNING state will be returned.
#
#
# If the requested realm is not found, the plugin will
# return an UNKNOWN state with an appropriate warning message.
#
# If there is an invalid [or no] response from the battle.net server,
# the plugin will return a CRITICAL state.
#
# $HeadURL: http://svn.jasonantman.com/public-nagios/check_wow.pl $
# $LastChangedRevision: 13 $
#
# Changelog:
# 2012-02-22 Jason Antman  (version 1.3):
#     * modified for new BattleNet JSON API
#     * added WARNING output if realm has queue
#
# 2008-07-21 Scott A'Hearn  (version 1.2):
#     * version on Nagios Exchange
#

# use modules
use strict;             # good coding practices
use Getopt::Long;           # command-line option parsing
use LWP;                # external content retrieval
use JSON;                               # JSON for API reply
use lib  "/usr/lib/nagios/plugins"; # nagios plugins
use utils qw(%ERRORS &print_revision &support &usage ); # nagios error and message libraries
use Data::Dumper;                       # debugging

# init global vars
use vars qw($PROGNAME); $PROGNAME="check_wow";
my ($ver_string, $browser, $jsonurl, $raw_json, $opt_V, $opt_h, $opt_r, $decoded) = (undef, undef, undef, undef, undef, undef, undef, undef);
$jsonurl = "http://us.battle.net/api/wow/realm/status?realm=";
$ver_string = "1.3";

# init subs
sub print_help ($$);
sub print_usage ($);

# define command-line option handling
Getopt::Long::Configure('bundling');
GetOptions(
    "V"   => \$opt_V, "version" => \$opt_V,
    "h"   => \$opt_h, "help"    => \$opt_h,
    "r=s" => \$opt_r, "realm=s" => \$opt_r);

# show version info, exit
if ($opt_V) {
    print_revision($PROGNAME, $ver_string);
    exit $ERRORS{'OK'};
}

# show help, exit
if ($opt_h) {
    print_help($PROGNAME, $ver_string);
    exit $ERRORS{'OK'};
}

# get first command-line param
$opt_r = shift unless ($opt_r);

# if no command-line param passed, show usage/help, exit
if (! $opt_r) {
    print_usage($PROGNAME);
    exit $ERRORS{'UNKNOWN'};
}

# new browser object, with agent
$browser = LWP::UserAgent->new();
$browser->agent("check_wow/$ver_string");

# retrieve JSON from WoW site
$jsonurl .= $opt_r;
$raw_json = $browser->request(HTTP::Request->new(GET => $jsonurl));

if ($raw_json->is_success) {
    # if success, process
    $raw_json = $raw_json->content;
} else {
    # otherwise, fail UNKNOWN
    print "UNKNOWN - Realm '$opt_r' status not received.";
    exit $ERRORS{'UNKNOWN'};
}

$decoded = decode_json $raw_json;

if($decoded->{realms}[0]->{status} != 1) {
    print "CRITICAL - Realm ".$decoded->{realms}[0]->{name}." Down (".$decoded->{realms}[0]->{type}.", population: ".$decoded->{realms}[0]->{population}.")\n";
    exit $ERRORS{'CRITICAL'};
} elsif($decoded->{realms}[0]->{queue} != 0) {
    print "WARNING - Realm ".$decoded->{realms}[0]->{name}." Has Queue (".$decoded->{realms}[0]->{type}.", population: ".$decoded->{realms}[0]->{population}.")\n";
    exit $ERRORS{'WARNING'};
} else {
    print "OK - Realm ".$decoded->{realms}[0]->{name}." Up (".$decoded->{realms}[0]->{type}.", population: ".$decoded->{realms}[0]->{population}.")\n";
    exit $ERRORS{'OK'};
}

# usage function
sub print_usage ($) {
        my ($PROGNAME) = @_;
    print "Usage:\n";
    print "  $PROGNAME [-r | --realm ]\n";
    print "  $PROGNAME [-h | --help]\n";
    print "  $PROGNAME [-V | --version]\n";
}

# help function
sub print_help ($$) {
        my ($PROGNAME, $ver_string) = @_;
    print_revision($PROGNAME, $ver_string);
    print "Copyright (c) 2008 Scott A'Hearn, 2012 Jason Antman\n\n";
    print_usage($PROGNAME);
    print "\n";
    print "   Standard World of Warcraft realm name, case sensitive.\n";
    print "\n";
    # support();
}

# end
~~~~
