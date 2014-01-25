Title: Update, Eventum/MySQLTicketing Integration
Date: 2008-02-21 14:53
Author: admin
Category: Tech HowTos
Tags: eventum, monitoring, mysql, programming, ticketing
Slug: update-eventummysqlticketing-integration

Well I know I haven't updated in a while. I have a whole bunch of links
that I'd like to comment on, but things have been horribly busy. You can
find the links in my ["1-toblog" folder on
del.icio.us](http://del.icio.us/jantman/1-toblog) (prefixed with "1-" so
it shows up at the beginning of my bookmark menu).

In monitoring land, I've paused my [Hyperic
HQ](http://www.hyperic.com/products/hq_oss.html) VM as I wasn't too
pleased with how the features panned out. I was invited to beta test
[Groundwork Open Source](http://www.groundworkopensource.com/) 5.2b, but
I'm not crazy about the open-ness of a non-public Beta, and am honestly
not that intrigued by the small feature set (though, admittedly, they do
need more documentation on the F/OSS version). I'd still like to try
them all, especially [Zenoss Core](http://www.zenoss.com/product/core),
but I'm pretty busy with class, and things are heating up at work and
with a few consulting projects.

In my "spare time" (read: staying up until 5 AM and somehow still
getting up for work at 9) I've been working on something that's been
bugging me for a while - getting [Nagios](http://www.nagios.org/) to
automatically open and update tickets in
[Eventum](http://eventum.mysql.org), the ticketing system that I (and
MySQL) use. The general idea is to use a "glue" script, written in PHP
(Eventum's native language). It will (hopefully) keep track of which
hosts/services it has opened tickets for (and what the ticket ID is),
and decide from that whether to open a new ticket or, if one already
exists for that host/service, update it. It should also handle changes
to assigned user/group, update categories, priorities, etc. This will
all be based on a DB table that maps problem severities and
hosts/services to the users, groups, categories, and priorities that
they should be assigned.

The biggest problem is that I'm not a whiz at object-oriented PHP, and
like any good OO program, Eventum is broken down into dozens of objects,
classes, and files. With the help of the [Xdebug debugging extension for
PHP](http://xdebug.org/), which prints full debugging output including
stack and function call traces, I've been able to \*finally\* - after
about four hours of work - write a simple little 15-line script that
uses ONLY existing Eventum classes, unmodified (except for a separate
init.php with some stuff commented out), which gets a list of users
assigned to an issue. From here, it shouldn't be difficult to get full
issue information and then, hopefully, add and update issues.

I have a [basic description of the project on my
wiki](http://www.jasonantman.com/wiki/index.php/Monitoring_Ticketing),
and the current (development, so could be broken) source code in CVS,
which can be [seen through ViewVC on my
site](http://cvs.jasonantman.com/cvs/Eventum-Nagios/).

Stay Tuned!
