Title: What is System Administration?
Date: 2010-04-24 09:08
Author: admin
Category: Miscellaneous
Tags: sysadmin, system administration
Slug: what-is-system-administration

I was recently reading an interesting article, "from tasks to
assurances: redefining system administration", by [Alva L.
Couch](http://www.cs.tufts.edu/~couch/), in the April 2010 issue of
[;LOGIN:](http://www.usenix.org/publications/login/). He makes a lot of
good points, mainly that system administration has been defined by
tasks, but should really be defined by assurances (a much more abstract
concept). This does make a lot more sense, and perhaps will aid me in
finally coming up with a succinct (but complete) answer for when people
ask me what I do.

It bears mention that my role as an SA probably isn't the same as many
others. Working at a University has its perks - and one is definitely
the inclination towards research, tinkering, and trying new things.
Another is the extremely tight budget - I'd estimate that only about 25%
of what my group supports (software-wise) actually has a vendor behind
it. Most of those services have primary admins assigned to them.

The group I work in is composed of 9 people (including myself). We're
responsible for the architecture (specifically authentication,
network-side stuff) for residential/dorm networking (ResNet), all of the
student computing labs (\~1,000 user stations) as well as printing
therein, the University-wide wireless network (from physical
installation through support), and a few other services. That doesn't
include all of the usual ancillary stuff - mail, DHCP, web apps,
storage, etc. It would probably surprise most corporate IT types that we
more or less function as an independent unit - we share certain
services, like Nagios monitoring, with other groups, but do most of our
work as a single standalone unit.

My own job (since I'm currently the only part-time person in our group)
is probably *very* different from most SAs. I'm the primary admin for
only one user-visible service, which is in the process of being phased
out (and is very lightly used currently). For the most part, I'd
describe myself as a "floating" admin - I'm usually assigned whatever
problems come up that are in my knowledge area (or more than the primary
admin can cram into a work week), and also do quite a bit of research
(mainly suitability analysis of new technologies). I'm also the DR guy,
and am in the process of implementing across the board an automated
installation, configuration, recovery and backup system for all of our
Linux/Unix boxes. As ironic as this may seem, while I'm not the primary
admin for any of our major services, if one of the boxes than run them
falls over, it's more or less my responsibility to get it back up and
running. Or at least have the plans and procedures for that laid out.

Something that is also quite different from many enterprise shops is our
software budget - which is almost non-existent. Except for a few
services - some of the stuff used to administer the Windows and Mac lab
machines, the printing systems, and the wireless stuff, we're pretty
much exclusively open source. As a result, there's rarely a vendor to
fall back on, and "fixing a problem" can often involve hours of reading
source.

> As an aside, I once had a phone screen where the interviewer asked me
> about a difficult problem I recently solved, and what my methodology
> was. I ran through about 20 steps. When I finished the list, the
> interviewer asked me, "at what point would you call the vendor for
> support?" My response: "vendor? what vendor?"

So I'm trying to think up a good answer to what I do, and what the other
SAs in my group do. There's the work in progress so far:

> We provide many different services to our users (all University
> faculty, staff, students, etc.). It's my job to ensure that those
> services are as reliable as possible, function correctly, are secure,
> and work as well as possible. When something does fail, no matter what
> it is, it's my job to get it back to normal. And when a new technology
> emerges that may increase the quality, reliability or security of a
> service we offer, it's my job to evaluate it and, if it is found to be
> worthy, implement it.
