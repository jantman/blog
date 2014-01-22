Title: How To Wipe a Bunch of Machines Quickly
Date: 2009-02-03 15:51
Author: admin
Category: Tech HowTos
Tags: automation, cobbler, dban, pxe, retirement, security, wiping
Slug: how-to-wipe-a-bunch-of-machines-quickly

**Updated 2009-03-05, see bottom.**

At work the other week, we decommissioned 24 old desktops - Dell GX280's
that were used in the student labs as print release stations. They
didn't have anything sensitive on them, just Windows XP, but with
licensing and all we have to wipe Windows off of them before surplussing
them. Since there were 24 of them, it wasn't exactly going to be the
quickest task. Moreover, the GX280's we used don't have *any* removable
media drives.

A few people mentioned [Darik's Boot And Nuke][] (DBAN), which is a
bootable Linux distro (CD or floppy) aimed at wiping all of the fixed
disks attached to a machine. While they do offer an "Enterprise" version
that supports network booting (and logging wipe verifications to a
central machine), the pricing isn't exactly favorable for a small
project (or something that just needs Windows to go away, not a
DoD-grade 7-pass overwrite with random data). Between the lack of a CD
drive and the apparent need to select wiping options at boot, this
didn't seem to be the best method for me.

Luckily, with a little googling, I came by the [Cobbler][] project, a
ready-to-run install server aimed at automating network-based OS
installation. It turns out that Cobbler has a wiki article on [system
retirement][] that deals with using Cobbler to automate a network boot
of DBAN. Cobbler takes control of DHCP and TFTP, boots the machine(s) to
a PXE boot menu, and allows selection of one of the cobbler "profiles".

The general procedure is something along these lines:

1.  Get the DBAN iso and grab the .ima image off of it. Loopback mount
    it.
2.  Copy the `initrd` and kernel into `/opt/cobbler/dban` as
    `initrd.img` and `vmlinuz`, respectively.
3.  Assuming you have cobblerd running (cobbler check), add a Distro for
    DBAN:
    `cobbler distro add --name=DBAN-1.0.7-i386 --kernel=/opt/cobbler/dban/vmlinuz --initrd=/opt/cobbler/dban/initrd.img --kopts="root=/dev/ram0 init=/rc nuke=dwipe floppy=0,16,cmos"`
4.  Add a Profile for it:
    `cobbler profile add --name=DBAN-1.0.7-i386 --distro=DBAN-1.0.7-i386`
5.  `cobbler sync`

Assuming all went well, when we PXE boot a machine on the same LAN as
the Cobbler system, we'll get DHCP and a PXE boot menu which will list
`DBAN-1.0.7.i386` as one of the options. On some of the GX280's that I
did, I had to go into the BIOS and enable PXE boot (or select PXE from
the BIOS boot menu). Now, when DBAN boots, we'll get the standard dmesg
output and then a selection screen allowing us to pick a wipe type (I
used the single pass all zeros for just getting rid of the old OS) and
select which disks to wipe. If you use the default wipe, just press
"space" to select all disks and then "F10" to begin the wipe.

This process allowed me to wipe 7 machines at once (8 port KVM, 1 port
for the server). With a better KVM or (even better yet) a totally
automatic system as described below, it would essentially be limited to
whatever the server and network hardware will handle.

To add a little more automation, we can run
`cobbler system add --name=default --profile=DBAN-1.0.7-i386` which adds
a default profile to Cobbler, saying that any machines with MACs not
specifically assigned to a profile should boot the DBAN profile, and
bypassing the PXE boot menu.

**WARNING:** what follows will setup Cobbler and DBAN to automatically
wipe all PXE-booting devices without ANY human intervention. Use at your
own risk and, for God's sake, don't plug your server into a production
network (I recommend this only in a lab environment with a dedicated
switch, all machines in one physical area, and no possibility of getting
on the same 'net as production machines).

It's theoretically possible to totally automate this setup. According to
the DBAN docs, it will also accept kernel options (kopts) that effect
how dnuke works - specifically, `--autonuke` to tell it to wipe without
human intervention and a method option such as `--method=zero` to select
the wipe method. This means that if we PXE boot with kernel options set
to `nuke="dwipe --autonuke --method=zero"` we should go straight to the
dwipe utility (the heart of DBAN) and automatically wipe all disks by
writing zeros once - without operator intervention. Unfortunately,
there's a [bug][] in the current (1.4.0) Cobbler which prevents
quote-encapsulated strings in kopts, meaning that we can't set one
kernel option to a string with whitespace as needed here. If this bug is
fixed, it should allow this process to work without any operator
intervention, assuming the clients will PXE boot.

**Updated 2009-03-05** I haven't tested it yet, but apparently the
Cobbler bug preventing complex kernel options has [been fixed][]. The
fix should be included in the 1.4.3 release and is currently in the
development tree.

  [Darik's Boot And Nuke]: http://www.dban.org/
  [Cobbler]: https://fedorahosted.org/cobbler/
  [system retirement]: https://fedorahosted.org/cobbler/wiki/SystemRetirement
  [bug]: https://fedorahosted.org/cobbler/ticket/148
  [been fixed]: https://fedorahosted.org/pipermail/cobbler/2009-February/002874.html
