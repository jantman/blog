Title: SunBlade Workstations
Date: 2007-12-12 22:51
Author: admin
Category: Hardware
Tags: sunblade sun solaris opensolaris install firmware boot
Slug: sunblade-workstations

So today I picked up two surplus SunBlade 150 workstations. The price
seemed right, and I figure that at the very least, they'd give me some
Sparc machines to play around with. The two seem slightly different.
Externally, one has a CD-RW and one has a DVD-ROM. The one with the DVD,
the first one I'm working with, has a 650MHz Sparc IIi, 512 Mb RAM, and
XXXXX HDD. I'll figure out the specs on the second when I get it
running.

They also both use simple EIDE drives, so I might put a new drive in,
after checking drive current drive information through SMART. I planned
on using one of the machines (probably this first one, the 650MHz with
the DVD) to replace my aging mailserver at home (a 350MHz Pentium II
Gateway desktop), running Solaris 10. The other one will be a
workstation/desktop for me, which will probably run either Solaris 10 or
Solaris Express Developer Edition (SXDE).

Unfortunately, the project seems to have hit a dead-end. Both systems
have hardware/NVRAM security setup, so they won't boot from CD without a
password. They also won't boot the existing Solaris installation, as
it's looking for a whole bunch of network services that don't exist. I
found a few suggestions online on how to bypass this, but none of them
worked. So, at this point, I have a few options to consider:

1.  Hope that as a Sun Microsystems Campus Ambassador, I can contact
    someone who can advise me on how to clear out the password or NVRAM.
2.  Hope that as a Rutgers employee, I can track down someone on the
    Camden campus where these came from that may have the NVRAM
    password.
3.  Break down and pay $40 each for \*new\* NVRAM chips.

We'll see what the next few days brings. Hopefully not resorting to a
solution that costs more than I paid for the machines.
