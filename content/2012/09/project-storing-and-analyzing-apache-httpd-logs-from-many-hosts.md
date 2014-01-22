Title: Project - Storing and Analyzing Apache httpd Logs from Many Hosts
Date: 2012-09-06 05:00
Author: admin
Category: Projects
Slug: project-storing-and-analyzing-apache-httpd-logs-from-many-hosts

I've recently started casual work on a side-project to collect, store,
and analyze apache logs from a bunch of servers - for the initial
implementation, I'm looking to handle about 15M access\_log lines per
day (that works out to 173 lines/second assuming an even distribution,
which there certainly isn't). Here is a selection of links that I've
been using for ideas and inspiration, both for the technical side (data
collection, transport, storage and analysis) and visualization:

-   [RRDtool - RRDtool Gallery][] - I'm starting a graphing/log analysis
    project, and looked here for some inspiration for my
    proof-of-concept code
-   [Creating pretty graphs with RRDTOOL][] from [Girish
    Venkatachalam][].
-   There's some good information on RRDtool's "Abberant Behavior
    Detection" (Holt-Winters prediction, deviation and failure
    detection) on the [rrdtool][], [rrdgraph\_examples][] and
    [rrdcreate][] documentation pages, but unfortunately no anchors to
    link directly to.
-   [Cube][] - "Cube is a system for collecting timestamped events and
    deriving metrics. By collecting events rather than metrics, Cube
    lets you compute aggregate statistics post hoc. It also enables
    richer analysis, such as quantiles and histograms of arbitrary event
    sets. Cube is built on MongoDB and available under the Apache
    License on GitHub."
-   [Cubism.js][] - "Cubism.js is a D3 plugin for visualizing time
    series. Use Cubism to construct better realtime dashboards, pulling
    data from Graphite, Cube and other sources. Cubism is available
    under the Apache License on GitHub." The demo on that page looks
    pretty cool.
-   [Highcharts Demo Gallery][] - JS chart/graph library. It requires a
    paid license for commercial use (though it's a bit unclear to me
    whether an internal ops dashboard would fall under this license
    provision) so I probably wouldn't go with this one. They have some
    cool charts, including a [dynamic line chart updating every
    second][], a [scatter plot][] and a nice [zoomable time-series
    graph][], though IMHO it's not as nice as the Google Chart Tools
    (formerly Google Visualization) [annotated timeline][].
-   [[ HOWTO ] Graphing Holt-Winters Predictive Analysis][] - Cacti
    forums
-   [dygraphs][] - an impressive permissive-license JS chart library
    dedicated to visualizing dense time-series data. Developed by Google
    and now used by them (Google Correlate, Google Latitude) as well as
    NASA, 10gen and others. There are some very cool demos on that main
    page, and also on the [tests page][].
-   [Graphite, JMXTrans, Ganglia, Logster, Collectd, say what ? « Planet
    DevOps][]
-   [Visage][]
-   [kgorman/mongo\_graph][] - a tool to pull data from MongoDB and put
    it in RRD files
-   [drraw][] - a perl-based graphing frontend (web UI) for RRDtool
-   [etsy/logster · GitHub][] - Etsy's Python tool to maintain a pointer
    on a log file, and parse at a regular rate feeding the data into a
    tool like Graphite or Ganglia.
-   [cebailey59/charcoal][] - a Sinatra app that allows creation of
    dashboards from Graphite, collectd, or any other service that
    creates images from URL calls.
-   [etsy/dashboard][] - some examples of how Etsy builds monitoring
    dashboards.
-   [GDash – Graphite Dashboard | R.I.Pienaar][] - a Sinatra dashboard
    app for Graphite, using Twitter bootstrap for visualization.
-   [paperlesspost/graphiti][] - a Ruby and JavaScript front-end for
    Graphite.
-   [Graphite Screenshots][] - just two, but they get the idea across
    pretty well.
-   [Graylog2][] - a centralized log management application with a
    powerful web interface. Stores logs in [ElasticSearch][] (which is
    built on Lucene, a Java-based index and search server) and
    statistics/graphs in MongoDB. It does analytics, alerting,
    monitoring/graphing and searching all through a web interface, and
    accepts log data via syslog, AMQP and GELF (its own log format).
    Java server and Ruby on Rails web UI.
-   [Logstash][] - another centralized log project that stores and
    indexes logs, with search via a web UI. "Ship any event to anywhere
    over any protocol." Takes many inputs including files, syslog, AMQP,
    Flume, STOMP, HTTP and even twitter, performs a number of filters
    including timestamp checks, parsing, dropping, joins, etc, and then
    sends logs back on an output including AMQP, Graylog2 GELF, STOMP,
    MongoDB, ElasticSearch, syslog, WebSockets and to Nagios. One
    particularly cool feature is its "file" input, which continuously
    tails a file and claims to be log rotation safe. Just cool.
-   [jordansissel's Logstash intro slides][].
-   [Kibana][] - an alternative interface for Logstash and
    [ElasticSearch][] that allows searching, graphing and analysis of
    log data stored in Logstash.
-   [Pivotal Labs: Talks - Metrics Metrics Everywhere][] (Coda Hale)
-   [PaperlessPost - @quirkey's talk on metrics][] - very good high
    level stuff, but slides only
-   [paperlesspost/graphiti][] - graphiti, a JS/Ruby frontend for
    Graphite that does graphs, dashboards, and point-in-time snapshots
    of graphs. Lots of functionality.
-   [Redis][] - a distributed key/value store that's really popular with
    the cool kids. [Another Redis Use Case: Centralized Logging •
    myNoSQL][]
-   [Charcoal][cebailey59/charcoal] - a [Sinatra][] (Ruby) dashboard app
    (ready for use on [Heroku][] but usable anywhere). Graphite-oriented
    but will work with any tool that generates images from URLs.
-   [etsy/logster][etsy/logster · GitHub] - etsy's Logster tool, which
    keeps a tail on log files, parses them, and ships metrics to
    Graphite or Ganglia.

  [RRDtool - RRDtool Gallery]: http://oss.oetiker.ch/rrdtool/gallery/index.en.html
  [Creating pretty graphs with RRDTOOL]: http://aplawrence.com/Girish/gv-rrdtool.html
  [Girish Venkatachalam]: 
  [rrdtool]: http://oss.oetiker.ch/rrdtool/doc/rrdtool.en.html
  [rrdgraph\_examples]: http://oss.oetiker.ch/rrdtool/doc/rrdgraph_examples.en.html
  [rrdcreate]: http://oss.oetiker.ch/rrdtool/doc/rrdcreate.en.html
  [Cube]: http://square.github.com/cube/
  [Cubism.js]: http://square.github.com/cubism/
  [Highcharts Demo Gallery]: http://www.highcharts.com/demo/
  [dynamic line chart updating every second]: http://www.highcharts.com/demo/dynamic-update/gray
  [scatter plot]: http://www.highcharts.com/demo/scatter/gray
  [zoomable time-series graph]: http://www.highcharts.com/demo/line-time-series/gray
  [annotated timeline]: https://developers.google.com/chart/interactive/docs/gallery/annotatedtimeline
  [[ HOWTO ] Graphing Holt-Winters Predictive Analysis]: http://forums.cacti.net/viewtopic.php?t=29963
  [dygraphs]: http://dygraphs.com/
  [tests page]: http://dygraphs.com/tests/
  [Graphite, JMXTrans, Ganglia, Logster, Collectd, say what ? « Planet
  DevOps]: http://www.planetdevops.net/?p=12289
  [Visage]: http://auxesis.github.com/visage/
  [kgorman/mongo\_graph]: https://github.com/kgorman/mongo_graph
  [drraw]: http://web.taranis.org/drraw/
  [etsy/logster · GitHub]: https://github.com/etsy/logster
  [cebailey59/charcoal]: https://github.com/cebailey59/charcoal
  [etsy/dashboard]: https://github.com/etsy/dashboard
  [GDash – Graphite Dashboard | R.I.Pienaar]: http://www.devco.net/archives/2011/10/08/gdash-graphite-dashboard.php
  [paperlesspost/graphiti]: https://github.com/paperlesspost/graphiti
  [Graphite Screenshots]: http://graphite.wikidot.com/screen-shots
  [Graylog2]: http://graylog2.org/
  [ElasticSearch]: http://www.elasticsearch.org/
  [Logstash]: http://logstash.net/
  [jordansissel's Logstash intro slides]: https://docs.google.com/present/view?id=dcmwwd94_16dfdxgpw8
  [Kibana]: http://rashidkpc.github.com/Kibana/
  [Pivotal Labs: Talks - Metrics Metrics Everywhere]: http://pivotallabs.com/talks/139-metrics-metrics-everywhere
  [PaperlessPost - @quirkey's talk on metrics]: http://aq.iriscouch.com/swinger/_design/swinger/index.html#/preso/aq-mdd/display/1
  [Redis]: http://redis.io/
  [Another Redis Use Case: Centralized Logging • myNoSQL]: http://nosql.mypopescu.com/post/8652869828/another-redis-use-case-centralized-logging
  [Sinatra]: http://www.sinatrarb.com/
  [Heroku]: http://www.heroku.com/
