Title: Getting Sun iLOM information within Linux
Date: 2010-09-16 10:28
Author: admin
Category: Tech HowTos
Tags: inventory, ipmi, ipmitool, ocs-inventory, sun, sunfire, sysadmin
Slug: getting-sun-ilom-information-within-linux

At work, I'm starting to implement [OCS Inventory
NG](http://www.ocsinventory-ng.org/) on our Linux boxes to keep track of
hardware. Part of the plan is also that we have a
[MediaWiki](http://www.mediawiki.org) installation for internal
documentation, and articles for every host (named as the hostname). I'm
going to pull data from OCS into the articles based on hostname (via a
PHP include) so the documentation will automatically include up-to-date
information on hardware.

Since we're moving to MySQL-backed DHCP, I decided that it would also be
nice to include DHCP information and links to our web tool to edit the
host (like setting PXE boot information). This is pretty easy for the
ethX interfaces, as OCS collects MAC addresses and I can search our DHCP
database for them. However, it isn't as simple for the iLOM interface,
which (obviously) OCS knows nothing about - though it's arguably one of
the most-forgotten things on our machines.

I know that HP Proliant servers have the nice little HP PSP (Proliant
Support Pack) that includes tools such as `hpasmcli`, but Sun doesn't
have anything like that. (We just have one HP box in production right
now, but I'll probably be adding support for it soon).

Enter [OpenIPMI](http://openipmi.sourceforge.net/). The iLOM has an IPMI
interface, and the standard OpenIPMI-tools package in CentOS
repositories has the ipmitool required to get the relevant information.
A call is pretty simple: `ipmitool -l open lan print 1` yields something
like:  

` Set in Progress         : Set Complete Auth Type Support       : NONE MD2 MD5 PASSWORD Auth Type Enable        : Callback : MD2 MD5 PASSWORD                         : User     : MD2 MD5 PASSWORD                         : Operator : MD2 MD5 PASSWORD                         : Admin    : MD2 MD5 PASSWORD                         : OEM      : IP Address Source       : DHCP Address IP Address              : 172.16.xxx.xxx Subnet Mask             : 255.255.255.224 MAC Address             : 00:14:4f:xx:xx:xx SNMP Community String   : xxxxxx IP Header               : TTL=0x00 Flags=0x00 Precedence=0x00 TOS=0x00 BMC ARP Control         : ARP Responses Disabled, Gratuitous ARP Disabled Gratituous ARP Intrvl   : 5.0 seconds Default Gateway IP      : 172.16.xx.xx Default Gateway MAC     : 00:00:00:00:00:00 Backup Gateway IP       : 0.0.0.0 Backup Gateway MAC      : 00:00:00:00:00:00 802.1q VLAN ID          : Disabled 802.1q VLAN Priority    : 0 RMCP+ Cipher Suites     : 2,3,0 Cipher Suite Priv Max   : XXXXXXXXXXXXXXX                         :     X=Cipher Suite Unused                         :     c=CALLBACK                         :     u=USER                         :     o=OPERATOR                         :     a=ADMIN                         :     O=OEM`  
Now it's just a matter of integrating this into ocsinventory-agent,
having it run the command if present (and Sun hardware), and parsing the
results. Once I have some actual code done, I'll pass it along.

Many thanks to `pseud0` on the Sun forums for answering my
[question](http://forums.sun.com/thread.jspa?messageID=11049794#11049794)
about this.
