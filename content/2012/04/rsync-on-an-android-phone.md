Title: Rsync on an Android phone
Date: 2012-04-04 20:40
Author: admin
Category: Android
Tags: android, rsync, tasker
Slug: rsync-on-an-android-phone

Every once in a while, there are some files that I want kept in sync
between my Android-based phone and one of my Linux (or Mac, or any Unix,
or maybe Windows too, but I use Linux...) boxes. Yeah, I can copy them
over manually via USB or even something a bit simpler like [AndFTP][]
(assuming you can SCP to the target machine). But that's a real pain for
anything like my [KeePass][] (well, actually [KeePassX][] and
[KeePassDroid][]) password database, that I might add something to at
any time and forget to sync. I also try to occasionally (waiting in
line?) backup SMS, call logs, etc. on my phone, and like to have those
synced back to the desktop automatically.

Enter the solution: [rsync backup for Android][], a [rsync][] client for
Android that includes Tasker plugins (there are a few things about the
app that I don't like, but it seems to be the only option at the
moment), and [Tasker][], an automation framework for Android.Tasker is
one of the few Android apps that I've actually bought (i.e. not
free/no-cost), and is currently selling for $6.49. It's an incredibly
capable task automator, very much akin to [Locale][] on steroids. On the
down side, Tasker can eat up battery life if you don't configure it
intelligently, and it's not *always* 100% reliable when interacting with
the system. On the positive side, Tasker can identify practically any
combination of states in the android system (from hardware and software
events to GPS location, time, signal status, etc.) and perform almost
any task on the system based on this information. Sure, this specific
problem could be solved with a cron replacement (which Android lacks, of
course), but Tasker can do things like play specific audio files when
you get an SMS from a specific number, mute audio at certain GPS
locations, or turn WiFi on when I get home and off when I leave the
house. It also has a plugin architecture, and rsync backup for Android
happens to have a plugin that works with it.

So, our goal is to have a daily, bi-directional, newest-file-wins sync
between a directory on our Android phone and a directory on a computer.
I'm not going to go into a lot of the computer-side stuff, mainly
because that varies quite a bit between operating systems, and also
because my personal setup is a bit paranoid in terms of security. For
the computer side, we'll need a machine that can be SSHed to from the
Internet (either a static IP or a known hostname/dynamic DNS), a user
that can run rsync over SSH, and a directory that's writable
(obviously).

**Setup:**

1.  Buy and install the [Tasker][1] app.
2.  Install the [rsync backup for Android][2] app.
3.  Configure the rsync stuff on the computer. In the simplest form,
    we'll just need a user that can login and run rsync, and a directory
    to sync from/to *(note: this should be a directory used only for
    syncing the phone...).*
4.  Open the rsync backup for Android app. Use Menu -\> Generate Keys to
    generate a new pair of SSH keys, and then get the public key setup
    on the target computer. See [the developer's web site][] for
    instructions.
5.  Once keys are setup, create a new profile called "PC-droid". Set the
    local directory to a new empty directory (I used `/sdcard/sync`),
    enter the remote host address, port, username, and remote directory,
    and select the private SSH key that you created. Check off "rsync on
    reverse direction". As this program is just a GUI wrapper around
    normal rsync binaries, you can specify additional options to the
    rsync command; my string ended up being
    `-vHrltDuO --chmod=Du+rwx,go-rwx,Fu+rw,go-rw --no-perms`. If it
    helps, at the bottom of the screen you can see the actual rsync
    command line that will be run. Save when done.
6.  Save the profile, then long-press it and select "Duplicate". Change
    the name to "droid-PC", uncheck "rsync in reverse direction", and
    change your additional options as needed (mine became
    `-vHrltDu --chmod=Dug+rwx,o-rwx,Fug+rw,o-rw --no-perms`). Save when
    done.
7.  Create a test file in the sync directory on the PC, and a different
    one in the sync directory on the droid.
8.  One at a time, in the rsync backup app, tap on the profile names. If
    all goes well, the syncs should run, and both files will now be in
    both places. If there are any problems, the output should help; the
    most likely issues are probably permissions, rsync command options,
    or SSH keys.
9.  Long-press each profile, select "Edit", and check off "Close log
    window after job is done". Save profile.
10. Now fire up Tasker. Click the "+" at the bottom of the screen to
    create a new profile, call it "sync", and click the check mark.
11. On the First Context panel, tap Time, and select when you want the
    jobs to run; I chose 03:01. Tap the check mark.
12. On the Task Selection panel, tap New Task. Give it a name, like
    "sync2".
13. On the Task Edit panel, tap the "+" button at the bottom left, tap
    Plugin, tap "rsync backup for Android", click the "Edit" button on
    the Configuration line, and select the PC-droid rsync profile. Tap
    the check mark in the lower left to save.
14. Repeat the last step for the droid-PC rsync profile.
15. Tap the check box in the lower left. This saves the profile.
16. In the main Tasker screen, make sure there's a green check to the
    right of the profile you just added, and that the button at the
    bottom right of the screen is set to "On".

Assuming this all went well, the next time the time you specified rolls
around, your sync should run. If you gave the task a name in step 12,
you can setup additional profiles to run it at other times (or use the
repeat logic builtin).

  [AndFTP]: https://market.android.com/details?id=lysesoft.andftp
  [KeePass]: http://keepass.info/
  [KeePassX]: http://www.keepassx.org/
  [KeePassDroid]: https://market.android.com/details?id=com.android.keepass
  [rsync backup for Android]: https://market.android.com/details?id=eu.kowalczuk.rsync4android
  [rsync]: http://rsync.samba.org/
  [Tasker]: https://market.android.com/details?id=net.dinglisch.android.taskerm
  [Locale]: http://www.twofortyfouram.com/
  [1]: https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm
  [2]: https://play.google.com/store/apps/details?id=eu.kowalczuk.rsync4android
  [the developer's web site]: http://android.kowalczuk.eu/rsync4android/
