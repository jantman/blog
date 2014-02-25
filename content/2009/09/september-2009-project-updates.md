Title: September 2009 Project Updates
Date: 2009-09-17 13:00
Author: admin
Category: Projects
Tags: machdb, php ems tools, PHPsa, Projects, rackman
Slug: september-2009-project-updates

I know I haven't been posting a lot, but here's an update on some of my
projects:

-   [PHP EMS Tools](http://www.php-ems-tools.com) - I've done quite a
    bit of work for the [ambulance
    corps](http://www.midlandparkambulance.com), and intend on rolling
    this into the main distribution. I've also added an Asterisk/AGI
    module to handle crew call-ins. It's going to be a long road, as I
    have to manually diff the ambulance corps version to the trunk
    version and merge the changes (leaving out anything specific to our
    organization), but I plan on doing it. The next version will also
    include historical tracking of roster information (member
    information, status, positions, committees, etc.) and LDAP
    integration for authentication.
-   **PHPsa** - My new project, tentatively called PHPsa, is an
    integrated dashboard for sysadmins. The idea is to develop a
    plugin-based portal for SA tools. Currently, I will be including
    some of my own projects - MultiBindAdmin (a tool to administer BIND
    and DHCPd, specifically geared towards split-view DNS with the
    inside behind NAT) and RackMan (a tool to track and visualize the
    location of devices within racks, including ability to temporarily
    move devices around) - as well as my updates to Nathan Hubbard's
    [MachDB](http://www.machdb.org/).

I've also done quite a bit of customization of the current version of
Nathan Hubbard's [MachDB](http://www.machdb.org/). It adds detailed
network interface information, information on expansion slots, and some
extra details for the system and storage. I plan on developing a patch
and contacting Nathan once I get a chance. It also includes a Python
collector script that I developed.
