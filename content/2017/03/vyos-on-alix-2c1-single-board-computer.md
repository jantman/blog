Title: VyOS on Alix 2C1 Single Board Computer
Date: 2017-03-04 12:27
Author: Jason Antman
Category: Hardware
Tags: vyos,vyatta,alix,virtualbox,network,router,firewall,linux,sbc
Slug: vyos-on-alix-2c1-single-board-computer
Summary: How to install VyOS 1.1.7 on an Alix 2c1 or similar i386 single board computer

Back in 2011 I [wrote a post](/2011/09/vyatta-networkos-routerfirewall-on-alix-board-compact-flash/) on installing
the formerly open-source [Vyatta](https://wiki.vyos.net/wiki/Vyatta) router/firewall distribution on an Alix compact flash-based single board
computer. I'd been using it for many years, since Vyatta Community was a completely F/OSS project. I stopped updating regularly sometime around
when Vyatta (now Vyatta Core, differentiated from their paid offering) began widening the gap between its F/OSS Core and paid versions.
It got much worse when [Brocade acquired Vyatta](http://newsroom.brocade.com/press-releases/brocade-acquires-vyatta-a-pioneer-and-leader-in-s-nasdaq-brcd-0949599#.WLr6DkArJhE)
in 2012. Soon thereafter open source builds stopped, the forums were shut down, the source code was made much more difficult to find, and
eventually vyatta.org itself was shut down. I won't go into further detail as there's been a lot written about this debacle and forcible destruction of a community,
such as [Chris Wadge's post](http://dotbalm.org/brocade-missed-the-boat-with-vyatta/) and
[this one](https://libertysys.com.au/2013/08/the-tragedy-of-vyatta-cores-demise/), but I will say that the above made it increasingly difficult to plan
an upgrade of my home router.

On the positive side, however, the [VyOS](https://vyos.io/) F/OSS fork has emerged, and seems to have quite a vibrant community
at this point. A few weeks ago, I decided to finally take the time to upgrade to the latest VyOS 1.1.7 on my aged
[Alix 2c1](https://www.pcengines.ch/alix2c1.htm) single board router (purchased in 2008; 3 LAN, 433 MHz AMG Geode LX700, 128MB RAM).
VyOS is targeted at the cloud (virtualization) or "real" hardware, and doesn't seem to have anywhere near as many people
installing on dedicated SBCs as the former Vyatta community (probably because of the astonishing drop in the price of small, fanless
systems in recent years). I wasn't able to find much information about installing VyOS on such hardware, aside from
[a few](https://forum.vyos.net/showthread.php?tid=6045) [forum](https://forum.vyos.net/showthread.php?tid=26029)
[threads](https://forum.vyos.net/showthread.php?tid=26881) and a [post on Elder Guerra's blog](http://elderguerra.blogspot.com/2014/04/vyos-routerfirewall-on-alix-board.html)
that actually makes reference to and is based on my original post from 2011.

So, for anyone who's interested, here's how I got VyOS 1.1.7 installed on my Alix SBC:

## Prerequisites

* A Linux machine with VirtualBox. For posterity, I did this on a recently updated Arch Linux machine, using VirtualBox 5.1.12 from Arch's repos (running via DKMS and with the Oracle extensions installed).
* A Compact Flash card to perform the install on (I used [this](https://www.amazon.com/gp/product/B00PW1PH14/) Wintec "Industrial Grade" SLC NAND 4GB card from amazon).
* A reader/writer for the card (my previous one was throwing errors, so I got [this](https://www.amazon.com/gp/product/B0056TYRMW/) USB one from Amazon).
* Ensure your user can read and write the raw disk devices. On Linux, this means your user must be in the ``disk`` group. If it isn't, you'll need to log out and back in after making that change.
* Assuming you're installing onto a headless board like the Alix, you'll need a null modem cable to connect to the serial console port, and whatever you need (USB to serial adapter) to plug that in to your computer.
* A terminal emulator installed on your computer (I use [minicom](https://alioth.debian.org/projects/minicom)).

## Configuration Migration

I just wanted to upgrade from my existing VC 6.3 installation, and use a new CF card. If you are doing a fresh install
and do not need to migrate the configuration, you can skip this section.

To migrate the configuration, I first set up a VyOS 1.1.7 VirtualBox VM, using the [vagrant-vyos](https://github.com/higebu/vagrant-vyos)
plugin for [Vagrant](https://www.vagrantup.com/) and the author's [vyos Vagrant box](https://atlas.hashicorp.com/higebu/boxes/vyos). I setup
three network interfaces on the VM to match the three on my Alix board, and put the ``Vagrantfile`` in the same directory as my config
backups from the current router.

Once I had the VM up and running with SSH access, I ran ``load /vagrant/config.boot`` to load the configuration backup, and let the
config migration tool do its work. This took a few iterations of modifying the old (VC 6.3) config until I got something that would
load cleanly into VyOS 1.1.7; note that per the [Migrating from Vyatta](https://wiki.vyos.net/wiki/Migrating_from_Vyatta) documentation,
coming from VC 6.4 or earlier, there were some manual changes I had to make before the old configuration would load in VyOS.
Once that was done, I committed and saved the config, then rebooted the VM and confirmed that it
came up correctly configured. I run SSH on a non-default port, so before reloading the VM I needed to edit the ``Vagrantfile``
to add ``config.ssh.guest_port = SSH_PORT_NUMBER`` and ``config.vm.network "forwarded_port", guest: SSH_PORT_NUMBER, host: SSH_PORT_NUMBER, id: "ssh"``.

Once finished, I copied ``/config/config.boot`` from the VM to my host OS. I removed the MAC addresses for the interfaces
and the ``vagrant`` user, and then used that as the starting configuration for my new install on the Alix board.

## Installation

1. Put your new CF card in the USB adapter and plug it in. Watch ``dmesg`` to see what device name it's assigned. __In this example, we'll call it /dev/sdX. Make SURE you correct that path in the below instructions to be the correct one for your CF card.__
2. Create a raw VMDK so VirtualBox can use the raw disk: ``VBoxManage internalcommands createrawvmdk -filename /home/$USER/vyos_cf.vmdk -rawdisk /dev/sdX`` (note that the filename must be an absolute path).
3. Download the VyOS i586 ISO from [vyos.net](https://vyos.io/). Optionally verify the GPG signature.
4. Manually create a new VirtualBox VM.
   1. Select "Linux" and then "Other Linux (32-bit)" for the OS type.
   2. Select the appropriate amount of RAM for your board (older Alix are 128 MB or 256 MB).
   3. Select "Use an existing virtual hard disk file" and select the raw VMDK you created in Step 2. Uncheck "use host I/O cache".
   4. Create the VM.
5. Edit the VM settings to remove the floppy disk device, mount the ISO in the optical drive, disable audio, and disable all network adapters.
6. Boot the VM. Wait for the VyOS ISO to boot and log in using the information provided in the banner.
7. Run ``install image`` and answer yes to the prompt.
8. Select Auto partitioning and select the CF card (it should be ``sda``, the only option).
9. Fill the whole device with the root partition.
10. Use the default name for the image and copy ``/config/config.boot``.
11. Set a password for the vyos Administrator account.
12. Setup grub on the one disk (``sda``).
13. You should now be returned to the prompt.
14. ``reboot`` and shut down the VM once it gets back to the BIOS or bootloader; installation is complete.
15. Delete the VM (don't delete files) and then remove the raw VMDK you created in Step 2.
16. Mount the CF card partition on your host OS (it's an ext4 partition). For the purposes of this example, we'll assume we're mounting it at ``/mnt/tmp``: ``mount /dev/sdX1 /mnt/tmp``
17. cd to the root of the partition: ``cd /mnt/tmp``
18. Find and ``cd`` to the ``live-rw`` directory for your image; for VyOS 1.1.7 installed with the default image name of "1.1.7", this is ``boot/1.1.7/live-rw`` on the partition.
19. If you are migrating a configuration file (above section), copy your configuration file to ``opt/vyatta/etc/config/config.new`` and chmod it 0755.
20. Unmount the CF card and remove it from your system.
21. Find a DB9 null modem cable and a USB to serial adapter. Plug the cable into the Alix board's serial port, and into your adapter, and plug it into the system.
22. Fire up your favorite terminal emulator (I use minicom) and connect at 9600 8N1.
23. If you have the board running already (already being used for something), connect and make sure you get a prompt. It helps to know that the serial works.
24. If the board is running, power it down and unplug all connections before proceeding to the next step.
25. Open up the Alix enclosure, and swap in your new CF card.
26. Close the board, plug in serial and network cables.
27. Plug in the power cable, and watch your terminal emulator. If all went well, you'll get the board's BIOS and then the bootloader and kernel output. Eventually you should be dropped to a login prompt.
28. Log in as the vyos user.
29. ``configure`` to enter configuration mode. Then:
    * If you are migrating a configuration as discussed above, ``load /opt/vyatta/etc/config/config.new``. It will take a while to load. Make any necessary changes, then run ``commit``.
    * If you are starting from scratch, follow the [User Guide](https://wiki.vyos.net/wiki/User_Guide) to setup the system.
30. Once the commit is done (it will take a while), ``save``. The router should now be up and running with the desired configuration.
31. Reboot the router to ensure it comes up correctly.
32. Backup the running configuration somewhere safe.

If you're running the PC Engines Alix.2, update the serial settings on the board as described on [my blog](http://blog.jasonantman.com/2011/09/vyatta-networkos-routerfirewall-on-alix-board-compact-flash/) or [this post](http://elderguerra.blogspot.com/2014/04/vyos-routerfirewall-on-alix-board.html).

I hope this can be of use to others.
