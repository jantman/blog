Title: Blacklists, Network Performance, New Project, XKCD
Date: 2007-10-10 14:03
Author: admin
Category: Projects
Tags: bandwidth, blacklist, comic, epcr, firefox, java, openepcr, patient care report, pcr, php ems tools, reverse-validation, XKCD
Slug: blacklists-network-performance-new-project-xkcd

Part 2 of today's thoughts...

**Blacklists, Blocking, Reverse-Validation** - Yes, they have some uses.
I use Daemon Synchronization in
[DenyHosts](http://www.jasonantman.com/wiki/index.php/DenyHosts) and
plug-ins like Pyzor in SpamAssassin. However, I've also been the victim
of blacklists, and the new Internet order, many times. There's a
conspiracy between ISPs - simply put, big ISPs want everyone else to use
big ISPs. I understand the logic behind reverse-validation. However, I
have a residential internet connection. I also run Linux. When I got
Verizon, I configured Postfix to deliver mail directly. Big mistake.
Most big email providers (AOL, MSN, probably Gmail too) will bounce back
e-mail that comes from a domain that doesn't reverse-validate. And since
Verizon owns my IP, despite the substantial sums of money they've been
getting from me, my IP doesn't reverse-validate to my domain name. To
top it off, Verizon blocks the usual SMTP ports on residential
connections, so I can't have people send me e-mail either. Everything
needs to be relayed through Verizon. To add to the frustration, Verizon
blocks port 80 on my connection, so I'm forced to serve my whole site on
an unused (and un-blocked) high-numbered port. And use
[DynDNS.org](http://www.dyndns.org) to redirect to my dynamic IP. This
wouldn't be so much of an issue if I didn't know that some large
companies have firewalls configured to block HTTP requests \*OUT\* to
any non-default port. As a result, my own father can't view my web site
or blog from work. What ever happened to the little guy?

**Network Performance** - I know I have old computers and an old switch.
But there's something wrong when network file transfers crawl by at \~3
Mbps. I setup [nttcp](http://sd.wareonearth.com/~phil/net/ttcp/) on two
of my machines to measure throughput, and was greeted with numbers in
the realm of 93-96 Mbps - what I'd expect on a 100 Mpbs network.
However, a file transfer between these two machines barely scratched 8
Mpbs. Maybe GigE is the answer, but I'll be looking into the theory
behind this in the next few days - admittedly, I don't know much about
network performance, but I'm willing to learn...

**New Project** - I've started planning on a new project,
[openEPCR](http://www.openepcr.org). My [PHP EMS
Tools](http://www.php-ems-tools.com) package for EMS and fire agencies
seems to be generating a lot of downloads (yet little community
interest), and I'm now seriously thinking about the lack of a free,
open-source Electronic Patient Care Report package for the pre-hospital
care industry. A lot of these organizations are volunteer and operating
on limited budgets. Stay tuned... all I'll say is that what I've planned
is something that you'd expect from me - open-source,
platform-independent, and geared towards limited hardware resources.
I'll probably be looking towards Java as a development platform, though
the interest generated in [Google Gears](http://gears.google.com/) may
also pay off. Of course, there's no way I can do such an ambitious
project myself, so I'm looking for developers to help out.

**Comic** - pretty much the only non-serious content in my Google Reader
account is [XKCD.com](http://xkcd.com). It's a great comic with
wonderful technical and geek humor. Today's
[comic](http://xkcd.com/327/) was so good that I just had to include
it...

[![image](http://imgs.xkcd.com/comics/exploits_of_a_mom.png)](http://xkcd.com/327/)
