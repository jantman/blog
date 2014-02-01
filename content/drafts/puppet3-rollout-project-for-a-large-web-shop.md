Title: Puppet3 rollout project for a large web shop
Date: 2013-10-25 16:29
Author: admin
Category: Puppet
Tags: puppet, puppet3
Slug: puppet3-rollout-project-for-a-large-web-shop
Status: draft

We've got a pretty sizable Puppet infrastructure at work, spanning about
240 nodes - currently a mix of Puppet Enterprise 2.5.0 on the production
and QA machines, and Puppet Open Source on many of the development and
testing boxes. We run the web presence and some associated services for
a bunch (about 150 or so) of large media properties (newspapers, TV and
radio stations), on an all-CentOS Linux infrastructure. Having gotten a
break in my time-sensitive work - I've got 2-3 weeks from when I
finished my last customer-visible project until the next dozen machines
get racked to build out a paid of new QA environments - I'm finally able
to move forward with our Puppet3 rollout, albeit at a breakneck pace.

I spent a few days diving into the current best practices, how others
are doing Puppet these days (especially [Puppet Labs' own Operations
team](https://github.com/puppetlabs-operations) and [Mozilla Release
Engineering](https://wiki.mozilla.org/ReleaseEngineering/PuppetAgain)),
and the great [side
decks](http://www.slideshare.net/search/slideshow?searchfrom=header&q=%22puppetconf+2013%22)
and [recently released
videos](http://www.youtube.com/playlist?list=PLV86BgbREluU02Ytlz80seDSKAbkx5pRg)
from PuppetConf 2013. Then I cut 31 tickets and started working through
them...

In this first of a series of posts, I'll describe the current state of
our puppet infrastructure, and our plans for the Puppet3 rollout (which
we'll handle in two phases). I plan on following this up with a series
of detailed posts on how we're implementing Puppet3, and hopefully
sharing some of the code I wrote (though some of it is admittedly
environment-specific).

## The Current State of Our Puppet

Put simply, our current Puppet environment is pretty poor. I'd say it's
typical of a grassroots, organic Puppet deployment (granted it's our
second, started in March 2011; and there are some hosts that never made
it into "2.0", still running 0.25.5 pointing to a nonexistent master).
We're currently running Puppet Enterprise 2.5.0 on almost all nodes,
pointing to a single production PE 2.5.0 master. Development/testing
nodes generally run 2.6.x Open Source, pointing at a single Open Source
"testing" master, which runs per-user puppet environments, manually
managed as clones of our single puppet git repo. All hosts have the
awful `$ssldir = $confdir/$server` hack for doing one-off testing runs
against the test puppetmaster.

We keep everything in one git repo, and currently have community
(forge/github) modules intermixed with our own, and some of them are
locally modified. The only "management" is a README.md file that lists
the source of each module, the version it was at when we downloaded the
tarball, and whether or not it has local changes. "Testing" is checking
out a feature branch to a per-user environment on the test puppetmaster,
and doing a one-time noop run of a suitable host against the test
puppetmaster, usually followed by a one-time agent run, after which we
do peer code review and then merge to the master branch in git, and
manually deploy master on the production puppetmaster. There's no
automated testing at all, and the whole procedure is manual (and done as
root).

Due to past disasters, Puppet agents are disabled on all production
hosts; Puppet is used to build out the host, and then `--disable`ed and
stopped. As a result, configuration state of the production environment
is dictated by the state of modules at the time a given host was built,
and has diverged widely between hosts. Non-production (development,
testing, QA, etc.) environments are slightly better, but have a handful
of modules that are out of date and constantly fail (causing runs on
approximately 20% of hosts, mainly our development environments, to show
as failed).

We currently use a directory full of modules, mainly homegrown, and
Puppet Enterprise Console (i.e. Puppet Dashboard) for report
storage/display and as an ENC. The ENC features of Dashboard don't come
close to meeting our needs; mainly the lack of support for parameterized
classes, the lack of a complete and detailed audit trail, the lack of
support for structured data (i.e. arrays and lists coming from the ENC),
the lack of ACLs or some sort of way to give a set of users access to
only certain nodes, and the inability to safely override or exclude
classes/parameters inherited from a group.

Currently, only our operations and automation teams have privileges to
push to the puppet repository, mainly because of the manual testing
requirements. We need to be able to allow developers access to puppet in
the same way that we have it, rather than requiring ops to manually push
and test.

## Plans for Our Puppet3 Infrastructure

Our plan is to move to Puppet3 and some current best practices around
testing and workflow, in two phases. The first phase will include the
buildout of the infrastructure and some minimal automated testing
(static testing and confirmation of successful runs), as well as
migration of existing hosts to the new puppet versions and masters.
Phase Two will include automated VM-based testing. If you're interested,
you can see my (slightly modified) elaboration meeting slides for the
[infrastructure portion on Google
Docs](https://docs.google.com/presentation/d/1U36N6la82nIPTDrgkKn9A8BpZ50Y5wb_rgJ-j26ahDM/pub?start=false&loop=false&delayms=30000)
and the [workflow portion as deck.js
slides](http://blog.jasonantman.com/GFX/puppet_workflow.html).
