Title: Apache httpd - logging for sites with and without load balancing
Date: 2012-05-30 09:46
Author: admin
Category: Tech HowTos
Tags: apache, bigip, f5, httpd, load balancer, logging
Slug: apache-httpd-logging-for-sites-with-and-without-load-balancing

There are a few unfortunate places where I have an Apache httpd server
serving multiple vhosts, some behind a F5 BigIp load balancer and some
with direct traffic. For sites behind the LB, the remote IP/host will
always show up as the LB's IP/host, not that of the actual client. Using
the default configuration with LogFormat directives in `httpd.conf`,
this means that either we need to define log formats per-vhost or lose
the client IP in one of our scenarios (LB or no LB).

I came by a simple solution to this on [Emmanuel Chantréau][]'s blog,
and here is my condensed version of it. It sets an environment variable
("bigip-request") if the BIOrigClientAddr request header is set (this
header holds the client's IP; it's the BigIp proprietary version of the
X-Forwarded-For header. You could easily substitute that more standard
header in the following snippet) and then sets the "combined" LogFormat
based on that variable - a version using BIOrigClientAddr if it is set,
and a version using the normal "%h" remote host otherwise.

In httpd.conf:

~~~~{.apacheconf}
# set the "bigip-request" env variable to "1" if there is a BIOrigClientAddr header in the request                                                                                                   
SetEnvIf BIOrigClientAddr . bigip-request
# we'll use this following LogFormat (BIOrigClientAddr in place of remote host) as "combined" IF the bigip-request env variable is set                                                                     
LogFormat "%{BIOrigClientAddr}i %l %u %t %v \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined_lb
# else we'll use this one (remote host IP address) as "combined" IF the bigip-request env variable is NOT set                                                                                   
LogFormat "%h %l %u %t %v \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
~~~~

And then in our vhost configuration:

~~~~{.apacheconf}
# use this log format if we're behind an LB
CustomLog logs/<%= domain %>_access_log combined env=!bigip-request
# or this format if we're not
CustomLog logs/<%= domain %>_access_log combined_lb env=bigip-request
~~~~

  [Emmanuel Chantréau]: http://www.maretmanu.org/homepage/inform/apache-forwarded.php
