Title: Perl script to convert F5 BigIp VIP address to list of internal pool member addresses
Date: 2012-04-24 22:04
Author: admin
Category: SysAdmin
Tags: bigip, f5, load balancer, perl
Slug: perl-script-to-convert-f5-bigip-vip-address-to-list-of-internal-pool-member-addresses

I often find myself logging in to the web UI of [F5
BigIp](http://www.f5.com/products/big-ip/) load balancers and tracing
down a VIP address to the servers that actually back it. This is an
arduous, repetitive task of tracing from the VIP list to the VIP details
page to find the default pool, then matching up that in the pool list
and checking the pool members page. Luckily, the F5 boxes have a [web
service API](https://devcentral.f5.com/) that can be used for tasks like
this. They have GPL sample code in Perl that uses only
[SOAP::Lite](http://search.cpan.org/~mkutter/SOAP-Lite-0.714/lib/SOAP/Lite.pm)
(as well as Getopt::Long and Pod::Usage) to interact with an F5 BigIp. I
wrote a simple script to trace a VIP to the appropriate internal pool
member addresses, assuming you have a simple configuration of VIP -\>
Single default pool -> pool members.

Usage is quite simple:

~~~~{.console}
> ./VipToInternalHosts.pl --host=prod-lb1.example.com --user=myname --pass=mypassword --vip=128.6.30.130:80
VIP 128.6.30.130:80 (f5_vip_name) -> Pool 'pool_name'
Members of Pool 'pool_name':
    10.145.15.10:80
    10.145.15.11:80
~~~~

The code can be found at
[http://svn.jasonantman.com/misc-scripts/VipToInternalHosts.pl](http://svn.jasonantman.com/misc-scripts/VipToInternalHosts.pl)
via either HTTP or SVN. I hope it's of use to someone else as well.
