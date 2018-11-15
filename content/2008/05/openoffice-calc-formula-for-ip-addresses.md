Title: OpenOffice Calc formula for IP addresses
Date: 2008-05-30 10:56
Author: admin
Category: Software
Tags: ip address, openoffice, spreadsheet, tuxtruck
Slug: openoffice-calc-formula-for-ip-addresses

It's been a while since I've posted. Things are quite busy, with work 4
days a week (9-5) and classes 6-9:30 at night 4 days a week (though
classes are Mon-Thurs and work is Tues-Fri).

I'm plodding along on with [TuxTruc](http://www.tuxtruck.org/)k - we now
have a domain name
([http://www.tuxtruck.org/](http://www.tuxtruck.org/)) and playlist
generation is finished. This weekend should yield playlist parsing. Once
MP3 playing is working, I'll begin the hardcore development - GPS, OBD,
and Bluetooth. Also, I'm working on a hardware budget for the prototype,
but it's ending up much higher than originally imagined. If I end up
going with the [Xenarc
MDT-X7000](http://www.xenarc.com/product/MDT-X7000.html) display (which
includes a head unit with DVD playing, amplifier, CD playing, and radio
- though those are features I'd rather to in software on the PC, and
just use the amplifier) which runs $800 USD, the total is looking more
like $2000 than the $1000 I had planned. More to the point, the X7000
currently has poor reviews, and is backordered everywhere pending a
firmware revision. I may end up going the route of a separate head unit,
or a dedicated amplifier (though volume control is still an issue) and
getting a better daylight-readable touchscreen (though I still have a
strong preference for a motorized in-dash type, given the theft rate
around school).

Another item of news - my mother is considering moving from Verizon FiOS
to the Cablevision/Optimum Triple Play - iO digital TV, cable, and
voice. Given that jasonantman.com - and all of my other machines - live
on shelves in her basement, this will have quite an impact on me. And a
good one! Optimum offers Business-grade service at 30 Mbps down/5 Mbps
up **with 5 static IPs** at a rate
that I can afford. So, there may be an end to DynDNS, and my sites might
finally live on port 80, like they should! On the down side, this would
mean (for digital TV) a major coax rewiring of mom's house - and RG-6/UQ
isn't cheap.

Anyway, the tip of the day - OpenOffice Calc formula to increase the
last quad of an IP address by one:

`=CONCATENATE(LEFT(A1;SEARCH(".[0-9]+$";A1));VALUE(RIGHT(A1;LEN(A1)-SEARCH(".[0-9]+$";A1)))+1)`

I was doing up a little spreadsheet of IPs in the office, and like a
good SA (with nothing else to do), came up with a formula to increase
the last octet by one. Just enter a dotted-quad IP in A1 (or whatever
other cell, correcting the formula), paste this below it, and copy down
the page to your heart's content. (Granted, it only changes the last
octet, and expects a properly formatted IP).
