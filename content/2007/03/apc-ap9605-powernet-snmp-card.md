Title: APC AP9605 PowerNet SNMP Card
Date: 2007-03-01 17:09
Author: admin
Category: Tech HowTos
Tags: ap9605, apc, powernet, snmp, UPS
Slug: apc-ap9605-powernet-snmp-card

In the theme of upgrades, I also purchased two APC SmartUPS1000 units
from refurbUPS.com. Now, I know that a lot of people are perfectly happy
with serial connectivity. And it has its positives. But I'm running 2-3
servers per UPS, older servers, wanted to be able to monitor the UPSs,
and perhaps control server shutdown, over the network.. So, I found that
refurbUPS.com also sells SNMP management cards for them. They sell a
refurbished AP9605 - it's an old 10BaseT PowerNet SNMP-only card (with
telnet management). Seemed good, and the price of $15 was right.

They showed up, but I couldn't find much about them online, let alone
anything useful.

After a phone call to APC, I managed to get the user's manual emailed to
me. The few instructions I found online were totally wrong.

The general setup goes like this:

1.  Connect network cable to card.
2.  Connect serial cable between a computer and the UPS's serial port.
3.  Get a terminal emulator, like
    [minicom](http://alioth.debian.org/projects/minicom). Speed is
    2400bps.
4.  connect and press enter. You'll be asked for a username and
    password. Use "apc" for both.
5.  5) Setup the network - IP, mask, gateway, etc.
6.  Ready-to-go!

I also have some information about the card on my wiki at:
[AP9605](http://wiki.jasonantman.com/index.php/AP9605).
