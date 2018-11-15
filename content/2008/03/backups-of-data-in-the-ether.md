Title: Backups of data in the ether
Date: 2008-03-06 12:11
Author: admin
Category: Miscellaneous
Tags: backups, del.icio.us, docs, google, reader
Slug: backups-of-data-in-the-ether

While I've often told mystified people that hosted services - the free
ones - aren't required to backup your data, and you should probably do
it yourself, I usually didn't worry about this very much - all of my web
apps are on my own boxes, as well as my email. However, out of
curiosity, I spent about 15 minutes the other day coding up a little
hack of a PHP script to keep track of what applications I use a lot
(specifically web-based ones that I can't easily have my OS keep track
of). After a day of trying to click the little "update" boxes on a
simple page when I used something, I realized how much of my data is
actually out of my own control. Maybe not anything critical, but
convenience stuff like [Google Reader](http://reader.google.com/),
[del.icio.us](http://del.icio.us/) for \*all\* of my bookmarks, and
occasionally [Google Docs](http://docs.google.com/) when I'm going to be
hopping from place to place, or may be using a machine that I don't
trust to SFTP something back home.

So, I decided to go about backing up some of this. The solution I aimed
for was simple - a BASH script that runs nightly via cron, and dumps the
data into my home directory on my main storage/backup server.

Google Reader seemed to be one of the most difficult - no easy URL
scheme, but I found a [simple script](http://blog.tobez.org/?p=49) that
makes use of Perl CPAN's
[WebService::Google::Reader](http://search.cpan.org/~gray/WebService-Google-Reader-0.07/)module
to grab a complete feed list. After seemingly an hour of CPAN updates
and dependencies scrolling down my screen,

Google Calendar Backup:  
Wonderfully simple. Go into Settings, copy the URLs to the private
calendar links (I used iCal format), and wget them.

del.icio.us backup:

~~~~{.bash}
curl --user usernam:pass -o myDelicious.xml -O 'https://api.del.icio.us/v1/posts/all'
~~~~

Google Reader Backup:  
Still in the works - Perl problems on my backup machine.

Google Docs Backup:  
Hopefully soon, though nothing important lives there.
