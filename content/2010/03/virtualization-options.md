Title: Virtualization Options
Date: 2010-03-19 20:55
Author: admin
Category: Projects
Tags: OpenVZ, virtualization, xen
Slug: virtualization-options

As I mentioned in [Downtime past few days, coping with storms][], as a
result of some things I noticed with a recent power outage, I've decided
to take the leap to virtualization. Given the cost of current hardware
that supports HVM (Intel VT-x or AMD-V ), I immediately decided that I
might as well give up on any thoughts of doing full virtualization or
getting new-ish hardware. So I settled on the next step up from what
have now - a set of [HP Proliant DL360 G3][] servers. I got them with a
90 day warranty from a reputable dealer, dual 2.8GHz Xeon (512K cache),
2Gb RAM, dual 36.4Gb U320 15k RPM SCSI disks and dual power supplies for
$99 each. My next step is to decide what virtualization software to use.

My main goals for the project are:

-   Lower power consumption through consolidation of servers.
-   Possibility to add capacity or resources by remotely powering up an
    idle server and migrating VMs to it.
-   Limited fault tolerance - ability to manually restore a VM that was
    running on failed hardware, onto an idle server.

I originally thought Xen, just out of reflex. However, given that all of
my servers have the same base - the same distribution and, ideally, the
same kernel and patch level - it seemed like a lot of overhead to
duplicate that for multiple VMs. So I started looking into [OS-level
virtualization][]. There are relatively few options, and I'll admit that
aside from Solaris Containers (which I learned about while working at
Sun) I don't know much about it. But [OpenVZ][] seems to be the front
runner in that area. My initial impression was that it made a lot of
sense - keep one common kernel, but allow containers/virtual
environments (CTs/VEs) to have, essentially, their own userland.
Unfortunately, it doesn't seem to be as hyped as Xen, and I haven't
heard very much about it in the enterprise context. And it requires
running a kernel from the OpenVZ project, which means I can't just
script updates through yum as easily as normal.

On the up size, OpenVZ would allow me to eliminate the duplication of
the kernel, and seems to have much less overhead than Xen (and logically
so). On the down side, I lose the ability to virtualize other OSes,
kernel versions, or make pre-packaged VMs. I've decided that if I wanted
to do that, I could dedicate a single machine.

I've spent the last day or so doing a lot of research, and have come up
with the following questions and concerns about OpenVZ which I hope to
be able to answer (I'll post the answers in a follow-up).

-   How do I handle distribution and kernel upgrades? The logical
    solution would be to migrate the CT to another host while I upgrade
    CT0 (the hardware OS/host/dom0 in Xen speak). But if the guest and
    host kernels must match, how does this work?
-   Can I do package upgrades within the guest/CT easily? WIll this play
    well with Puppet?
-   How will I handle backups? Is it logical to run [bacula][] within
    each CT, or just on CT0? If just on CT0, how do I easily verify that
    a particular CT was backed up?
-   WIll everything play well with Puppet? (see below)
-   Am I willing to throw away my KickStart-based installs? And,
    similarly, am I willing to give up the possibility of migrating from
    a container to a Xen host or a physical host (easily)?
-   OpenVZ live migration relies on rsync. This means that there's a
    significant delay (compared to shared storage) and also that I can't
    migrate off of a host that's down. Is there a way around this?
-   Similarly, live migration requires root SSH key exchange
    (passwordless) between the hosts. This seems about equivalent to
    using `hosts.equiv`. Do I really want root on one box to mean root
    on another box (and all of the containers on that box)?
-   Can I still firewall CT0? How will this work?

It seems to me that OpenVZ may be significantly less enterprise-class
than Xen. Sure, this is just my home setup, but I hold it to the same
standards I use for my work systems. In fact, I usually test new
technologies at home before I suggest them at work. A lot of the writing
on the [OpenVZ wiki][] seems to be riddled with spelling errors. They
claim "zero downtime" live migration, but if they have to rsync 2Gb of
MySQL tables, that sounds like a lot more than "zero". And, most
shockingly, the [Hardware testing][] wiki page talks about making sure
your hosts aren't overclocked or undercooled, and running `cpuburn` to
test your system under high load. Sorry, but the engineers at HP, Sun,
IBM, etc. handle that for me and most people I know. So, I'm a bit
worried about the seriousness of the OpenVZ project.

Most worrisome is a post I found in the [OpenVZ forum][], ["Stopping
puppet on hn stops it in all VE"][]. It seems that, since CT0 is aware
of all of the guest container processes, they show up in ps lists. Most,
if not all RedHat init scripts use killproc to stop and restart
services. This means that a `service syslog stop` on the CT0 (host) will
stop **all** `syslog` processes, including all of them in the CTs. This
seems like a major issue. Sure, I could replace `killproc` on CT0 with a
script that parses the process list, isolates the PIDs for those running
on CT0, and kills them. But what else needs to be fixed? Nagios check
scripts would need to be adjusted. Is there anything else that would
come back and bite me?

The bottom line is that (I guess this is logical) it seems that
containers in OpenVZ will seem - and act - a lot less like a logical
host than they would under Xen.

  [Downtime past few days, coping with storms]: /2010/03/downtime-past-few-days-coping-with-storms/
  [HP Proliant DL360 G3]: http://h18000.www1.hp.com/products/quickspecs/11504_na/11504_na.HTML
  [OS-level virtualization]: http://en.wikipedia.org/wiki/Operating_system-level_virtualization
  [OpenVZ]: http://www.openvz.org/
  [bacula]: http://www.bacula.org
  [OpenVZ wiki]: http://wiki.openvz.org/
  [Hardware testing]: http://wiki.openvz.org/Hardware_testing
  [OpenVZ forum]: http://forum.openvz.org
  ["Stopping puppet on hn stops it in all VE"]: http://forum.openvz.org/index.php?t=msg&goto=14818&
