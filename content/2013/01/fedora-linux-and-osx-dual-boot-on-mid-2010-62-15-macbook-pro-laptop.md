Title: Fedora Linux and OSX Dual Boot on Mid-2010 (6,2) 15" MacBook Pro Laptop
Date: 2013-01-21 12:13
Author: admin
Category: Tech HowTos
Tags: bootloader, efi, fedora, gpt, grub, installation, laptop, mac, macbook, os x
Slug: fedora-linux-and-osx-dual-boot-on-mid-2010-62-15-macbook-pro-laptop

As part of the transition from a contractor to a full-time employee of
[Cox Media Group Digital & Strategy](http://www.cmgdigital.com) (check
out our [github](https://github.com/cmgdigital)), I've been issued a
[Mid-2010 (6,2)](http://support.apple.com/kb/SP582) 15" [MacBook
Pro](http://en.wikipedia.org/wiki/Macbook_pro#Technical_specifications_2)
laptop, to replace my current [Early-2008
(3,1)](http://support.apple.com/kb/SP11) MacPro desktop. The desktop is
currently running [Fedora](http://fedoraproject.org/) 17, dual-boot with
with Mac OS X (left in place for firmware updates and emergencies) using
the [rEFInd boot manager](http://www.rodsbooks.com/refind/index.html) to
choose between the two OSes. It took me two days to get this working
right on my desktop, but it had been my plan to duplicate this setup on
my laptop. I found a lot of conflicting information online, but I
decided to give it a try.

Well, I have Fedora 18 and OS X 10.8 dual-booting on the laptop, but not
as planned. After a day and a half of research, troubleshooting and
re-installs, here's what I found to actually work, in the hope that
nobody else will go through the ordeal I went through. Following that
are some notes about the new Fedora 18 installer (Anaconda 18),
especially important for anyone who's used Linux for a while. To those
who are new to Linux, don't be dissuaded by the above. Most of the
frustration I experienced is because I've been using Linux for a
relatively long time (about 10 years), had my own ideas about exactly
how I wanted things setup (which are decidedly *not* supported by
Fedora), and had some assumptions about the installation process based
on earlier versions.

**How to get it working:**

Forget about rEFInd. This had been the original advice from [Matthew
Garrett](http://mjg59.dreamwidth.org/),
[@mjg59](https://twitter.com/mjg59), kernel coder, contributor to the
Anaconda project, and all-around authority on booting Linux on EFI/UEFI
hardware. My advice, and the method that worked for me:

1.  Shrink your Mac partitions and leave as much free space as you want
    for Fedora. using the Disk Utility tool in OS X (I also created an
    8GB VFAT partition that both OSes can read/write to).
2.  [Download Fedora 18](http://fedoraproject.org/en/get-fedora) 64-bit
    DVD image, I chose the KDE version. Verify the sha256 sum if you
    want (they don't have a readily visible link to the checksum file.
    Copy the download link, paste it into your address bar and remove
    the filename. You should get a directory index that includes a
    `-CHECKSUM` file.
3.  Per the Installation Guide's [Making Fedora USB Media
    page](http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/Making_USB_Media-UNIX_Linux.html),
    use `liveusb-creator` to setup the installation image on the USB
    flash drive (I needed to start it with the `--reset-mbr` option).
    You can also use other tools (dd if you're not on a Fedora-based
    distro), or a DVD, but this is the method I chose.
4.  Due to a [bug in
    liveusb-creator](https://fedorahosted.org/liveusb-creator/ticket/810),
    you may need to manually edit `/EFI/boot/grub.cfg` on the created
    USB stick if grub gives you a file not found error. If that happens,
    please see my bug report above for the action to take (in short, you
    need to mount the USB stick, `chmod u+w /EFI/boot/grub.cfg` then
    edit that file and replace every occurrence of "isolinux" with
    "syslinux" and every occurrence of
    "root=live:LABEL=Fedora-18-x86\_64-Live-KDE.iso" with
    "root=live:LABEL=LIVE").
5.  Boot the USB drive (use the alt key when you turn on the laptop to
    select the USB drive) and just install Fedora normally, letting it
    do its thing. Select a boot disk and let it put GRUB2 on the EFI
    partition.

When you boot, it will boot to GRUB. There will be some options for Mac
OS there, but they don't work (more on that below). If you want to boot
Mac, hold down the alt/option key when you power on the laptop, which
will bring you to the boot disk selector and you can pick the Mac disk.
I know it's not pretty or ideal, but it's the best option right now.

**Making it Better:**

GRUB2 tries to automatically detect other OSes and configure them in the
boot loader (this is done through `/etc/grub.d/30_os-prober`, commonly
just referred to as `os-prober`). It tries to boot Mac directly through
the xnu\_kernel64 module, which not only isn't installed on the boot
partition by default, but just doesn't work with at least Mountain Lion
(10.8). So getting GRUB to boot Mac means either having the bugs in the
xnu module fixed, or figuring out how to setup a chainloader to boot
from GRUB to Mac. The latter is probably the method I'll investigate,
but for now, since I rarely use Mac, I'm happy having to use the alt key
at boot to get there. To remove the annoying, broken Mac OS options from
the grub screen, run the following commands as root (they assume you
have your EFI partition mounted at `/boot/efi` which I believe Fedora
should do by default:

~~~~{.bash}
cp /boot/efi/EFI/fedora/grub.cfg /boot/efi/EFI/fedora/grub.cfg.bak
echo 'GRUB_DISABLE_OS_PROBER="true"' >> /etc/default/grub
grub2-mkconfig > /boot/efi/EFI/fedora/grub.cfg
~~~~

**Thoughts on the Fedora 18 Anaconda Installer**

I found a couple of issues with the new Anaconda 18 installer that were
either unweildy or confusing for someone who's been installing Linux for
a long time. Overall, the new installer is very nice. It has a clean,
even elegant UI, a relatively nice flow from start to completion, and is
certainly beginner-friendly. It has fewer options than any Linux
installer I've ever used before - not even options for package
selection, firewall or SELinux configuration, etc. - but I guess this is
in line with the goal of making Fedora a desktop OS for the masses. I
would have appreciated an "advanced mode" installer that was more like
Fedora 17 (or even much older versions), but I guess I'm an edge case,
at least in the Fedora community. However, I did find two things
especially difficult, both related to the fact that my laptop has two
main drives (a 500GB hard drive and a 120GB SSD):

First, the installer prompted me to select a "boot disk". I guess I
should have read the installation guide, but I assumed that nomenclature
translated to either "which disk should the automatic partitiioning put
yout `/boot` partition on" or "which disk should I set the bootable flag
on in the partition table". In fact, it means "which disk should I put
GRUB on the EFI partition of". I installed, rebooted, and was shocked -
and somewhat distressed - to boot directly to GRUB2 instead of the
rEFInd installation I had setup. The installer didn't have any of the
previously-customary "warning: this will overwrite your MBR/EFI boot
partition" notices, so I felt safe letting it continue. It turned out
that this was the way I ended up going, and it also turns out that
there's a bug in Anaconda that makes it fail installation if you tell it
not to write a bootloader to disk (though it's patched by one line of
Python code). But I was deeply distressed that - contrary to the
experience of every, admittedly more complicated, Linux installer I'd
used before - the Fedora 18 installer overwrote my EFI bootloader
(analogous to overwriting the MBR on a BIOS boot machine) without ever
warning me or asking for a confirmation.

Secondly, the partitioning tool is clearly designed for only one
destination disk. The overview screen lists configured partitions by
label and mount point, but not by physical device, so figuring out which
partitions are on which physical disks takes a click on each and every
partition to view that information in the detail panel. When you create
a new partition, it's automatically put in a LVM volume group spanning
all disks. Changing the target of the automatically created volume group
requires a few clicks, as does changing the physical disks backing any
new volume groups. To assign a newly created partition to a specific
disk, you have to click on an unlabeled "tool" icon under the list of
partitions, far away from the information on the partition in question.
It's a nice interface for someone who clicks the "partition
automatically" button, or who just knows they want to add "an extra
partition", but for anyone who has a specific layout in mind (like
having `/`, `/boot` and `/var`, specifically sized, on the SSD and
`/home` on the rotating disk) it takes about 4-5 more clicks and dialogs
to add a partition than the last Fedora installer did. Mainly, it's
lacking any sort of Advanced Mode for partitioning that allows the user
to quickly and accurately layout a more complex partitioning scheme.

Below are some screenshots from the Fedora 17 and Fedora 18 Installation
Guides, which contrast both the overview of all partitions and the
individual partition settings:

Fedora 18 Overview, from [9.13. Creating a Custom Partition
Layout](http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/s1-diskpartitioning-x86.html):  
  

![image](http://www.dedoimedo.com/images/computers_years/2013_1/fedora-18-installer-configure-partitions.jpg)  
  
Fedora 17 Overview, from [9.14. Creating a Custom Layout or Modifying
the Default
Layout](http://docs.fedoraproject.org/en-US/Fedora/17/html/Installation_Guide/s1-diskpartitioning-x86.html):  
  

![image](http://docs.fedoraproject.org/en-US/Fedora/17/html/Installation_Guide/images/diskpartitioning/ddmain.png)  
  
Fedora 18 Partition Creation/Editing, from [9.13.3. Create LVM Logical
Volume](http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/Create_LVM-x86.html):  
  

![image](http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/images/diskpartitioning/lvm-pv.png)  
  
Fedora 17 Partition Creation/Editing, from [9.14.2. Adding
Partitions](http://docs.fedoraproject.org/en-US/Fedora/17/html/Installation_Guide/Adding_Partitions-x86.html):  
  

![image](http://docs.fedoraproject.org/en-US/Fedora/17/html/Installation_Guide/images/diskpartitioning/part-add.png)
