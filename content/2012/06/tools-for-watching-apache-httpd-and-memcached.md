Title: Tools for watching apache httpd and memcached
Date: 2012-06-26 13:46
Author: admin
Category: Tech HowTos
Tags: apache, memcached, perl, top, troubleshooting
Slug: tools-for-watching-apache-httpd-and-memcached

Recently I was working on a code release on a site running PHP on
[Apache httpd](http://httpd.apache.org/), and using
[\>memcached](http://memcached.org/). Without getting into specifics, we
had a number of issues that were both Apache and memcached problems, and
little visibility into them as it was running on an older server without
much monitoring in place. I started looking around for simple tools that
could provide a bit more insight, without many dependencies (as the
machine is a relatively minimalist install). Here are some of the
options I found:

-   [memcache-top](http://code.google.com/p/memcache-top/) - A top-like
    script that pulls stats from memcached instances and can show both
    per-instance, total and average usage %, hit rate, number of
    connections, time to run the stats query, evictions, gets, sets, and
    read and write amounts. Best of all, it's a very small perl script
    that requires only IO::Socket and Time::HiRes. Here's a small
    example of the output:

        memcache-top v0.6       (default port: 11211, color: on, refresh: 3 seconds)

        INSTANCE                USAGE   HIT %   CONN    TIME    EVICT   GETS    SETS    READ    WRITE
        127.0.0.1:11211         86.6%   99.4%   115     0.6ms   0.0     4114    1669    1.3M    24.2M
        127.0.0.1:11212         85.5%   59.9%   2       0.4ms   0.0     0       0       90      8055

        AVERAGE:                86.0%   79.6%   58      0.5ms   0.0     2057    834     682.4K  12.1M

        TOTAL:          0.9GB/  1.0GB           117     1.0ms   0.0     4114    1669    1.3M    24.2M

-   [damemtop](https://github.com/dormando/damemtop) is also a nice
    top-like memcached tool. On the positive side, you can specify any
    column from "stats", "stats items" or "stats slabs" in the
    configuration file, and can choose between average or one-second
    snapshots for each column. On the down side, it requires the YAML
    and AnyEvent Perl modules, so it has some uncommon dependencies.

        damemtop: Tue Jun 26 14:02:24 2012 [sort: hostname asc] [delay: 3s]
        hostname           all_version  all_fill_rate  hit_rate  evictions  curr_items  curr_connections   cmd_get  cmd_set  bytes_written  bytes_read  get_hits  get_misses  
        TOTAL:             
        NA                 NA           NA             NA        NA         NA          NA                 87       32       491,735        30,894      86        1           
        AVERAGE:           
        NA                 NA           86.00%         99.00%    NA         NA          NA                 43       16       122,933        7,723       43        1           
        10.200.1.78:11211  1.2.6        86.63%         98.04%    0          0           -1.00204024880524  51       19       386,492        21,613      50        1           
        10.200.1.78:11212  1.2.6        85.46%         NA        0          0           0                  0        0        11,373         31          0         0           
        10.200.1.79:11211  1.2.6        87.31%         100.00%   0          0           -1.00204024880524  36       13       82,479         9,219       36        0           
        10.200.1.79:11212  1.2.6        85.08%         NA        0          0           0                  0        0        11,389         31          0         0           
        loop took: 0.305617094039917

I'm still looking around for something for apache that uses mod\_status
and isn't too verbose; ideally I'd like to be able to watch memcached,
apache response codes/times, and apache mod\_status all in the same
terminal window.
