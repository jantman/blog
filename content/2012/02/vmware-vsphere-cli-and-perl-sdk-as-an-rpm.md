Title: VMWare vSphere CLI and Perl SDK as an RPM
Date: 2012-02-28 19:01
Author: admin
Category: Tech HowTos
Tags: perl, rpm, vcli, vmware, vsphere
Slug: vmware-vsphere-cli-and-perl-sdk-as-an-rpm

Lately I've been playing around with the VMWare [vSphere SDK for
Perl](http://www.vmware.com/support/developer/viperltoolkit/), since the
new job uses a bunch of VMWare stuff (and I've been starting my foray
into Perl as a new language, and am amazed by the [massive
number](http://www.cpan.org/) of modules out there). As much as I find
[`yum`](http://yum.baseurl.org/) limiting having used
[`zypper`](http://en.opensuse.org/Portal:Zypper) on OpenSuSE, I'm not
much of a fan of non-natively-packaged software. Not only is it more
difficult to maintain and upgrade a system and nearly impossible to
nicely automate when building from source (or a proprietary installer
script), it's also much more difficult to transition from a development
environment to production.

In a quick search, I found a perfectly working spec file and some
RHEL/Cent-specific patches (and even beginner-level `rpmbuild`
instructions) for the current 5.0.0-422456 VMWare CLI and Perl SDK for
x86\_64 at
[http://www.firetooth.net/confluence/display/public/vSphere+Perl+SDK+and+CLI+RPM+Packages](http://www.firetooth.net/confluence/display/public/vSphere+Perl+SDK+and+CLI+RPM+Packages).
Many thanks to [Vaughan
Whitteron](http://www.linkedin.com/in/vwhitteron) of NSW in Australia
for posting this! It built and installed without any problems on my
Fedora 16 desktop, and a CentOS 6.2 development box.
