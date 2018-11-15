Title: Nagstamon on Fedora 17
Date: 2012-10-05 07:37
Author: admin
Category: Miscellaneous
Tags: fedora, nagios. icinga, nagstamon, package, rpm
Slug: nagstamon-on-fedora-17

Since I started my last job, I've been using
[Nagstamon](http://nagstamon.ifw-dresden.de/) on my workstation; it's a
really handy little system tray application that monitors a
Nagios/Icinga instance and shows status updates/summary in a handy
fashion, including flashing and (optionally) a sound alert when
something changes. Unfortunately, there doesn't seem to be a Fedora 17
package for it, though there is an entry on the [Fedora package
maintainers
wishlist](http://fedoraproject.org/wiki/Package_maintainers_wishlist#N-O).
The closest I was able to find is a
[repoforge/RPMforge](http://pkgs.org/centos-6-rhel-6/repoforge-i386/nagstamon-0.9.7.1-2.el6.rf.noarch.rpm.html)
package of Nagstamon 0.9.7.1, along with a [source
RPM](http://apt.sw.be/source/nagstamon-0.9.7.1-2.rf.src.rpm).

Here are the steps to build that package on F17:

1.  Download and install
    [rpm-macros-rpmforge](http://apt.sw.be/source/rpm-macros-rpmforge-0-6.rf.src.rpm).
2.  As root, edit `/etc/rpm/macros.rpmforge` and comment out the `%dist`
    macro, so we'll still have the default "fc17" dist tag.
3.  `wget http://apt.sw.be/source/nagstamon-0.9.7.1-2.rf.src.rpm`
4.  rpmbuild --rebuild nagstamon-0.9.7.1-2.rf.src.rpm

Hopefully this will help someone else as well. At the moment, Nagstamon
is actually up to version 0.9.9, so hopefully I'll build a newer package
sometime soon.
