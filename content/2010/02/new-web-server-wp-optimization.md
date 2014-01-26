Title: New web server, WP optimization
Date: 2010-02-28 23:19
Author: admin
Category: Projects
Tags: apache, optimization, performance, wordpress
Slug: new-web-server-wp-optimization

Tonight, more or less on a whim, I moved my blog from my older (dual
1GHz Pentium III Coppermine, 1GB RAM, 10k RPM SCSI disks, Compaq
Proliant DL360 G1, OpenSuSE 10.2 32-bit) web server to my newer one
(dual 1.4GHz Pentium III, 2GB RAM, 10k RPM SCSI disks, HP Proliant DL360
G2, CentOS 5.3 32-bit). I did some profiling with
[ab](http://httpd.apache.org/docs/2.0/programs/ab.html) (ApacheBench),
and just moving from one server to the other got some serious
performance gains (I was profiling with runs of 1000 requests total, 10
concurrent requests). I also added the [W3 Total
Cache](http://wordpress.org/extend/plugins/w3-total-cache/) Wordpress
plugin, which got the numbers to look even better!

As a side note, this was all done pretty quickly (moving the database
and tarball for the vhost, installing the plugin, changing DNS), so
please give me a heads-up if you experience any problems.

The numbers are rather impressive:

<table border="1">
<tr>
<td>
</td>
<th>
Total Time(s)

</th>
<th>
RPS

</th>
<th>
Avg. Connection Time (ms)

</th>
</tr>
<tr>
<th>
Old Server

</th>
<td>
1192.252

</td>
<td>
838.75

</td>
<td>
11,893

</td>
</tr>
<tr>
<th>
New Server

</th>
<td>
569.121

</td>
<td>
1757.09

</td>
<td>
5,667

</td>
</tr>
<tr>
<th>
Default W3tc Config

</th>
<td>
23.754

</td>
<td>
42,098.44

</td>
<td>
237

</td>
</tr>
<tr>
<th>
Tuned W3tc

</th>
<td>
12.281

</td>
<td>
81,428.76

</td>
<td>
122

</td>
</tr>
</table>
All tests were performed on my workstation, a Dell Precision 470, two
dual-core Xeons at 2.8 GHz, 2GB RAM, 16GB swap, OpenSuSE 11.1 64-bit.
This was on the same LAN and subnet as the servers, with the workstation
connected via a 1Gbps copper Ethernet link and the web-serving
interfaces of the servers connected via 100Mbps (There's a trunk in
between, from the gigabit aggregation switch to the 100Mbps distribution
switch).
