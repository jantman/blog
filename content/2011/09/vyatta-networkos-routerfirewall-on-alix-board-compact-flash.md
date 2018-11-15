Title: Vyatta NetworkOS router/firewall on Alix board / Compact Flash
Date: 2011-09-30 14:16
Author: admin
Category: Hardware
Tags: alix, embedded, network, pcengines, router, vyatta
Slug: vyatta-networkos-routerfirewall-on-alix-board-compact-flash

__Update March 2017__: I have an updated version of this procedure for VyOS,
the open source community fork of Vyatta, available in a new post:
[VyOS on Alix 2C1 Single Board Computer](/2017/03/vyos-on-alix-2c1-single-board-computer/).

With the impending move to an apartment in Georgia and the migration of
my rack full of servers to a hosting provider, there's no longer a need
for me to run my [Vyatta VC](http://www.vyatta.org/) router on a beefy
dual-CPU RAIDed [DL360
G3](http://h18000.www1.hp.com/products/quickspecs/11504_na/11504_na.HTML)
HP Proliant server chassis. I found an older PCEngines [Alix
2c1](http://pcengines.ch/alix2c1.htm) single board computer (433 MHz AMD
Geode LX700 , 128MB DDR DRAM, CompactFlash (CF) card socket, MiniPCI, 3x
10/100 ethernet) lying around, and decided to turn that into the new
router. But I've been so spoiled by Vyatta's good performance (well, at
least on an x86 server) and the *real* CLI, so I don't think I can go
back to something like [m0n0wall](http://m0n0.ch/wall/) or
[pfSense](http://www.pfsense.org/), and since it's going to be my only
network services box (also doing DNS, DHCP, firewalling, NAT, and maybe
IPsec VPN) it's not viable to use the type of older Cisco or Juniper
hardware that I can afford.

The down side is that Vyatta isn't really designed or tuned for small
systems, let alone CF media that doesn't take too well to lots of
writes. So, I'm going to begin experimentation with doing a CF install
of the current Vyatta Core 6.3, and we'll see how it goes and what
tuning I do over time.

I found two relatively good references; a [post on the vyatta.org
forum](http://www.vyatta.org/forum/viewtopic.php?t=502) from 2008,
relating to Vyatta version 4 (also on the author's
[blog](http://dataflip.blogspot.com/2008/06/optimizing-vyatta-for-compact-flash.html)),
and a [blog
post](http://peytongroup.wordpress.com/2010/02/16/vyatta-community-on-a-compact-flash/)
detailing a more complex
[SquashFS](http://squashfs.sourceforge.net/)/[tmpfs](http://en.wikipedia.org/wiki/Tmpfs)/[UnionFS](http://unionfs.filesystems.org/)
read-only Vyatta install. Given my relatively short timeframe and little
free time, I decided to try the former approach for now, and plan to
make a more customized and tuned CF version of Vyatta in the future.

**Creating the actual disk image:**

My development platform at the moment is an intel-based MacBook Pro,
running MacOS X 10.6.4 and VirtualBox 4.0.12. As much of a Linux fan as
I am, my work laptop runs Mac (like everyone else in the office) and
lately I can't guarantee that I'll be at my desktop long enough to
finish anything. The target is an Alix2c1 with a 2GB SanDisk Ultra CF
card (yes, I know an industrial card would be better, but I couldn't get
my hands on one). For starters, I created a new VirtualBox VM with the
following settings:

-   OS Type: Linux 2.6
-   Base Memory: 128MB
-   Boot Order: Floppy, CD-ROM, Hard Disk
-   IDE Controller Primary: mounted vyatta-livecd\_VC6.3 ISO image
-   IDE Controller Secondary: RAW VMDK image (created below)
-   Audio: None
-   Network: Disabled *(this is important, as Vyatta saves the
    interfaces by hardware address, and it would require some config
    editing and reboots to change them)*
-   Serial Port: disconnected (but present)

One difficulty I ran into on Mac is mounting the raw CF card in the
VirtualBox guest. I plugged it in via a USB reader, and of course it
automatically mounted in MacOS. I ejected it and the `/dev/disk1` device
disappeared. It turns out that the full procedure (as far as I could
tell) for Mac is:

-   Plug in the CF card and reader.
-   It should automount. Run `mount` to see what the actual device is -
    in my case, the `/dev/disk1s1` partition was mounted, so the disk is
    `/dev/disk1`.
-   Run `sudo umount -f /dev/disk1`. It seems that the MacOS automounter
    has a god complex, so you may need to re-run this command quite a
    few times throughout the process if you get device or resource busy
    errors.
-   In an appropriate directory, create the raw VMDK image with:
    `VBoxManage internalcommands createrawvmdk -filename rawdisk.vmdk -rawdisk /dev/disk1`.
-   When creating your VM, you'll have an option to select Use an
    Existing Virtual Disk. Use that option, and select the file created
    in the last step.

Once that's done, and you've setup the VM with the raw disk, boot the VM
(should boot to the Vyatta LiveCD), login as usual for an install
(vyatta:vyatta), and the the fun begins:

1.  At the prompt after logging in, `sudo su -`
2.  Edit `/opt/vyatta/sbin/install-system` (hint: Vyatta has nano and vi
    installed. `nano -c filename` shows line numbers) and change the
    `ROOT_FSTYPE` variable (line 78 in VC6.3) from "ext4" to "ext2".
3.  Run `install-system`. I used all default options (including one
    partition) and it seemed to work fine. It took a minute or two to
    create the ext2 filesystem on my 2GB CF card.
4.  The file copy took even longer... so be patient, or have a book
    handy.
5.  When system-install finishes and you get the root prompt back,
    before rebooting, continue with some minor tweaks:
6.  `mkdir /mnt/temp`
7.  `mount /dev/sda1 /mnt/temp`
8.  `cd /mnt/temp`
9.  Edit `boot/grub/grub.cfg` and change all occurrences of
    "root=UUID=..." entries for the "linux" lines (lines 13, 18, 23, 28
    in my grub.cfg) to "root=/dev/sda1". My only real reason for this
    change is so that I can move my altered config files (config.boot,
    fstab and grub.cfg) with minimal changes when I upgrade or make a
    different vyatta CF card, without having to update the UUID for the
    new partition.
10. Edit `etc/fstab` and change the "UUID=..." device to "/dev/sda1".
11. `shutdown`. Once the VM is stopped, you can remove the CF card.
12. The PCEngines Alix.2 boards use a default serial console speed of
    38400 baud. Pretty much every network device, plus Linux and Vyatta,
    use a default speed of 9600 baud. Once I got the CF card installed
    in the Alix board and hooked it up to my laptop (null modem cable to
    a PL-2303 based USB to serial adapter, minicom for terminal
    emulation), I set my terminal emulator to 38400 8N1, powered the
    board, and then pressed 's' during POST to get into BIOS settings.
    Option '9' sets the Alix to 9600 baud, 'Q' to quit, and 'Y' to save
    changes permanently. The board will reboot, and once the terminal
    emulator is set back to 9600 baud, serial console should work fine
    both in BIOS and in the OS.

If all worked well, you should be able to boot into Vyatta and login as
the default "vyatta" user (which you set a password for during the
install). Assuming you know your way around Vyatta, it's pretty standard
from here, though there are a few things you may want to check or
configure right away:

1.  In configuration mode (`configure`) run `show interfaces`. All of
    your physical ethernet interfaces should appear, along with their
    MAC addresses.
2.  Some changes to reduce the number of log writes to the CF card:
    `set system syslog console facility all level notice` and
    `set system syslog global facility protocols level notice`.
3.  Configure interfaces. with firewalls, IP addresses or DHCP, etc.
4.  Do whatever other configuration you need for a minimal system -
    dhcp, dns, nat, etc.

And that's it - this should give you a working Vyatta system on CF on an
Alix board. Stay tuned, hopefully in a month or so I'll get around to
customizing it a bit more, based on the second blog entry linked above.
