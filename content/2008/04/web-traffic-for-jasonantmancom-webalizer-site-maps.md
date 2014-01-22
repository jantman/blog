Title: Web Traffic for JasonAntman.com - Webalizer, Site Maps
Date: 2008-04-22 15:52
Author: admin
Category: Projects
Tags: bacula, bandwidth, connectivity, ISP, Nagios, webalizer
Slug: web-traffic-for-jasonantmancom-webalizer-site-maps

I've been working on the design of a town council campaign site for a
friend - [www.mikennick08.com][]. It's hosted by an additional Apache
vhost on my personal server (and running off of port 10015 - ugh). I
setup [Webalizer][] for him, so I figured I'd give my own webalizer
installation a check. Wow - 30,215 hits this month alone. That reminded
me of a problem with my ignored hosts - 17,600 of those hits were
Googlebot, and another 2,065 were Yandex (a Russian search engine).

Amazingly, though, it seems like Google is only indexing my blog. My
precious wiki seems out of whack, not to metion my CVS repository.

So, this reminded me of two long-overdue tasks:

1.  Get webalizer to properly ignore the common bots.
2.  Get sitemaps of my entire site.

So, off to the races!

First, I added Googlebot, Yandex, and a few others to webalizer.conf
with IgnoreAgent directives. Then, after clearing out my entire output
directory - and waiting a LONG time for it to run - bingo! Real stats.
Down to about 8000 hits for the month, which seems more logical, even
including the \~2,000 hits from Google feedfetcher.

Next stop was sitemaps. It tooks some PHP magic to hack apart the
MediaWiki sitemaps, put in the correct URLs (it was showing an
internal-only hostname), and drop all that and my Blogger rss.xml in an
index file. It's now 2 AM, and it just crashed and burned - the PHP
script worked fine, but for some reason my entries in
sitemaps\_index.xml - which pointed to sitemaps in a subdirectory - came
back with errors. Well, something to work on tomorrow.

This morning I checked my backups and noticed that nothing had run in 3
days. It turns out I just had one failed job holding everything up. And
I screwed up - I was home this weekend and forgot to swap tapes. It'll
be another 2 weeks before I can. But, I took the time to setup a backup
status box on my administrative portal (more on that later) and will
also be revising my apparently ineffectual Nagios check script.

On a few side notes: First, I'm seriously thinking of dumping Verizon
FiOS. While I really like the service, their static IP (business)
variant is $100/month for 15 Mbps down / 2 Mbps up, whereas
Cablevision's Optimum Business with static IP is $55/month for 30 Mbps
down / 5 Mbps up!

Most of the previous projects have been put on hold for the time being
(mainly because of impending final exams at school) - the new Gigabit
Ethernet switch for backups, testing Zenoss and upgrading monitoring (to
a new product or Nagios 3), etc.

  [www.mikennick08.com]: http://www.mikennick08.com/
  [Webalizer]: http://www.mrunix.net/webalizer/
