Title: Centralized Storage via SFTP
Date: 2008-04-21 17:28
Author: admin
Category: Tech HowTos
Tags: fuse, sftp, ssh, sshfs, storage
Slug: centralized-storage-via-sftp

For quite a while, I've been planning on centralizing a lot of my
personal storage (documents, miscellaneous stuff) on one machine at
home. The biggest problem that I have is that, while a VPN would be a
good solution for my apartment (if I could get [IPcop][]to do VPN
between two dynamic IPs), it doesn't really work for my mobile life. My
laptop is often connected to untrusted wireless, and unknown firewall
configurations, so VPN isn't always the best (and definitely not the
easiest) option. Given road warrior use, NFS is obviously out of the
question.

After a little searching, I found the [SSHFS][] module for [FUSE][],
which allows userspace mounting of a SFTP filesystem. Despite some
initial hiccups, I managed to get it setup on two machines - my laptop
and a desktop in the apartment. This week I'll finish working on the
rest of the machines - and eventually replace my aging [SSH gateway][]
machine (currently a 10-year-old Gateway mini tower) with a [Soekris][]
box.

The setup was pretty easy:

1.  Make sure you have public key authentication setup for ssh between
    the machines, using RSA keys.
2.  Make sure fuse, libfuse, and the related packages are installed.
3.  Install the sshfs package.
4.  Make sure your user is added to the "trusted" group (for OpenSuSE).

After that, just give it a spin, as the user that you want to mount the
filesystem as:

`sshfs hostname:/path/to/mount /path/to/local/mountpoint`

Once that worked pefectly, I added the following to my .bash\_profile:

`# this handles SSHFS mount of the central-home dirif [ -a /path/to/local/mountpoint ]; then  echo "HOSTNAME home is mounted at /path/to/local/mountpoint"else  echo "Mounting HOSTNAME home at /path/to/local/mountpoint..."hostname:/path/to/mount /path/to/local/mountpoint`  
`fi`

  [IPcop]: http://www.ipcop.org/
  [SSHFS]: http://fuse.sourceforge.net/sshfs.html
  [FUSE]: http://fuse.sourceforge.net/
  [SSH gateway]: http://www.jasonantman.com/wiki/index.php/SSH_Gateway_Box
  [Soekris]: http://www.soekris.com/
