Title: Leap Year Windows Azure Cloud Outage
Date: 2012-03-20 18:12
Author: admin
Category: SysAdmin
Tags: azure, microsoft, outage, release, testing, windows
Slug: leap-year-windows-azure-cloud-outage

I haven't talked about Microsoft in quite a while (mainly because I
don't follow mainstream tech news as much anymore), but I happened by a
very interesting [post on the Windows Azure
blog](http://blogs.msdn.com/b/windowsazure/archive/2012/03/09/summary-of-windows-azure-service-disruption-on-feb-29th-2012.aspx)
the other day. It's a very detailed postmortem of the major outage of
the Windows Azure cloud service which occurred from 4:00 PM PST on
February 28<sup>th</sup> through 2:15 AM on March 1<sup>st</sup>. Before I get into any of
the details, I should say that it really is a nice, well-done post. And
the fact that they're willing to do such a detailed, public postmortem -
and admit the failures that they did - is a step in the right direction
for Microsoft (a company that I don't particularly care for, to put it
lightly).

I'm going to glance over the majority of the post, though I highly
recommend that anyone interested in running web-scale services,
specifically highly available ones, read it. The general overview
(really just the points that are germane to my discussion) is as
follows: An agent running inside the guest VM instances (i.e. domU)
communicates with a counterpart on the host OS (i.e. dom0) over an
encrypted channel, authenticated by certificate. The certs are generated
and passed from the guest to the host when the guest instance is first
initialized, which means when an app is first deployed, scaled out, OS
updated, or when an app is reinitialized on a new host. This cert was
generated for a 1-year validity period, by adding 1 to the integer year
- hence, the generation process failed on February 29th of a leap year,
as the cert end date wasn't valid. When the cert generation failed, the
guest agent essentially stopped cold. The host agent waited for a 25
minute timeout, then re-initialized the guest and started over. After
three of these failures, the host assumes there's a hardware error
(since the guest would have reported a more specific error otherwise),
declares itself in an error state, and tries to move its current
workload over to another host. Which re-initializes the guests on that
host, thereby causing a chain-reaction of failures in this case. Skip
forward the 2-1/2 hours it took them to identify the problem, and
further 2-1/2 hours to get a fix ready. They fast-tracked their fix to 7
clusters that had already been in the process of a software update, but
ended up with those clusters in an inconsistent state with
incompatibilities between the guest and host networking subsystems,
bringing down previously-unaffected instances on these clusters.

This whole scenario offers a few important points on both the
development and operations sides:

**Inputs need error checking, and errors need to be raised.** So the
first problem here was the failed cert generation. I'll leave alone the
fact that, in my opinion, doing math on a the integer year of a date is
a high school or college programming mistake, and never should have been
made by someone doing platform coding for a major company (believe it or
not, 25% of years are leap years </sarcasm\>). If whatever code was
generating the cert was smart enough to check the cert end date validity
and error out, that error should have been pushed up the stack to
somewhere where it could be handled - or, at least, sent to a central
log server that does error trending.

**Secure communications when provisioning need an insecure error path.**
This is somewhat connected to the previous point. If the normal process
of creating a new instance and communicating errors up the stack relies
on certs and authentication or encryption, there should be some method
of communicating errors with *that* process either up the stack, or to a
separate event correlation/trending system. Errors with a
certificate-based system are not unusual, and even something as simple
as a vastly incorrect time set on the guests could have caused this same
problem. In environments where management/control communication between
levels of a system are encrypted or authenticated, there should be some
way for lower levels of the system to deliver a meaningful error message
"somewhere". Even if this is just a syslog server or web service that
listens for errors and can escalate a warning when the numbers spike,
it's a useful alarm and debugging tool.

**Autonomous systems shouldn't lightly assume hardware failures.** It's
arrogance for a host system to assume that just because it can't
instantiate new guests, a hardware failure exists. This entire incident
is a perfect example that, at least if hardware error indicators are
properly monitored, it's more likely for a software problem to be
falsely identified as a hardware problem than the other way around. All
of my points are somewhat related, but I can think of many more reasons
why a new guest can't be instantiated that are software-related rather
than hardware-related.

**Autonomous control mechanisms need historical trending, and need to
call for help if this looks wrong.** These host systems tried to
instantiate new guests three times, waiting 25 minutes in between, and
then declared themselves bad and tried to migrate guests to other hosts.
From what I understand, Microsoft got it right in having a "kill switch"
that prevented further migration of guests. What they didn't have right
was reporting of autonomous actions (guest migration) to a central
location that performs trending. The 25 minute timeout with three
attempts is a great safety feature, but if the status of guest creation
actions was reported to a central server, it would have been much more
quickly apparent that 100% of guest creations in the past, say, 10
minutes, had failed - across all clusters. I know plenty of shops that
do little, if any, real-time analysis and historical comparisons of
their log data. But when systems are designed to perform self-healing
and autonomous actions, it's imperative that these actions are tracked
in near-real-time, compared to historical averages, and that deviation
from a baseline is identified and escalated to humans.

**Release procedures are more, not less, important when the sky is
falling.** The extended downtime of the last seven clusters was because
of an improperly QA'ed update that was pushed out bypassing the normal
release and testing procedures. As a matter of fact, it was so poorly
QA'ed that the update totally broke networking for the guest VMs, and
was still pushed out. I'm sure this was more of a management/executive
decision than one made by the actual engineers, but organizations (even
management) need to understand that when the sky is falling, services
are down, and everybody is stressed, it's *more* likely for mistakes and
oversights to happen, and this is when a proper, well-documented QA and
release procedure (including phased rollout) is *most* important.
Failure to follow these procedures results in exactly what happened in
this case - making an already bad problem much worse.

Even *I* can't blame Microsoft specifically for all this (though the
whole thing would have been avoided if they just represented timestamps
as integers like the rest of us...), but it is a good opportunity for us
all to learn from a major incident at a "pretty well known" company.

release procedures are most important when things are already going
wrong
