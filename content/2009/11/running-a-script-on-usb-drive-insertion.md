Title: Running a script on USB drive insertion
Date: 2009-11-11 11:47
Author: admin
Category: Miscellaneous
Tags: linux, script, udev, usb
Slug: running-a-script-on-usb-drive-insertion

Before I even get into how to do this, **be warned:** this is a *really*
bad idea unless you can ensure total physical access control to the
machine. About the only place I'd ever use it is in a non-networked
embedded system in a secure location. Its original intent is to handle
loading of pictures onto a Linux-based digital photo frame.

So, you want to run a specific script on insertion of a USB drive.
Here's how to use udev to do it:

1.  Create `/etc/udev/rules.d/99-usbhook.rules`:

        :::text
        ACTION=="add",KERNEL=="sd*", SUBSYSTEMS=="usb", ATTRS{product}=="Mass Storage", RUN+="/root/bin/usbhook %k"

    This will run "/root/bin/usbook", passing it the device name as an
    argument, every time a USB Mass Storage device is plugged in.

2.  run `udevcontrol reload_rules`
3.  Create your usbhook script.
4.  Enjoy

Here is my usbhook script to copy all files from a USB mass storage disk
to a specific location. It includes quite a bit of debugging, and also
checks for the presence of a file called "foobarbaz.txt" on the device
before copying the files over.

~~~~{.bash}
#!/bin/bash

# script to move over all files from a USB key
# when it is inserted into the system.

# should be called from a udev rule like:
#ACTION=="add",KERNEL=="sd*", SUBSYSTEMS=="usb", ATTRS{product}=="Mass Storage", RUN+="/root/bin/usbhook %k"

# Copyright 2009 Jason Antman.  
# 

# CONFIGURATION
DEBUG=1 # set to 1 for debugging output
DEST="/home/foo/" # destination for files


DEVICE="$1" # the device name
LOGFACILITY="kernel.info" # for debugging output


if [ ${DEBUG:=0} == 1 ]; then logger "$LOGFACILITY" usbhook called with arguments: "$DEVICE"; fi

sleep 5 # delay 5 seconds to wait for mount

mount | grep "$DEVICE"
FOO="$?"

if [ $FOO == 0 ];
then
    if [ ${DEBUG:=0} == 1 ]; then logger "$LOGFACILITY" usbhook device mounted: "$DEVICE"; fi
else
    if [ ${DEBUG:=0} == 1 ]; then logger "$LOGFACILITY" usbhook device NOT mounted: "$DEVICE" - exiting; fi
    exit 0
fi

BAR=`mount | grep "$DEVICE" | awk '{ print $3 }'`

if [ -e "$BAR/foobarbaz.txt" ]
then
    if [ ${DEBUG:=0} == 1 ]; then logger "$LOGFACILITY" usbhook "$BAR"/foobarbaz.txt found; fi
else
    if [ ${DEBUG:=0} == 1 ]; then logger "$LOGFACILITY" usbhook "$BAR"/foobarbaz.txt NOT found - exiting; fi
    exit 0
fi

cp -R "$DEVICE"/* "$DEST"
~~~~

This was tested on [OpenSuSE](http://www.opensuse.org) 10.3.
