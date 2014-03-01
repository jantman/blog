Title: Metrics Part 1
Date: 2013-03-06 21:24
Author: admin
Category: Ops
Tags: diamond, graphing, graphite, metrics, monitoring, munin, statsd
Slug: metrics-part-1
Status: draft

At work we're currently in between metric collection and display
(graphing) tools. We've got [munin](http://munin-monitoring.org/) on its
way out (but still largely responsible for collection via munin-node)
and [graphite](http://graphite.wikidot.com/)/carbon/whisper on its way
in for storage and display/graphing. But we've yet to fill the void for
data collection. We have a few ideas for specific areas (as we're a
python shop, we seem to have decided on
[Diamond](https://github.com/BrightcoveOS/Diamond) as the munin-node
replacement, and we're pretty sold on
[statsd](https://github.com/etsy/statsd/) to push to Graphite), but
there are still a number of slots that need to be filled. And as such,
we're starting to amass a bunch of shell and Python scripts pushing data
to Graphite every minute (or 30 seconds), just so we can get something
better than Munin.

So, I thought I'd take a few minutes to outline some of my thoughts on
the topic. I've [written about similar topics
before](/2012/09/project-storing-and-analyzing-apache-httpd-logs-from-many-hosts/),
and even if you're one of the people who doesn't really buy into the
whole [monitoring sucks](https://github.com/monitoringsucks/blog-posts)
camp, there are
[a](http://lusislog.blogspot.com/2011/07/monitoring-sucks-watch-your-language.html)
[lot of](http://lusislog.blogspot.com/2011/06/why-monitoring-sucks.html)
[really](http://obfuscurity.com/2011/07/Monitoring-Sucks-Do-Something-About-It)
[good](http://jedi.be/blog/2012/01/03/monitoring-wonderland-metrics-api-gateways/)
[posts](http://www.devco.net/archives/2011/03/19/thinking_about_monitoring_frameworks.php)
about monitoring and metric collection out there. And I'm sure there are
a few that suggest a specific solution, but this is obviously something
we have to explore on our own - and working for a mostly Python shop
adds an incentive to not just use the newest, coolest thing written in
Ruby or Node.

## What I Already Know

I know we're using [Graphite](http://graphite.wikidot.com/) (and
carbon-cache) for storing and displaying data. We like it, we're already
using it, it's written in our strongest language, and it's cool. We
might investigate alternate web front-ends (the current one, admittedly,
could use more than a little work). We're also going to be using
[Brightcove's Diamond](https://github.com/BrightcoveOS/Diamond) as a
collector, likely to replace munin-node; however, it's not known how
many of our metrics will actually pass through Diamond, and what other
collector(s) we may or may not have.

## Identifying the Problem with Collection

We know that we want metrics and event data from, in the simplest terms,
as many places as possible. Disk is cheap and it's better to have unused
historical data than have no data on a metric when you need it.  
3 sources of metrics:  
- code that's ours and can send metrics natively  
- code that's not ours, but can either be modified to send metrics
natively, or will return metrics via a programmatic interface (command
line, JSON, XML, etc.) that can be easily grabbed and shipped elsewhere  
- stuff other than the above, that requires parsing of log files,
screen-scraping HTML or similar "ugly" ways of extracting metrics
