Title: Microsoft submits driver code for Linux kernel
Date: 2009-07-23 09:32
Author: admin
Category: Ideas and Rants
Tags: gpl, kernel, linux, microsoft
Slug: microsoft-submits-driver-code-for-linux-kernel

I read a very interesting [article on Linux-Mag.com][] today. The gist
of it is that Microsoft (as happily announced in a [press release][])
has submitted 20,000 lines of code for inclusion into the kernel.
Specifically, the code is comprised of a number of drivers that will
enable Linux to run better under Microsoft Hyper-V.

Yes, that's right, Microsoft released code under GPLv2 and is asking for
it to be put in Linux. They released it under the license that they call
"cancer". And the entire purpose is, essentially, saying "we want your
project to run well as a guest under our hypervisor.

The Linux Mag article did touch on some recent news, such as Microsoft's
[lawsuit against TomTom][] ([settled in late March][]) claiming that the
Linux kernel infringes their VFAT patents and the 2004 [EU antitrust
case (PDF)][].

A number of things are immediately apparent to me:

-   The only reason for this is so Linux will virtualize well under
    Windows/Hyper-V.
-   Microsoft doesn't seem to be making any similar effort to allow
    Windows to virtualize well under Xen (and it seems to me that many
    more people would want Windows on a reliable Linux host than the
    other way around).
-   Microsoft reached a settlement with TomTom, but never did anything
    to indemnify the Linux community at large.
-   This is **not** a Microsoft endorsement (or even recognition) of the
    GPL.
-   Microsoft [made threats][] about Linux violating "over 228" of its
    patents in 2007.

There's a [post][] on [Greg Kroah-Hartman's blog][] (he's the kernel
maintainer who will - or will not - eventually be in charge of the
inclusion of the code). It should be noted that **this all started** due
to a guy who I really admire, [Stephen Hemminger][], the principal
engineer at Vyatta (whose router product I absolutely love, and their
mock advertisements are just as wonderful). Steve has a [post on his
blog][] giving the background.

So what do *I* think should be done? Include the code. But first... (I
know Microsoft doing all of this at once would be a dream, but maybe one
or two of them would be nice)

1.  If they haven't already done so, Microsoft should publicly recognize
    the GPL and all of its terms as being a legally binding license.
2.  Prior to having any Microsoft code included in the Linux kernel,
    Microsoft publicly states that the Linux kernel, as of the time they
    submitted their code, does not infringe on any Microsoft
    intellectual property.
3.  It would be nice of Microsoft would agree to some level of
    cooperation with the Linux community.
4.  Microsoft pledges to allow, support, and actively develop for
    Windows as a guest under Xen and KVM.

  [article on Linux-Mag.com]: http://www.linux-mag.com/cache/7439/1.html
  [press release]: http://www.microsoft.com/presspass/features/2009/Jul09/07-20LinuxQA.mspx
  [lawsuit against TomTom]: http://www.linux-mag.com/id/7325
  [settled in late March]: http://arstechnica.com/microsoft/news/2009/03/microsoft-and-tomtom-settle-patent-dispute.ars
  [EU antitrust case (PDF)]: http://ec.europa.eu/comm/competition/antitrust/cases/decisions/37792/en.pdf
  [made threats]: http://www.linux-watch.com/news/NS6670466370.html
  [post]: http://www.kroah.com/log/linux/microsoft-linux-hyper-v-drivers.html
  [Greg Kroah-Hartman's blog]: http://www.kroah.com/log/
  [Stephen Hemminger]: http://linux-network-plumber.blogspot.com/
  [post on his blog]: http://linux-network-plumber.blogspot.com/2009/07/congratulations-microsoft.html
