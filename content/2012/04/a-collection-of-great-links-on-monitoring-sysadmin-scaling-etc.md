Title: A Collection of Great Links on Monitoring, SysAdmin, Scaling, etc.
Date: 2012-04-21 10:24
Author: admin
Category: Miscellaneous
Tags: amqp, etsy, facebook, limoncelli, links, mongodb, monitoring, monitoringsucks, netflix, sensu
Slug: a-collection-of-great-links-on-monitoring-sysadmin-scaling-etc

I've had a bunch of tabs open in my browser for a while - stuff that I
read, thought was wonderful, and wanted to comment on. At risk of
letting it pile up forever, here's a collection of links that I thought
were really interesting or insightful...

-   [MongoDB is Fantastic for Logging][] - I was looking into some log
    storage ideas, and came by this post (on the MongoDB blog) about why
    Mongo is well-suited to storing logs.
-   [Sensu][] - a Ruby-based cloud-oriented monitoring system. It uses
    AMQP/RabbitMQ to communicate between the clients and server, which
    is a really big part of what I think monitoring should be.
-   [High Scalability][] - this is one of the few blogs I follow on a
    regular basis. Some really wonderful stuff, and great food for
    thought.
-   [Everything Sysadmin: Fear of Rebooting][] - A great article on Tom
    Limoncelli's blog about why we fear rebooting machines and why this
    is bad - moreover, why we should reboot often.
-   [The Netflix Tech Blog: Fault Tolerance in a High Volume,
    Distributed System][] - This is a *really, really* cool post NetFlix
    about how latency increases in a single subsystem can bring down
    their whole API in seconds, and how they combat this. Really cool
    stuff.
-   [Ars Technica - Exclusive: a behind-the-scenes look at Facebook
    release engineering][] - Ars Technical is more or less "mainstream
    media" to me, but this is a really interesting writeup on Facebook's
    release engineering process, albeit at a higher level. Specifically,
    it talks about their automation, phased rollouts, rollbacks, and how
    they release the Facebook codebase as a single giant binary, sent
    out via BitTorrent.
-   [Monitoring Sucks blog posts (github)][] - The "monitoing sucks"
    movement really speaks to me, having worked extensively with Nagios,
    Cacti, and similar technologies. Specifically, having rolled out
    monitoring in a variety of "weird" scenarios (a lot of monitoring
    devices or whole networks behind NAT, on dynamic IP connections, or
    otherwise unreachable from a central server), I've felt a lot of
    pain in the current want of doing things. There are a lot of
    **really** good thoughts linked here, especially the ["wonderland"
    series by Patrick Debois][] and the ["Latency sucks" series by
    Lindsay Holmwood][]. This really got me thinking about my ideal
    monitoring system, which among other things, would integrate the
    "alerting" functions of Nagios with graphing/trending and
    correlation, would be based on some sort of message queue
    architecture (that supports multiple levels of proxies that could
    gracefully support NAT and multiple hops), and would be configured
    almost totally on the originating "client" (unlike the pain of
    distributed Nagios/Icinga).
-   [Mike Brittain - Metrics Driven Engineering at Etsy (3.2MB PDF)][] -
    presentation slides. I'd *love* to see the video. Some really good
    ideas about putting the science back into being a SysAdmin. Also
    mentions a few tools I really want to play around with (including
    ganglia, graphite, logster and StatsD). Also mentions adding PHP
    memory usage and time to Apache logs, which I don't believe I never
    thought of.
-   Some really thoughtful posts from R. I. Pienaar on [Thinking about
    monitoring frameworks][] and [Composable Architectures][]. Some
    really good stuff, but what else would you expect from someone [like
    this][].

  [MongoDB is Fantastic for Logging]: http://blog.mongodb.org/post/172254834/mongodb-is-fantastic-for-logging
  [Sensu]: http://www.sonian.com/cloud-monitoring-sensu/
  [High Scalability]: http://highscalability.com/
  [Everything Sysadmin: Fear of Rebooting]: http://everythingsysadmin.com/2012/03/fear-of-rebooting.html
  [The Netflix Tech Blog: Fault Tolerance in a High Volume, Distributed
  System]: http://techblog.netflix.com/2012/02/fault-tolerance-in-high-volume.html
  [Ars Technica - Exclusive: a behind-the-scenes look at Facebook
  release engineering]: http://arstechnica.com/business/news/2012/04/exclusive-a-behind-the-scenes-look-at-facebook-release-engineering.ars/1
  [Monitoring Sucks blog posts (github)]: https://github.com/monitoringsucks/blog-posts
  ["wonderland" series by Patrick Debois]: http://jedi.be/blog/2012/01/03/monitoring-wonderland-survey-introduction
  ["Latency sucks" series by Lindsay Holmwood]: http://holmwood.id.au/~lindsay/2012/01/09/monitoring-sucks-latency-sucks-more
  [Mike Brittain - Metrics Driven Engineering at Etsy (3.2MB PDF)]: http://assets.en.oreilly.com/1/event/65/Metrics-driven%20Engineering%20at%20Etsy%20Presentation.pdf
  [Thinking about monitoring frameworks]: http://www.devco.net/archives/2011/03/19/thinking_about_monitoring_frameworks.php
  [Composable Architectures]: http://www.devco.net/archives/2011/04/04/monitoring_framework_composable_architectures.php
  [like this]: https://github.com/ripienaar/
