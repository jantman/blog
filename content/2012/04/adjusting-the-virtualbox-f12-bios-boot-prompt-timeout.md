Title: Adjusting the VirtualBox F12 BIOS Boot Prompt Timeout
Date: 2012-04-09 13:52
Author: admin
Category: Software
Tags: provisioning, pxe, rdp, sysadmin, vbox, virtualbox, virtualization, vm
Slug: adjusting-the-virtualbox-f12-bios-boot-prompt-timeout

I'm working from home today, connected by VPN. I'm in the process of
testing a bunch of Puppet stuff, and needed to re-image a bunch of
[VirtualBox](https://www.virtualbox.org/) VMs on my desktop at work,
using PXE boot to [Cobbler](https://fedorahosted.org/cobbler/). I'm only
connected to the desktop by SSH, and running the VMs with `VBoxHeadless`
and connecting to them via RDP (well, VRDP). The problem with this is
that if I start a VM on my console window, then switch to my RDP client
and connect, by the time the VM gets keyboard focus, it's already past
the VBox "Press F12 to select boot device" prompt and booting from disk.
I could modify the boot order on the VM, but then that becomes a pain
when it reboots after the install.

Thanks to some of the guys on the [VirtualBox IRC
channel](https://www.virtualbox.org/wiki/IRC), I found out about the
`--bioslogodisplaytime` option for VMs, which controls the length of
time (in milliseconds) that the boot splash screen is shown (the default
value seems to be 0). It's included in the [reference guide to
VBoxManage](http://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvm)
in the modifyvm section. Setting this to a value of 10 seconds or so, as
shown below, is more than enough for me to start the VM, Alt-Tab to my
RDP client, connect to the VM, and hit 'F12' to select a one-time
network boot:

~~~~{.text}
VBoxManage modifyvm VMNAME --bioslogodisplaytime 10000
~~~~
