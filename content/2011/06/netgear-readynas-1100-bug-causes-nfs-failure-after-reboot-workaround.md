Title: Netgear ReadyNAS 1100 Bug causes NFS Failure after reboot - workaround
Date: 2011-06-28 08:40
Author: admin
Category: Tech HowTos
Tags: appliance, embedded, linux, nas, netgear, nfs, readynas
Slug: netgear-readynas-1100-bug-causes-nfs-failure-after-reboot-workaround

At work, we have a [Netgear ReadyNAS
1100](http://www.readynas.com/?cat=23). It's a 4TB NAS appliance, a cute
little 1U half-depth Linux box with 4 SATA disks, a RAID controller, and
some firmware to do a whole bunch of fancy stuff (mainly geared towards
consumers and very small shops - all configuration is point-and-click
web UI). We've been using it for storing archived log data and
low-priority backups. At the beginning of this problem, it was running
RAIDiator 4.1.6 firmware since December of last year (over 6 months),
and hadn't had any configuration changes in at least 4 months.

Last week, I had to power off the unit and remove the power cables for
some rack maintenance. I went through the usual full shutdown procedure
in the web UI, and also told it to \`fsck\` the volumes, as that hadn't
been done in quite some time. Unfortunately, when the unit came back up,
even after I could log into the web UI, I couldn't mount the NFS shares
on my backup server. I kept getting messages like:

~~~~{.bash}
[root@backup-server ~]# mount -a
mount: mount to NFS server 'css-readynas' failed: RPC Error: Program not registered.
~~~~

so my next step was to check RPC status of the readynas, from the
client. That was also a bit of a surprise:

~~~~{.bash}
[root@backup-server ~]# rpcinfo -p css-readynas                        
   program vers proto   port                                              
    100000    2   tcp    111  portmapper                                  
    100000    2   udp    111  portmapper                                  
    100011    1   udp    620  rquotad                                     
    100011    2   udp    620  rquotad                                     
    100011    1   tcp    623  rquotad                                     
    100011    2   tcp    623  rquotad                                     
    100024    1   udp  32765  status                                      
    100024    1   tcp  32765  status                                      
    100005    1   udp   2051  mountd                                      
    100005    1   tcp   3006  mountd                                      
    100005    2   udp   2051  mountd                                      
    100005    2   tcp   3006  mountd                                      
    100005    3   udp   2051  mountd                                      
    100005    3   tcp   3006  mountd 
~~~~

Somewhere in that list is supposed to be nfsd, listening on port 2049.
Next, I did an nmap (port scan) of the readynas:

~~~~{.bash}
[root@backup-server ~]# nmap -sU -p2047-2050 css-readynas             

Starting Nmap 4.11 ( http://www.insecure.org/nmap/ ) at 2011-06-23 15:21 EDT
Interesting ports on css-readynas.rutgers.edu (172.16.25.108):              
PORT     STATE         SERVICE                                              
2047/udp closed        dls                                                  
2048/udp closed        dls-monitor                                          
2049/udp open|filtered nfs                                                  
2050/udp closed        unknown  
~~~~

Interesting. The port scan shows that *something* is listening on port
2049. But rpcinfo doesn't seem to recognize it as a NFS server.

At this point, through FrontView (the web UI) I backed up the
configuration and went through a few reboot cycles, with no change. I
then started tweaking everything I could that I thought would restart
the NFS server - I added and removed allowed hosts for the NFS share,
enabled and disabled sync mode, etc. I started searching the [ReadyNAS
Forum](http://www.readynas.com/forum/) and found a post that reported a
very similar problem - [upnpd grabbing nfsd
port](http://www.readynas.com/forum/viewtopic.php?f=20&t=23139). The
user reported that he was getting the same "RPC Error: Program not
registered" message, and in `daemon.log` on the ReadyNAS, found a line
including "storage nfsd[1087]: nfssvc: Address already in use". I
remembered that I'd setup the ReadyNAS to forward all logs to our
central syslog server and, sure enough, found an identical message that
something had already bound to UDP port 2049 when NFS was starting. I
tried confirming that upnpd was disabled and rebooting, but that didn't
help. Grepping my logs for "nfs" returned:

~~~~{.bash}
daemon.log:Jun 23 12:43:43 css-readynas nfsd[2331]: nfssvc: Address already in use
daemon.log:Jun 23 15:26:33 css-readynas nfsd[2724]: nfssvc: Address already in use
kern.log:Jun 23 11:35:29 css-readynas kernel: Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
kern.log:Jun 23 12:43:43 css-readynas kernel: NFSD: Using /var/lib/nfs/v4recovery as the NFSv4 state recovery directory
kern.log:Jun 23 12:43:43 css-readynas kernel: NFSD: starting 90-second grace period
kern.log:Jun 23 14:56:20 css-readynas kernel: Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
kern.log:Jun 23 15:12:41 css-readynas kernel: NFSD: starting 90-second grace period
kern.log:Jun 23 15:26:33 css-readynas kernel: NFSD: Using /var/lib/nfs/v4recovery as the NFSv4 state recovery directory
kern.log:Jun 23 15:26:33 css-readynas kernel: NFSD: starting 90-second grace period
~~~~

</p>
My next step was a few more reboots, with no change. I then upgraded the
RAIDiator firmware to the latest, 4.1.7. Still no luck. I installed the
[Enable root SSH](http://www.readynas.com/?p=4203) addon, and that's
when things became very clear:

~~~~{.bash}
css-readynas:/var/log# netstat -unlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name   
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           794/snmpd           
udp        0      0 0.0.0.0:514             0.0.0.0:*                           673/syslogd         
udp        0      0 172.16.25.108:137       0.0.0.0:*                           1672/nmbd           
udp        0      0 0.0.0.0:137             0.0.0.0:*                           1672/nmbd           
udp        0      0 172.16.25.108:138       0.0.0.0:*                           1672/nmbd           
udp        0      0 0.0.0.0:138             0.0.0.0:*                           1672/nmbd           
udp        0      0 0.0.0.0:161             0.0.0.0:*                           794/snmpd           
udp        0      0 0.0.0.0:162             0.0.0.0:*                           802/snmptrapd       
udp        0      0 0.0.0.0:2086            0.0.0.0:*                           1565/rpc.mountd     
udp        0      0 127.0.0.1:22081         0.0.0.0:*                           1599/raidard        
udp        0      0 172.16.25.108:22081     0.0.0.0:*                           1599/raidard        
udp        0      0 0.0.0.0:22081           0.0.0.0:*                           1599/raidard        
udp        0      0 0.0.0.0:988             0.0.0.0:*                           819/rpc.rquotad     
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           729/avahi-daemon: r 
udp        0      0 0.0.0.0:111             0.0.0.0:*                           666/portmap         
udp        0      0 0.0.0.0:881             0.0.0.0:*                           1553/rpc.statd      
udp        0      0 0.0.0.0:32765           0.0.0.0:*                           1553/rpc.statd     
~~~~

</p>
For some ***very*** strange reason, snmpd had bound to port 2049 (the
nfs port) instead of 161. That left no port for nfs to bind to.

**Solution:**

<p>
~~~~{.bash}
 
css-readynas:/var/log# /etc/init.d/snmpd stop                                                       
Stopping network management services: snmpd snmptrapd readynas-agent.                               
css-readynas:/var/log# /etc/init.d/nfs-kernel-server start
Exporting directories for NFS kernel daemon...done.
Starting NFS kernel daemon:mount: nfsd already mounted or /proc/fs/nfsd/ busy
mount: according to mtab, nfsd is mounted on /proc/fs/nfsd
 statd nfsd mountd.
css-readynas:/var/log# /etc/init.d/snmpd start
Starting network management services: snmpd snmptrapd readynas-agent.
~~~~

Stop snmpd, restart nfs-kernel-server so that it grabs port 2049 like it
should, and then start snmpd back up. If all went well, nfsd should now
be listening on UDP 2049, and snmpd should be listening on UDP 161 like
it should. To confirm:

~~~~{.bash}
css-readynas:/var/log# netstat -unlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           -
udp        0      0 0.0.0.0:514             0.0.0.0:*                           673/syslogd
udp        0      0 172.16.25.108:137       0.0.0.0:*                           1672/nmbd
udp        0      0 0.0.0.0:137             0.0.0.0:*                           1672/nmbd
udp        0      0 172.16.25.108:138       0.0.0.0:*                           1672/nmbd
udp        0      0 0.0.0.0:138             0.0.0.0:*                           1672/nmbd
udp        0      0 0.0.0.0:161             0.0.0.0:*                           26161/snmpd
udp        0      0 0.0.0.0:162             0.0.0.0:*                           26163/snmptrapd
udp        0      0 0.0.0.0:2086            0.0.0.0:*                           1565/rpc.mountd
udp        0      0 127.0.0.1:22081         0.0.0.0:*                           1599/raidard
udp        0      0 172.16.25.108:22081     0.0.0.0:*                           1599/raidard
udp        0      0 0.0.0.0:22081           0.0.0.0:*                           1599/raidard
udp        0      0 0.0.0.0:988             0.0.0.0:*                           819/rpc.rquotad
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           729/avahi-daemon: r
udp        0      0 0.0.0.0:2158            0.0.0.0:*                           -
udp        0      0 0.0.0.0:111             0.0.0.0:*                           666/portmap
udp        0      0 0.0.0.0:2160            0.0.0.0:*                           26161/snmpd
udp        0      0 0.0.0.0:881             0.0.0.0:*                           1553/rpc.statd
udp        0      0 0.0.0.0:32765           0.0.0.0:*                           1553/rpc.statd
~~~~

All is well. Now to confirm this from the client machine:

~~~~{.bash}
[root@backup-server ~]# rpcinfo -p css-readynas
   program vers proto   port
    100000    2   tcp    111  portmapper
    100000    2   udp    111  portmapper
    100011    1   udp    988  rquotad
    100011    2   udp    988  rquotad
    100011    1   tcp    991  rquotad
    100011    2   tcp    991  rquotad
    100024    1   udp  32765  status
    100024    1   tcp  32765  status
    100005    1   udp   2086  mountd
    100005    1   tcp   3131  mountd
    100005    2   udp   2086  mountd
    100005    2   tcp   3131  mountd
    100005    3   udp   2086  mountd
    100005    3   tcp   3131  mountd
    100003    2   udp   2049  nfs
    100003    3   udp   2049  nfs
    100003    4   udp   2049  nfs
    100003    2   tcp   2049  nfs
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100021    1   udp   2158  nlockmgr
    100021    3   udp   2158  nlockmgr
    100021    4   udp   2158  nlockmgr
    100021    1   tcp   4189  nlockmgr
    100021    3   tcp   4189  nlockmgr
    100021    4   tcp   4189  nlockmgr
~~~~

Ok, NFS is now there. It all looks good, and re-running `mount -a` on
the client successfully mounts the NFS share.

We'll see what happens next time I have to reboot the ReadyNAS. In the
mean time, I'm going to try to bring this to the attention of Netgear
support and hope they do something about it.
