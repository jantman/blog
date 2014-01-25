Title: Brother HL2170W DHCP Problems
Date: 2009-04-11 11:53
Author: admin
Category: Miscellaneous
Tags: dhcp, hl2170w, printer, vlan
Slug: brother-hl2170w-dhcp-problems

Two weeks ago, I [wrote about the Brother
HL-2170W](/2009/03/brother-hl-2170w-great-features-from-a-personal-laser-printer/)
that I got for my mother. It seemed absolutely wonderful. Until the
night of March 31st, just before Conficker was supposed to strike. Being
that mom's computer is the only one at home running Windows, I finished
up a long-standing project - and moved her desktop, printer, and AppleTV
over to a separate VLAN that's not routable to anything else internal
(i.e. anything important, or anything of mine). I'd already had the
"client" VLAN setup for a while, so it was just a matter of tweaking the
firewall rules and moving the static DHCP assignments from one subnet to
the other.

Well, that's where the problems started. While her Windows XP desktop
and AppleTV coped nicely, and got their new addresses in DHCP as they
should, the HL2170W did not, As a matter of fact, after two hours, I
hadn't seen a single DHCP request, even though I had the lease time set
to 10 minutes for both subnets. So, I tried administratively downing the
switch port a few times, to no avail. After a day of waiting, I came
back to the problem - and *still* found nothing in the DHCP logs from
that printer. I emailed mom and asked her to power-cycle it a few
times... still nothing! It wasn't even requesting DHCP when rolled, let
alone at a regular interval!

Fast forward a week or so, to today. I'm ready to call Brother Support,
as my mother hasn't had use of her new printer in a week and a half. I'm
infuriated - I've rolled the printer dozens of times, and not a single
event in the DHCP log. I know it's sending traffic from the port - I've
reset the counters and they're changing. I tried moving it back to the
original VLAN and confirmed that it still has its' original IP. I could
get into the web interface via [lynx](http://lynx.isc.org/) and \*tell
it\* to refresh DHCP, but this seemed quite pointless - there's no way
it's physically possible to send the web request and then switch the
port to the new VLAN before it gets DHCP.

So, I'm ready to call Brother Support. I then notice that the printer is
turned off at the moment. From the switch log, it looks as though it's
been powered off for six days. So, I turn it on. And then go about
starting my prep for the Brother call, first opening up a tail on the
DHCP server log, grepped for the proper interface. And, wouldn't you
know, as I get up to let the dog out, the printer starts spitting out
pages!

As far as I can tell, there's something *seriously wrong* with the
Brother HL-2170W DHCP implementation. Specifically, it didn't get an
address on the new VLAN until it was powered off for a \*long\* time.
Even reboots wouldn't trigger a request, until the box had been powered
off for *days*. More importantly, though, it seems that it only gets
DHCP ***once*** when it boots, and totally disregards the lease time!
