Title: Brother HL-2170W - great features from a personal laser printer
Date: 2009-03-18 21:29
Author: admin
Category: Hardware
Tags: printer, review
Slug: brother-hl-2170w-great-features-from-a-personal-laser-printer

**I've posted an [update about serious DHCP problems with this
unit](/2009/04/brother-hl2170w-dhcp-problems/).**

Last week my mother's printer died, and she asked me to find a new one
for her. After a quick look on [NewEgg](http://www.newegg.com) (sort by
ratings is a wonderful thing) I found the [Brother
HL-2170W](http://www.brother-usa.com/Printer/ModelDetail.aspx?ProductID=hl2170W).
Aside from having a wireless interface (only a security hole, as far as
I'm concerned) it seemed pretty cool - tiny B&W laser, Ethernet, PCL6,
23ppm, 32 MB RAM, 250 sheet capacity and 2400x600 dpi. So, for a mere
$99 USD, I bought it for her.

When the printer showed up, I was a bit let down to find no sticker
bearing the MAC address on either the box or the printer itself - and
given the one-button hard control, there wasn't a way to manually print
a config sheet. So, after plugging it into the network and using the
DHCP logs to give it a static assignment, a quick reboot of the printer
had everything working. As usual, I skipped to the last few pages in the
installation manual, and found the ½ page section on the web interface.
Configuration was pretty simple - change the admin password, disable a
bunch of unneeded services, etc. And then, when playing around with the
admin interface, I found a bit of a holy grail - there in the
enable/disable services screen were two options that I found unusual for
a "personal" printer; **Telnet** and **SNMP**. I immediately tried both.
An snmpwalk revealed the usual (RFC1213, HOST-RESOURCES, and
Printer-MIB) including information on status and consumables. Though the
Telnet login process wasn't terribly intuitive, "help" revealed familiar
set/show/clear functionality as well as an option to zero out counters.
While I was a bit let down to see that there wasn't a way to view
consumable status or printer status, it did allow access to every
conceivable configuration parameter, including a few that weren't
mentioned on the web interface.

All in all, while I can't comment about reliability or quality yet, this
cute little printer seems to have quite a feature set, especially when
it comes to manageability and remote troubleshooting (a good thing for
any printer that's used by a family member who you support). And best of
all, it supports IPP and LPR.
