Title: The state of Puppet External Node Classifiers
Date: 2012-02-26 12:45
Author: admin
Category: Puppet
Tags: dashboard, foreman, node classifier, puppet
Slug: the-state-of-puppet-external-node-classifiers

**Update November 2013**: This post has brought an amazing amount of
traffic to my blog, probably because it still seems to be one of the
only ENC comparisons out there. Both Dashboard (and Puppet Enterprise
Console) and The Foreman have changed quite a bit since I wrote this.
Foreman has certainly been developed at warp speed. I'll try to write an
update to this sometime soon, but be advised that the information here
is somewhat dated.

At work, we're in the process of rolling out
[puppet](http://projects.puppetlabs.com/projects/puppet) for
configuration management of our servers. It will be an integral part of
the provisioning process of all new physical and virtual hosts, and will
also be phased in on existing hosts as possible. Right now, we have an
initial puppet install that was "development", but we're about to move
to "production" (new puppetmaster in our production infrastructure,
production MySQL, etc.). We've been using
[Dashboard](http://puppetlabs.com/puppet/related-projects/dashboard/),
but just as a report viewer. Up until now, we've been using nodes.pp and
per-node flat-file manifests. I've got a few issues with this, but the
biggest is that all of our node definitions (and their classes and
parameters) live in the same SVN repository as our modules and other
puppet configuration. Not only does this mean a checkout and commit just
to change a node parameter or add a module/class to a node, but it also
means that for my team members who don't have previous puppet
experience, it greatly blurs the line between administering puppet
(developing and maintaining modules) and using puppet (building a node,
changing node params or modules/classes), since both tasks are
accomplished in the same SVN repository.

So, I've been pushing an [External Node Classifier
(ENC)](http://docs.puppetlabs.com/guides/external_nodes.html) with a web
interface as one of the biggest feature enhancements we need for our
puppet install. The complicating factor is that I've been given a time
frame of approximately 1 week to get the "production" puppetmaster
running on our production infrastructure and marked as "done". That
includes the ENC. At my last gig, at Rutgers University, I wrote our ENC
in PHP (actually I wrote it for my half-dozen or so boxes at home, and
brought it to Rutgers gratis), and it also handled kickstart file
distribution and PXE configuration, and was extended to also set DHCP
and DNS for the hosts - a one-stop solution. Unfortunately the code is
very organization-specific, not terribly solid, and the UI looks awful,
so it's not a fit for the current employer. So I have to find something
else that fits the bill. I have a list of initial ("phase 1")
requirements that are a mix of functionality that we require and
management requirements:

-   Must support environments, since we make use of them.
-   Must support default values for parameters based on environment,
    "zone" (a custom fact and variable we define), or a combination of
    both.
-   For accountability and legal reasons, must have full auditing of all
    changes by all users (and, obviously, support authentication).
-   Display node last run time and status.

As well as at least the ability to implement some of our phase 2
requirements:

-   Ability to show modules and classes applied to a node, including
    those required/included through other modules/classes/roles.
-   Should support at least some level of puppet report display.
-   Ability to trigger a node run (kick) from the UI.
-   Some level of permission separation, ACL or RBAC so that we could
    potentially delegate control of a certain module or parameter, on a
    certain group of nodes, to the development team.
-   Per-node links to other tools such as Icinga/Nagios or our wiki.
-   Some way of detecting valid classes and modules (and our "role"
    module) per-environment (i.e. available modules/classes/roles should
    be pulled from the configs, not manually entered).
-   Ability to display puppet docs from modules/classes

Our current situation makes this even more difficult: we're an
operations team of five (hiring at the moment to fill the position of
the sixth), and I believe I'm the only member of the team with any real
software development experience. And none of us have experience with
Ruby (which Puppet and most of its universe is written in). This means
that any in-house solution runs the risk of being unmaintainable should
I get hit by a bus (some of our team have various levels of experience
with Perl and other scripting languages, but not really from an app
development perspective). Because of these reasons, there's a management
aversion to anything that we code ourselves (well, these reasons, and
the fact that with a shorthanded team we don't have much time for
projects without an immediate impact).

So, I spent hours looking around online trying to find existing
web-based ENC projects, and came up with a pretty small list:

-   [Dashboard](http://puppetlabs.com/puppet/related-projects/dashboard/),
    the Puppet Labs web UI. It's the most common web-based puppet ENC as
    far as I know, and since it's an official Puppet Labs project (and
    the basis for their Puppet Enterprise UI), its future is pretty
    secure. But it's still very basic (let alone enterprise features),
    and has a plugin system that is very young.
-   [The Foreman](http://theforeman.org/projects/foreman) is probably
    the second-most-common puppet ENC, and has also been around about as
    long as Dashboard. Its features are nice, and it includes support
    for Kickstart (management of TFTP and DHCP) and DNS, as well as some
    virtual machine management. Unfortunately, we already have DHCP and
    DNS infrastructure so I'm sure it would be quite a bit of effort to
    integrate it with our environment, and for a non-Ruby shop, it has
    the same problem with maintainability of custom code.
-   [initr](http://www.ingent.net/projects/initr/wiki), a
    [Redmine](http://www.redmine.org/) plugin that functions as an ENC
    and manages modules. It includes RBAC and leverages Redmine. But
    since we don't use Redmine, it's not much of an advantage.
-   [OpenNMS Puppet Node
    Pusher](http://www.gitorious.org/opennms-puppet-node-pusher)An ENC
    script for [OpenNMS](http://www.opennms.org/), which we also don't
    use.

I was pretty amazed to see that nobody had written a puppet web UI/ENC
in PHP (or Perl or Python), especially since Puppet is now quite
popular.

So, I'm essentially left with the following options:

-   Start from scratch and write my own in PHP. By far the worst option,
    since we don't have anyone on our team who's likely to maintain it,
    and the Puppet community is Ruby-focused.
-   Use Foreman, since it's the only one that appears to offer audit
    logging, have a bunch of features that don't work for us, and
    hopefully deal with it.
-   Learn Ruby, write plugins for Dashboard, and hope that Puppet Labs
    or someone else will pick them up and maintain them if I can't.

At the moment, I've decided to investigate Foreman and initr in a bit
more depth, and also play around with the Dashboard code and try to pick
up some Ruby (as they're all written in Ruby anyway). I'll also discuss
these options with the team and see how opinions go (keeping in mind
that the higher the likelihood of the community picking up/merging my
changes, the better).
