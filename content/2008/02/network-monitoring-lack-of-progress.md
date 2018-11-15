Title: Network Monitoring (lack of) Progress
Date: 2008-02-06 00:07
Author: admin
Category: Software
Slug: network-monitoring-lack-of-progress

So, I've been plodding along after troubleshooting some VPN issues with
my Solaris workstation that I use for Sun work. After that, I started
work on the Xen box. Big surprise - none of the PS/2 inputs are working.
I knew that the PS/2 riser card was loose, but now I can't get any
input. I gave a USB mouse and keyboard a shot, but it's flat-out
impossible to use them with a 1U slide-out KVM console. So, back to my
room and VNC.

Now, problem 2. I'm trying to use the SuSE/YaST builtin VM manager.
Unfortunately, it can't read half of my known-good SuSE CDs, and for
some reason the other half come up with a mysterious error that it can't
find /tmp/{random string}/suse/i586/install-initrd-1.0-72.i586.rpm. This
is most troubling because I have 2 VMs setup on the machine, and
installed them both without a problem.

By now a new OpenSuSE 10.3-KDE .iso should be done downloading (thank
God for a 1.5Mbps download rate at home), so I'll keep hacking away at
it...
