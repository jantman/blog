Title: Modern (0.10.x+) NodeJS RPMs on CentOS/REHL 5 and 6
Date: 2013-06-06 20:47
Author: admin
Category: Tech HowTos
Tags: build, centos, EPEL, node, nodejs, package, packaging, redhat, RHEL, rpm, specfile
Slug: modern-0-10-x-nodejs-rpms-on-centosrehl-5-and-6

I posted back in January about [RPM Spec Files for nodejs 0.9.5 and v8
on CentOS
6](/2013/01/rpm-spec-files-for-nodejs-0-9-5-and-v8-on-centos-5/). In
that post I also said that I was unable to get recent NodeJS to build on
CentOS 5 because of a long chain of dependencies including node-gyp, v8,
http-parser, glibc, etc. I said I couldn't get it to build. Well, I have
good news for both distro versions.

On the CentOS/RHEL 6 side, thanks to a lot of work by T. C.
Hollingsworth and others, NodeJS 0.10.5 is currently in the official
[EPEL](http://fedoraproject.org/wiki/EPEL) repositories. They seem to be
keeping the packages pretty current, but if you need newer, you can
always grab the SRPMs from EPEL and build the newer versions. This is
great, because it means I no longer need to maintain the spec files and
do my own builds. I don't think I really did anything to help get this
package in EPEL, other than ping a few people and comment on a few
tickets.

For CentOS/RHEL 5, I finally have packages, but they're not exactly
pretty. The dependency solving issues still stand; they're rooted at the
dependency of node-gyp which requires the v8 C++ JavaScript library, and
is required to compile shared object addons. The best solution that I
(and a few others) could find is simply not to build node-gyp, and not
to have support for addons or package any addons; we just have the
binaries that NodeJS's Makefile creates, and everything else is
interpreted. A [coworker](https://twitter.com/toxigenicpoem) found
[https://github.com/kazuhisya/nodejs-rpm](https://github.com/kazuhisya/nodejs-rpm)
which contains a configure patch and specfile for a dead-simple CentOS
5/6 RPM of NodeJS 0.10.9, which essentially just uses EPEL's python26
packages to power the NodeJS build process, configures and uses the
Makefile's `make binary` command to spit out a NodeJS binary tarball,
and then packages that. That whole process way out of line from the
[Fedora Packaging
Guidelines](http://fedoraproject.org/wiki/Packaging:Guidelines), and
also only dumps out nodejs, nodejs-binary and nodejs-debuginfo packages,
so I also can't just substitute in a different package name in my puppet
manifests (which install nodejs, nodejs-devel and npm packages). So I
[forked that repository](https://github.com/jantman/nodejs-rpm-centos5)
and made some changes to the specfile: I gave the package name a prefix
("cmgd\_", since that's where I work these days) and some warnings in
the description, to make it abundantly clear that these packages are
very far from what you find in EPEL and other repositories, and broke
npm and the devel files out into their own subpackages. Hopefully this
spec file will be of use to someone else who also has the unfortunate
need of supporting recent NodeJS on CentOS 5. If there's enough
interest, I'll consider building the packages and putting them in a
repository somewhere.

You can see the NodeJS 0.10.9 on CentOS 5 spec file, a patch, and the
READMEs at
[https://github.com/jantman/nodejs-rpm-centos5](https://github.com/jantman/nodejs-rpm-centos5).
Patches and/or pull requests are greatly appreciated, especially from
anyone who wants to make the spec file more Fedora guidelines compliant.
