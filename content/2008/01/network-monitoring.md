Title: Network Monitoring
Date: 2008-01-29 03:06
Author: admin
Category: Miscellaneous
Slug: network-monitoring

I was reading [Ben Rockwood's blog][] before (as I do every day, thanks
to the magic of [Google Reader][]), where he had an [article praising][]
[up.time network monitoring software][]. Now, up.time (have I ever
mentioned that I \*hate\* names with punctuation in them?) is
proprietary software. And, given their support options, level of
integration, and fancy web site, I assume it's probably not cheap. They
bill it as turnkey monitoring - they claim to be "up and monitoring"
within 15 minutes "including the download". They also have an
[impressive list of clients][], including JP Morgan, Merrill Lynch,
Cingular Wireless, Verizon Wireless, T-Mobile, Wyeth Medica,
Hewlett-Packard (how ironic - did the OpenView team hear about this?),
and a whole slew of other clients including major hospitals. Aside from
the irony of HP using their product, I wonder to what extent these
clients use up.time. Surely the likes of Merrill Lynch can afford more
than a turnkey solution. And I'd bet that Verizon Wireless doesn't use
anything 100% off-the-shelf to monitor their communications systems.

Anyway, this got me thinking about network monitoring systems. Well,
open-source ones, since I like the idea of having control over
infrastructure. The forerunners seem to be [Nagios][] (my personal
choice), [GroundWork Monitor][] (available in both open-source and
proprietary versions), [Zenoss][] ("Core" free version and a paid-for
Enterprise version), [Zabbix][], [OpenNMS][], and [Munin][], [Cacti][],
or one of the other [MRTG][]-/RRD-based applications for
graphing/trending.

As stated, I've always been a Nagios man. I've been running it for 3+
years, and it's always worked well for me. Once you spend days learning
to cope with the config files, it's a breeze. Until they go and change
them in Nagios 3. The one thing that I always missed was built-in
graphing and trending. And some sort of \*good\* log analysis. So,
Nagios 3 is coming out (the Nagios site claims to get Nagios 3 up and
running in 15 minutes, as well), and I guess I should upgrade. However,
after looking around a bit, I came to a frightening realization -
Zabbix, Zenoss, and OpenNMS look a heck of a lot better than Nagios.
Their interfaces appear much nicer (personally I think OpenNMS wins) and
they seem to have a lot more features, too - like Zenoss's inventory and
configuration management. So, this got me thinking that there might be a
change in the future - even though I've put hundreds of hours of
painstaking customization into Nagios.

We'll see where it goes. My main concern is that whatever I pick can
handle integrating with my soon-to-be-implemented barcoded hardware
inventory and tracking system. Integration with a good log parses,
configuration file management system, and reporting system would be good
too. We'll see if the other offerings can stand up to testing (the
concept of device detection is especially intriguing) or whether I'll
just end up building myself a Nagios front-end that pulls various bits
of data (text, graphs, pictures, HTML, etc.) from various other sources
such as Munin, Cacti, an inventory system, log parsing, etc.

  [Ben Rockwood's blog]: http://www.cuddletech.com/blog/index.php
  [Google Reader]: http://www.google.com/reader
  [article praising]: http://www.cuddletech.com/blog/pivot/entry.php?id=893
  [up.time network monitoring software]: http://www.uptimesoftware.com/
  [impressive list of clients]: http://www.uptimesoftware.com/clients.php
  [Nagios]: http://www.nagios.org/
  [GroundWork Monitor]: http://www.groundworkopensource.com/products/os-overview.html
  [Zenoss]: http://www.zenoss.com/product/core
  [Zabbix]: http://www.zabbix.com/
  [OpenNMS]: http://www.opennms.org
  [Munin]: http://munin.projects.linpro.no/
  [Cacti]: http://www.cacti.net/
  [MRTG]: http://oss.oetiker.ch/mrtg/
