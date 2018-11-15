Title: Website, Blog, Bacula
Date: 2007-10-10 13:35
Author: admin
Category: Software
Tags: bacula, blog, jasonantman, mediawiki, wiki
Slug: website-blog-bacula

**Website** - In personal news, I've finished migrating all of the
information content of [JasonAntman.com](http://www.jasonantman.com) to
a wiki, based on [MediaWiki](http://www.mediawiki.org). I'm still
getting some kinks ironed out, and working on customization, but it
seems to be coming along very well. It's wonderfully easy to update
information and to link between articles. Most of the content is more
like notes than articles, but I'm trying to put most of my SysAdmin and
programming notes up there, both for my own future reference and that of
anyone who happens by the site. As always, though, some content will
just live its' life as a blog entry, so I encourage searching of my blog
as well. This is my fourth instance of MeidaWiki, and while I haven't
set them up to play together, they all run wonderfully - and share a lot
of common configuration (though I have separate instances of the code).
Hopefully I'll do a bunch of reorganization of the wiki sometime, and
keep adding new content. Some of the newer pages include pages on
[DenyHosts](http://www.jasonantman.com/wiki/index.php/DenyHosts) and
[HPASM](http://www.jasonantman.com/wiki/index.php/Hpasm) (from my blog
post).

**Blog** - I know the template is awful. It's on my list of things to
do, and should be at the top of the queue in approximately 2056.

**Bacula** - Up to now, my backups have been a total kludge. The mere
explanation of this elicits a feeling of nausea. A shell script on my
backup storage server executes via cron. Each of the four important
servers on my network (mail, web, monitoring, and development) have
shell scripts that handle local backups - tar'ing up a list of
directories, MySQL dumps, etc. - then tar gzip the whole thing and plop
it in a local directory. The backup server executes these scripts and
then copies the temporary files to its own disk via SCP. All of this is
handled through an [expect](http://expect.nist.gov/) script, that runs
each server consecutively. By morning, I end up with a 6+ hour job
that's finished, and dumped gigs of files on the backup server. Before
finishing each machine, it deletes any backups on the backup server that
are older than 10 days. After copying everything, it deletes the
client's local copy. The bottom line is that if a machine goes down, I
can re-install the OS and all packages, and then have the backups of
just /etc and user data. Not beautiful. Even worse, my backup storage
server doesn't have a tape drive. When I get around to it, I run a
script on my development/storage box that copies the latest backups from
each machine, located on the backup server, to a tempdir and then writes
them to tape. To top it all off, I have only one network, so all of
these gigs of data are crawling across my ancient 10/100 switch, along
with all other connectivity to the outside world.

Unfortunately, it doesn't look like I'll have the money to upgrade to
Gig-E any time soon, even just for the 5 machines involved. More to the
point, there's no way that I'll have the money to buy a manageable Gig-E
switch that can come anywhere close to my [BayStack
450-24T](http://www.jasonantman.com/wiki/index.php/BayStack_450-24T).
So, it's time to invest... well... time... in a good backup
infrastructure. After doing a lot of research, I came to two findings:

1.  The two main options seem to be [AMANDA](http://www.amanda.org/) and
    [Bacula](http://www.bacula.org/).
2.  I don't like how AMANDA works.

So, I'm going to give Bacula a shot. I did consult the
[SAGE](http://www.sage.org/) mailing list for advice, and got some
recommendations for [BackupPC](http://backuppc.sourceforge.net/), but
Bacula seems to be more my type of thing. Well, I did an install, and
spent about 8 hours hacking around with the config files. No luck.
Bacula is designed to be highly modular and scalable, but to be honest,
I find the config files to be \*very\* complicated. Furthermore, I
wasn't able to find any good example configurations with documentation.
After brainstorming for a while (laying in bed watching Law & Order and
reading the Bacula docs on dead trees) I decided to give in - despite my
continued efforts to stop using it, I checked
[Webmin](http://www.webmin.com) and, surely enough, they have a Bacula
module. After starting with fresh config files, I was able to get Bacula
up and running on my development/storage server (a fresh install of
openSuSE 10.1) as the director. I got a file daemon installed on the web
server. Everything looked wonderful.

The current status: My backup storage server does only that - storage of
backups. Nothing else. It's still running SuSE 9.3. The Bacula RPMs for
9.3 are from the 1.x tree, and all of my other machines are running
openSuSE 10.x, with Bacula 2.x. I gave it a shot but, sure enough, a
Bacula 2.x director won't jive with a 1.x storage daemon. And I'm in
dependency hell - Bacula 2.x requires upgrades of everything from the C
libs all the way up. So, I'm going to give a shot at an upgrade of the
storage machine via YaST, and see where I get.
