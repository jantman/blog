Title: Solaris, Linux News
Date: 2007-11-14 14:33
Author: admin
Category: Miscellaneous
Slug: solaris-linux-news

Well, I've been pretty busy lately, between school work and work for Sun
and Rutgers. Rutgers seems to be planning a new student lab, so I'll
probably have a hand in that. And I'm now doing troubleshooting and
on-site support for RUwired and the Smart Classrooms. It's a big step
down from programming web apps, but quite refreshing to have a job that
gets me out of the dungeon now and then.

I'm also planning my first tech demo as the Sun Campus Ambassador, which
will tentatively be held on December 4th at the [RUSLUG][] meeting. Stay
tuned for more.

In other news, unfortunately, I haven't gotten my surplus from Rutgers
yet. I'm sitting here in my cube, staring at a pile of equipment with
nowhere to go. I just hope that this works out next week so I'll have
some time to play around on Thanksgiving weekend.

Anyway, I was reading an [article][] that I saw on Digg about WalMart's
$200 Linux-based computer. What a great idea. Admittedly, I shop at
WalMart now and then (well, I'm in college) and one line got me a bit:  
"The gPC is built using tiny components, but put inside a full-size case
because research indicates that Wal-Mart shoppers are so unsophisticated
they equate physical size with capability."  
Though I'll admit that it's probably true. The author seemed to think
that Linux may have found its' niche, and was even bold enough to say
that, "While the price of hardware has fallen dramatically, the price of
Windows hasn’t. This could be Microsoft’s Achilles’ Heel. "

Well, ahmen. I've been mentioning that for quite a while now, as many
others have. We've reached the point where Microsoft Windows and
Microsoft Office is considerably more expensive than the computer that
they run on. OEMs like Dell are selling Linux-based PCs (granted they
aren't really advertising them, and I didn't see any mention of them
when I glanced through their Home/Home Office lineup), and even WalMart
is selling Linux-based systems. What I wonder, though, is how long it
will take mainstream consumers to look at two shiny little CDs,
befuddled that they cost more than a whole computer, and wonder what
other options there are.

To go off on a tangent for a moment, yesterday I took delivery of a
beautiful Wastern Digital My Book external hard drive. It's the first
one I've bought in almost three years, since my LaCiE (F.A. Porsche
design) disk croaked on me and took 100 GB of photo scans with it. This
one, a My Book Premium ES, is a 500 GB disk in a 3-pound-ish box, which
cost $150 with shipping. I remember the first time I saw a writable DVD,
when I was doing an internship in video postproduction. They kept the
blanks locked up. I don't think I ever would have imagined paying $150
to have half a terabyte in the palm of my hand. Anyway, the great thing
about this model is that it has a 3.0 Gbps eSATA connector, so it can
easily be used as \*fast\* exteral storage. So, once I got it, I set
about backing up my laptop. Hopefully by this time tomorrow, I'll have a
laptop that dual-boots openSuSE 10.1 (pure 64-bit) and OpenSolaris SXDE
9/07.

Back on topic, I'm totally enthused that Linux is finally making headway
in the desktop market. However, a few minutes ago, sitting here at my
desk, I was struck with panic. The same type of panic that would hit a
driving instructor if he sent his student out in a car and then realized
the poor kid didn't know there was a brake. Linux is a multi-user
operating system. At its' heart, it's designed to be a server-bound
Unix. And all of a sudden it struck me that people are downloading
Ubuntu or some other easy-to-use distro, and nobody told them where the
brake is!

I doubt that most new Linux users know what I (or any experienced user)
take(s) for granted. I'd hope that Ubuntu doesn't enable SSH by default,
but I don't know. But, realistically, how people who "try" Ubuntu
because it's "free" (as in free beer) understand administration and
security of Linux systems? If they run SSH, do they know to run
something like [denyhosts][]? Do they even know what system logs are or
where they are found, let alone check them? Do they understand file
checksumming, and something like [Tripwire][]? More importantly, do they
understand the power of their system, and how much it could do without
their knowledge?

Many security experts have conjectured that the lack of Linux viruses is
simply because Linux has such a low market share. However, with no user
education, imagine how simple a "virus" could be. And how devastating.
Let's glance by the fact that Windows has poisoned Linux users. Most
Windows users are used to clicking "ok" to everything that pops up. So,
when Linux asks them for a root password to install software, or perform
some other action, the default reaction will probably be to do it. After
all, if the OS wants it, it should be done. Let's not even think of
those Linux distros that totally disregard root and give the user root
privileges - the designers aimed to get rid of the security advantages
of a Unix-like OS, and did so perfectly.

Surely, Linux security will improve in ways that are easier for novices
to understand. File permissions should be checked by a scrpit, as well
as checksums, system logs, etc. and it can all be tied up in a simple
interface. But, let's think about this for a minute. Digg ran an article
at the end of last year claiming 8 Million Ubuntu users. Let's say that
only a million of them are complete novices. How many of them, do you
think, would think twice if they got an email or went to a web page
(that looked "official") that asked them to download and run a script in
order to update something. Or just a popular web site that asked them to
download some package or file and run it, in order to be able to view
some content? It's only one line in cron to start a DDoS attack. Maybe
two lines.

I'm all for Linux moving to the desktop. Paying more for an OS than you
paid for the computer is just insanity. Paying for any software when
there's a prefectly good free alternative isn't too smart. And, for the
majority of casual computer users, a Linux-based system would work
perfectly - not to mention the stability and lack of frustration from
BSODs, etc. But before this happens, there needs to be a community
effort to educate new users about security, about the differences
between Linux and Windows (or Mac), and about what is "bad" (malicious,
just out of place, etc.). Most of all, there needs to be a concerted
effort to develop all-in-one security tools that monitor logs,
filesystems, system files, installed packages, permissions, etc. and
present them in a simple, user-friendly manner (i.e. this is wrong, the
system thinks it should be this, click for more information or click to
fix it - and, of course, an easy way to rollback changes. ). Perhaps
most important for new users, and ease-of-use, is a way to track these
changes based on what package initiates them.

If you haven't tried Linux, give it a shot. It doesn't cost anything,
it's secure, stable, and fast, it runs on half the machine that Vista
needs, and best of all, it promotes Free Software ("open source") which,
after all, is in the interest of everyone who uses a computer.
[Ubuntu][] will even mail you a CD for free! If you're not ready to give
up Windows, download [OpenOffice][]. And, if you're already a Linux
guru, have a look at [OpenSolaris][] - if you're a developer or a
SysAdmin, you'll thank me for suggesting it (and Sun will mail you a
free CD or DVD, too!). They even have LiveCD Solaris
versions.<span style="display: block;" id="formatbar_Buttons"><span class="down" style="display: block;" id="formatbar_CreateLink" title="Link" onmouseover="ButtonHoverOn(this);" onmouseout="ButtonHoverOff(this);" onmouseup onmousedown="CheckFormatting(event);FormatbarButton('richeditorframe', this, 8);ButtonMouseDown(this);"></span></span>

  [RUSLUG]: http://ruslug.rutgers.edu
  [article]: http://blogs.zdnet.com/hardware/?p=926
  [denyhosts]: http://denyhosts.sourceforge.net/
  [Tripwire]: http://sourceforge.net/projects/tripwire/
  [Ubuntu]: http://www.ubuntu.com
  [OpenOffice]: http://www.openoffice.org
  [OpenSolaris]: http://www.opensolaris.org
