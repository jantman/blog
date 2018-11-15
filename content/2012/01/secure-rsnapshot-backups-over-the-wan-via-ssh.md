Title: Secure rsnapshot backups over the WAN via SSH
Date: 2012-01-15 17:26
Author: admin
Category: Software
Tags: backups, linode, rsnapshot, rsync, security, ssh, wrapper
Slug: secure-rsnapshot-backups-over-the-wan-via-ssh

Since I moved all of my WAN-facing stuff (mail, web, this blog, svn
etc.) to a virtual server with [Linode](http://www.linode.com), and just
have a desktop at home, it's no longer practical to use
[Bacula](http://www.bacula.org/) for backups. Linode manages daily and
weekly backups through their backup service, but they'll only restore a
full filesystem at a time. I wanted something that would keep daily and
weekly incremental backups long enough that I could find a file changed
(or accidentally deleted) a few days or weeks ago. Since I'd be backing
up to my desktop at home (which is on a residential dynamic IP
connection), the logical solution was something using
[rsync](http://rsync.samba.org/). Even better than that is the
[rsnapshot](http://rsnapshot.org/) tool, which builds upon rsync and
hard links to manage incremental backups with as little disk usage as
possible (though I'd certainly recommend excluding log files).

I'm pretty strict about security. Since my home connection has a dynamic
IP, things are a bit more complicated - I can't push from the server, I
can't ACL or firewall the server to just my home IP, and an IPsec VPN
would be difficult to accomplish (not to mention add a lot of overhead
to big file transfers). So, I opted for a solution that uses SSH
key-based authentication, forced comands, and a C wrapper.

The configuration of rsync and rsnapshot is mostly out of the scope of
this post. There are plenty of good resources for that, so I'll just
cover the things that won't be found in most tutorials. Also, I'll be
referring to the remote machine to be backed up as the "remote host" and
the local machine which triggers the backup and stores the data as the
"local host".

## Local Host Setup - Part I

1.  Choose and create a directory to store your backups in. I have a 1TB
    external disk mounted at `/mnt/backup/`, so I chose
    `/mnt/backup/rsnapshot/`.
2.  Generate two sets of password-less SSH keys using the `ssh-keygen`
    program. One will be used to run the rsync command on the remote
    host, the other will be used to trigger your pre- and post-backup
    scripts. Name them accordingly (i.e.
    "remoteHostname\_remoteBackupUsername\_cmd" and
    "remoteHostname\_remoteBackupUsername\_rsync"). Now, get (scp) the
    public key for each pair to the remote host.

## Remote Host Setup

1.  Ensure that rsync is installed on the host.
2.  Create a user to run the backups. I called this user "rsyncuser".
    Create a home directory, and a group for the user. Do not set a
    password (you don't want password logins).
3.  Copy the public key files you created above to the user's `~/.ssh/`
    directory.
4.  Cat the "remoteHostname\_remoteBackupUsername\_cmd" public key into
    the user's `~/.ssh/authorized_keys` file.
5.  Now comes the first fun part. Let's assume that your pre- and
    post-backup scripts are `/root/bin/rsnapshot-pre.sh` and
    `/root/bin/rsnapshot-post.sh`, respectively. As root, grab a copy of
    cmd-wrapper.c (from
    [GitHub](https://github.com/jantman/misc-scripts/blob/master/cmd-wrapper.c)
    or at the bottom of this post). Modify for your use - the only thing
    likely to change is line 38, which ensures it will only run for a
    member of GID 502. Change this to rsyncuser's GID. Compile the
    wrapper with `gcc -o cmd-wrapper cmd-wrapper.c`. Copy it to
    rsyncuser's home directory (/home/rsyncuser), `chown root:rsyncuser`
    and `chmod 4750`. Yes, this sets the SUID bit. The program will now
    be owned by root, and runnable *as root* by rsyncuser (or, more
    specifically, any member of the rsyncuser group).
6.  Open rsyncuser's `.ssh/authorized_keys` file in a text editor. At
    the beginning of the "remoteHostname\_remoteBackupUsername\_cmd" key
    line, prepend `command="/home/rsyncuser/cmd-wrapper"`. This sets up
    SSH forced command (there's a good overview in [O'Reilly's SSH: The
    Definitive
    Guide](http://oreilly.com/catalog/sshtdg/chapter/ch08.html)) so that
    when this key is used to login, it will directly execute
    `/home/rsyncuser/cmd-wrapper` and then exit, without allowing access
    to anything else.
7.  Add rsyncuser to `AllowUsers` in `/etc/ssh/sshd_config` (you *do*
    limit user access via SSH, right?) and then reload sshd.
8.  Now, if you SSH to rsyncuser@remoteHost from the local host, using
    the "\_cmd" ssh key and a command of "pre" (i.e.
    `ssh -i /path/to/remoteHostname_remoteBackupUsername_cmd rsyncuser@remoteHost pre`),
    it should execute `/root/bin/rsnapshot-pre.sh` ad root, and you
    should see the output locally.
9.  Repeat the above step for the post-backup script (replacing "pre"
    above with "post"). You should now have your pre- and post-backup
    scripts working, and triggered remotely. *(Note: these steps, and
    some of the other setup here, is a bit more complex so that it will
    work better with rsnapshot backups of multiple remote hosts.)*
10. Cat the "remoteHostname\_remoteBackupUsername\_rsync" public key
    into the backup user's `~/.ssh/authorized_keys` file.
11. As root, grab a copy of rsync-wrapper.c (from
    [GitHub](https://github.com/jantman/misc-scripts/blob/master/rsync-wrapper.c)
    or at the bottom of this post). Modify for your use - the only thing
    likely to change is line 38, which ensures it will only run for a
    member of GID 502 (change this to rsyncuser's GID), and perhaps the
    path of or arguments passed to rsync (the wrapper will call
    `/usr/bin/rsync --server --sender -vlogDtprRe.iLsf --numeric-ids . /`).
    Compile the wrapper with `gcc -o rsync-wrapper rsync-wrapper.c`.
    Copy it to rsyncuser's home directory (/home/rsyncuser),
    `chown root:rsyncuser` and `chmod 4750`.
12. Open rsyncuser's `.ssh/authorized_keys` file in a text editor. At
    the beginning of the "remoteHostname\_remoteBackupUsername\_rsync"
    key line, prepend `command="/home/rsyncuser/rsync-wrapper"`. This
    will run rsync with the arguments specified in rsync-wrapper.c every
    time this key is used to login.

## Local Host Setup - Part II

I use totally separate configs for each host that I backup, to keep
things clean and to let me enable, disable, or tweak one remote backup
without affecting the others.

1. Create host-specific pre- and post-backup scripts. I put them in
    `/etc/rsnapshot.d/`.
    `/etc/rsnapshot.d/pre-remoteHostName.sh`:

        :::bash
        #!/bin/bash
        
        # do anything else needed on the local system before a backup
        ssh -i /path/to/remoteHostname_remoteBackupUsername_cmd rsyncuser@remoteHost pre

    `/etc/rsnapshot.d/post-remoteHostName.sh`:

        :::bash
        #!/bin/bash

        # do anything else needed on the local system after a backup
        ssh -i /path/to/remoteHostname_remoteBackupUsername_cmd rsyncuser@remoteHost post

2.  Setup a set of rsync include and exclude files (see `man rsync(1)`,
    `--include-from=` and `--exclude-from=`). I put mine at
    `/etc/rsnapshot.d/rsync-include-remoteHostName.txt` and
    `/etc/rsnapshot.d/rsync-exclude-remoteHostName.txt`, respectively.
    (Examples included at the bottom of this post).
3.  Configure rsnapshot. I use a separate config file for each remote
    host. Copy the default `/etc/rsnapshot.conf` to
    `/etc/rsnapshot-remoteHostName.conf`. The important items are
    `rsync_short_args`, `rsync_long_args`, `ssh_args`, `cmd_preexec`,
    `cmd_postexec` and `backup`. Here's an example of my config file,
    with comments and blank lines removed:

        config_version  1.2
        snapshot_root   /mnt/backup/rsnapshot/
        cmd_cp          /bin/cp
        cmd_rm          /bin/rm
        cmd_rsync       /usr/bin/rsync
        cmd_ssh         /usr/bin/ssh
        cmd_logger      /bin/logger
        cmd_du          /usr/bin/du
        cmd_rsnapshot_diff      /usr/bin/rsnapshot-diff
        interval        daily   14 # save 14 daily backups
        interval        weekly  6 # save 6 weekly backups
        verbose         2
        loglevel        3
        logfile /var/log/rsnapshot-remoteHostName.log
        lockfile        /var/run/rsnapshot-remoteHostName.pid
        rsync_short_args        -a
        rsync_long_args --delete --numeric-ids --relative --delete-excluded
        ssh_args        -i /path/to/remoteHostname_remoteBackupUsername_rsync
        exclude_file    /etc/rsnapshot.d/rsync-exclude-remoteHostName.txt
        include_file    /etc/rsnapshot.d/rsync-include-remoteHostName.txt
        link_dest       1
        use_lazy_deletes        1
        cmd_preexec     /etc/rsnapshot.d/pre-remoteHostName.sh
        cmd_postexec    /etc/rsnapshot.d/post-remoteHostName.sh
        backup  rsyncuser@remoteHostName:/      remoteHostName/

    The `backup` line is what tells rsync what to back up (`/` on
    remoteHostName, logging in as rsyncuser), and where to back up to
    (snapshot\_root/remoteHostName/).

4.  Create two scripts that will actually trigger the backups, which
    I'll call `/root/bin/rsnapshot-daily.sh` and `/root/bin/rsnapshot-weekly.sh`:

    `/root/bin/rsnapshot-daily.sh`:

        :::bash
        #!/bin/bash

        /usr/bin/rsnapshot -c /etc/rsnapshot-remoteHostName.conf daily
        # add other hosts here; note, they'll run in series

    `/root/bin/rsnapshot-weekly.sh`:

        :::bash
        #!/bin/bash

        /usr/bin/rsnapshot -c /etc/rsnapshot-remoteHostName.conf weekly
        # add other hosts here; note, they'll run in series

5.  Add two entries to root's croontab to run the rsnapshot backups.
    Adjust the following days and times to your liking:

        :::text
        0 1 * * Mon /root/bin/rsnapshot-weekly.sh # run the weekly backups every Monday at 01:00
        30 2 * * * /root/bin/rsnapshot-daily.sh # run the daily backups every day at 02:30, which *should* be after the weekly finished on Monday morning

6.  Check, after the next scheduled runs, that everything appears to
    have run correctly. If you want, you can manually trigger the daily
    script and watch what happens. If you do this more than once, you
    should delete the directories it creates, or else rotation will be
    messed up. If you have issues with rsync, aside from the usual
    troubleshooting, check that rsync-wrapper.c is calling rsync with
    the same arguments that rsnapshot is sending. It may be useful to
    use my
    [print-cmd.sh](https://github.com/jantman/misc-scripts/blob/master/print-cmd.sh)
    script in place of the "rsync-wrapper" forced command. This script
    will simply log the command rsnapshot calls via SSH.

Assuming all of this worked, you should now have a fairly secure
SSH-based remotely-triggered backup system. In a follow-up post I
provide my [Nagios Check Plugin for Rsnapshot
Backups](/2012/02/nagios-check-plugin-for-rsnapshot-backups/).

The referenced scripts, config files, etc. are below:

`cmd-wrapper.c`:

~~~~{.c}
#include 
#include 
#include 
#include 
#include 
#include 

/********************************************
 * Wrapper - Secure Yourself                
 *                                          
 * 2007 - Mike Golvach - eggi@comcast.net   
 * Modified 2012 by Jason Antman  
 *  - configured for use as pre- and post-backup script wrapper
 *                                          
 * USAGE: cmd-wrapper [pre|post]
 *
 * $HeadURL: http://svn.jasonantman.com/misc-scripts/cmd-wrapper.c $
 * $LastChangedRevision: 26 $
 *                                          
 ********************************************/

/* Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License */

/* Define global variables */

int gid;

/* main(int argc, char **argv) - main process loop */

int main(int argc, char **argv, char **envp)
{
  char *origcmd;

  origcmd = getenv("SSH_ORIGINAL_COMMAND");

  /* printf ("Original Command:%s\n", origcmd); */

  /* Set euid and egid to actual user */

  gid = getgid();
  setegid(getgid());
  seteuid(getuid());

  /* Confirm user is in GROUP(502) group */

  if ( gid != 502 ) {
    printf("User Not Authorized! Exiting...\n");
    exit(1);
  }

  /* Check argc count only at this point */

  if ( argc != 1 ) {
    printf("Usage: cmd-wrapper [pre|post]\n");
    exit(1);
  }

  /* Set uid, gid, euid and egid to root */

  setegid(0);
  seteuid(0);
  setgid(0);
  setuid(0);

  /* Check argv for proper arguments and run
   * the corresponding script, if invoked.
   */

  if ( strncmp(origcmd, "pre", 3) == 0 ) {
    if (execl("/root/bin/rsnapshot-pre.sh", "rsnapshot-pre.sh", NULL) < 0) {
      perror("Execl:");
    }
  } else if ( strncmp(origcmd, "post", 4) == 0 ) {
    if (execl("/root/bin/rsnapshot-post.sh", "rsnapshot-post.sh", NULL) < 0) {
      perror("Execl:");
    }
  } else {
    printf("ERROR: Invalid command: %s\n", origcmd);
    printf("Usage: COMMAND [pre|post]\n");
    exit(1);
  }
  exit(0);
}
~~~~

`rsync-wrapper.c`:

~~~~{.c}
#include 
#include 
#include 
#include 
#include 

/********************************************
 * Wrapper - Secure Yourself                
 *                                          
 * 2007 - Mike Golvach - eggi@comcast.net   
 * Modified 2012 by Jason Antman  
 *  - configured for use as rsync wrapper
 *                                          
 * $HeadURL: http://svn.jasonantman.com/misc-scripts/rsync-wrapper.c $
 * $LastChangedRevision: 26 $
 *                                          
 ********************************************/

/* Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License */

/* Define global variables */

int gid;

/* main(int argc, char **argv) - main process loop */

int main(int argc, char **argv)
{

  /* Set euid and egid to actual user */

  gid = getgid();
  setegid(getgid());
  seteuid(getuid());

  /* Confirm user is in GROUP(502) group */

  if ( gid != 502 ) {
    printf("User Not Authorized! Exiting...\n");
    exit(1);
  }

  /* Check argc count only at this point */

  if ( argc != 1 ) {
    printf("Usage: rsync-wrapper\n");
    exit(1);
  }

  /* Set uid, gid, euid and egid to root */

  setegid(0);
  seteuid(0);
  setgid(0);
  setuid(0);

  /* Check argv for proper arguments and run
   * the corresponding script, if invoked.
   */
  if (execl("/usr/bin/rsync", "rsync", "--server", "--sender", "-vlogDtprRe.iLsf", "--numeric-ids", ".", "/", NULL) < 0) {
    perror("Execl:");
  }
  exit(0);
}
~~~~

`/etc/rsnapshot.d/rsync-include-remoteHostName.txt`:

~~~~{.text}
# Include
+ /dev/console
+ /dev/initctl
+ /dev/null
+ /dev/zero
+ /usr/local/*
~~~~

`/etc/rsnapshot.d/rsync-exclude-remoteHostName.txt`:

~~~~{.text}
# Exclude
- /cgroup/*
- /dev/*
- /lib/*
- lost+found/
- /proc/*
- /sys/
- /tmp/
- /var/log/*
~~~~
