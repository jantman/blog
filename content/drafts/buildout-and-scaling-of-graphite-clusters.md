Title: Buildout and Scaling of Graphite Clusters
Date: 2013-09-05 20:17
Author: admin
Category: Uncategorized
Slug: buildout-and-scaling-of-graphite-clusters
Status: draft

Blog posts -  
1. Building a graphite cluster and migrating data from standalone  
2. Monitoring graphite/stasd and their internal metrics  
3. patch to add matrics - lost data, latency, metrics received by path
X deep  
4. statsd blacklist patch  
graphite aggregation methods  
cluster rebalancing, megacarbon

Graphite and Statsd - Performance and Monitoring

I've been planning a series of blog posts on
[Graphite](http://graphite.readthedocs.org/en/latest/) and [Etsy's
statsd](https://github.com/etsy/statsd) for a while now, as I've spent
the past week at work transforming our previous single VM running
graphite into a 3-node bare-metal cluster (albeit on very old,
repurposed hardware). A few days ago, just as I was polishing up our
internal documentation that would form the core of those blog posts, a
production deploy introduced a new metric being pushed to statsd from
inside an object in our CMS. That metric happened to include a
relatively unique URL component. This is the graph of our master
carbon-relay's metricsReceived from the time of the deploy, until I took
some decisive action:

[![graph of metricsReceived, linear increase from 100,000 to over
750,000 in 3.5
hours](/GFX/metricsReceived.png)](/GFX/metricsReceived_large.png)

While this obviously wasn't good, it did teach me quite a bit about
Graphite, how it scales and handles load, what our capacity is and what
to watch for early warning of problems. Since most of this post is about
graphite, I'll take a minute to mention statsd, which we push most of
our metrics through. It performed amazingly well. I supposed it's just
because graphite is disk-bound, but even when we hit 750k
metrics/minute, statsd still showed virtually no resource usage on its
host (a VM), and certainly no signs for concern. My only complaints with
statsd are that I would absolutely love a way to blacklist certain
runaway metric strings (with wildcards or a regex) at runtime (I opened
[issue 293](https://github.com/etsy/statsd/issues/293) about this), and
that by default statsd continues sending 0 value for metrics to its
backends even if no value was received for the metric, which gave me a
brief moment of confusion when I finally stopped the flow of abusive
metrics but saw no real change in the data going to graphite.

First, the machines we're using for Graphite are IO-bound, and we know
it. The three cluster nodes are Dell PowerEdge 1950s with two spinning
disks each (single Xeon 5150 with 2 cores at 2.6GHz, 4MB L2 cache; 4x 4G
DDR2-667 memory; PERC 6/i RAID controller with dual 68GB 15k/3Gbps SAS
Seagate ST373454SS disks in RAID-1, disk cache disabled, write back, no
read ahead). It's inefficient, but it's all we can allocate to graphite
at the moment, and it's a lot better than the one VM it was on a week
ago. All that said, I was quite impressed with how graphite performed
under extraordinary load - made much worse because most of these metrics
were unique, so the number of new whisper files created was quite high.
The core of what I learned (both during the issues, and from the folks
on [\#graphite on Freenode](irc://irc.freenode.net/#graphite)) is that
if we want to scale to 2+ million metrics every 10 seconds, we need a
good RAID setup with SSDs, and a fair amount of RAM. But despite all
three nodes in our cluster being IO-bound (effectively maxed on IO) and
maxed out on memory, graphite never died, and I wasn't able to find any
obvious loss of large amounts of data. Things just got REALLY slow.

Before I go into the internals of graphite and what I learned, let's
look a bit at some graphs of the graphite processes and hosts, and what
they show (click the images for larger versions). Keep in mind that in
most of these graphs, they're including three physical hosts, each with
one carbon-relay and two carbon-caches, plus a master carbon-relay on
one of the hosts.

[< img src="/GFX/creates\_vs\_io\_read\_await.png" width="800"
height="480" alt="graph of iostat read\_await vs carbon-cache creates.
When creates reach approx. 500/minute across the cluster, await begins
to show spikes." /\>](creates_vs_io_read_await_large.png)

[< img src="/GFX/creates\_vs\_io\_read\_ms.png" width="800" height="480"
alt="graph of iostat milliseconds reading vs carbon-cache creates. When
creates reach approx. 1000/minute, read time increases from near-zero to
over 50% of clock time." /\>](creates_vs_io_read_ms_large.png)

[< img src="/GFX/metricsReceived\_vs\_carbon-cache\_memUsage.png"
width="800" height="480" alt="graph of carbon-relay metrics received vs
carbon-cache memory usage. Memory usage climbs unevenly but in a
generally similar fashion to metrics received, but does not decrease.
The second spike in metrics received simply increases memory use."
/\>](metricsReceived_vs_carbon-cache_memUsage_large.png)

[< img src="/GFX/metricsReceived\_vs\_carbon-relay-master\_memUsage.png"
width="800" height="480" alt="graph of carbon-relay metrics received vs
carbon-relay master memory usage. This graph is a signigicant departure
from the other, close-to-linear relationships. Master carbon-relay
memory usage stays largely steady from 95k metrics/minute to
approximately 300k metrics/minute, then almost doubles within one sample
period (from approx. 16 MB to approx. 28 MB) and maintains that level to
the peak of 750k metrics/minute."
/\>](metricsReceived_vs_carbon-relay-master_memUsage_large.png)

[< img src="/GFX/metrics\_recvd\_vs\_flush\_time.png" width="800"
height="480" alt="graph of carbon-relay metrics received vs statsd time
flushing graphite stats. the best-fit line of the two graphs would
almost match." /\>](metrics_recvd_vs_flush_time_large.png)

[< img src="/GFX/metrics\_recvd\_vs\_iops.png" width="800" height="480"
alt="graph of carbon-relay metrics received vs IOPS. It's clear that we
were near our IOPS ceiling prior to this event when handling about 300k
metrics per minute, and at 75k metrics per minute we're using about half
of our available IO." /\>](metrics_recvd_vs_iops_large.png)

[< img src="/GFX/metrics\_recvd\_vs\_iostat\_queue\_length.png"
width="800" height="480" alt="graph of carbon-relay metrics received vs
IO queue length. Shows that we were already at maximum disk queue at
300k metrics/minute before the event, but after limiting metrics down to
75k per minute IO queues dropped to about 25% of capacity."
/\>](metrics_recvd_vs_iostat_queue_length_large.png)

[< img src="/GFX/metrics\_recvd\_vs\_iostat\_wps.png" width="800"
height="480" alt="graph of carbon-relay metrics received vs IO writes
per second. Writes per second increase roughly linearly with
metricsReceived from 95k metrics/minute to about 175k metrics/minute,
and then level off when IO is saturated."
/\>](metrics_recvd_vs_iostat_wps_large.png)

[< img src="/GFX/metrics\_recvd\_vs\_iostat\_write\_bytes.png"
width="800" height="480" alt="graph of carbon-relay metrics received vs
IO bytes written. This is an even better indication than the previous
graph that writes to disk continue acceptably up to about 175k
metrics/minute and then level off, indicating IO saturation and metric
create queueing in carbon-cache."
/\>](metrics_recvd_vs_iostat_write_bytes_large.png)

[< img src="/GFX/metrics\_vs\_relay-master\_cpuUsage.png" width="800"
height="480" alt="graph of carbon-relay master metrics received vs
carbon-relay master CPU usage. Through the entire event up to 750k
metrics/minute, master carbon-relay CPU usage stayed almost perfectly in
step with the number of metrics. Aside from some spikes and dips, the
CPU usage line almost perfectly mirrors the slope of the metrics
received line." /\>](metrics_vs_relay-master_cpuUsage_large.png)

- what the various internal stats mean  
- how to interpret them  
- what to graph  
- early indicators of problems  
- creates - this is the number of NEW whisper files written to disk. If
this goes up (it has a max per interval), you're getting a bunch of
never-before-seen metrics. In my environment, there's a pretty clear
line of how many creates per minute are normal, and how many are a new
metric that ops should have been aware of (and, if it wasn't planned
for, will be a problem).  
- metricsReceived - especially take a look at the second derivative, or
acceleration. Large changes here in either direction are probably BAD.  
- io service time - once this starts rising substantially, carbon
queues will begin filling  
- carbon.agents memUsage - large jumps in memory usage for carbon-cache
indicates an increase in incoming metrics, or that IO has slowed down.  
- late indicators of problems  
- missing data points in carbon.\* internal metrics  
- carbon.agents avgUpdateTime - this is the time taken to write metrics
to disk. If it jumps above a reasonable baseline, your IO is fully
saturated.  
- statsd graphiteStats.flush\_time - if statsd starts experiencing
higher latency flushing metrics to graphite, so will everything else.
When this starts happening, overall latency of the end-to-end system is
increasing.  
- io queue length - there's a maximum for this. When you hit the
ceiling, the system's latency will shoot up.  
- carbon.agents cache.size - this is a pretty poor indicator, and is
really more of a "kiss your ass goodbye" alarm. If the size of the cache
gets larger than metricsReceived, you've got a backlog growing faster
than IO can handle, and need to fix the problem immediately
