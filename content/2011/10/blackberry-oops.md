Title: Blackberry Oops
Date: 2011-10-13 22:20
Author: admin
Category: Miscellaneous
Tags: blackberry, outage
Slug: blackberry-oops

If you've been following the tech news lately, you've probably heard at
least a bit about the [massive][] [blackberry][] [outage][] over the
past three days. While yes, it's the first truly grand failure of RIM's
infrastructure in their 12-year history, it's also a wonderful case
study.

Apparently the outage started Monday morning with RIM infrastructure in
Europe, the Middle East and Asia. However, by Wednesday, it had become a
global outage/slowdown of BlackBerry infrastructure (specifically the
parts that go through RIM - email, web browsing, and BBM; voice calls
and SMS/MMS were unaffected). With BlackBerry's market share falling,
Android's rapidly growing (and Android slowly becoming a viable
enterprise option), and the launch of the iPhone 4S just around the
corner, the timing of this couldn't be worse for RIM.

RIM's original [statement][] about the problem, at 21:30 on Tuesday
October 11th, was,

> The messaging and browsing delays that some of you are still
> experiencing were caused by a core switch failure within RIM’s
> infrastructure. Although the system is designed to failover to a
> back-up switch, the failover did not function as previously tested. As
> a result, a large backlog of data was generated and we are now working
> to clear that backlog and restore normal service as quickly as
> possible. We sincerely apologise for the inconvenience caused to many
> of you and we will continue to keep you informed.

I haven't been able to find much more technical information than that -
a [CNET article from Tuesday][] goes into as much depth as anything I
could find. I did find one mention (misplaced the link) that the core
switch in question uses technology from "multiple vendors". So what
follows is part common sense (for me... why not for a multi-national
corporation?) and part speculation. If you're unfamiliar with RIM's
architecture, the pertinent points are that all Internet-bound traffic
(browsing, email, and BBM) is piped through RIM's data centers, where
it's encypted and who-knows-what-else'ed (perhaps [monitored][]) before
going back out onto the 'net. In the Enterprise market, their big claim
is encryption/security, and monitoring/management/policy enforcement on
handsets.

First main point: RIM is a *big* company. The thought that they rely on
an (apparently custom) core switch - a *single* core switch for multiple
*continents* - is amazing. It's even more amazing that they'd let such a
large part of their infrastructure ride on an architecture with,
apparently, an untested failover mechanism. Of course I don't know all
the details, but I'd hope that for a single piece of hardware which is
so critical, they'd a) have a cold spare physically nearby so a
replacement wouldn't take a day or two, and b) if they can't do an
online failover test, at least have a full lab environment to test the
failover in.

Second main point: Their big claim through all of this is that they
didn't lose any data - email, BBM, etc. - it just got delayed. So if
there was a core switch failure in their data center serving EMEA, and
the next day global services slowed to a crawl, the only thing that
comes to mind to me is a waterfall; EMEA went down, and they started
rerouting traffic to their North America data center. The increased load
- probably a disaster recovery plan they never truly tested or even
planned - brought everything to a screeching halt, and caused them to
resort to simply caching messaging and pushing it out bit by bit as the
infrastructure could handle. Oops.

So what are my (admittedly poorly-informed) thoughts on this?

1.  Scaling out works. Scaling up - especially with single points of
    failure, or N+1 redundancy - is dangerous. If RIM had scaled out and
    used regional data centers, with a close-to-commodity core and as
    much redundancy as possible, this wouldn't have happened. Sure,
    infrastructure costs money. But if that one "core switch" had been
    1,000 devices spread across multiple racks in multiple data centers,
    this never would have happened. And the devices would be
    comparatively cheap enough to probably keep spares on hand too. And
    regularly test their failover procedures. To all of the big
    businesses (apparently like RIM) who still think that big iron is
    the only way to do things right... maybe it's time to take a hard
    look at that, and compare your architecture to that of the modern,
    new, hip giants like Google and Facebook. Grids and clusters. Nodes
    that can fail without anyone blinking. Scaling out might not fix
    every problem, but having half the world on a single core switch
    with N+1 redundancy probably isn't smart either.
2.  Disasters need to be planned for. Every possible contingency needs
    to be planned for. Plans need to be tested, regularly. If your giant
    core switch goes down and the failover doesn't "function as
    previously tested", there's a serious problem both in your disaster
    planning, and in your validation and test procedure. If you have
    half of your customer base riding on a failover plan that isn't
    *regularly* tested or otherwise validated, that's bad. While I can
    argue that the whole architecture - given this massive point of
    failure - could stand to be re-thought, the real issue here is with
    test/validation methodologies and procedures. For a company with 70
    million users, having a piece of infrastructure this critical fail,
    and the failover 'not work as tested' is a very serious issue.
3.  Damage control is important. As I said, I can only imagine that the
    severe service degradation outside of EMEA was due to rerouting data
    from EMEA to the remaining functional data center(s). Such a
    solution should only be considered if it has been tested, or at
    least has engineering validation. If it was part of the disaster
    recovery plan, it obviously isn't actually a suitable solution, and
    served only to increase the scope of the outage. If it wasn't part
    of the disaster recovery plan, and was decided on-the-fly, someone
    really didn't do their research and engineering before putting the
    fix in place. A workable solution should have been planned ahead of
    time. And if one wasn't, it's very bad practice - this outage shows
    the results - to put in place a fix that hasn't been thought out.

For a company whose business is so telecom-focused, this seems like a
glaringly bad design that shouldn't be acceptable in a telecom.

  [massive]: http://www.cnn.com/2011/10/12/tech/mobile/blackberry-outage/
  [blackberry]: http://abcnews.go.com/blogs/technology/2011/10/blackberry-outage-spreads-to-u-s/
  [outage]: http://www.nytimes.com/2011/10/14/technology/rim-struggles-to-overcome-blackberry-outages.html?_r=1
  [statement]: http://www.rim.com/newsroom/service-update.shtml
  [CNET article from Tuesday]: http://www.computerworld.com/s/article/9220736/RIM_global_outage_caused_by_core_switch_failure_fix_under_way
  [monitored]: http://online.wsj.com/article/SB10001424052970204612504576608561811929654.html
