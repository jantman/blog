Title: *nix
Date: 2007-09-28 13:22
Author: admin
Category: Miscellaneous
Tags: Digg, Eric S Raymond, linux, solaris, sun, Unix
Slug: nix

First off, my Sun blog should be coming sometime this weekend/early next
week. If I post anything interesting there, I'll be sure to cross-post
it.  
This morning at work, while reading [Digg][], I came by two interesting
links that got me thinking:  
[5 Reasons Your Parents Should Use Linux][] and [Ten Things Linux
Distros Get Right (That MS Doesn't)][].  
Now, I'll admit, my \*nix experience is pretty much limited to Linux.
I've used BSD a few times, but only as pre-built images for embedded
systems like my [Soekris][] boxen. I've used Solaris mainly just as a
user/web developer in SSH at work. And while I now have a work computer
running Solaris 10 and a SXDE image on my laptop, I'm still relatively
new - and, given that I'm now doing hardware support and wireless work,
I don't even know what I need another machine in the office for.  
That being said, the second link got me thinking. Specifically, about
something I read in [The Art of Unix Programming][] [Wikipedia] by Eric
S. Raymond (available online [here][]) with regards to interface design.
One quote that I was able to find in the online version, comes from
Chapter 11, under the subtitle "Tradeoffs between CLI and Visual
Interfaces",  
<span style="font-style: italic;">"Resistance to CLI interfaces tends to
decrease as users become more expert. In many problem domains, users
(especially
</span><span style="font-style: italic;" class="emphasis">*frequent*</span><span style="font-style: italic;">
users) reach a crossover point at which the concision and expressiveness
of CLI becomes more valuable than avoiding its mnemonic load. Thus, for
example, computing novices prefer the ease of GUI desktops, but
experienced users often gradually discover that they prefer typing
commands to a shell."  
<span style="font-style: italic;"></span></span>There is another similar
quote in the book, mentioning how resistance to the CLI drops as
<span style="font-style: italic;">typing speed</span> increases.  
Unfortunately, in some areas I'm still bound to Windows. Though my only
personal use for it is to control an ancient Umax Mirage IIse SCSI
scanner (with only Windows and Mac drivers), I ultimately need to touch
it now and then - whether on my mother's box (she claims she has to have
Windows and MS Office because "that's what businesses use") or as admin
of the four boxes at the [Ambulance Corps][] where I volunteer.  
However, whenever I am (unfortunately) pushed into the task of working
on a Windows box, I always feel something lacking. To be blunt, I don't
see how experienced users can deal with it. And this isn't just an issue
of multiple desktops, or reliability (I expect my desktop to have months
of uptime, and my servers to have years). This isn't just pro-Linux,
it's anti-Windows. Linux is great. Solaris seems wonderful, and I can't
want to move my servers over. And, believe it or not, due to playing
around with the Solaris Management Console, for the first time in 5
years, I plan on running X on my servers.  
What this is, is a talk about total workflow. Years ago, I reached the
point where I am more comfortable at the command line, or in an
Ncurses-style GUI, than in X.  
I an attribute this to two factors - verbosity and speed. The CLI is as
verbose as anything can get. I remember setting a static IP on a Windows
box. I had to navigate the Start menu, open up the control panel, the
network thingy, click on the network card, and work through a series of
dialogs. In Linux, I clicked on the terminal icon, typed "sudo ifconfig
eth0 up 192.168.0.211" and then a password. Done. Likewise, refreshing a
DHCP lease on Windows requires a whole bunch of "repair connection"
nonsense, whereas in Linux all it requires is "dhclient eth0". The
bottom line I know what I'm doing. Windows should have an option to let
me quickly do it.  
Speed is a related issue. Click, click-click, drag, click, click....
what about just typing? Even for people who aren't CLI-friendly, there's
Ncurses. YaST2, the SuSE/openSuSE administration tool, has both GUI and
Ncurses interfaces. I always use the Ncurses interface. Why? Because
I've been using it for years. I know that if I want to add a user
through YaST, I hit the down arrow 7 times, tab once, down 5, enter. Tab
once more to bring up the add user dialog. I can do this in well under a
second. What's the bottom line? Well, first of all, my hands are already
on the keyboard. That's where they like to stay. That's where they're
comfortable. My fingers need to move a \*lot\* less to navigate with the
arrow keys, tab, and enter than they do to use a mouse. If you know what
you're doing, if you already know what you're looking for, then a mouse
is slower than the speed of thought (or reaction).  
So where's the Windows bashing? Simple. How do people at Microsoft deal
with this? How does the guy who \*wrote\* that network settings dialog
deal with navigating the GUI every time, even though he already knows
exactly what he wants to do - and probably the system calls to do it?  
The bottom line is that every time I sit down at a Windows machine, I
wonder how the most popular OS is one that doesn't give any thought to
advanced users. I know that I can type faster than I can move a mouse,
why don't you let me use that? More importantly, why didn't Microsoft
ever think that people would use computers on a network? When I
installed Solaris, I wanted to edit a config file. I hadn't customized
\*anything\* yet, hadn't installed any other software, nothing. Yet, I
was able to open up a terminal and grab my .emacs file from my laptop in
one line (scp).  
To be totally honest, the question running through my mind is something
like "everything is so much quicker on Linux. How do experts deal with
Windows?"<span style="font-style: italic;"><span style="font-style: italic;"></span>  
</span>

  [Digg]: http://digg.com
  [5 Reasons Your Parents Should Use Linux]: http://www.foogazi.com/2007/09/27/5-reasons-your-parents-should-use-linux/
  [Ten Things Linux Distros Get Right (That MS Doesn't)]: http://warpedvisions.org/2006/12/30/ten-things-linux-distros-get-right-that-ms-doesnt/
  [Soekris]: http://www.soekris.com
  [The Art of Unix Programming]: http://www.catb.org/~esr/writings/taoup/
  [here]: http://www.catb.org/~esr/writings/taoup/html/
  [Ambulance Corps]: http://www.midlandparkambulance.com
