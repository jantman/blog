Title: Motorola Droid: Rooted 2.0.1 to Rooted 2.2 (CyanogenMod)
Date: 2010-09-04 16:50
Author: admin
Category: Miscellaneous
Tags: android, cyanogen, cyanogenmod, droid, root
Slug: motorola-droid-rooted-2-0-1-to-rooted-2-2-cyanogenmod

As of this morning, my Motorola Droid was still running rooted 2.0.1
(build ESD56, baseband C\_01.3E.01P) with SPRecovery 0.99.2b. Well
yesterday I for the random deletion of all SMS bug again, and I decided
it's time to upgrade. I never upgraded to 2.1 - mainly out of laziness.
When it first came out, nobody had a patched update.zip yet to preserve
root. When I looked back into the situation a few weeks ago (when
Froyo/2.2 came out), I found that pretty much the whole community had
moved from patched update.zip's to full ROM images. I didn't want to
lose my apps, data, settings, etc. and couldn't find any instructions
that didn't include a wipe/reset, so I decided to keep putting it off.

Well, after yesterday's bug (and after I played with the Camera app on
an Incredible and saw how much nicer it is), I decided it was time to
bite the bullet and move to [CyanogenMod][] ROMS. I performed the
upgrade this morning, and it seems to have worked OK, though I haven't
been using the phone very much since it finished.

**Rooted 2.0.1 to CyanogenMod 2.2 procedure:**

I'm starting with a Motorola Droid, 2.0.1 (build ESD56), rooted,
baseband C\_01.3E.01P, with SPRecovery 0.99.2b

1.  Perform full Nandroid backup through SPRecovery.
2.  Run [Call Logs Backup & Restore][] (v1.8) to backup call log.
3.  Run [SMS Backup & Restore][] (v3.4) to backup SMS data.
4.  Run [MyAppsList][] to make a list of all installed apps as HTML,
    including market links. Save to SD card.
5.  Run [Bookmark Sort & Backup Free][] to backup bookmarks to SD card.
6.  Run [ASTRO][] file manager and backup ALL apps to SD card.
7.  Mount the SD card on another computer and copy all the backups you
    just made to somewhere safe.

For the rest of the procedure, I more or less followed the [CyanogenMod
Droid Full Update][] guide.

1.  Buy & install [ROM Manager][] Premium.
2.  Flash ClockworkMod Recovery.
3.  Use ROM Manager to backup current ROM to SD card, copy the backup
    somewhere safe on another computer.
4.  ROM Manager - download CyanogenMod 6.0.0 for Droid with AWDLauncher
    and Google Apps.
5.  Check off "wipe data and cache", click OK.
6.  Phone reboots into recovery, flashes new image, and boots to
    CyanogenMod Froyo (2.2, build FRG22D), still has baseband
    C\_01.3E.01P.
7.  Enter your Google account information to begin sync. Your Google
    data (calendar, contacts, etc.) should be synced as well as all of
    your Market apps. You will, however, lose all of your app settings.

**Post-Upgrade:**

After the upgrade, there were a few things I had to do, and a few issues
that I wasn't prepared for. Here's a list of them, and the solutions I
found (if any) in no particular order...

-   Restore bookmarks, call log, SMS backup.
-   All of my per-contact ringtones were gone. As far as I could find,
    there's no known good way of backing up and restoring these.
-   I obviously lost the HD-quality video hack I'd applied to the Droid,
    as well as anything else I'd done in the boot settings file.
-   I apparently lost the following apps (not restored when the phone
    synced with Google):
    -   [Package Tracking][]
    -   [Python for Android][]
    -   [SL4A][]
    -   [Tetronimo][]

-   The following apps were added by CyanogenMod (or are new since
    2.0.1):
    -   [Chrome to Phone][] - [chrometophone][] - send links from Chrome
        browser to your phone using some Google messaging service
    -   [Dev Tools][Chrome to Phone] -
    -   [DPSManager][Chrome to Phone] -
    -   [News and Weather][Chrome to Phone]
    -   [Places][Chrome to Phone] - [Google Places][]
    -   [Spare Parts][Chrome to Phone] - apparently allows access to
        some settings not available through the Settings menu
    -   [Speech Recorder][Chrome to Phone]
    -   [Superuser][Chrome to Phone] - App to graphically manage root
        access
    -   [Talk][Chrome to Phone] - [Google Talk][]
    -   [Terminal Emulator][Chrome to Phone] (somehow I have two
        installed...?)
    -   [Twitter][Chrome to Phone]
    -   [Videos][Chrome to Phone]
    -   [Voice][Chrome to Phone] - [Google Voice mobile][]

-   These apps had data associated with them which was somewhat
    important (I wrote the script below to handle the move):
    -   [Alarm Clock Plus][Chrome to Phone]
    -   [Barnacle WiFi Tether][Chrome to Phone]
    -   [ConnectBot][Chrome to Phone]
    -   [gReader][Chrome to Phone]
    -   [Jewles][Chrome to Phone]
    -   [Nagroid][Chrome to Phone]

-   Had to re-set my notification sounds - Flutey Phone for incoming
    calls, Look at Me for messaging and Highwire for other
    notifications.
-   Much to my pleasure, my WiFi settings, saved networks, etc.
    magically came back. Haven't checked bluetooth yet.
-   I had to change my voicemail number (Settings -\> Call Settings -\>
    Voicemail Settings) to automatically wait and enter my password.

</ol>
At the moment, this script is obviously setup to do one app at a time,
hard-coded in the APP variable. It also assumes that the app data
directory is stored at /sdcard/restore/$APP.

~~~~{.bash}
#!/bin/bash

APP="com.vp.alarmClockPlusDock"

BIN_PATH="/system/xbin/"
DATA_PATH="/data/data/"
BACKUP_PATH=""
PERMS_PATH="/data/system/packages.list"

OWNER=`grep -i "$APP" /data/system/packages.list | awk '{ print $2}'`

echo "OWNER=$OWNER="

/system/xbin/mv /data/data/"$APP" /data/data/z
/system/xbin/mv /sdcard/restore/"$APP" /data/data/"$APP"
/system/xbin/rm -Rf /data/data/z

/system/xbin/chown -R 10069:10069 /data/data/"$APP"

/system/xbin/chmod 751 /data/data/"$APP"

if [ -e  /data/data/"$APP"/cache ]
then
    /system/xbin/chmod -R 771 /data/data/"$APP"/cache
fi

if [ -e /data/data/"$APP"/databases ]
then
    /system/xbin/chmod 771 /data/data/"$APP"/databases
    /system/xbin/chmod 660 /data/data/"$APP"/databases/*.db
fi

if [ -e /data/data/"$APP"/files ]
then
    /system/xbin/chmod -R 771 /data/data/"$APP"/files
    /system/xbin/chmod 660 /data/data/"$APP"/files/*
fi

if [ -e /data/data/"$APP"/lib ]
then
    /system/xbin/chown -R system:system /data/data/"$APP"/lib
    /system/xbin/chmod -R 755 /data/data/"$APP"/lib
fi

if [ -e  /data/data/"$APP"/shared_prefs ]
then
    /system/xbin/chmod 771 /data/data/"$APP"/shared_prefs
    /system/xbin/chmod 660 /data/data/"$APP"/shared_prefs/*
fi

echo "DONE."
~~~~

I'll update this now and then as I have more to add to it...

  [CyanogenMod]: http://www.cyanogenmod.com/
  [Call Logs Backup & Restore]: market://search?q=com.riteshsahu.CallLogBackupRestore
  [SMS Backup & Restore]: market://search?q=com.riteshsahu.SMSBackupRestore
  [MyAppsList]: market://search?q=com.boots.MyAppsList
  [Bookmark Sort & Backup Free]: market://search?q=com.happydroid.bookmarks
  [ASTRO]: market://search?q=com.metago.astro
  [CyanogenMod Droid Full Update]: http://wiki.cyanogenmod.com/index.php?title=Full_Update_Guide_-_Motorola_Droid
  [ROM Manager]: market://search?q=com.koushikdutta.rommanager
  [Package Tracking]: market://search?q=com.ztech.packagetracking
  [Python for Android]: market://search?q=com.googlecode.pythonforandroid
  [SL4A]: market://search?q=com.googlecode.android_scripting
  [Tetronimo]: market://search?q=com.mahoney.tetronimo
  [Chrome to Phone]: 
  [chrometophone]: http://code.google.com/p/chrometophone/
  [Google Places]: http://googleblog.blogspot.com/2010/04/introducing-google-places.html
  [Google Talk]: http://www.google.com/talk/
  [Google Voice mobile]: http://www.google.com/mobile/voice/
