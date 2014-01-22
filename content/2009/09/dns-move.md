Title: DNS Move
Date: 2009-09-17 13:07
Author: admin
Category: Projects
Tags: bind, dns, multibindadmin
Slug: dns-move

Yesterday I finally began moving DNS for my sites from GoDaddy to my own
in-house system of master/slave [BIND9][]. While both DNS servers are
currently at the same location and on the same WAN connection (heck,
they're beind the same router, too), so is all of the rest of my
infrastructure. Migrating jasonantman.com was definitely the most
critical task, this has allowed me to easily use my new project,
[MultiBIND Admin][] to manage DNS. In addition to just being simpler
than using GoDaddy's tool, it allows me to manage DNS for both the
external view and the NATed internal view in one tool. I did have a
brief mail outage thanks to some incorrect MX records being served by
the slave, and a few other issues with the caching DNS servers at work
not expiring the old records, but all seems to be well now. It was a
relatively smooth transition, though I haven't yet moved over some of my
older less used domains.

The next part of my project, when I move the ambulance corps hosted
services in-house, will be trying to find a decently-priced DNS hosting
company that will just act as a slave, to keep DNS up if my WAN
connection goes down.

  [BIND9]: https://www.isc.org/software/bind
  [MultiBIND Admin]: http://multibindadmin.jasonantman.com
