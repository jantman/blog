Title: Apache2 - list Name-Based Virtual Hosts
Date: 2010-02-11 09:48
Author: admin
Category: Tech HowTos
Tags: apache, configuration, linux
Slug: apache2-list-name-based-virtual-hosts

Here's a little tidbit that I never knew until I had an
[Apache2](http://httpd.apache.org/) name-based virtual host problem:
`httpd -S` lists the vhosts that are being served by Apache, and how
they were parsed from the config files.

The output on one of my servers looks something like:

~~~~{.text}
[root@web2 vhosts.d]# httpd -S
VirtualHost configuration:
wildcard NameVirtualHosts and _default_ servers:
_default_:443          web2.jasonantman.com (/etc/httpd/vhosts.d/ssl-host.conf:7)
*:80                   is a NameVirtualHost
         default server www.jasonantman.com (/etc/httpd/vhosts.d/000-default.conf:1)
         port 80 namevhost www.jasonantman.com (/etc/httpd/vhosts.d/000-default.conf:1)
         port 80 namevhost rackman.jasonantman.com (/etc/httpd/vhosts.d/rackman.jasonantman.com.conf:1)
         port 80 namevhost whatismyip.jasonantman.com (/etc/httpd/vhosts.d/whatismyip.jasonantman.com.conf:1)
Syntax OK
~~~~

This is quite useful in debugging vhost problems, especially those pesky
times when a request that should go to a specific vhost is being served
by the default (in my case at this time, I had two ServerName directives
instead of a ServerName and a ServerAlias).
