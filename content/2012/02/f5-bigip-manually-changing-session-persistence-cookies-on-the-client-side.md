Title: F5 BigIp - Manually Changing Session Persistence Cookies on the Client Side
Date: 2012-02-03 13:32
Author: admin
Category: Tech HowTos
Tags: bigip, cookies, debugging, f5, load balancer, perl, persistence, web app
Slug: f5-bigip-manually-changing-session-persistence-cookies-on-the-client-side

Yesterday I was asked to help out a bit debugging issues with a site
that sits behind a [F5 BIG-IP](http://www.f5.com/products/big-ip/) load
balancer (LB). It's a pretty simple site, load balanced between two web
servers. The developers were complaining about intermittent page load
issues, so I immediately considered a problem with one of the two
servers (*ass*uming that the devs were clearing cookies and cache
between attempts). The LB is using HTTP Cookies for client session
persistence, but no matter how many times I cleared my cookies, I kept
being sent to the same back-end server. I know I could have added an
iRule to the LB, but it seems like bad practice to change a production
configuration for debugging something like this.

If your site uses a BigIp with cookies for persistence, it's no problem
to edit the cookies manually to force yourself to another back-end
server. Simply look through the cookies for a given site using something
like the [Web Developer addon for
Firefox](https://addons.mozilla.org/en-US/firefox/addon/web-developer/);
the BigIp cookie is named like "BigIpServer<poolname\>". The encoding
information is specified by F5 in their knowledge base [sol6917:
Overview of BIG-IP persistence cookie
encoding](http://support.f5.com/kb/en-us/solutions/public/6000/900/sol6917.html).
I also managed to find a Perl one-liner from Tyler Krpata, Manger of
Security Engineering at Constant Contact, [in a post on his
blog](http://www.tylerkrpata.com/2009/06/decode-f5-bigip-cookie-in-one-line-of.html).
I built on that work to develop the following perl script, which can
both encode and decode BigIP cookie IP/port values. The latest version lives
on my [GitHub misc-scripts repository](https://github.com/jantman/misc-scripts/blob/master/bigipcookie.pl).

~~~~{.perl}
#!/usr/bin/perl

#
# Perl script to de/encode F5 BigIp persistence cookies.
#
# The latest version of this script can always be obtained from:
#    via HTTP ot SVN
#
# Update information and description can be found at:
#   
#
# Copyright 2012 Jason Antman  .
#
#########################################################################################
#
# LICENSE: AGPLv3 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see .
#
# If you make any modifications/fixes/feature additions, it would be greatly appreciated
# if you send them back to me at the above email address.
#
#########################################################################################
#
# CREDITS:
# - F5 itself for the formula: 
# - Tyler Krpata 
#     for the Perl one-liner that this logic is based on.
#
# $HeadURL: http://svn.jasonantman.com/misc-scripts/bigipcookie.pl $
# $LastChangedRevision: 27 $
#
# Changelog:
#
# 2012-02-02 Jason Antman :
#   - initial version
#

use strict;
use warnings;

if ( $#ARGV < 0 ) {
    print "USAGE: bigipcookie.pl \n";
    exit 1;
}

if ($ARGV[0] =~ m/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}):(\d+)$/) {
    my $ipEnc = $1 + ($2*256) + ($3 * (256**2)) + ($4 * (256**3));
    my $portEnc = hex(join "", reverse ((sprintf "%04x", $5) =~ /../g));
    print "$ipEnc.$portEnc.0000\n";
}
elsif ($ARGV[0] =~ m/^(\d+)\.(\d+)\.0000$/){
    # decode a cookie value
    my $ipEnc = $1;
    my $portEnc = $2;
    my $ip = join ".", map {hex} reverse ((sprintf "%08x", split /\./, $ipEnc) =~ /../g);
    my $portDec = hex(join "", reverse ((sprintf "%04x", $portEnc) =~ /../g));
    print "$ip:$portDec\n";
}
else {
    print "USAGE: bigipcookie.pl \n";
    exit 1;
}
~~~~

An example of the usage:

~~~~{.console}
jantman@palantir:pts/8:~/bin/misc-scripts > ./bigipcookie.pl 192.168.23.50:80
840411328.20480.0000
jantman@palantir:pts/8:~/bin/misc-scripts > ./bigipcookie.pl 840411328.20480.0000
192.168.23.50:80
~~~~

On a side note for those of your who are security-conscious: yes, of
course, this means that if you're using BigIp with cookie persistence,
it is disclosing the internal IP and port of your server to your end
users.
