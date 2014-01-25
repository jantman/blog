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

-   [RRDtool - RRDtool
    Gallery](http://oss.oetiker.ch/rrdtool/gallery/index.en.html) - I'm
    starting a graphing/log analysis project, and looked here for some
    inspiration for my proof-of-concept code
-   [Creating pretty graphs with
    RRDTOOL](http://aplawrence.com/Girish/gv-rrdtool.html) from [Girish
    Venkatachalam]().
-   There's some good information on RRDtool's "Abberant Behavior
    Detection" (Holt-Winters prediction, deviation and failure
    detection) on the
    [rrdtool](http://oss.oetiker.ch/rrdtool/doc/rrdtool.en.html),
    [rrdgraph\_examples](http://oss.oetiker.ch/rrdtool/doc/rrdgraph_examples.en.html)
    and [rrdcreate](http://oss.oetiker.ch/rrdtool/doc/rrdcreate.en.html)
    documentation pages, but unfortunately no anchors to link directly
    to.
-   [Cube](http://square.github.com/cube/) - "Cube is a system for
    collecting timestamped events and deriving metrics. By collecting
    events rather than metrics, Cube lets you compute aggregate
    statistics post hoc. It also enables richer analysis, such as
    quantiles and histograms of arbitrary event sets. Cube is built on
    MongoDB and available under the Apache License on GitHub."
-   [Cubism.js](http://square.github.com/cubism/) - "Cubism.js is a D3
    plugin for visualizing time series. Use Cubism to construct better
    realtime dashboards, pulling data from Graphite, Cube and other
    sources. Cubism is available under the Apache License on GitHub."
    The demo on that page looks pretty cool.
-   [Highcharts Demo Gallery](http://www.highcharts.com/demo/) - JS
    chart/graph library. It requires a paid license for commercial use
    (though it's a bit unclear to me whether an internal ops dashboard
    would fall under this license provision) so I probably wouldn't go
    with this one. They have some cool charts, including a [dynamic line
    chart updating every
    second](http://www.highcharts.com/demo/dynamic-update/gray), a
    [scatter plot](http://www.highcharts.com/demo/scatter/gray) and a
    nice [zoomable time-series
    graph](http://www.highcharts.com/demo/line-time-series/gray), though
    IMHO it's not as nice as the Google Chart Tools (formerly Google
    Visualization) [annotated
    timeline](https://developers.google.com/chart/interactive/docs/gallery/annotatedtimeline).
-   [[ HOWTO ] Graphing Holt-Winters Predictive
    Analysis](http://forums.cacti.net/viewtopic.php?t=29963) - Cacti
    forums
-   [dygraphs](http://dygraphs.com/) - an impressive permissive-license
    JS chart library dedicated to visualizing dense time-series data.
    Developed by Google and now used by them (Google Correlate, Google
    Latitude) as well as NASA, 10gen and others. There are some very
    cool demos on that main page, and also on the [tests
    page](http://dygraphs.com/tests/).
-   [Graphite, JMXTrans, Ganglia, Logster, Collectd, say what ? « Planet
    DevOps](http://www.planetdevops.net/?p=12289)
-   [Visage](http://auxesis.github.com/visage/)
-   [kgorman/mongo\_graph](https://github.com/kgorman/mongo_graph) - a
    tool to pull data from MongoDB and put it in RRD files
-   [drraw](http://web.taranis.org/drraw/) - a perl-based graphing
    frontend (web UI) for RRDtool
-   [etsy/logster · GitHub](https://github.com/etsy/logster) - Etsy's
    Python tool to maintain a pointer on a log file, and parse at a
    regular rate feeding the data into a tool like Graphite or Ganglia.
-   [cebailey59/charcoal](https://github.com/cebailey59/charcoal) - a
    Sinatra app that allows creation of dashboards from Graphite,
    collectd, or any other service that creates images from URL calls.
-   [etsy/dashboard](https://github.com/etsy/dashboard) - some examples
    of how Etsy builds monitoring dashboards.
-   [GDash – Graphite Dashboard |
    R.I.Pienaar](http://www.devco.net/archives/2011/10/08/gdash-graphite-dashboard.php)
    - a Sinatra dashboard app for Graphite, using Twitter bootstrap for
    visualization.
-   [paperlesspost/graphiti](https://github.com/paperlesspost/graphiti)
    - a Ruby and JavaScript front-end for Graphite.
-   [Graphite Screenshots](http://graphite.wikidot.com/screen-shots) -
    just two, but they get the idea across pretty well.
-   [Graylog2](http://graylog2.org/) - a centralized log management
    application with a powerful web interface. Stores logs in
    [ElasticSearch](http://www.elasticsearch.org/) (which is built on
    Lucene, a Java-based index and search server) and statistics/graphs
    in MongoDB. It does analytics, alerting, monitoring/graphing and
    searching all through a web interface, and accepts log data via
    syslog, AMQP and GELF (its own log format). Java server and Ruby on
    Rails web UI.
-   [Logstash](http://logstash.net/) - another centralized log project
    that stores and indexes logs, with search via a web UI. "Ship any
    event to anywhere over any protocol." Takes many inputs including
    files, syslog, AMQP, Flume, STOMP, HTTP and even twitter, performs a
    number of filters including timestamp checks, parsing, dropping,
    joins, etc, and then sends logs back on an output including AMQP,
    Graylog2 GELF, STOMP, MongoDB, ElasticSearch, syslog, WebSockets and
    to Nagios. One particularly cool feature is its "file" input, which
    continuously tails a file and claims to be log rotation safe. Just
    cool.
-   [jordansissel's Logstash intro
    slides](https://docs.google.com/present/view?id=dcmwwd94_16dfdxgpw8).
-   [Kibana](http://rashidkpc.github.com/Kibana/) - an alternative
    interface for Logstash and
    [ElasticSearch](http://www.elasticsearch.org/) that allows
    searching, graphing and analysis of log data stored in Logstash.
-   [Pivotal Labs: Talks - Metrics Metrics
    Everywhere](http://pivotallabs.com/talks/139-metrics-metrics-everywhere)
    (Coda Hale)
-   [PaperlessPost - @quirkey's talk on
    metrics](http://aq.iriscouch.com/swinger/_design/swinger/index.html#/preso/aq-mdd/display/1)
    - very good high level stuff, but slides only
-   [paperlesspost/graphiti](https://github.com/paperlesspost/graphiti)
    - graphiti, a JS/Ruby frontend for Graphite that does graphs,
    dashboards, and point-in-time snapshots of graphs. Lots of
    functionality.
-   [Redis](http://redis.io/) - a distributed key/value store that's
    really popular with the cool kids. [Another Redis Use Case:
    Centralized Logging •
    myNoSQL](http://nosql.mypopescu.com/post/8652869828/another-redis-use-case-centralized-logging)
-   [Charcoal](https://github.com/cebailey59/charcoal) - a
    [Sinatra](http://www.sinatrarb.com/) (Ruby) dashboard app (ready for
    use on [Heroku](http://www.heroku.com/) but usable anywhere).
    Graphite-oriented but will work with any tool that generates images
    from URLs.
-   [etsy/logster](https://github.com/etsy/logster) - etsy's Logster
    tool, which keeps a tail on log files, parses them, and ships
    metrics to Graphite or Ganglia.

