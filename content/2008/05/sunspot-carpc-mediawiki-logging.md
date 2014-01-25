Title: SunSPOT; CarPC; MediaWiki Logging
Date: 2008-05-07 10:03
Author: admin
Category: Projects
Tags: bluetooth, car, carpc, conres, gps, linux, mediawiki, novell, obd, rutgers, sun, sunspot, suse, tuxtruck
Slug: sunspot-carpc-mediawiki-logging

Well, finals season is upon me. That's probably why I haven't been
posting much lately (I haven't even been checking [Google
Reader](http://reader.google.com/) - I'll have to delete a few thousand
entries when I get back into the swing of things). I've been pretty
busy, between studying, projects, and work. I'll be working 4 days a
week through June 20th, as well as taking night classes 4 nigths a week
(unfortunately not the same 4 days) through July 3, in an effort to
graduate Rutgers on time (after transferring in and also switching
majors). Work after June 20th is up in the air - who knows how hard the
budget cuts will hit.

My internship as the Sun Microsystems Campus Ambassador to Rutgers is
over on May 12th. I got a chance to do the Rutgers IT Vendor Fair with
Sun, and met a few cool people - especially including Matt McGrath of
[Continental Resources](http://www.conres.com/), a Sun Strategic iForce
Partner, who's doing some wonderful things with the [Sun Education
Essentials Matching Grant
Program](http://www.sun.com/solutions/landing/industry/education/edu_essentials.jsp),
and [Skip Paul](http://opsamericas.com/), a Linux Systems Engineer for
Novell's Open Platform Solutions group. I also finally cracked open my
demo set of [SunSPOT](http://www.sunspotworld.com/)s. Wonderful little
devices, radio, run Java on the bare metal, and have temperature
sensors, accelerometers, and liberal I/O. My first development exereice
will probably be making a temperature and acceleration data logger for
my truck, but there's surely more to come. They're great!

My newest project - which I'm hoping to spend nearly the whole summer on
- is the [TuxTruck](http://www.jasonantman.com/tuxtruck/). I've been
frustrated with the lack of "smartness" in my truck (an 06 Ford F-250),
not to mention having to remember my MP3 player so I can listen to
podcasts on the way to work, and having so many gadgets in my truck. So,
the solution is obvious: a Linux-based
[CarPC](http://en.wikipedia.org/wiki/Carpc). A nice little Mini-ATX box
under a seat, with a 7" pull-out touchscreen in the dash (replacing the
factory radio). It's a big, complicated, and expensive project - but I
want one, and I could use some experience with smaller systems.  
The major features I have planned:

1.  Realtime GPS navigation
2.  Hands-free bluetooth calls from my cell, with address book, routing
    to contact address, possibly voice dialing.
3.  Realtime weather
4.  OBD-II interface, for vehicle diagnostics and fuel
    efficiency/performance profiling
5.  Audio - at a minimum searching and playing MP3s, and automatically
    downloading podcasts and throwing them in a playlist. Perhaps also
    an AM/FM tuner

It's not an easy project. So far, the major challenges seem to be:

-   No full-featured GPS navigation package available. The ones that are
    available don't seem to be too easy to integrate into my planned
    GUI, which will allot them 800x420 pixels (on an 800x480 screen) and
    requre the bottom toolbar to be always available.
-   How to handle processing of multiple data streams that require
    near-real-time processing - specifically, GPS with text-to-speech,
    turn-by-turn directions, plus playing audio, plus responding to an
    incoming phone call in a timely manner, pausing the audio, and
    stopping GPS audio but continuing navigation.
-   Whether to install a smaller stereo and use aux input for audio, or
    totally rip out the stereo, use an amp with the computer as its only
    input, and then how to control volume?

There will be more to come in the future. For now, take a look at [the
TuxTruck github](https://github.com/jantman/tuxtruck).

* * * * *

**Update Saturday, March 2, 2013** - I'm in the process of migrating my
legacy CVS and Subversion repositories to
[github.com](http://github.com/jantman/). The forgotten SVN repository
for TuxTruck has been migrated there, and the CVS repository will soon
be moved there as well. Tuxtruck.org has been permanently taken offline
and redirected to the GitHub repository.

* * * * *

<span style="font-weight: bold;">Mediawiki Logging</span> - I recently
had a situation where I had to confirm how much work someone had done on
a MediaWiki-based project. The Recent Changes page only goes back 30
days, and walking through the History of each page is a pain. After
looking around in the database a bit, I found a few tables of interest:

-   Table "users" includes fields "user\_touched" (last time the user
    was updated) and "user\_editcount" (a really simple count of the
    users' number of edits).

-   Table "recentchanges" holds a lot of data... seemingly the entire
    life of the wiki

