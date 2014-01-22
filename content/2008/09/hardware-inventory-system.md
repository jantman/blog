Title: Hardware Inventory System
Date: 2008-09-12 13:01
Author: admin
Category: Projects
Tags: configuration, inventory
Slug: hardware-inventory-system

After a few crazy weeks at work, the pay check is finally here, and I've
decided to allocate some of the money to hardware upgrades of my
personal machines. While [Nagios][] gives me a good idea of where
performance is a problem, I'm still running a large amount of "legacy"
hardware (my home router/firewall is a 350MHz P-II desktop) and hardware
age is a significant factor in my upgrade plans.

So, I set out looking for a program (most likely some backend scripts
that dump data to MySQL, and then a PHP front-end) to perform a hardware
inventory - essentially, run a script on each box, find out the system
details, and dump it in a DB. Now that my pool of upgrade candidates is
above a dozen machines, at multiple locations, some of which are
single-use boxes often neglected/forgotten, doing this in my head isn't
the easiest.

So, while I've been googling and searching some mailing list archives,
I'm also developing a set of requirements.

The chief requirements:

-   Ability to run a script on a remote machine and have the results
    returned in a meaningful format. Most likely, a single script, run
    as root (SUID or sudo) that returns nice, formatted, SQL-ready
    results (so the parsing of platform-specific command output will
    happen on the client, with every client returning a normalized data
    set).
-   Ability to track hardware changes - i.e. disks swapped from one box
    to another, NIC replacement, processor upgrade, etc.
-   Each piece of hardware tracked individually, allowing future support
    of fully tracking components, spares, etc.
-   Support for future barcoding of components and physically-performed
    inventory.

</p>

Some of the data that I'd like collected:

-   Data on a machine stored by chassis vendor name and serial
    numer/service tag.
-   Hostname associated with each box.
-   Architecture, number of CPUs/cores and type, model, speed, socket
    (for upgrade planning/ordering).
-   Motherboard model/manufacturer, serial number, HW and SW/FW
    revisions, manufacture date.
-   Storage (internal & directly connected external) - type, interface,
    capacity, specifications/manufacturer and model.
-   Amount fo RAM, type of RAM, and configuration of cards (number of
    empty slots).
-   PCI card configuration - number and type/mfr/model of cards, as well
    as number of empty slots
-   For all NICs - MAC addresses, current IPs, as well as link
    type/speed and connected switch/port.

I'd also like some level of software inventory, especially for those
machines that may be running "forgotten" services:

-   [nmap][] scan results.
-   OS-generated list of running services, with GUI including a
    blacklist of "default" services not to be displayed, and possibly
    also cross-links to Nagios status.
-   Possibly a parsed output from ps, using a blacklist as shown above.
-   If a firewall is running on the system, a list of all open ports.

I'll be checking out some options today. Unfortunately, I have a feeling
that there's most likely nothing that supports my requirements, and I'll
probably end up implementing a lot of this myself.

  [Nagios]: http://www.nagios.org
  [nmap]: http://nmap.org/
