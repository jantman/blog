Title: Shamelessly Over-Engineered Coax Lightning Protector
Date: 2018-07-05 16:43
Modified: 2018-07-05 16:43
Author: Jason Antman
Category: DIY
Tags: network, lightning, surge, fiber, coax
Slug: shamelessly-over-engineered-coax-lightning-protector
Summary: My shamelessly over-engineered coax lightning protector using fiber media converters.

I wrote a few weeks ago about my [new router purchase](/2018/06/new-home-router---partaker-i5) thanks to a close lightning strike that came in over the coax for my cable TV and Internet (we have aerial lines in my neighborhood) and fried a good portion of my network (my router, switch, and the on-board Ethernet port on my desktop). A few days later I learned that at least four of my neighbors had damage from the same storm, all to devices connected to incoming coax or their home networks, and in some cases much more catastrophic than mine.

Given what this _could_ have cost me both monetarily and in time - if it had decimated my desktop and/or the rest of my wired devices - I decided that I had to find a decent solution. I bought an inexpensive UPS to provide backup power and hopefully-better AC surge protection (it's not a double-conversion so I'm doubtful it would do much for a lightning-induced surge) but still needed to figure out a solution for coax, the actual source of the damaging surge last month. Unfortunately it seems that there aren't many options for suppressing high-current surges on coax that work without permanent installation and with broadband Internet. There certainly are some, but many seem to either have little proof for their effectiveness against lightning-induced surges or are single-use devices that fail destructively and _should_ stop the surge.

After trying for a while to come up with a decent, reliable solution I realized that I may be approaching the problem from the wrong direction. My cable modem is rented from Comcast, and I really don't care if it gets damaged from lightning - that's Comcast's problem. What I care about is my network. And while there may not be accepted and readily-accessible methods of protecting coax, air-gapping an Ethernet network is both feasible and relatively common. Enter, the shamelessly over-engineered coax lightning protector:

[![side view of my desk with the fiber media converters installed](/GFX/mediaconverter1_sm.jpg)](/GFX/mediaconverter1_med.jpg)

[![close-up of one end of the fiber circuit](/GFX/mediaconverter2_sm.jpg)](/GFX/mediaconverter2_med.jpg)

[![close-up of the other end of the fiber circuit](/GFX/mediaconverter3_sm.jpg)](/GFX/mediaconverter3_med.jpg)

For $84 - a small fraction of the damage that could have been done - I bought a pair of [10Gtek 10/100/1000Base-Tx to 1000Base-LX](https://www.amazon.com/gp/product/B06XZ6CV6W/) copper to fiber media converters and a [2M SC-SC singlemode patch cable](https://www.amazon.com/gp/product/B009938B50/). I hooked one of them to my router via a standard Cat6 UTP patch cable and the other to the cable modem with a similar cable. Between them is only non-conductive optical fiber, effectively providing a relatively complete air gap between the cable modem connected to the coax (which is strung pole-to-pole in the air, effectively like a lightning rod) at one end and my network at the other. The cable modem and its media converter are plugged directly into the wall on a separate circuit from my computer... so for a surge to make it to my network (assuming everything is wired as it appears to be), it would need to jump from the coax to the mains and then travel to the breaker panel on the other side of the house, back through a separate circuit to my desk, and through my UPS.

It may be horribly over-engineered, but for less than $100, I have some peace of mind that the damage from last month won't be repeated.
