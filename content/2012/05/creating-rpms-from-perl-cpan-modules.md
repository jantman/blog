Title: Creating RPMs from Perl CPAN Modules
Date: 2012-05-15 15:01
Author: admin
Category: Tech HowTos
Tags: cpan, cpan2rpm, perl, rpm, yum
Slug: creating-rpms-from-perl-cpan-modules

I try my absolute best to always install software on my Linux boxes as
[RPM][]s, installed through [Yum][] (yes, I use [CentOS][] on servers
and [Fedora][] on my desktops/laptops). Not only is this more-or-less
required to sanely manage configuration through Puppet, but it also lets
me recreate a machine, or install dependencies for something, in one
simple command line. Unfortunately, I run quite a bit of Perl code, and
there are a lot of [CPAN][] Perl modules that aren't in any of the usual
CentOS/Fedora repositories.

Enter cpan2rpm: a Perl script that, in its simplest invocation,
downloads a specified CPAN module and automatically builds RPMs and
SRPMs for it. The [original version][] by [Erick Calder][] hasn't been
touched since 2005, but there's [a newer version from Mediaburst][],
[cpan2rpmmb][], that seems to incorporate some nice improvements and
worked quite well for me.

  [RPM]: http://en.wikipedia.org/wiki/RPM_Package_Manager
  [Yum]: http://yum.baseurl.org/
  [CentOS]: http://www.centos.org
  [Fedora]: http://fedoraproject.org/
  [CPAN]: http://www.cpan.org/
  [original version]: http://perl.arix.com/cpan2rpm/
  [Erick Calder]: http://www.arix.com/ec/
  [a newer version from Mediaburst]: http://www.mediaburst.co.uk/blog/creating-perl-module-rpms/
  [cpan2rpmmb]: http://www2.mbstatic.co.uk/wp-content/uploads/2009/09/cpan2rpmmb
