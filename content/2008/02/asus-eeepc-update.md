Title: Asus eeePC Update
Date: 2008-02-04 19:12
Author: admin
Category: Miscellaneous
Tags: eeepc, linux
Slug: asus-eeepc-update

More to come sometime this week, when I have enough sanity and time to
write.

In the mean time...

So it's been two weeks since classes started again, and that means two
weeks using my now-beloved eeePC 4G Surf (details in a [previous
post][]). Granted, I have my "desktop replacement" laptop ([a Linux
Certified LC2464][]) to use at my desk at home or at my apartment -
though the "desktop replacement" really means that it's easy to move
from one desk to another.

So far, I really love it, but I have a few issues:

1.  I should have bought an 8GB SDHC card instead of the 4GB that I got
    - especially with a full install of OpenSuSE with Sun's JDK and
    OpenOffice, the 2GB root partition is 99% full!
2.  After using a desktop for hours, it takes a few lines of text for my
    fingers to re-adjust to the small keyboard. Hopefully it'll get
    easier with time.
3.  Unfortunately, I don't have space for kernel headers or source, so I
    can't compile the customized version of asus\_acpi. I can't find any
    binary packges, or binary kernel modules for my kernel version. That
    prevents me from using sleep/hibernate/suspend, and also means I
    don't get accurate battery calculations. I've found from usage that
    the battery lasts 2-3 hours with wireless on and minimal screen
    brightness. Also, unfortunately, (maybe because of the ACPI issue?)
    if I dim the screen and then the screensaver comes on, when I log
    back in it resets to full brightness.
4.  As of this week, there's still no MadWifi driver for the Atheros
    card in the 4G. I have to run it under Ndiswrapper. As a result, I
    can't get monitor mode, so the eee is effectively useless for
    wireless site surveys and security work. There's talk of a
    forthcoming MadWifi, but if nothing shows up, I may have to go with
    a USB adapter (I don't want to void the warranty by swapping out the
    internal Mini-PCI adapter).
5.  Not a problem with the eeePC, but it seems like quite a few web
    sites that I've visited are horribly coded - with static screen
    sizes assumed. On the small screen on the eee, the biggest issue is
    when the first few characters of every line on some sites are cut
    off, thereby rendering the content illegible. This is an issue out
    of Asus' control, but can be a hindrance to full use. I have,
    however, found that for many sites, switching FF to "full screen"
    mode (F11) helps.

Stay tuned for more, and some new scripts to automate wireless surveys,
rogue AP detection, etc. And maybe even some work with autonomics and or
configuration tools.

  [previous post]: http://www.jasonantman.com/blog/2008/01/eeepc-solaris-other-updates.html
  [a Linux Certified LC2464]: http://www.linuxcertified.com/linux-laptop-lc2464.html
