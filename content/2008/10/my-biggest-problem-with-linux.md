Title: My biggest problem with Linux
Date: 2008-10-27 15:27
Author: admin
Category: Miscellaneous
Tags: linux, patch management, solaris, updates, upgrades
Slug: my-biggest-problem-with-linux

__Update / Notice:__ This post was written in 2008. The world has
changed since then. A lot. We have good, easy configuration management
like Puppet, Chef, etc. (which, in fact, I
[use to manage my desktop and laptop](https://github.com/jantman/workstation-bootstrap))
and, more importantly, creating and destroying servers can be done in
[seconds](http://aws.amazon.com/cloudformation/) rather than hours.
In short, in my opinion, this post is a rant about a problem that no longer
exists. If you're still thinking of things the way this post does, you're
doing it wrong.

For one of my wonderful classes, Internet Security, I'm doing a
presentation on "patch management". While I'm obligated to cover Windows
- and, of course, will talk about MacOS - I'll obviously be spending a
good deal of time on the Unix/Linux side of things. This has gotten me
thinking about one of my biggest problems with Linux (and specifically
[OpenSuSE](http://www.opensuse.org), my usual default distro. Patch
management is utterly awful.

Here's the problem: I have about a dozen machines under my control. I
need to keep them all up-to-date. Currently, I manually do patches and
upgrades via YaST or zypper. I thought about scripting this through
zypper, but that doesn't make any sense - the packages on the machines
are far from homogenous, so there's no clear way to make one script that
updates them all. I considered using Puppet or CFengine or something of
that sort, but that's too heavy-weight for me - for only a dozen
machines, many of which are personal or development only, that's a lot
to keep track of by hand, and a lot of work defining which patches
should be applied, and which machines shouldn't be changed.

My other peeve is distribution upgrades. About three of my machines are
still running OpenSuSE 10.0 or 10.1, both of which are unsupported, and
no longer even have downloads available. Why? Becuase I've done major
OpenSuSE upgrades before, broken a LOT of stuff, and I simply can't risk
that on machines that can't stand extended downtime. This process
\*needs\* to be made easier. Bottom line - it should be made no more
difficult or unreliable than a kernel upgrade. IMHO, the biggest selling
point for Solaris is its' ability to do a total upgrade to a second
partition, and switch-over at runtime. Why doesn't Linux (or SuSE) have
this yet?

*What's my ideal solution?* A curses application that uses text-file
backends (curses so I can run it over SSH even if I have a slow link or
high latency, like from a SSH session on my cell phone, if need be). The
app would allow me to list all of the machines I want managed. It would
connect to the machines over standard SSH, and would leave an extensive
audit trail of what's done, both on the management console and on the
machines (as well as running as a dedicated user). The application would
maintain an inventory of all of the packages on every machine. It would
check daily for new patches/updates to any of those packages, and e-mail
me a daily summary of what's new, including all dependency changes, and
which machines need the update. It would also allow me to define, on a
per-machine (or per-group-of-machines) basis, rules for packages that
must stay at their current version - i.e. I have a bunch of PHP4 apps,
so machine X needs to stay at PHP4. The e-mail summary would include any
packages that aren't going to be updated for a specific machine because
of dependency/version rules, as well as warnings about any new packages
that have a dependency that has a rule set. I could then run the main
curses app on my admin machine and, starting from NO selections, select
which updates I want to apply and whether I want to ignore or create new
rules to keep something at its current version, on a per-machine or
per-group basis. This curses app would generate a file (XML?) of what to
do (which would also be generated or edited by hand, easily). The XML
file would then be fed into a script that downloads all of the needed
packages to a central (local) mirror (or, optionally, for remote
machines, has them download locally on the machine), checksums them, and
then installs them (running commands over SSH) on all applicable
machines. It would then keep a log of all changes, both on each machine
changed (in a master changelog file) and on the central administrative
machine. **Most importantly**, the curses interface would have a simple,
quick way to back out any specific update or group of updates for all
machines, a group of machines, or one machine. All data needed to back
out a change would be kept on each machine (say, cleaned up at the next
update of that package and all of its' dependencies) with
machine-readable instructions kept in a central file, allowing local
rollbacks - i.e. a machine goes down, I realize that it was because of
an update to package X, and on the local machine I can check the
changelog, see an entry like "Package X updated 1.0.0 to 1.0.1 on
yyyy-mm-dd, Change ID 1234" and then, to rollback, simply issue a
command like "patchmgt rollback 1234" on the effected machine.

Just some ideas, and a little rant.
