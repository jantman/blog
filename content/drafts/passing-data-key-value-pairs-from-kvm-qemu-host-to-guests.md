Title: Passing data / key value pairs from KVM qemu host to guests (CentOS Linux)
Date: 2013-08-30 18:51
Author: admin
Category: SysAdmin
Tags: kvm, libvirt, linux, qemu, virtualization
Slug: passing-data-key-value-pairs-from-kvm-qemu-host-to-guests
Status: draft

Many virtualization hypervisors (including VMWare, Xen, VirtualBox,
etc.) have some way (with varying degrees of simplicity) of passing data
from the host/dom0 into the guest/domU. Unfortunately,
[KVM](http://www.linux-kvm.org) does not. I have a bunch of KVM hosts
and guests running CentOS. I'd like to pass some key-value pairs from
the host to the guest. Or really, I'd like to pass one string - the
hostname of the dom0 machine - to the guest. Unfortunately there doesn't
seem to be a simple way to do this that meets my requirements:

1.  Work nicely with my libvirt-managed guests, which are installed with
    Cobbler's [koan](https://github.com/cobbler/cobbler/wiki/Koan) tool
2.  Require minimal reconfiguration of the running guests.
3.  Be safe for use on existing hosts and guests.
4.  Work "right" across live migrations of a guest

My first thought was to use qemu/kvm's file sharing feature (passthrough
filesystem mounts, a.k.a. "9p virtio" as it uses the 9p filesystem
drivers) that allow mounting of a directory on the host filesystem from
within the guest. Unfortunately, there's two problems with this approach
in my environment:

1.  This is totally unusable on CentOS/RHEL, as their kernels are not
    configured with the [required CONFIG\_NET\_9P and other related 9P
    options](http://wiki.qemu.org/Documentation/9psetup).
2.  I've found conflicting information, but it looks as though virtio-9p
    shares may not be supported for live migration. There's a
    [qemu-devel mailing list thread from April
    2013](http://lists.gnu.org/archive/html/qemu-devel/2013-04/msg00303.html)
    regarding patches for this, but I was unable to find a conclusive
    answer to whether or not they were merged and working. The [Fedora
    Virtualization Deployment and Administration Guide (19.0.1
    draft)](http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Virtualization_Deployment_and_Administration_Guide/chap-Virtualization_Administration_Guide-KVM_live_migration.html)
    says,

    > Shared storage must mount at the same location on source and
    > destination systems. The mounted directory names must be
    > identical.

    which I take as indication that this *may* be possible.

I then examined a number of other possibilities:

-   Setting the smbios "serial" string through the libvirt XML, which
    would give a way of passing a single string (unknown length limit)
    into the guest, but it would be tied to the libvirt XML not the
    host, and therefore wouldn't change with live migration.

I do, however, have a number of theories which *may* fit all of my
requirements, with the possible exception of not playing well with
`koan` for installation, and being difficult to roll out to existing
guests:

-   Qemu recently introduced the [QEMU Guest Agent (libvirt
    wiki)](http://wiki.libvirt.org/page/Qemu_guest_agent) (also [qemu
    wiki](http://wiki.qemu.org/Features/QAPI/GuestAgent) and [Fedora
    Virtualization Deployment and Administration
    Guide](http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Virtualization_Deployment_and_Administration_Guide/qemu-ga.html)),
    which is intended to allow "things" on the host to control "things"
    on the guest (so it works the opposite way we want). At the moment,
    it doesn't appear to have any functionality beyond initiating a
    reboot or shutdown from the guest OS, and trying to freeze
    filesystems before a snapshot. Also to be noted is that the
    host-guest agent communication takes place over a virtio-serial
    character device mapped to a path on the host filesystem, so there's
    no fancy communication going on here, and no reason why we couldn't
    implement a similar system ourselves. Furthermore, it needs to be
    manually added to the libvirt XML to be setup.
-   My VMs are currently setup with bridged networking on the host, and
    only that one interface. If they were configured with a host-only
    network on a second NIC, it would be trivial to setup all KVM hosts
    to the same IP on their host-only net (probably 192.168.0.1) and
    serve DHCP to their VMs, and then have a daemon on the host
    (lightweight web server? something even simpler?) that serves the
    key-value pairs, or whatever else is desired.
-   It might be possible to achieve the goal of the virtio-9p idea by
    using disk images stored on the host. Unfortunately, there are 2
    main drawbacks to this idea currently:
    -   It's unknown how this will react with live migration.
    -   It's unknown whether multiple guests can mount (read-only) the
        same disk image on the host.
    -   This is a lot of work/overhead to get one string to the guest.

http://www.linux-kvm.org/page/VMchannel\_Requirements
