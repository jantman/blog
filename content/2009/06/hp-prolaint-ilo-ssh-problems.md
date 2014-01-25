Title: HP Prolaint iLO SSH Problems
Date: 2009-06-11 23:52
Author: admin
Category: Tech HowTos
Tags: ilo, openssh, proliant, ssh
Slug: hp-prolaint-ilo-ssh-problems

There's a known issue with the SSH implementation in the iLO firmware
for HP Proliant servers (specifically G2 and G3) and OpenSSH 5.1p1.
There was a
[thread](http://marc.info/?l=openssh-unix-dev&m=122095298729858&w=2) on
the OpenSSH developers list that referenced this problem and suggested a
solution, but it doesn't seem to be a sure fix.

This problem is present on my DL360 G2's which are running the 1.84
2006-05-05 version of the iLO firmware (iLO 1.84 pass9) with the P26
2004.05.01 version of the system firmware. I also see the issue on a
DL380G3 running iLO 1.92 2008.04.24 and system firmware P29 2004.09.15.
The only way that I can reliably get into the iLO is by SSHing from a
box with an older version of SSH, such as 4.2p1.

<p>
Most of the things that I could find online referenced unsetting the
LANG environment variable:

~~~~{.bash}
unset LANG
~~~~

and then SSHing with agent forwarding disabled:

~~~~{.bash}
ssh -a hostname-ilo
~~~~

Unfortunately this combination doesn't seem to do it for me.

I happened to stumble by [this
post](http://www.mail-archive.com/debian-ssh@lists.debian.org/msg00904.html)
to the debian-ssh mailing list, which suggested that shortening the new
OpenSSH version string fixed the problem.

I was able to confirm that the version string is, in fact, the sole
problem. I downloaded the source of OpenSSH 5.2p1 and, with the
following small patch to version.h, managed to get SSH working to the
iLO perfectly:

~~~~{.diff}
--- openssh-patched/version.h   2009-06-12 00:35:48.000000000 -0400
+++ openssh-5.2p1/version.h     2009-02-22 19:09:26.000000000 -0500
@@ -1,6 +1,6 @@
 /* $OpenBSD: version.h,v 1.55 2009/02/23 00:06:15 djm Exp $ */

-#define SSH_VERSION    "OpenSSH"
+#define SSH_VERSION    "OpenSSH_5.2"

-#define SSH_PORTABLE   ""
+#define SSH_PORTABLE   "p1"
 #define SSH_RELEASE    SSH_VERSION SSH_PORTABLE
~~~~

</p>
I patched version.h, ran \`./configure\`, \`make\`, and then copied the
compiled ssh binary to /usr/bin/ilossh, so that my original ssh binary
would be intact, and the ilossh binary would be left alone by RPM
upgrades.
