Title: Synaptics touchpad driver synclient in Fedora 16 / Xorg with UDEV
Date: 2012-01-27 17:51
Author: admin
Category: Tech HowTos
Tags: synaptics, synclient, thinkpad, touchpad, xorg
Slug: synaptics-touchpad-driver-synclient-in-fedora-16-xorg-with-udev

I just installed [Fedora 16][] on an older IBM [ThinkPad T42][] laptop.
Unfortunately, the two mouse buttons below the [UltraNav][] touchpad
just won't work at all. Before opening up the case and fiddling around,
I decided to try a software solution. Even after fairly exhaustive
research, I couldn't find anyone with a similar problem.

I did, however, find out that the synaptics touchpad driver has a
`synclient` tool that can output the hardware events read directly from
the input device. I tried running `synclient -m 100` (to monitor
hardware events every 100ms), but the only output that I got was
`Can't access shared memory area. SHMConfig disabled?`. This was all a
bit confusing to me, since Fedora 16 doesn't even use an `xorg.conf`
file. I was even more confused by a fair amount of information saying
that SHMConfig is no longer used in synaptics 1.2+.

Long story short, the solution lies in
`/usr/share/X11/xorg.conf.d/50-synaptics.conf`, which holds the
synaptics config snippets for xorg. All you need to do is add the
SHMConfig line before the end of the section:

~~~~{.text}
Section "InputClass"
    Identifier "touchpad catchall"
    Driver "synaptics"
    ...
    Option "SHMConfig" "on"
EndSection
~~~~

and then restart your X server. Now, running `synclient -m` should work
fine.

I have to thank Red Hat's [Kevin Fenzi][] (nirik on [\#fedora on
irc.freenode.org][]) for putting another set of eyeballs on the problem,
and throwing out some ideas that finally led me to the solution.

  [Fedora 16]: http://fedoraproject.org
  [ThinkPad T42]: http://www.thinkwiki.org/wiki/Category:T42
  [UltraNav]: http://www.thinkwiki.org/wiki/UltraNav
  [Kevin Fenzi]: http://fedoraproject.org/wiki/User:Kevin
  [\#fedora on irc.freenode.org]: http://webchat.freenode.net/?randomnick=1&channels=fedora&uio=d4
