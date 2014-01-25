Title: Updates, SuSE Online Update Issues
Date: 2007-11-01 15:29
Author: admin
Category: Ideas and Rants
Slug: updates-suse-online-update-issues

It's been way too long since I've posted an update. But I haven't been
doing nothing. In fact, I've been quite busy - and not just with school
and Sun and the Rutgers job. So, I'll go through a few of the happenings
of the past few weeks.

<span style="font-weight: bold;">Machine & Online Update
Problems.</span> First, I lost two machines. About a month ago, my main
storage machine (STOR1) running a 6-disk SCSI array of 18.2-Gb disks in
RAID 0+1 lost two disks in an hour. Strange. Next time I was home, I
pulled the two bad disks (bringing it down to 4 disks total), put
OpenSuSE 10.1 back on it (10.2 won't play well with my old Compaq RAID
controllers - the machine is a G1 Proliant ML370) and installed Bacula.
I'm happy to say that after a weeks' worth of work, I have Bacula
working and backing up 3 machines locally. Unfortunately, I have two
machines - my mail and SSH server and my storage server with a 250Gb IDE
drive - that were running SuSE 9.3 (still!). They wouldn't take Bacula
from RPM or source, as the director (STOR1) was running Bacula 2.x and
the only RPMs available were 1.x. I attempted an Online Update through
YaST/YoU. Well, wouldn't you know, it ran, it updated, and the whole
system broke. I mean gone. I couldn't run \*any\* command in the shell,
at all, because - you guessed it - YoU updated glibc. To a much newer
version, and pretty much everything was linked to the old version. I
couldn't even "exit" to end my session.

Well, luckily, I had data on the 250-Gb disk and everything else on a
10Gb, so next time I was home, I put OpenSuSE 10.2 on the box, and I now
have a 250Gb Bacula storage target on the network. Maybe I'll even
upgrade to Gig-E sometime soon to speed up those slow weekly full
backups.

<span style="font-weight: bold;">Help, My files are gone!</span> The big
storage box with the 250-Gb disk has been called "janus" for years,
since I called my do-everything-box "saturn" and the rest were Saturn's
moons. Since then, things have become complicated enough that I adopted
a functional naming convention, and the box became "STOR2" when I
re-installed the OS. Well, about a week later, I SSH'd into saturn - a
10-year-old Gateway desktop, 40Gb  
HDD, 192Mb RAM, and a PII-350MHz processor - that now runs my mail
server and is my externally-visible box to SSH into. I ran "ls" in my
home directory, and got nothing. Nothing at all. It just hung there. I
exited and tried again. I tried as root. By then I had about a dozen "D"
state ls processes. I was stumped. I tried everything. My first thought
was a stale NFS mount, but I checked, and everything looked right. I
could ls portions, like "ls a\*" and get good output. I could strace ls
and see all the right output. But I couldn't ls. Just the one directory
- not any subdirectories - but any user. I spent hours looking around,  
to no avail. It wasn't until two nights ago - about a week into the
problem - that I finally gave up and rebooted to get rid of those
now-zombie processes. And, wouldn't you know, ls worked perfectly. Why?  
Yeah, you probably guessed that, too. When I looked over fstab and
mount, everything looked normal - except that after two years, the
hostname "janus" looked perfectly correct to me!

<span style="font-weight: bold;">Rack.</span> After some discussion with
my roommates, last Friday night I found a 42U Compaq rack enclosure -
complete with wheels, door, and a side panel, on Craigslist from a
seller a few towns over. We all drove over in the truck and, $65 later,
we now have a 42U rack in the living room of our apartment. It's a thing
of beauty. We got it setup around 10:30 PM, and Joe and I were up until
6 AM the next morning bringing down the network, moving hardware to the
rack, re-cabling, and bringing everything back up. We did hit a few
snags - mainly because I demanded an IP switch from 192.168.0.xxx to
192.168.2.xxx so that I could easily setup a VPN from the IPcop firewall
at the apartment to its' matching counterpart in my basement at home.
Well, things are still being added to the rack, but it's coming along
very nicely.

<p>
<center>
![image](http://www.jasonantman.com/GFX/rack1sm.jpg)

</center>
</p>
**The Rack** - (clockwise from top left) some ballast in the bottom (an
ancient Proliant 6000 with 12 or so SCSI disks and 3 power supplies, 3x
220MHz pentium, not running), 3 AM - Joe troubleshooting the IPcop box,
with the rack almost fully loaded, Soekris net4501 as a temporary
firewall/router (running m0n0wall), me in my new home...err... rack.

<span style="font-weight: bold;">VPN.</span> The main impetus behind the
IP switch was my desire to have an IPsec VPN between home and the
apartment. Beyond ease of use, a good intranet, and the hope of being
able to SSH into my various boxen  
without going through saturn, my one externally-visible SSH server, I
was also psyched about the idea of small backups with Bacula over the
VPN, and the hope of getting two Nagios boxes - one at each end - that  
would work in concert. Well, of course, the subnet mask here is /22 and
everything at home is still /24, so it's going to take a bit of work
this weekend, but hopefully everything will come together well. Stay
tuned.

<span style="font-weight: bold;">PBX.</span> While I was working on VPN
stuff, Joe took it upon himself to forcibly commandeer one of my spare
boxes and setup
[Trixbox](http://www.trixbox.org/)<http: org><span style="text-decoration: underline;">
</span>(formerly Asterisk @ Home) on the LAN. At the moment, we're
waiting for an FXO card to show up in the mail - and for the money to
get a few SIP phones for testing - but it looks like it'll all be up and
running, and we may even move over to VoIP in the apartment. To make
things better, we have Festival working, and I'm well on my way to a
Nagios interface that will be able to dial an extension (or dial out)
and speak an alert.

<span style="font-weight: bold;">Conserver.</span> A lot of stuff on the
rack has serial console access - switches, IPcop, routers, development
stuff, and - hopefully soon - some Sun hardware. So, a terminal server
sounded great. After some research, I came up with two possibilities - a
[page](http://www.eng.auburn.edu/users/doug/console.html) from 1998
giving an example of a kludge of a console server using GNU Screen, and
[conserver](http://www.conserver.com/), a purpose-built application that
can operate in a client-server model over the LAN, and also includes
good handling of locking on a per-user basis and console locking. I
planned two incarnations of the console server - the first and current
development machine is an ancient PII laptop with 192MB RAM, CD drive,
10Gb HDD, networking, and serial and USB ports. I decided to give serial
to USB adapters a shot.

My first installation was [Debian](http://www.debian.org/)-based, as
[OpenSuSE](http://www.opensuse.org/) 10.2 won't load on such an old
machine. However, after grappling with learning a new distro, I opted to
reinstall with [CentOS](http://www.centos.org/) 5.0, a much more natural
transition from SuSE. After installing CentOS, it only took me a few
hours to get everything humming away, and get conserver compiled,
installed, and running. Configuration is fairly simple though, on my
next box, I'm going to have it install to the locations I'm used to -
/bin instead of /usr/local/bin, etc. All in all, it seems to work well.
I didn't try networked mode, but it works beautifully by SSHing into the
box. It handles multiple users on the same console very well, shows the
status of the consoles, and allows stealing of locks. I'm working on
writing a Nagios check script for it in Python, but be warned - a
console's "up" or "down" status is simply whether the port is open. You
can, obviously, pull the cable from the device and still see "up".

The one issue with this kludgey test setup is that my USB serial
adapters seem to change device names on reboot. I currently have two,
and at the last reboot, /dev/ttyUSB0 and /dev/ttyUSB1 switched names
which created some confusion. When I get around to it, I plan on getting
a small, quiet, older (and cheap) 1U server with a PCI slot to serve as
the console server. I have a few spare Equinox breakout cables for
multiport serial cards, and I might be able to find and use a card that
they fit.

<span style="font-weight: bold;">Netra.</span> For a while, I've been
wanting to try Solaris, and I can't think of a better way to do it than
buying some Sparc hardware, for the fun of it. Well, I found a Sun Netra
T1 on Ebay, 500MHz Sparc-II, 512Mb RAM, 40Gb HDD (SCSI) for $47 on Ebay,
and couldn't resist it. I ordered it Sunday night. Sure enough, Tuesday
afternoon, I get the following E-Mail:  
"</http:><span style="color: rgb(0, 0, 0);font-family:arial,sans-serif;font-size:10;">Hello,  
This is Bcd-parts. we contact you because we make a mistake in this
item: 230185304870. we put it online but we sell it before, so we do not
have any of this item. I'm apologize about this mistake, we will refund
the money as soon you respond back the email.  
Thank you!"

Amazingly, I was able to resolve the issue that day, and the refund is
being processed. However, I don't have my server!  
</span><http: org>  
<span style="font-weight: bold;">Nagios.</span> I'm a big fan of
[Nagios](http://www.nagios.org/). I use it at home to monitor all of my
hosts, as well as some remote systems that I'm responsible for. I make
heavy use of the check\_by\_ssh plugin, so that it doesn't require any
infrastructure past pubkey authentication for the Nagios user. Now that
I have a few systems running in the apartment also, once I get the VPN
setup, I'll be installing Nagios down here as well, and probably trying
to tackle the task of setting up the two servers to jive by passing
passive check results of the LAN hosts to each other.

<span style="font-weight: bold;">Print Quota.</span> We have a shared
laser printer in the apartment, used by all five people living there.
It's a low-end Brother model. After a discussion one evening, I got very
interested in finding out how many pages each user is printing. The
built-in print server doesn't provide this functionality, nor does it
support JCL. So, I googled for a solution... and, amazingly, didn't find
one. The most that I could find is that there are two big Unix-based
print quota packages, but both of them require a print server between
the network and the printer - an option that I may consider, but don't
really want to implement. I don't need the ability to deny printing, or
figure out how much toner is used, or anything fancy like that - I just
want to find out how many pages each user on a defined list prints.

After some brainstorming, I came up with an awful kludge that might
work. I wrote a Python script that screen-scrapes the print server's web
interface for the current lifetime page count and status. The concept is
essentially that I put a server on the network, and configure the switch
so that it is a monitor port for the printer. I then have access to 1)
the printer's page count and 2) all traffic to/from the printer. I've
thought of two ways to get the page count of a job:  
</http:>

1.  Dump all of the TCP traffic to the printer. When a job starts, find
    the IP (and MAC?) that started it. Wait for it to finish. Wait a few
    seconds, check the printer status, if it's back to "ready", get the
    page count.
2.  Dump the traffic to the printer. Analyze all traffic to extract the
    print job information, and get the page count there. Then check
    against the printer's web interface (so we don't count pages when it
    ran out of paper or jammed).

Obviously, \#2 is much more complex. However, \#1 already is wrought
with edge cases - two users printing simultaneously, a paper jam that
causes the printer to wait (and the script times out and returns a page
count of 0), etc. We'll see where I get in designing a solution.

Once each job is complete, and we have a page count, we can put that
into a database with the date and time, page count, printer name (the
advantage to this is that it would theoretically support multiple
printers as long as it could see their traffic), client IP and MAC, and
client username (looked up from a table mapping IP/MAC to username).

<span style="font-weight: bold;">Surplus</span>. One of the wonderful
things about working for Rutgers is that they own millions of dollars of
computer equipment. Usually, it seems like when they're done with it, it
falls into a black hole of buybacks, trade-ins, and disposal. However,
it just so happened that my department has a lot of stuff they're
getting rid of, and I was able to work out an employee purchase before
it disappears. So, coming to a rack in my living room (or my basement at
home) is a Dell PowerEdge 2550, PowerEdge 650, two rackmount
monitor/keyboard/mouse units, a BackUPS Pro 1400 (no monitoring, but
better than nothing), a BayStack 350T-HD switch, a Xerox DocuPritn
N4525, and a few other goodies. I'm already working on putting OpenSuSE
10.3 as Xen dom0 on the 650 and Solaris SXCE 11 (built 75) on the 2550.
We'll see what happens with it all soon...  
<http: org></http:>
