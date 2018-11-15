Title: New Projects
Date: 2009-07-16 14:05
Author: admin
Category: Miscellaneous
Tags: bind, dns, google, PHPsa, rackman
Slug: new-projects

In terms of ongoing projects, I should be updating RackMan sometime
soon, and also adding the demo site.

I've begun to move DNS for all of my domains in-house, mostly because
since everything is behind NAT, it's a real pain to manage DNS entries
in two places (one of them being GoDaddy's web interface). Because of
the NAT issue, I'm also writing my own BIND configuration tool,
currently named [MultiBIND
Admin](http://multibindadmin.jasonantman.com). In addition to managing
multiple zones in a sane way, it stores all configuration in MySQL.
Among other things, it can store different IP addresses for A records
for the inside and outside views. Zone files can either be pulled by a
script on the name server (push capability is being worked on) or
downloaded (for uploading to a DNS hosting provider like GoDaddy).

For my final project for my XML web design class, I'm going to be making
some "mashup" with RackMan, Google Maps, Google Visualizer, Nagios, and
a few other tools...

Stay tuned...
