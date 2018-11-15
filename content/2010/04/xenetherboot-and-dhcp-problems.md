Title: Xen/Etherboot and DHCP Problems
Date: 2010-04-20 10:46
Author: admin
Category: Software
Tags: dhcp, dhcpd, etherboot, ldap, pxe, xen
Slug: xenetherboot-and-dhcp-problems

Well, I've spend the better part of the last week or so debugging a
problem with out new Xen VMs (on one host) not getting DHCP leases.
Since our DHCP servers (ISC DHCPd 3.0.6) are using Brian Masney's [LDAP
patch](http://personal.cfw.com/~masneyb/) (which has recently been
included in [mainline
DHCPd](http://www.isc.org/files/release-notes/42b2_0.html)), I assumed
that this might be the source of some of the problems.

The Xen client booting process uses [Etherboot](http://etherboot.org/)
(specifically 5.4.2 on my machines) to get DHCP and PXE for the client.
The Etherboot ROM is generated online with
[ROM-o-Matic](http://rom-o-matic.net/) (by the Xen devs) and is then
packaged into `hvmloader` (though I would not find this out until much
later in my investigation, given the piss-poor documentation about it).
So, aside from pulling the SRPM for Xen and looking around, I decided I
couldn't really debug much on the client end (I wasn't getting any
BIOS-like messages from Xen, so the client end seemed to be pretty much
a black box).

After a week of re-examining our DHCP servers, moving the client between
pieces of hardware and different networks, tracing out the DHCP logs,
and debugging everything in-between, I finally resorted to doing packet
captures and analyzing them. Last Thursday (my last work day of the
week), I popped my laptop on the same network, set it up in DHCP, and
did some captures of the laptop (which worked correctly) and the problem
VM.

Sometime around 10:00 PM, long after I'd gotten home, I had opened
captures of both the good and bad hosts in separate
[Wireshark](http://www.wireshark.org/) windows, and was going through
them line-by-line. I'd also written a nifty little [Perl
script](/GFX/dhcptest.pl) (my weakest language) using
[Net::DHCP::Packet](http://search.cpan.org/~fvandun/Net-DHCP-0.11/lib/Net/DHCP/Packet.pm)
to craft packets identical to the ones from the working and FUBAR hosts,
and inject them into the network. The only thing I could find different
was the value of the "secs" field of the DHCPDISCOVER packets (octets 9
and 10), which are supposed to contain the number of seconds that have
passed since the host started booting ([RFC
1541](http://www.faqs.org/rfcs/rfc1541.html)). My laptop (the working
host) started getting replies from the server at 21 seconds. I took my
Perl packet-injecting script, and started adjusting the "secs" values of
both the working and bad packets. Sure enough, with identical packets
from each host, the values converged. Anything with "secs" below 2 got
no response from the DHCP server, anything with 2 or greater got a
correct lease.

Then it hit me. When we used to have a primary/secondary DHCP server
setup (with manual failover), we'd configured the secondary server with
`min-secs: 2`, instructing it to not give out any leases to clients with
a "secs" value of under 2, to prevent the secondary server from
answering if, for some reason, the primary was still online. Bingo.

At this point, I'm waiting to have a meeting of the binds before I add a
network-level override of "min-secs: 0" for the networks in question.
But I'm relatively confident that everything will go smoothly from there
on.

This experience highlighted that one small "bug" can confuse 3 people
for the better part of a week:

[Etherboot](http://etherboot.org/) (at least 5.4.2) doesn't increment
the "secs" field in its DISCOVER packets as RFC 1541 suggests. Therefore
anyone with "min-secs" in their dhcpd configuration won't ever give out
a lease.

In hindsight, it really was a brain-dead moment. There was a little note
in the dhcpd logs that I, and the others, totally overlooked:
"DHCPDISCOVER (...) 0 secs < 2". I guess I should have turned my brain
on and realized that those few characters were probably important, and
there for a reason, no matter how unassuming (and un-error-like) they
may be...
