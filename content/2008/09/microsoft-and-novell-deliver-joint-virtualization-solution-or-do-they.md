Title: Microsoft and Novell Deliver Joint Virtualization Solution - or do they?
Date: 2008-09-11 11:40
Author: admin
Category: Miscellaneous
Tags: microsoft, novell, suse, virtualization
Slug: microsoft-and-novell-deliver-joint-virtualization-solution-or-do-they

From PRNewsWire: [Microsoft and Novell Deliver Joint Virtualization
Solution Through
Partners](http://www.prnewswire.com/cgi-bin/stories.pl?ACCT=104&STORY=/www/story/09-11-2008/0004883058&EDATE=).
The headline of the press release: "Supported by Dell and other channel
partners, solution includes SUSE Linux Enterprise Server running as
optimized guest on Windows Server 2008 Hyper-V."

Now, maybe I'm not up on the news regarding my favorite distribution,
but it seems to me that a deal allowing SuSE to be virtualized as a
**guest** under Windows is not only "joint", but plain moronic. Despite
the marketing efforts of Microsoft, Unix-based systems (including Linux)
have always had the upper hand in availability, reliability, and
performance.

I must say, from what I've heard, Windows Server is getting \*much\*
better in these areas - and I've even heard that the latest version
includes an option to install without a graphical environment, and even
includes a command-line that's useful. It's about time.

However, it seems to me, that any virtualization deal between Microsoft
and a Linux distributor can provide only one logical solution: Windows
Server virtualized as a guest in a high-availability Linux host. More
importantly, without the insane per-processor licensing - a per-VM
instance license that's hardware-agnostic and allows VMs to be migrated
across hardware as the admin sees fit.

Oh, and one more insight. If Microsoft wants to be a serious player in
the virtualization arena, here's a few "simple" steps:

1.  Get Windows Server to work correctly under Xen, VirtualBox, etc.
    Certify it. Provide the correct guest OS tool packages
2.  Provide simple management of Windows in a virtualized environment -
    minimally, a standard SSH server that's compatible with OpenSSH, a
    GUI-less environment, and a serial console.
3.  Get rid of per-processor licenses. Provide a basic license that
    allows for, say, 10 VMs to be running at once, and allows as many
    installs as needed - the only licensing is based on the amount of
    VMs actually running. i.e., if you have 10 VMs and one gets
    corrupted, you can bring that one down and online a back-up image,
    without violating the license.
4.  Make licensing processor-agnostic. Want to migrate a Xen VM (Windows
    guest) from a dual-core Pentium to an 8-core Xeon, or even a 16
    processor SPARC? Sure, no problem.


