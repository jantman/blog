Title: Netgear ReadyNAS 1100 and long UID numbers
Date: 2009-06-23 16:45
Author: admin
Category: Hardware
Tags: debian, helpdesk, netgear, readynas
Slug: netgear-readynas-1100-and-long-uid-numbers

I spent part of the day installing a [Netgear ReadyNAS
1100](http://www.netgear.com/Products/Storage/ReadyNAS1100.aspx) for
backup storage. It's a cute little 1U storage appliance with 4 SATA disk
bays, two Gig copper ports and about every sort of hokey service you
could possibly want in something that's billed as a small business
storage server but running a sort-of-scaled-up home appliance OS. That
being said, it comes at a wonderful price (we bought one empty and added
4x 1.5TB disks) and runs Linux.

I had a few minor issues with the installation (more along the lines of
trying to do things that weren't clearly documented rather than problems
with the unit). NetGear tech support ("ProSupport Labs") was quite good
once I got past the first level or two, and Mark H. who helped me with
most of my issues was one of the best tech support people I've ever
spoken to. In fact, he probably ties with [Paulo from
HP](/2007/03/managing-g1-proliant-servers-with-modern-linux/)
for the best tech support person I've ever dealt with.

Anyway, the only issue with the NetGear installation that we weren't
able to resolve was the fact that the web configuration tool
("Frontview") will only accept UIDs of a maximum of five characters.
Here at Rutgers, we have a unified UID space, with numbers well in
excess of 100,000. As a result, my plan of having NFS play well wasn't
really going to work. Mark wasn't able to come up with a solution
(obviously - it's something that, at best, can get fixed in the next
version of the firmware) but he took copious notes, had me confirm them,
and told me he'd bring it up to the ReadyNAS engineering team when they
meet Thursday, and will try and e-mail me back to follow up. He also
spent quite some time on the phone with me, both of us researching what
kernel the ReadyNAS 4.1.5 firmware runs (2.6.17.8, mostly vanilla Debian
as per mark) and when long UID support was available (at least 2.4).
Overall, I was very impressed that Mark knew quite a bit about Linux -
even more than your average Linux desktop user - and quite a bit about
the internals of the ReadyNAS.

Just on a hunch, after my tech support call, I used the Frontview
"Config Backup" tool's "Users and Groups" option to backup the user and
group information. Sure enough, it was just a force-download of a Zip
archive... of the pertinent files. I was able to hand-hack /etc/passwd
and re-upload it, and it seemed to work fine.

*The following is **NOT** endorsed by Netgear in any way, shape or form.
It's a hack that may or may not work. Do this at your own risk - I have
no idea if some future (or past) firmware change might make bad things
happen, or whether there are some features which don't jive with this.
All I've tested is HTTP logins, the fact that the web interface shows
the \>2\^16 UID correctly, and NFS.*

**Procedure:**

1.  Create desired user in Frontview tool, leaving UID field blank. (In
    my case, the user is assigned the next sequential UID, 1002).
2.  Frontview "System" -\> "Config Backup", "Backup" tab, select only
    "Users and Groups".
3.  Download config files and unzip.
4.  Open `/etc/passwd` from the config archive in a text editor, change the
    automatically assigned UID (1002) to the desired UID (101739).
5.  Re-zip the directory tree and re-upload to ReadyNAS.
6.  Enjoy.

