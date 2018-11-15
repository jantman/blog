Title: Getting SunSPOTs working under OpenSuSE 10.1
Date: 2008-05-13 13:09
Author: admin
Category: Software
Tags: java, linux, netbeans, sun, sunspot
Slug: getting-sunspots-working-under-opensuse-101

So I've been playing around with[SunSPOT](http://www.sunspotworld.com)s
lately. Or trying to. My only x86 (32-bit) machines are an old desktop
running OpenSuSE 10.1 and my eeePC. It looks like I just killed my new
install on the 8GB SDHC card, so I gave the desktop a try. I'd already
tried once with the install of Orange from the CD that came with them,
and had NetBeans 6 installed, so I had to do some recovery. The
procedure was as follows:

1.  Install all of the Java6 java-sun packages (specifically the base as
    devel).
2.  Download the Java 6 JDK from Sun, and install all of the RPMs.
3.  Screw with /usr/lib/jvm and get it sane - specifically, replace all
    of the symlinks that point to /etc/alternatives with new ones
    pointing to the Java6 install in /usr/lib/jvm/java-1.6.0-sun-1.6.0
4.  Delete your entire .netbeans directory (I was having serious issues
    with NetBeans).
5.  Start NetBeans from the command line with an explicitly set jdkhome:
    "netbeans --jdkhome /usr/lib/jvm/java-1.6.0-sun-1.6.0
6.  Download the SPOT plugin for NetBeans, following the instructions on
    [Bruno Ghisi's
    blog](http://weblogs.java.net/blog/brunogh/archive/2008/04/starting_with_s.html).
7.  Once installed, you should have a little SPOT-looking icon on the
    toolbar below "Navigate". Click on it, and launch SPOTManager from
    the link in the right panel ("Sun SPOTs Info", the link is an icon
    not text). Go through whatever configuration is needed.
8.  Upgrade local SDK to Purple (Click the SDK tab, select "v3.0 Purple"
    from the right panel, click the Upgrade button near the bottom).
9.  Upgrade your demos following davidgs's [blog
    posting](http://blogs.sun.com/davidgs/entry/beta_follow_up).
10. Upgrade all of the SPOTs to Purple (plug them in one at a time, on
    the SPOTManager SunSPOTs tab, click "Upgrade").
11. I'm still having some minor issues here. I'll update when I have
    everything figured out...

