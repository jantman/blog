Title: Nagios Check Plugin for Linode Monthly Bandwidth Usage
Date: 2012-02-29 20:32
Author: admin
Category: Software
Tags: linode, monitoring, Nagios, plugin
Slug: nagios-check-plugin-for-linode-monthly-bandwidth-usage

Since I have most of my public-facing stuff hosted with
[Linode](http://www.linode.com/?r=5c8ad2931b410b55455aadbcf0a8d86d6f698a91),
and I have a monthly bandwidth cap (albeit one that I'll probably never
come close to), I decided that it would be a good idea to add my monthly
bandwidth usage to my monitoring system. Luckily, Linode offers this
(their billing view of it - which is, of course, what I'm concerned
about) via their [API](http://www.linode.com/api/), and it's very nicely
implemented in [Michael Greb's](http://michael.thegrebs.com/)
[WebService::Linode](http://search.cpan.org/~mikegrb/WebService-Linode/)
Perl (CPAN) module.

Using Michael's Perl module, I wrote
[check\_linode\_transfer.pl](https://github.com/jantman/nagios-scripts/blob/master/check_linode_transfer.pl)
(github link) as a Nagios check plugin. It seems to be working fine for
me, and runs with the embedded perl interpreter, though it may not be
100% up to par with the Nagios plugin spec (for one, I used utils.pm
instead of
[Nagios::Plugin](http://search.cpan.org/~tonvoon/Nagios-Plugin-0.36/lib/Nagios/Plugin.pm)).
About the only thing unusual is that I store my API keys in a perl
module, so you'll need to create something like this in your plugin
directory (usually `/usr/lib/nagios/plugins`:

~~~~{.perl}
package api_keys;

require Exporter;
@ISA = qw(Exporter);
@EXPORT_OK = qw($API_KEY_LINODE);

$API_KEY_LINODE = "yourApiKeyGoesHere";

1;
~~~~

The latest version of the plugin will always be available at
[https://github.com/jantman/nagios-scripts/blob/master/check\_linode\_transfer.pl](https://github.com/jantman/nagios-scripts/blob/master/check_linode_transfer.pl).
The current version is also below. It's free for anyone to use under the
terms of [GNU GPLv3](http://www.gnu.org/licenses/gpl.html), though I
would really like it if any changes/patches/updates are sent back to me
for inclusion in the latest version.

~~~~{.perl}
#! /usr/bin/perl -w

# check_linode_transfer.pl Copyright (C) 2012 Jason Antman 
#
# Define your Linode API key as $API_KEY_LINODE in api_keys.pm in the plugin library directory
#  a sample should be included in this distribution.
#
# This plugin requires WebService::Linode from CPAN, with a patch - add the following to the end of sub _error{} in Linode/Base.pm:
#  $self->{err} = $err; $self->{errstr} = $errstr;
# Also - bug in WebService::Linode::Base docs, example, line 3 should be:
#  my $data = $api->do_request( api_action => 'domains.list' );
# not:
#  my $data = $api->do_request( action => 'domains.list' );
#
##################################################################################
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# you should have received a copy of the GNU General Public License
# along with this program (or with Nagios);  if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA
#
##################################################################################
#
# The latest version of this plugin can always be obtained from:
#  $HeadURL$
#  $LastChangedRevision$
#

use strict;
use English;
use Getopt::Long;
use vars qw($PROGNAME $REVISION);
use lib "/usr/lib/nagios/plugins";
use utils qw (%ERRORS &print_revision &support);
use api_keys qw($API_KEY_LINODE);
use WebService::Linode;
use Data::Dumper;

sub print_help ();
sub print_usage ();

my ($opt_c, $opt_w, $opt_h, $opt_V, $opt_s, $opt_S, $opt_l, $opt_H);
my ($result, $message);

$PROGNAME="check_linode_transfer.pl";
$REVISION='1.0';

$opt_w = 60;
$opt_c = 80;

Getopt::Long::Configure('bundling');
GetOptions(
    "V"   => \$opt_V, "version" => \$opt_V,
    "h"   => \$opt_h, "help"    => \$opt_h,
    "w=f" => \$opt_w, "warning=f" => \$opt_w,
    "c=f" => \$opt_c, "critical=f" => \$opt_c
);

if ($opt_V) {
    print_revision($PROGNAME, $REVISION);
    exit $ERRORS{'OK'};
}

if ($opt_h) {
    print_help();
    exit $ERRORS{'OK'};
}

$result = 'OK';

my $api = new WebService::Linode(apikey => $API_KEY_LINODE, nowarn => 1);
my $data = $api->do_request( api_action => 'account.info' );
if(! $data) {
    $result = "UNKNOWN";
    print "LINODE TRANSFER $result: ".$api->{errstr}."\n";
    exit $ERRORS{$result};
}

my ($used, $pool, $pct) = ($data->{TRANSFER_USED}, $data->{TRANSFER_POOL}, 0);

$pct = ($used / $pool) * 100;

if($pct >= $opt_c){
    $result = "CRITICAL";
}
elsif($pct >= $opt_w){
    $result = "WARNING";
}

print "LINODE TRANSFER $result: $pct"."%"." of monthly bandwidth used ($used / $pool GB)|usedBW=$used; totalBW=$pool\n";
exit $ERRORS{$result};

sub print_usage () {
    print "Usage:\n";
    print "  $PROGNAME [-w ] [-c ]\n";
    print "  $PROGNAME [-h | --help]\n";
    print "  $PROGNAME [-V | --version]\n";
}

sub print_help () {
    print_revision($PROGNAME, $REVISION);
    print "Copyright (c) 2012 Jason Antman\n\n";
    print_usage();
    print "\n";
    print "    Percent of network transfer used\n";
    print "\n";
    support();
}
~~~~
