Title: Managing Ubiquiti Networks MAC ACLs from a script
Date: 2011-01-06 16:06
Author: admin
Category: Tech HowTos
Tags: airos, mac, PHP, security, ubiquiti, wap, wireless
Slug: managing-ubiquiti-networks-mac-acls-from-a-script

I have a small web-based tool for allowing members of an organization to
register their wireless MAC addresses, and then automatically adding
them to the MAC ACL on [Ubiquiti](http://www.ubnt.com) AirOSv2 APs. It's
a pretty quick hack, along with a simple and ugly web-based tool, but it
gets the job done for a non-profit with only 25 people. After [posting
about it on the Ubiquiti
forum](http://www.ubnt.com/forum/showthread.php?t=21133) and getting a
request from someone for the code, I decided to put it out there for
anyone who wants it. The script is mostly based on SCPing configs to and
from the AP and SSHing in to run commands, and will need passwordless
public key auth to the AP.

The code itself is in subversion at
[http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/](http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/).
It's composed of four files:

-   [updateAPconfigs.php.inc](http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/updateAPconfigs.php.inc)
    - the main PHP file with three functions for working with the APs
-   [wirelessTools.php](http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/wirelessTools.php)
    - My PHP page for users to add MACs. It's pretty rough and is mostly
    based on handling our LDAP authentication/group framework, but it
    gives a fair example of how I store MACs in a MySQL table and then
    rebuild a given AP config file with the current list of MACs. I
    doubt it will be useful to anyone else as more than an example.
-   [wireless.sql](http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/wireless.sql)
    - The schema for the SQL database I use to store MACs.
-   [README.txt](http://svn.jasonantman.com/misc-scripts/ubiquiti-mac-acl/README.txt)
    - Readme file including some warnings on the lack of error checking
    in the functions.

</p>
Hopefully this will be of some use to someone. I should probably mention
two important things here. First, the AP only accepts up to 32 MAC
addresses, so if you feed the `makeNewConfigFile()` function an array
with more than 32, it will just stop at the 32^nd^. Also, be aware, this
SCPs a config file to the AP, runs `cfgmtd` and the reboots the AP. If
you send it a bad config file, who knows what will happen. If you allow
your users to add MAC addresses, your APs will reboot every time someone
adds one.

All I ask is that if you use this, leave a comment to thank me, and if
you make any changes/additions/bugfixes, please send them back to me.

Also, I have some [Nagios check scripts](/2010/03/nagios-check-scripts/)
that are useful for Ubiquiti APs.
