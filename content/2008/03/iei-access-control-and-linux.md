Title: IEI HubMax Access Control and Linux
Date: 2008-03-31 12:43
Author: admin
Category: Tech HowTos
Tags: access control, door lock, hubmax, iei, ieib
Slug: iei-access-control-and-linux

At the [Midland Park Ambulance
Corps](http://www.midlandparkambulance.com/), where I've been
volunteering my time as an EMT and all-around tech guru for three years,
we have an [IEI HubMax2 access control
system](http://www.ieib.com/product-details.html?id=49). Maybe overkill
for us (only 78 users in it, including old codes), it's pretty simple -
a box with some microcontrollers sits in a wiring closet, and is hooked
up to keypads at each door, and relays to electromechanical strikes.
Type in the right code, and the door opens. Obviously, it also logs all
entries as well as unknown codes (but doesn't log the actual code if
unknown, so instead of removing old users, I set their codes to an
invalid timezone so the doors don't open, but accountability is still
intact). Well, the old box died - fried by a surge from a blown computer
that was hooked up to its' serial port. New one was installed this
weekend - an 8 hour ordeal.

The problem with the system is that to program it, I have to grab the
laptop out of one of the ambulances, have IEI's proprietary
Windows-based programming software (which programs it via sending and
receiving full binary memory maps of the controllers over 1200 baud
serial), and spend half an hour in the utility closet (next to the
furnace) where the box is waiting for memory maps to transfer over the
slow direct connection. Well, there's a proliant server running
[OpenSuSE](http://www.opensuse.org/) seven feet away... why not use
that?

While IEI offers their
[eMerge](http://www.ieib.com/products-browser-managed.html) systems -
appliance servers that manage their access control units via a web
interface - for $6000, which run RedHat, they won't even respond to my
emails inquiring whether they have Linux-based programming software for
their HubMax line. We don't get that many new members per year, so I
figured just programming in a few spare codes will handle it. Removing
people can wait, as people usually leave on good terms. However, every
once in a while something's amiss at the building (usually a door left
ajar, or food left out), and I'm called upon to pull the logs. It's a
pain in the @$$. I have to hunker down in that utility closet with a
laptop, waiting for the whole memory map to download over 1200 baud just
to see who came and went. Porting the software to Linux wouldn't be a
quick project. This is even worse during the school year when I'm living
in my apartment an hour away, taking classes full time, and still
working 25 hours a week.

<span style="font-style: italic;">The Solution</span>: At the end of my
eight-hour install, everything was programmed and setup, but the logs
were still bothering me. Then I hit on an idea. Remembering how archaic
the real-world interfacing of these things seemed to me (how can you use
binary memory maps? What about a serial terminal with an ASCII command
set, or even Ethernet and SNMP or Telnet? I really want to build one of
these things running real-time Linux...), I started to flip through the
manual and, sure enough, found a command (entered on a 12-key keypad on
the main board) to dump logs in realtime to a serial line printer.

I ran a cable to the Linux-based server not 10 feet away, fired up
Kermit, issued the Enable Log Print code, and tried a code entry on the
keypad by the front door. Bingo!

In the two days since, I have a little daemon coded in PHP (yes, PHP)
that reads the serial line and dumps all log data (entries, exits, door
ajar, unknown code, access denied) to both a text file (for debugging
and redundancy) and into a MySQL database. Another hour of coding and I
have a simple web GUI, available on any of the computers on the LAN, for
officers to check who's come, and who tried to get in but couldn't.

I've never written a daemon before, so I still have a bit more research
to do - mainly in terms of error handling and how to keep it constantly
running. However, I have a first version working.

In the next few days I'll start posting better code for ieilogd. I have
[some in CVS now](http://cvs.jasonantman.com/cvs/ieilogd/), but it's
kludgey (well, it was written through
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
on a Windows laptop in a utility closet at 3 AM). It also has quite a
bit of user-handling code that's specific to the roster format of my
package [PHP EMS Tools](http://www.php-ems-tools.com).
