Title: LIRC and Hauppauge PVR-150 on OpenSuSE 11.0
Date: 2008-09-01 10:37
Author: admin
Category: Tech HowTos
Tags: hauppauge, linux, lirc, mythtv, opensuse, pvr-150, suse
Slug: lirc-and-hauppauge-pvr-150-on-opensuse-110

Well, despite what's been said elsewhere, it *IS* possible! It's a bit
error-ridden at first, but here is the procedure that I used to compile
and install the PVR-150 patched LIRC 0.8.3-CVS.

First, Download the tarball mentioned in the [Version 3 blog
post](http://www.blushingpenguin.com/mark/blog/?p=24) at [Marks
Braindump](http://www.blushingpenguin.com/mark/blog/). You can pretty
much follow his instructions on the installation in the blog post, with
some changes that are specific to getting it to compile on OpenSuSE 11.

1.  First, remove all traces of the OpenSuSE LIRC from you system.
    Uninstall the RPMS and everything else that goes with them. Then
    unload all of the kernel modules, especially lirc\_i2c (if you have
    it loaded).
2.  In your kernel source directory, run
    `make oldconfig && make prepare.`
3.  In your kernel source directory, run `make prepare scripts` which,
    among other things, compiles the required `genksyms` scurript.
4.  I was getting a compile error like "WARNING: Symbol version dump
    /usr/src/\`uname -r\`/Module.symvers is missing". Find out which
    kernel you're running (`uname -r`). In yout kernel source directory,
    copy your Module.symvers file from /usr/src/linux-obj. I was running
    i386 architecture with the "default" kernel, so mine was located at
    `/usr/src/linux-obj/i386/debug/Module.symvers`. Copy that into
    `/usr/src/linux`.
5.  In the lirc (patched) directory, run `setup.sh` as instructed. DO
    NOT tell it to run configure - just save settings and exit.
6.  Edit the generated `configure.sh` file, adding a
    `--with-kerneldir=/usr/src/KERNELDIR`, replacing KERNELDIR with the
    actual path to your kernel soruce (i.e. /usr/src/\`uname -r\`).
7.  `make`. If no errors, `make install`.
8.  I decided to reboot at this point, and when I did, everything worked
    perfectly.

Also, I found that I needed to explicitly specify `--device=/dev/lirc0`
when starting LIRC, as well as not specifying a driver. I just took the
`/etc/init.d/lirc` from the official OpenSuSE 11.0 package, commented
out line 108 in `makeargs()` that adds the `-H $LIRC_DRIVER` to the
args, and added `LIRC_DEVICE="/dev/lirc0"` to the top after the INIT
info.

Unfortunately, figuring out this process took me a long time. I've
reconstructed these instructions from various post-it notes, the
whiteboard next to my desk, and some bash history files and terminal
dumps. If this doesn't seem to work for you, please drop an email to
jason AT jason antman DOT com, with as much information as you have, and
I'll figure it out and update the instructions.

Now, finally, an up-to-date system AND [MythTV](http://www.mythtv.org).
