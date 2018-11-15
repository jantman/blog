Title: The Death of a Disk
Date: 2007-09-07 11:34
Author: admin
Category: Hardware
Slug: the-death-of-a-disk

A few months ago, a disk on my Compaq Proliant ML370 went down. The
machine has 6 Ultra3 Wide SCSI 15k RPM drives, 18 Gb each, in a RAID
0+1, so I figured that between such a configuration and weekly complete
tape backups, I'd be pretty much set. At least for a "home" user. I
powered down the system (eek! downtime!), feeling lucky that it didn't
host any critical services. At a loss for a spare drive, and hoping that
the decade-old SCSI controller was just having a bad morning, I let the
system sit for a few hours and then powered up. It rebuilt any lost data
and came back fine.

Unfortunately, a week ago, the same problem happened. The good news is
that there wasn't much important "data" on the disk. The bad news is
that the disk was the root partition, and that I lost \*both\* mirrored
drives in a 42 minute window. The system is now down indefinitely,
pending my winning the lottery and getting the money for two 15k SCSI
disks.

Now, I originally wasn't too worried. The system is mainly used for
storing unimportant data. However, I quickly remembered three facts
about STOR1:

1.  My two and *only* tape drives are hooked up to this box.
2.  This box is my CVS server, so now not only are my nightly builds
    stopped, but I don't have CVS access.
3.  The To-Do list item stating "fix STOR1 backup script and re-enable
    cron job" should have been a higher priority.

So, in the future, you will not only read about data recovery operations
using a LiveCD, bare metal recovery of the system, but you can also
expect my [wiki](http://wiki.jasonantman.com) to include a page on
implementation of Bacula.
