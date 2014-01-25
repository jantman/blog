Title: Tech - Updates
Date: 2007-12-11 15:54
Author: admin
Category: Projects
Tags: passwords
Slug: tech-updates

First of all, until I decide on either splitting my blog, or setting up
separate 'channels' for personal and technical stuff, I'll annotate the
difference in post titles.

So I have a few days of sanity - the last week of classes - before exam
time. Hopefully I'll wrap some things up, and even finish my Christmas
shopping ([ThinkGeek](http://www.thinkgeek.com) will be happy...). I
don't have a whole lot of real value to say, but a few notes on upcoming
projects.

-   I'm going to be buying a few SunBlade 100s and 150s as surplus from
    Rutgers. I'm probably going to have one or two running at home
    replacing my ancient mail server. I might also bring my PowerEdge
    2550 home to virtualize a few of my machines - though, arguably, my
    two backup machines are the best candidates, though I don't like the
    idea of virtualizing backups.
-   I think the new mail server will run Solaris, though I haven't
    looked into the technicalities of
    Procmail/Postfix/SpamAssassin/some-IMAP-server on Solaris.
-   [Print
    Accounting](http://www.jasonantman.com/blog/2007/11/print-accounting.html)
    is finished, though the GUI isn't completely done. I'll have it in
    CVS sometime this week.

I'm thinking about password managers. I posted a comment to the
[SAGE](http://www.sage.org/) mailing list, but didn't get many helpful
replies. I'm looking for a solution that can keep track of all of my
usernames and passwords. It needs to be secure. Very secure. I'd like to
set separate passwords for almost every machine/account that I have.
More importantly, I want something easily portable. Unfortunately, I
find things like the
[Mandylion](http://www.thinkgeek.com/gadgets/security/91a2/) a bit
limiting - not only does the device generate passwords for you, so you
can't really store many notes (I might want to keep track of a URL, name
for the entry, username, member number, etc.) but it's also a single
hardware device - no way to back it up, and easy to lose. I also saw the
[IronKey](http://www.thinkgeek.com/gadgets/security/99f1/) which sounds
damn good - especially the Mission Impossible-esque self-destructing
encryption chip. But that means that some @$$ just has to type in 10
incorrect passwords and it's useless. Moreover, it needs to be plugged
into a system, so if I don't have a laptop and I'm not at a trusted
terminal, there's ample security risk.

I talked to my roommate (an EE major) about hardware solutions, but they
seem to be a bit expensive and way too much R&D time. So, it seems like
the only real solution is software. At the moment, what I have to work
with includes a [Nokia 770 Internet
Tablet](http://maemo.org/community/wiki/nokia_770_hardware_specification/),
a Blackberry 7250 (hopefully being replaced by a Treo 650p or 700p
soon), an array of Linux desktops, and my laptop (right now a Linux box
that stays on my desk, but maybe a MacBook, iBook, or [Asus
eeePC](http://eeepc.asus.com/) soon).

The overall idea is to create a set (or trio, or quartet) of
applications to act as a password manager. They would store passwords
and related information (initial acitvation date, reset date, scheduled
reset date, username, system/site name, notes) in a flat file or a
simple database like
[BDB](http://www.oracle.com/technology/products/berkeley-db/index.html).
That file would then be encrypted using GNUpg and strong encryption.
Another possibility is separate files per "class" of password, such as
one for root accounts, one for user accounts, one for web sites, etc.
with different encryption strength for each class (speed may be an issue
for en/decrypting large files on small devices like phones.

In terms of the program, ideally I'd have a graphical client for my
phone (Treo or Blackberry) probably written in Java, a graphical client
for the Nokia 770 (maybe Java, maybe something using Python and native
GTK), a graphical client for my laptop, and a CLI client for the 770 and
laptop. Databases would have to be sync'ed across machines - the 770 is
easy enough to just find the newest file and copy it, or manually
decrypt, diff, and then encrypt. I don't know how I'd do it on the
phones, the only thing I can think of right now is to pay for data
usage, and then manually copy over to the phone (either via SFTP, SCP,
or a HTTPS connection).
