Title: Creating RPMs from Perl CPAN Modules
Date: 2012-05-15 15:01
Author: admin
Category: Software
Tags: cpan, cpan2rpm, perl, rpm, yum
Slug: creating-rpms-from-perl-cpan-modules

I try my absolute best to always install software on my Linux boxes as
[RPM](http://en.wikipedia.org/wiki/RPM_Package_Manager)s, installed
through [Yum](http://yum.baseurl.org/) (yes, I use
[CentOS](http://www.centos.org) on servers and
[Fedora](http://fedoraproject.org/) on my desktops/laptops). Not only is
this more-or-less required to sanely manage configuration through
Puppet, but it also lets me recreate a machine, or install dependencies
for something, in one simple command line. Unfortunately, I run quite a
bit of Perl code, and there are a lot of [CPAN](http://www.cpan.org/)
Perl modules that aren't in any of the usual CentOS/Fedora repositories.

Enter cpan2rpm: a Perl script that, in its simplest invocation,
downloads a specified CPAN module and automatically builds RPMs and
SRPMs for it. The [original version](http://perl.arix.com/cpan2rpm/) by
[Erick Calder](http://www.arix.com/ec/) hasn't been touched since 2005,
but there's [a newer version from
Mediaburst](http://www.mediaburst.co.uk/blog/creating-perl-module-rpms/),
[cpan2rpmmb](http://www2.mbstatic.co.uk/wp-content/uploads/2009/09/cpan2rpmmb),
that seems to incorporate some nice improvements and worked quite well
for me.
