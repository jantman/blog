Title: Getting oVirt up and running
Date: 2012-09-07 05:00
Author: admin
Category: Tech HowTos
Tags: fedora, kvm, ovirt, qemu, redhat, rhev, spice, virtualization
Slug: getting-ovirt-up-and-running

The bulk of this post was written way back in April 2012. If you're just
coming here, and looking to setup oVirt, you should probably [skip down
to the postscript][] for an update, and ignore most of the content here
(as it's applicable to an older oVirt version).

I recently started setting up [oVirt][], the community version of Red
Hat Enterprise Virtualization, at work for some testing (mainly a
"sandbox" VM environment, and because [Foreman][] [supports][] it). To
start with, I had two nodes, each with two dual-core Xeon processors
(VT-x capable) with 20GB RAM, one with 600GB internal storage and one
with 140GB internal. While oVirt's documentation isn't exactly
wonderful, I found a blgo post by Jason Brooks, [How to Get Up and
Running with oVirt][], which gives a great walkthrough of getting the
oVirt Engine setup on a machine, and also setting up that same machine
as a VM host. As oVirt is still fairly young, this is all done on
Fedora. I performed my installation via Cobbler, though I'm afraid to
admit it was an entirely manual, interactive install.

I did run into a few bumps during Jason's tutorial. In step 15, adding
the data NFS export as a Storage Domain, I was unable to add the NFS
export. I found the [Troubleshooting NFS Storage Issues page on the
oVirt wiki][], ensured that SELinux was disabled and that the export had
the correct permissions, confirmed that `/etc/nfsmount.conf` specified
`Nfsvers=3`, rebooted, and then ran the `nfs-check.py` script. At this
point, I was able to add the other storage domains in steps 15 and 16.

My second issue was that even on Fedora 16, I simply can't get the spice
client (through the `spice-xpi` browser plugin) to work. As far as I can
tell from the logs, it looks like `spicec` is being sent a value of
"None" for the secured port parameter, instead of the correct port
number. I assume this is a bug in oVirt, but I'll revisit this problem
when I have time. In the mean time, I changed my test VM to use VNC,
which is launched by installing the `ovirt-engine-cli` package (see
below) on your client computer, connecting to the oVirt API with
ovirt-shell:  

` ovirt-shell --connect --url=https://ovirt-engine.example.com:8443/api --user=admin@internal --password adminpassword`  
and then running `console vm_name`. This launches the `vncviewer`
binary, which is in the "tigervnc" package on Fedora.

**Installing ovirt-engine-cli**

To run `ovirt-shell` on your workstation (Fedora 16, of course...)
you'll need the ovirt-engine-cli and ovirt-engine-sdk packages. I
manually downloaded them from
[http://www.ovirt.org/releases/nightly/fedora/16/][], versions 2.1.3 and
1.6.2, respecitively. The SDK and CLI are python based, so there are a
few Python dependencies, all of which were automatically solved by yum.
I know there are SDK and CLI packages out there for other distros, but
haven't tried them yet.

**Installing Linux Guests**

Installing a CentOS 6.2 x86\_64 guest was relatively straightforward,
and my usual kickstart infrastructure worked fine. The only catch was
the VirtIO storage interface, which shows up as `/dev/vdx` instead of
`/dev/sdx`; I just added another kickstart metadata option in Cobbler
that allows me to use `sdx` by specifying "virtual=yes" (for our VMWare
hosts), or `vdx` by specifying "virtual=ovirt".

**Setting up Authentication**

As installed, oVirt only has one user, "admin@internal"; it requires an
external directory service for user authentication. Currently, it
supports IPA, Red Hat's Enterprise Identity Management tool (combines
RHEL, oVirt Directory Server, Kerberos and NTP; perhaps [FreeIPA][]
would work as well?) and Microsoft Active Directory. As much as I'd like
to give IPA or FreeIPA a try, my company already has an AD
infrastructure, so I opted to go that route. Documentation is given in
the [oVirt 3.0 Installation Guide][], starting on page 96.
Unfortunately, I was never about to get AD auth working correctly, so I
just worked with the one admin user.

**Adding a Node**

The biggest issue I had was adding the second node to oVirt. I attempted
to use the DVD Import feature of Cobbler on the [oVirt Node Image
ISO][], but that failed. I then found the image's
`LiveOS/livecd-iso-to-pxeboot` script and used that to make a kernerl
and initrd, and kernel parameters, for Cobbler. PXE works fine.

<a name="postscript"></a>**Postscript:** I ended up blowing away my
oVirt installation in favor of testing other things. At some point, the
engine install got corrupted in a way that I just couldn't fix; even
though I spent all day one Saturday working on it, it took more time
than I could allocate to a personal project. So this post is really
semi-complete at best. However, there is some good news. Jason Brooks'
original post, [How to Get Up and Running with oVirt][], was written for
oVirt 3.0, as was this post. Since then, there has been a new release,
[oVirt 3.1][], which apparently has a better UI and a better installer.
Jason Brooks has a new post, [Up and Running with oVirt, 3.1 Edition][],
which covers installation and configuration of both an all-in-one
machine and a separate node. If you're looking to try oVirt, I'd
recommend you give that a shot. Unfortunately (and strangely, given that
this is supposed to be the "upstream" of RedHat's proprietary RHEV) it's
still all based on Fedora.

  [skip down to the postscript]: #postscript
  [oVirt]: http://www.ovirt.org
  [Foreman]: http://theforeman.org/
  [supports]: http://blog.theforeman.org/2012/03/vnc-support-built-in-foreman.html
  [How to Get Up and Running with oVirt]: http://blog.jebpages.com/archives/how-to-get-up-and-running-with-ovirt/
  [Troubleshooting NFS Storage Issues page on the oVirt wiki]: http://www.ovirt.org/wiki/Troubleshooting_NFS_Storage_Issues
  [http://www.ovirt.org/releases/nightly/fedora/16/]: http://www.ovirt.org/releases/nightly/fedora/16/
  [FreeIPA]: http://freeipa.org
  [oVirt 3.0 Installation Guide]: http://www.ovirt.org/wiki/File:OVirt-3.0-Installation_Guide-en-US.pdf
  [oVirt Node Image ISO]: http://www.ovirt.org/get-ovirt/
  [oVirt 3.1]: http://wiki.ovirt.org/wiki/OVirt_3.1_release_notes
  [Up and Running with oVirt, 3.1 Edition]: http://blog.jebpages.com/archives/up-and-running-with-ovirt-3-1-edition/
