Title: Dealing with unplanned downtime - productively
Date: 2009-09-17 12:50
Author: admin
Category: Miscellaneous
Tags: sysadmin, time management
Slug: dealing-with-unplanned-downtime-productively

While I've read and really appreciate [Tom Limoncelli][]'s [Time
Management for System Administrators][], the current state of my life
(mainly that it's split between work, personal projects, a freelance
client, administering the systems of a the [ambulance corps][] and real
people, and that my "work day" is whenever I'm awake) has prevented me
from really implementing most of the advice. However, I do try to be as
productive as I can.

Without getting into details, a few weeks ago, $WORK suffered a major
electrical failure that required everything in the data center to be
powered down. This happened around 10:30 AM, and the majority of groups
simply powered down their machines and left, planning to return around 2
AM (the estimated power restoration time). After getting our machines
down and stopping for pizza, I remembered how much of a pain it was to
work in the racks bringing everything down. While my group only has two
racks, we've had a lot of changeover lately, and the cabling had gotten
quote messy. Noting this, I mentioned it to my two higher-ups,
remembering that we had a stock of assorted length patch cables. We were
able to make an "emergency" run to our cable vendor and pick up a box of
1- 2- and 3-foot power cables.

While everyone else was home or in their offices dodging the pieces of
falling sky (everything was down including VoIP and mail), we were the
only group getting real productive work done in the data center. The
power failure, rather than a catastrophic event, was a great opportunity
- the only time we could pull *every* cable in a production rack and
re-do all power and patches.

So, here's my SA tip for the day - everyone has some big projects that
they'd like to do, require downtime, but aren't critical enough to
schedule something. So, keep a list of these and have the parts on hand.
Whether it's a "just in case" hardware swap-out, re-patching, or
anything else, eventually you (depending on the environment that you
work in) might have one of those times when the solution to the problem
is out of your hands and there's nothing else to do. Use this time
productively.

  [Tom Limoncelli]: http://whatexit.org/tal/
  [Time Management for System Administrators]: http://www.amazon.com/o/ASIN/0596007833/tomontime-20
  [ambulance corps]: http://www.midlandparkambulance.com
