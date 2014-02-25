Title: Vyatta Initial Impressions
Date: 2009-02-26 10:06
Author: admin
Category: Projects
Tags: cisco, networking, router, vyatta
Slug: vyatta-initial-impressions

I'm part-way through the major overhaul of my home network (hosting this
blog and everything else jasonantman.com) that I've been planning for
quite some time. The current hardware is... uh... currently... described
on my Hardware
page, but I soon plan on ditching the wiki and moving to a CMS for my
entire site.

Anyway, so far I've decommissioned my aged HP ProCurve 2424M switch
and replaced it with used but less-aged Cisco 2948G from [Horizon
Datacom](http://horizondatacom.com/) (purchased on Ebay). Quite an
upgrade. In order to handle network backups a little better, I'm also
adding a Cisco 4912G 12-port Gigabit (GBIC) aggregation switch for the
administrative/backup VLAN - though this was purchased via ebay from
[RedApe Technologies](http://stores.ebay.com/RedApe-Technologies) in PA.
The switch came with 12 1000BASE-SX GBICs, and I plan to do a mix of
copper (1000BASE-T) where it's already available (onboard NICs) and
1000BASE-SX where there's enough room in the box for a card.

On the hardware side, I also have 2 new boxes - a set of HP Proliant
[DL360
G2](http://h18000.www1.hp.com/products/quickspecs/11049_na/11049_na.HTML)'s
from [MJS Global](http://www.mjsglobal.com/), who I've done business
with before. The prices were great, and though one of them showed up
with a faulty temperature sensor that prevents boot, MJS has been
wonderful and is shipping me a replacement motherboard. One of the boxes
will be running [Vyatta](http://www.vyatta.org/) (vee-AH-tha) VC5
router/firewall software, and the other will be a new services box
running internal DNS, DHCP, NTP, and whatever else.

On the hardware side, I'm also planning some extended downtime a few
weekends from now, when I should finally have a 42U rack to replace the
Sears shelves my equipment is now on. It'll be a fun-filled evening of
racking equipment and re-patching everything. Also, hopefully within a
few weeks, I'll be moving my WAN pipe from Verizon FiOS residential to
Optimum Business, which is essentially re-packaged residential but
provides 5 static IPs, no blocked ports, and 30 Mbps down/5 Mbps up.

**Vyatta**

When planning this upgrade, I think I looked at every open source router
package out there, as well as some of the lower-end or older Cisco
models. I'm currently running [IPcop](http://www.ipcop.org/), which does
everything I need except it doesn't handle multiple WAN IPs, and all
configuration is via a web interface - which means every time I want to
make a change remotely (and during the week I'm not home) I have to
forward HTTPS over SSH. After doing an extensive feature comparison, I
ended up narrowing it down to a relative newcomer - Vyatta. Though I
don't know how much of it is marketing hype, they are targeted squarely
at Cisco, and provide relatively enterprise-level features; a
JunOS-based CLI, BGP, OSPF, and all of the other important stuff.

Yesterday I attempted an install of Vyatta CE 5 Beta on one of the
DL360G2's. The only real problem that I found was the install script
doesn't support CCISS drives, as found in the Proliants, but a few
manual hacks to the script fixed that. By far the best thing about
Vyatta is it's based on vanilla Debian Lenny, and full root shell access
is available, so modifying the install script - or even adding
non-Vyatta packages - is a cinch. I haven't really played around with it
too much, but it appears to be a wonderful mix of Linux and an
enterprise router CLI. While root has a full BASH shell, and the Vyata
commands are all done as shell aliases (so users still have access to
shell primitives and OS commands), configuration is accomplished via a
JunOS-like command set. You still get "commit" and "rollback" in config
mode, and can still do fun things like save and load configs to/from
tftp, ftp and *http*. On the other hand, I doubt I'll do config backups
that way since I can just use scp or sftp.

The Vyatta box will probably go home this weekend, and get hooked up to
the network for config-only use (and I can always get in via iLO on the
hardware) and hopefully come up sometime in the next few weeks.

At this point, the most daunting task is figuring out how to get all of
the existing links to my site to work - since jantman.dyndns.org will be
legacy, and most of the site structure will probably change to use
name-based vhosts. Lately I've been trying to use the real subdomains in
all of my public links, so the transition (planned for a while) will
work, but I'm sure there are still plenty of links out there that will
need dealing with (maybe keep port 10011 serving HTTP with a massive
mod\_rewrite script to redirect to the right place???), as well as
checking everything on the web server to make sure there aren't any
absolute URLs (like WordPress).
