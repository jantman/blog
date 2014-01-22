Title: Inaccuracies in Google Analytics for Website Stats
Date: 2012-03-17 11:46
Author: admin
Category: Miscellaneous
Tags: analytics, google, logging, statistics, stats
Slug: inaccuracies-in-google-analytics-for-website-stats

I use Google Analytics for visitor stats on this blog. Not because I'm
trying to direct-market to my readers or become Big Brother, but for a
number of simple reasons:

-   It's simple - no software for me to update, and nothing that needs
    to run on my server and read through giant log files every night.
    Google does it all for me.
-   It gives a lot more information than I can get from just web server
    logs.
-   Because of Google's "big brother" tracking, and the vast number of
    sites that they track people on, I can tell things I'd have no other
    way of knowing, like how long someone stayed on my page.
-   They tell me *useful* stats like which search keywords brought the
    most people to my site and which posts are the most popular, which I
    keep in mind when writing new stuff and updating older posts.
-   They tell me information about client operating system and browser
    version, which I think tells quite a bit about my audience.
-   As far as I know, they're pretty good at filtering out anything
    other than an actual human visitor.
-   They tell me stats that have no real use to me, but are just cook -
    like what countries my visitors are from, what type of Internet
    connection they're on, their screen resolution, etc.

Obviously not for google, but for me, all of these stats are totally
anonymous - I just get percentages or numbers of visits, it's not like I
can see all of the details per-IP address. The most important aspect to
me is just the ease of use - I sign up and put a little snippet of code
on my pages, and I get an amazing dashboard interface with all of this
information. Nothing to install and update on my server, and (most
importantly, since I'm now running everything of mine on one virtualized
server) no massive program to run as a cron job that has to read all my
server log files.

Last week I was talking with a couple of my co-workers, specifically
about the stats that I get from Google Analytics. While I know it's not
uncommon to run [NoScript][] especially among the more security- and
privacy-conscious groups of people, I was a bit disturbed to hear that
they all block Google's tracking code in their browsers via NoScript. I
assume there's also a percentage of people who still just turn off
JavaScript alltogether (although I can't imagine how they use the modern
Web), and many who use the [Google Analytics Opt-Out][] feature. So,
especially with as technical an audience as I have, I guess that means
I'm likely missing a large number of visitors in my stats. On one hand,
I want to respect the privacy of my visitors, and respect their desire
to opt-out of advanced tracking. On the other hand, since I no longer
parse web server logs for statistics, these privacy-conscious visitors
aren't even showing up in what I think of as my monthly visit count, or
in my information on what posts and search keywords are most popular,
which I only use for "good" purposes - to make my blog more useful. So
that's a bit of a conundrum.

I'll admit that I do run [Google AdSense Ads][] on my blog, and I'm sure
there are some people who block the ads. On one hand, that upsets me a
bit; I run this blog to try and share information that I find or learn
with others, and the hosting costs aren't insignificant. If I can get
paid to just show some ads, to try and help offset the cost of running
the site, I think that's good. And if other people can help support the
site by just letting the ads stay on the page, why not? On the other
hand, my hosting costs $50/month (granted the server also handles all of
my email, and a *whole bunch* of other sites). I've been participating
in Google AdSense since March 5, 2010 (two years and two weeks), and my
"estimated earnings" are currently $80. The payout is in $100
increments. So, I haven't seen a cent from it in two years, so I've
given up being concerned with it. If you want to be nice, and find my
posts interesting, click on one of the ads. Unfortunately, unless I get
famous, the ads aren't going to come close to offsetting even part of
the cost of running the site.

Google itself [says][], "In order for Google Analytics to record a
visit, the visitor must have JavaScript, images, and cookies enabled for
your website." There seems to be some buzz about this on the 'net, and
I've seen [a][] [number][] [of][] (translated; [original post in
Dutch][]) posts advocating building a request to a Google Analytics GIF
manually on the server side, and then including it as an image element
inside a `<noscript>` tag in the page. While this is probably one of the
nicer solutions (and much more likely to reduce double-counting), it
doesn't capture any of the advanced data (screen resolution, etc.) that
JavaScript-based Analytics does, and more importantly, I imagine that
many of the Ad blocking extensions also block traffic to
google-analytics.com, so this is an incremental improvement at best.
There are also [quite][] [a][1] [few][] posts about how to make a
request to Analytics purely server-side. This has a few disadvantages as
well; it bypasses the google domain blacklisting problem that the
client-side image has, but it also means you lose the client IP address
(and therefore geolocation), and that you double-track any user who
allows javascript (so you need a separate profile, and then need to
average out the results). It also means that you track every search
engine and bot that crawls your site, and possibly every person who
clicks a link and then hits "back" before the page finishes loading. I
found another blogger who [commented about][] the wide disparity he saw
between Google Analytics, the [StatsPress][] WordPress plugin, and
[AWstats][] (a server-side log file analyzer).

**So what's the solution?**

Most of the options have a down side, but I'm looking for something
that's the best I can reasonably do. As much as I'd rather not, I'm
going to look into self-hosted alternatives to Google Analytics (a
self-hosted JavaScript-based stats provider), in the hopes that NoScript
users will be more friendly to scripts coming from my own domain, and
sending requests to my own domain, than ones from Google or other major
trackers. I don't think I want to try anything that parses web server
logs as a primary approach, as I don't think I could ever get a
meaningful comparison to Google Analytics or something else
JavaScript-based.

I did have one other idea which I think is interesting, though a bit of
an overhead. I could have Apache (or, more likely, a Perl script called
in the Apache configuration) generate a random string for each request,
and save it in an Apache environment variable. The environment variable
would then be added to a field in the server logs, and also added (via
PHP or whatever else generates the pages server-side) as a custom
parameter for the JS tracking code, enabling page hits to be correlated
between the JS tracking and the server logs. Assuming the JS tacking
backend stores its data in a sane format (and as raw data, not just
aggregated), and at the cost of a serious performance penalty, a
server-side statistics program like [AWstats][] or [Webalizer][] could
be patched to lookup the unique identifier in the JS stats data store,
and ignore all hits which were tracked that way.

I'm going to start by looking into self-hosted open source alternatives
to Google Analytics, which I'll post about sometime hopefully soon.

  [NoScript]: http://noscript.net/
  [Google Analytics Opt-Out]: http://tools.google.com/dlpage/gaoptout?hl=en
  [Google AdSense Ads]: https://www.google.com/adsense/
  [says]: http://support.google.com/googleanalytics/bin/answer.py?hl=en&answer=55610
  [a]: http://garmahis.com/tips/google-analytics/#use-Google-Analytics-without-JavaScript
  [number]: http://djangosnippets.org/snippets/2338/
  [of]: http://translate.google.com/translate?hl=en&sl=nl&u=http://andrescholten.nl/google-analytics-zonder-javascript/
  [original post in Dutch]: http://andrescholten.nl/google-analytics-zonder-javascript/
  [quite]: http://www.vdgraaf.info/google-analytics-without-javascript.html
  [1]: http://blog.datalicious.com/google-analytics-without-javascript-rss-xml-e
  [few]: http://blogs.walkerart.org/newmedia/2009/11/12/building-walkers-mobile-site-google-analytics-without-javascript-pt2/
  [commented about]: http://www.realityburst.com/battle-of-the-inaccuracies-how-accurate-is-google-analyticsawstatsstatpress
  [StatsPress]: http://wordpress.org/extend/plugins/statpress/
  [AWstats]: http://awstats.sourceforge.net/
  [Webalizer]: http://www.webalizer.org/
