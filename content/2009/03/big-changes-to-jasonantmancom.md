Title: Big Changes to JasonAntman.com
Date: 2009-03-05 10:22
Author: admin
Category: Projects
Tags: fios, optimum, vyatta
Slug: big-changes-to-jasonantmancom

Well, I finally broke down and ordered Optimum Business. Come tomorrow,
I'll be moving from Verizon FiOS residential with a dynamic IP, much
blocked (hence jantman.dyndns.org:10011) and 10Mbps down/2Mbps up to
Optimum Business with 30 down/5 up, a block of 5 static IPs, and no
blocked ports.

It's going to be a crazy weekend. Probably not the best thing the week
before midterms, but oh well. Tomorrow morning I'm picking up a 42U rack
for home to replace the Sears shelving unit my boxes are currently on.
Cablevision is supposed to be here between 2-5 PM to do the install
(yes, they insist that for Business they do the install, even though
it's only a 4-foot coax run from the first splitter to the demarc). I've
got [Vyatta](http://www.vyatta.org) CE5 Beta installed on a [Proliant
DL360G2](http://h18000.www1.hp.com/products/quickspecs/11049_na/11049_na.HTML)
as the new router, ready to go (after some configuration). I'll probably
keep FiOS up until I know the new router is working correctly (I'll do a
test on my management VLAN).

Once Optimum and the new router is up, the fun starts:

1.  Forward the appropriate ports on the new router, including 80 (in
    addition to 10011).
2.  Bring the old router down and make sure the new one is up,
    operational, and forwarding all the right ports.
3.  Update DynDNS to point to the first IP, used as a catch-all for old
    DynDNS links.
4.  Begin assignment of the 5 IPs (everything will be behind NAT) based
    on a list of what hosts need valid reverse DNS, and then adding
    other ports (NATed) as needed.
5.  Update DNS for JasonAntman.com and the other domains.
6.  Update Optimum reverse DNS.
7.  Ensure that everything works as planned, DNS is up, ports are
    forwarded, and everything is as before (at least in terms of HTTP).
8.  Once DNS is up, reconfigure Apache to have a vhost handling any
    legacy requests to port 10011 and rewrite them to
    www.jasonantman.com.
9.  Setup a vhost for 'www' that takes URLs that used to be
    subdirectories (i.e. www.jasonantman.com/blog) and rewrites them to
    requests for the appropriate subdomain. Simultaneously move
    everything from the default vhost to name-based vhosts.
10. Ensure that old jantman.dyndns.org:10011 requests are being
    redirected properly, and requests for subdirectories under the web
    root are going to the right subdomain.
11. Check that this all works acceptably with the existing
    blogger-to-wordpress rewrite script.
12. **Finally** start rolling out some of the new services that I had
    waiting for the new connection.
13. Start the arduous process of reconfiguring my mail server, moving
    from Fetchmail from Verizon to an actual mail server, make
    everything work, and make sure my IPs aren't blacklisted.
14. **Ugh.** Find anywhere in the entire 'net where my old @verizon.net
    address appeared (especially GoDaddy, DynDNS, other important stuff)
    and change it to the new jasonantman.com address.
15. Since this is all in my mother's basement (there's nothing like a
    mother's love, especially when it comes to a constant hum emanating
    from the ground level of a house), figure out what to do for her
    when the verizon.net email goes away.

So I might have some downtime this weekend, but when things come back
up, I'll be done with this DynDNS and Port 10011 crap.
