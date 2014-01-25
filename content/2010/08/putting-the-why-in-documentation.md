Title: Putting the Why in Documentation
Date: 2010-08-06 14:51
Author: admin
Category: Miscellaneous
Tags: documentation, sysadmin
Slug: putting-the-why-in-documentation

I work as a Linux Sysadmin (among many other non-official titles) in a
small group that mainly provides services. We run wireless and student
computing labs across a whole campus, but other than that (and most of
that) is just back-end systems - web servers, RADIUS, DHCP, etc. As a
result, I write no end-user documentation. I generally think of this as
a blessing, since the people who read my documentation are people who
think (more or less) like me.

However, I've just started writing the wiki page for a rather large
system I developed. And in writing the docs, and thinking about what was
missing from the (practically non-existent) documentation on the system
I was replacing, it got me thinking a lot about the documentation
writing process. Most of us have heard that there are two general types
of documentation - end-user docs and developer (and I'm rolling SysAdmin
in here) documentation. End-user docs tell someone how to use what we
built. Developer docs tell people how to troubleshoot, fix, modify, and
extend it. Usually.

But there's one very important piece that's missing from most
developer-level documentation I've read: why it's built the way it is.
Sure, this isn't applicable in all instances. This is obviously ignored
by closed-source software developers when writing documentation for
release. And I'm sure it's ignored in some larger shops just out of fear
that the interns will explain why they need to iterate a database result
set. But for those of us who are designing and building systems, I'd
argue that documenting the reasons behind our decisions is much more
important than how-to-fix-it or how-to-rebuild-it documentation. Sure,
it's atrocious practice, but that can all be gleaned from examining a
live system or backups. But when it comes time for the next person (or
you or I, five years down the road) to re-design or drastically modify
our creations, some documentation of the decisions we made - and the
reasoning behind them - will be extremely useful.

Case in point: My latest project started as performance analysis of a
large DHCP server using the [Masney LDAP
patch](http://personal.cfw.com/~masneyb/) to [ISC
DHCPd](http://www.isc.org/software/dhcp). After over a week of
performance testing and trying different configurations and theories
(all of which I "documented" in my text file lab notebook), we ended up
deciding to totally remove LDAP from the system, move to configuration
files generated from MySQL, and keep everything (including the logs) in
ramdisk. We found performance bottlenecks in both the LDAP communication
and disk IO. We have the performance test output to prove it. We have
the results of dozens of tests with different configurations, as well as
a number of problems we identified with the LDAP patch. And from
testing, we have a handful of issues identified and fixed in the new
system, whose fixes aren't exactly intuitive.

The previous system had pretty poor documentation, but even worse, it
was only functional documentation - what the system does, and how it
does it. There was no discussion of why the parsing script disregarded
lines with a certain string in them, why the daemon is restarted every
night, why LDAP was chosen in the first place, or any performance
metrics (so we had no original as-intended baseline to compare against).

So for those of you designing systems and documenting them (you \*do\*
document them, *right*?), please include **why** in your documentation.
The next time someone needs to fix or tweak or re-engineer the system,
they'll be able to figure out what happens on line 123 of the init
script themselves. But it might take them hours to figure out *why* it's
done, or *why* it's done *that way*.
