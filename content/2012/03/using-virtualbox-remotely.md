Title: Using VirtualBox Remotely
Date: 2012-03-09 12:00
Author: admin
Category: Tech HowTos
Tags: rdp, virtualbox, virtualization, vm
Slug: using-virtualbox-remotely

At work, I have a pretty beefy workstation (a Dell OptiPlex 990 with a
3.4GHz Intel Core i7-2600 and 8GB RAM running Fedora 16) that I usually
run a few VMs on as my test/development environment. I usually reboot my
machine every other week or so, and start VirtualBox and my VMs once the
system boots. All of the VMs are Linux boxes, running test-only, so I
never really cared about RDP or anything like that. Today I'm working
from home and need to setup a new development environment, so here's how
to get VirtualBox working nicely assuming you've never set it up for
VRDP (its Virtual Remote Desktop Protocol) before, and have a network
connection (LAN or VPN or something) to the machine running VirtualBox.
I currently have VirtualBox OSE 4.1.8 installed from [rpmfusion][] RPM.
Most of this can be found in [Chapter 7 of the VirtualBox manual][], but
here's a step-by-step method.

<ol>
<li>
First, download the Oracle (non-free) Oracle VirtualBox VM Extension
Pack tarball from the [VirtualBox Downloads Page][], which provides VRDP
support (as well as support for the virtual USB 2.0 device, Intel PXE
Boot ROM support for the E1000 NIC driver, and experimental Linux host
PCI passthrough suport). Then install it using:

~~~~{.text}
sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-4.1.8-75467.vbox-extpack
~~~~

</li>
<li>
Assuming you have an existing VM (you can list them using
`VBoxManage list vms`), enable VRDP support on it:

~~~~{.text}
VBoxManage modifyvm "VM name" --vrde on
~~~~

</li>
<li>
I like to assign specific ports to VRDP on each VM so I can "bookmark"
them in my [KRDC][] client by VM name. I generally start with 10011, as
the 10011-10049 range is both unassigned and doesn't appear in my
`/etc/services`:

~~~~{.text}
VBoxManage modifyvm "VM name" --vrdeport 10011
~~~~

</li>
<li>
Start the VM, using VBoxHeadless (shows more debugging/errors, but also
stays in the foreground, so you'll want to use [screen][] or something
like it):

~~~~{.text}
VBoxHeadless --startvm "VM name"
~~~~

If all went well, it should show some output including a confirmation
that the VRDE server is running on the correct port:

~~~~{.text}
Oracle VM VirtualBox Headless Interface 4.1.8_OSE
(C) 2008-2012 Oracle Corporation
All rights reserved.

VRDE server is listening on port 3389.
~~~~

</li>
</ul>
That's it. Assuming you're using something like [screen][], you can
start a whole bunch of new VMs, and still keep the VBoxHeadless output
in case of an error.

  [rpmfusion]: http://nonfree.rpmfusion.org/
  [Chapter 7 of the VirtualBox manual]: http://www.virtualbox.org/manual/ch07.html
  [VirtualBox Downloads Page]: https://www.virtualbox.org/wiki/Downloads
  [KRDC]: http://kde.org/applications/internet/krdc/
  [screen]: http://www.gnu.org/software/screen/
