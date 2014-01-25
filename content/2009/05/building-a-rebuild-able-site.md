Title: Building a Rebuild-able Site
Date: 2009-05-06 08:42
Author: admin
Category: Puppet
Tags: backup, configuration, kickstart, linux, puppet, recovery, work
Slug: building-a-rebuild-able-site

At $WORK, my group runs about two dozen servers that provide services
for over 60,000 users. They're a mix of Windows and Linux, with some old
Solaris stuff thrown in there. The one thing they have in common is
they're all hand-built, hand-configured, and old. They've been around
for a while. At the moment, we don't even have an adequate backup
system.

So, being the closest thing to a SysAdmin we have (my official title is
still Student Systems Programmer), it's my job to build a new
installation, configuration and backup infrastructure. We've already
standardized on [CentOS](http://www.centos.org) as a University-wide
distro, and have a local full mirror, so I don't need to choose a
distro. I do, however, have to plan the installation and backup
architecture. The main requirements are:

1.  Lowest overall time for bare-metal recovery to a working system.
2.  Ease of use, as people other than myself will need to administer it
    (so they should be able to do so from a cheat sheet in the wiki).
3.  Repeatability - it should be easy and intuitive to make an
    almost-exact-copy of a machine.

I started a thread a few days ago on the SAGE mailing list, which you
can find
[here](http://mailman.sage.org/pipermail/sage-members/2009/msg00447.html).

At the moment, it looks like the general idea that I'm going with is to
use [Kickstart](http://fedoraproject.org/wiki/Anaconda/Kickstart) to
install the systems, using a basic and minimal Kickstart file. Basic
package selection (minimalist) with just what's needed to configure the
system with a hostname and network settings for the management VLAN.
I'll then have Kickstart install and configure a configuration
management package - I'm leaning towards
[Puppet](http://reductivelabs.com/products/puppet/) over
[Cfengine](http://www.cfengine.org/) and am starting testing. The config
management software will handle all of the customization for the system
(everything different from the base generic Kickstart install) so it's
all kept under the control of config management from step 1.

The final part is a backup system, mainly for whatever eventually -
whether out of human error or simple laziness - ends up out of the
config management system's control. Our previous SA had settled on
[Zmanda](http://www.zmanda.com/), the paid version of
[Amanda](http://www.amanda.org/), which comes with specific plugins for
MySQL and MSSQL. I'm also looking at [Bacula](http://www.bacula.org),
mainly because of its' advanced features, scheduling (especially the new
scheduling in Bacula 3) and scalability.

The beauty that I see in having Kickstart do something minimal and then
letting Puppet handle the rest is that (especially since we've
standardized on SunFire X4100's with identical configurations) I can
kickstart and rack up a few spare machines, and to get them up and
running all I need to do is power them up (iLOM) and tell Puppet what to
make them.

I'm currently starting testing of both Puppet itself and getting
Kickstart to start the puppet install and daemon (instructions from
[David Lutterkort's blog (Red Hat software
engineer)](http://watzmann.net/blog/index.php?cat=21)). We'll see how
everything goes...
