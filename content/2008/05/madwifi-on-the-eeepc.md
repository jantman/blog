Title: Madwifi on the eeePC
Date: 2008-05-04 22:32
Author: admin
Category: Software
Tags: atheros, eeepc, madwifi, wifi, wireless
Slug: madwifi-on-the-eeepc

So, I've started a new [OpenSuSE](http://www.opensuse.org) install on my
eeePC. The 4GB SDHC card that I originally used was getting a bit
cramped - I couldn't even fit the kernel source! So, I bought a new 8GB
SDHC card and started from scratch. I know that OpenSuSE 11 is coming up
soon, but I just couldn't wait, so I just used OpenSuSE 10.3 again.

I followed my [previous
how-to](http://www.jasonantman.com/wiki/index.php/OpenSuSE_10.3_on_eeePC_External_SDHC),
and also am updating it with some new information - such as my
xorg.conf. Most interestingly, though, I actually got MadWiFi to work
with the [Atheros
AR5BXB63](http://madwifi.org/wiki/Compatibility/Atheros#AtherosAR5BXB63)
on the eeePC! I haven't tested everything yet (specifically WPA/WPA2)
but it seems to work fine. I've updated [my
HowTo](http://www.jasonantman.com/wiki/index.php/OpenSuSE_10.3_on_eeePC_External_SDHC#Update_2008-05-02)
with the instructions, but mainly it hinges on using
madwifi-ng-r2756+ar5007 ([gzipped
tarball](http://snapshots.madwifi.org/special/madwifi-ng-r2756+ar5007.tar.gz))
and compiling from source.

**Note:** This HowTo is based on the original eeePC 701 4G and OpenSuSE
10.3. It may not be needed for newer versions of OpenSuSE or newer
versions of the eeePC.
