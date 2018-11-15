Title: Getting WoW working on OpenSuSE under Wine
Date: 2010-09-05 22:52
Author: admin
Category: Miscellaneous
Tags: warcraft, wine, wow
Slug: getting-wow-working-on-opensuse-under-wine

Ok, I'll admit it, I've been playing
[WoW](http://www.worldofwarcraft.com). I'm not usually the gamer type,
but my girlfriend pressured me into it a bit and, hey, if a woman's idea
of quality time is sitting in the same room in front of computers
playing a [MMORPG](http://en.wikipedia.org/wiki/Mmorpg), who am I to
complain? My non-work-hours productivity had suffered quite a bit, but
I'm not yet at risk of becoming a full-on addict.

So, for a slight diversion from the usual content...

Of course, I'm not going to run Windows just to play a game, and the
screen on my MacBook Pro is pitifully small compared to the 24" LCD on
my desktop. So I've been running WoW through
[Wine](http://www.winehq.org/) on an admittedly out of date
[OpenSuSE](http://www.opensuse.org/) 11.1 install on my workstation (a
Dell Precision 470 - 2 Gb 400Mhz DDR ECC RAM, 16 Gb swap, dual 2.8GHz
Xeons with HT, 16 KB L1 cache, 1 MB L2 cache, and a pitiful ATI Radeon
3600 HD, and everything in /home (including the game) on a 7200 RPM SATA
disk).

With my recent need to upgrade to Burning Crusade, I hit a few bumps. I
ended up wiping out my entire `~/.wine` and starting from scratch with a
fresh install, and having to apply all of the patches (luckily I backed
everything up to another drive so I already had the patches downloaded).
Of course, I backed up the data if import (`Interface` and `WTF` and WoW
was the only thing I had installed through wine).

I went through a number of different attempted settings for wine, OS
settings, etc. through the different patches (essentially try a patch,
change settings until it worked, move on to the next). The biggest snag
I hit was every few patches, X would lock up. No keyboard or mouse
input, the caps lock, num lock, etc. keys wouldn't respond,
Ctrl+Alt+{Backspace|Delete} wouldn't work, *but* I still had SSH access,
so I could just kill the `Wow.exe` process and try again. Each time this
happened was right after I accepted the second message (TOS or EULA,
whichever comes second)... the last thing I'd see in the log is:

    fixme:reg:GetNativeSystemInfo (0x374045c4) using GetSystemInfo()

and then it would lock up with Wow.exe using 400% CPU as per `top`
(which *does* make some sense given dual CPUs with HT). Needless to say,
I have 4 pages of notes detailing the process it took me to get to a
working fully-patched install. I don't know if different patches need
different tweaks, and don't really feel like transcribing the entire
process. But here's the final state of all the things I tweaked.

I'm running OpenSuSE 11.1, kernel 2.6.27.45-0.1-default (SMP x86\_64),
wine 1.3.1 (1.3.1-1.1 from the OpenSuSE
[Emulators:/Wine/openSUSE\_11.1](http://download.opensuse.org/repositories/Emulators:/Wine/openSUSE_11.1/)
repo) running under WindowMaker 0.92.0-204.6.

If you happen to find this post and give it a shot, please comment if it
worked, or what you did differently. If it will be of help, drop me a
line and I'll transcribe and post my entire process.

First note that I start WoW via a bash script (`~/bin/warcraft.sh`) that
sets up my switched mouse buttons in WindowMaker (yeah, I'm very
left-handed) and also `chmod -R`'s the whole
`.wine/drive_c/Program Files/World of Warcraft` 777, which seems to be
required for WoW (and the perms get gronked after patches). The chmod is
a good starting point for troubleshooting.

1.  `winecfg` under "Libraries" tab add overrides for `msvcr80` and
    `wldap32` as "(native, builtin)"
2.  `winetricks vcrun2005sp1`
3.  Run warcraft Installer through wine, auto-install Gecko when asked.
    When install finishes, begin patching.
4.  `winetricks fakeie6`
5.  add `SET gxApi "opengl"` to `Config.wtf`
6.  `winetricks nt40`
7.  `wine regedit`, create a key HKEY\_CURRENT\_USER -\> Software -\>
    Wine -\> Direct3D if it doesn't exist, create string value
    "OffscreenRenderingMode" =\> "backbuffer".
8.  `winecfg`, in Graphics tab, check off "Allow the window manager to
    decorate the windows" and "Allow the window manager to control the
    windows" (fixed my last hang at patch 3.3.5-12340)

