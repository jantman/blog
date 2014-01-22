Title: Search for a small-scale but automated RPM build system
Date: 2013-05-13 05:00
Author: admin
Category: Tech HowTos
Tags: build, linux, nodejs, package, packaging, repository, rpm, rpmbuild, software, sysadmin, yum
Slug: search-for-a-small-scale-but-automated-rpm-build-system

***This post is part of a series of older draft posts from a few months
ago that I'm just getting around to publishing. Unfortunately, I have
yet to find a build system that meets my requirements (see the last
paragraph).***

At work, we have a handful - currently a really small number - of RPM
packages that we need to build and deploy internally for our CentOS
server infrastructure. A number of them are just pulled down from
specific third-party repositories and rebuilt to have the vendor set as
us, and some are internally patched or developed software. We run
websites, and on the product side, we're a Python/[Django][] shop (in
fact, probably one of the largest Django apps out there). We don't
deploy our Django apps via RPM, so building and distributing RPMs is
definitely not one of our core competencies. In fact, we really only
want to do it when we're testing/deploying a new distro, or when an
upstream package is updated.

Last week I pulled a ticket to deploy [node.js][] to one of our build
hosts, and we've got a few things in the pipeline that also rely on it.
I found the [puppetlabs-nodejs][] module on Github that's supposed to
install it on RHEL/CentOS, but it pulls packages from
[http://patches.fedorapeople.org/oldnode/stable/][], and the newest
version of nodejs there is 0.6.18, which is quite old. I can't find any
actively maintained sources of newer nodejs packages for RHEL/CentOS
(yeah, I know, that's one down side to the distributions...). However, I
did find that nodejs 0.9.5 is being [built for Fedora 18/19 in the
Fedora build system][], is already in the Fedora 18 Testing and Fedora
Rawhide repos, but is failing its EL6 builds in their system. The
decision I've come to is to use the puppetlabs-nodejs module to install
it, but try and rebuild the Fedora 18 RPMs under CentOS 5 and 6.

So that's the background. Now, my current task: to search for an RPM
build system for my current job. My core requirements, in no specific
order, are:

-   Be relatively easy and quick to use for people who have a specfile
    or SRPM and want to be able to "ensure =\> present" the finished RPM
    on a system. i.e., require as little per-package configuration as
    possible.
-   Be able to handle rebuilding "all" of our RPMs when we roll out a
    new distro version. Doesn't necessarily need to be automatic, but
    should be relatively simple.
-   Ideally, not need to be running constantly - i.e. something that
    will cope well with build hosts being VMs that are shut down when
    they're not needed.
-   Handle automatically putting successfully built packages into a
    repository, ideally with some sort of (manual) promotion process
    from staging to stable.
-   Have minimal external (infrastructure) dependencies that we can't
    satisfy with existing systems.

So, the first step was to research existing RPM build systems and how
others do this. Here's a list of what I could find online, though most
of these are from distributions and software vendors/projects, not
end-user companies that are only building for internal use.

-   [Koji][] is the build system used by [Fedora][] and RedHat. It's
    about as full-featured as any can be, and I'm familiar with it from
    my time at [Rutgers University][], as it's used to maintain their
    CentOS/RHEL packages. It's based largely on Mock. However, [setting
    up the build server][] is no trivial task; there are few
    installations outside of Fedora/RedHat, and it relies on either
    Kerberos or an SSL CA infrastructure to authenticate machines and
    clients. So, it's designed for too large a scale and too much
    infrastructure for me.
-   PLD Linux has a [builder script][] that seems to automate `rpmbuild`
    as well as fetching sources and resolving/building dependencies. I
    haven't looked at the script yet, but apparently it's in PLD's
    "rpm-build-tools" package.
-   PLD Linux also has a CVS repository for something called
    [pld-builder.new][]. The [README][] and [ARCHITECTURE][] files make
    it sound like a relatively simple mainly-Python system that builds
    SRPMS and binary packages when requested, and most importantly,
    seems like a simple system that uses little more than shared
    filesystem access for communication and coordination.
-   ALT Linux has [Sisyphus][], which combines repository management and
    web interface tools, package building and testing tools, and more.
-   The Dries RPM repository uses (or at least used... my reference is
    quite old) [pydar2][], "a distributed client/server program which
    allows you to build multiple spec files on multiple
    distribution/architecture combinations automatically." That sounds
    like it could be what I need, but the last update says that it isn't
    finished yet, and that was in **2005**.
-   Mandriva Linux has pretty extensive information on their build
    system [on their wiki][] and a [build system theory page][], but it
    seems to be largely a hodgepodge of shell scripts and cronjobs, and
    is likely not a candidate for use by anyone other than its
    designers.
-   Argeo provides the [SLC framework][] which has a "RPM Factory"
    component, but I can't seem to find much more than a wiki page, and
    can't tell if it's a build automation system or just handles mocking
    packages and putting them in a repo on a single host.
-   Dag Wieers' repositories use (or used) a set of python scripts
    called [DAR, "Dynamic Apt Repository builder"][]. They're on
    [github][] but are listed as "old" and haven't been updated in at
    least 2 years. The features sound quite interesting, and though it's
    based on the Apt repo format, it might provide some good ideas for
    implementing a similar system.

**Update four months later:** I've yet to find a build system that meets
my requirements above. For the moment I'm only managing \~20 packages,
so my "build system" is a single shell script that reads in some
environment variables and runs through using [mock][] to build them in
the correct order (including pushing the finished RPMs back into the
local repository that mock reads from) and then pushing the finished
packages to our internal repository. Maybe when I have some spare time,
I'll consider a project to either make a slightly better (but simple)
RPM build system based on Python, or get our [Jenkins][] install to
handle this for me.

  [Django]: https://www.djangoproject.com/
  [node.js]: http://nodejs.org/
  [puppetlabs-nodejs]: https://github.com/puppetlabs/puppetlabs-nodejs
  [http://patches.fedorapeople.org/oldnode/stable/]: http://patches.fedorapeople.org/oldnode/stable/
  [built for Fedora 18/19 in the Fedora build system]: http://koji.fedoraproject.org/koji/packageinfo?packageID=15154
  [Koji]: https://fedorahosted.org/koji/wiki
  [Fedora]: http://fedoraproject.org/wiki/Koji
  [Rutgers University]: http://koji.rutgers.edu/koji/
  [setting up the build server]: http://fedoraproject.org/wiki/Koji/ServerHowTo
  [builder script]: https://www.pld-linux.org/developingpld/builderscript
  [pld-builder.new]: http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-builder.new
  [README]: http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-builder.new/doc/README?rev=1.5
  [ARCHITECTURE]: http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-builder.new/doc/ARCHITECTURE?rev=1.6
  [Sisyphus]: http://en.altlinux.org/Sisyphus
  [pydar2]: http://dries.ulyssis.org/rpm/pydar2/index.html
  [on their wiki]: http://wiki.mandriva.com/en/Category:Build_System
  [build system theory page]: http://wiki.mandriva.com/en/Development/Packaging/BuildSystem/Theory
  [SLC framework]: https://www.argeo.org/wiki/SLC
  [DAR, "Dynamic Apt Repository builder"]: http://dag.wieers.com/home-made/dar/
  [github]: https://github.com/dagwieers/dar
  [mock]: http://fedoraproject.org/wiki/Projects/Mock
  [Jenkins]: http://jenkins-ci.org/
