Title: Updated Android App List
Date: 2010-08-15 13:19
Author: admin
Category: Android
Tags: android, droid
Slug: updated-android-app-list

Here's the current list of the apps that are running on my Droid and
seem interesting (I'm still running 2.0.1, build ESD56). This is an
update to my earlier post, [My Android Apps][], so I left out everything
that was already in that post.

This list was generated with [MyAppsList][], though I did massage it a
bit after generation (mainly because it copied text that was all on
*one* line, though it does output HTML with market links and the apps in
li elements). The simple script to make the output a little more
blog-friendly is:

~~~~{.bash}
cat apps.txt | sed 's/<\/li>/<\/li>  
/g' | sed 's///g' | sed 's/<\/font>//g' | sed 's///g'
~~~~

-   [Adobe Reader][] (v9.0.1) - full version of Adboe Reader
-   [Altitude Free][] (v1.0.5) - Shows your current altitude from GPS.
-   [AndroZip][] (v1.0.1) - Good all-around file manager and archive
    manager.
-   [arcMedia][] (v0.24b) - Media (video) player.
-   [Barnacle Wifi Tether][] (v0.5.1) - WiFi tethering for rooted Droids
    with stock kernel. See my [WiFi tether for Droid][].
-   [Bluetooth File Transfer][] (v3.40) - Good tool for transferring
    arbitrary files, contacts, etc. over bluetooth.
-   [Bookmarking for Delicious.com][] (v1.3.2) - Delicious bookmarking,
    so I can now keep my Droid in sync with all of my desktops, laptops,
    etc.
-   [ConvertPad - Unit Converter][] (v1.4.2) Simple but full-featured
    unit converter. Need to know how many twips there are in a fathom?
    No problem...
-   [DriveSafe.ly][] (v1.3.47) - cool app that reads incoming SMS to
    you. Can automatically activate when it connects to bluetooth.
-   [gReader][] (v1.6.8) - Good RSS reader with sync to Google Reader
    and automatic sync of articles for offline viewing.
-   [Handcent SMS][] (v3.2.6) - Just got this, still figuring it out,
    but appears to be a *much* nicer messaging app with popups
    (including reply box) for incoming SMS, nicer view, etc.
-   [My Verizon Mobile][] (v5.0) - Verizon's app that shows your current
    monthly minute, SMS, and data usage, as well as other stuff.
-   [MyAppsList][] (v1.4 BETA) - App used to generate this list.
-   [Package Tracking][] (v1.9b) - Simple package tracking for UPS,
    FedEx, etc. Unfortunately it doesn't provide any notifications and
    it only remembers one tracking number at a time.
-   [PdaNet][] (v2.42) - USB or Bluetooth tethering (official client
    software is Mac and Windows only).
-   [Ping][] (v1.6.9) - Ping app.
-   [Python for Android][] (v0) - Python interpreter for SL4A. So far,
    it doesn't seem to be able to do too much in my opinion.
-   [ShopSavvy][] (v3.6.6) - Scan a bar code, see the lowest prices for
    that product both online and in local stores.
-   [SL4A][] (v0) - Scripting environment for Android with pluggable
    interpreters. So far, it seems to be missing a lot of Android
    classes that would make it useful for doing device-specific things
    (like listing installed apps).
-   [VoiceMemo][] (v1.0.1) - Simple voice memo app. I use it quite a
    bit, but there's no simple way to email SMSes, it only titles them
    by date and time recorded, and it doesn't keep the phone awake
    (recordings seem limited to 60 seconds or so).

  [My Android Apps]: /2010/02/my-android-apps/
  [MyAppsList]: market://search?q=com.boots.MyAppsList
  [Adobe Reader]: market://search?q=com.adobe.reader
  [Altitude Free]: market://search?q=com.speedymarks.android.altitudeFree
  [AndroZip]: market://search?q=com.agilesoftresource
  [arcMedia]: market://search?q=sns.arcMedia.playerInterface.arm6
  [Barnacle Wifi Tether]: market://search?q=net.szym.barnacle
  [WiFi tether for Droid]: http://blog.jasonantman.com/2010/08/wifi-tether-for-droid/
  [Bluetooth File Transfer]: market://search?q=it.medieval.blueftp
  [Bookmarking for Delicious.com]: market://search?q=org.peterbaldwin.client.android.delicious
  [ConvertPad - Unit Converter]: market://search?q=com.mathpad.mobile.android.wt.unit
  [DriveSafe.ly]: market://search?q=com.drivesafe.ly
  [gReader]: market://search?q=com.noinnion.android.greader.reader
  [Handcent SMS]: market://search?q=com.handcent.nextsms
  [My Verizon Mobile]: market://search?q=com.vzw.hss.myverizon
  [Package Tracking]: market://search?q=com.ztech.packagetracking
  [PdaNet]: market://search?q=com.pdanet
  [Ping]: market://search?q=com.mm.network
  [Python for Android]: market://search?q=com.googlecode.pythonforandroid
  [ShopSavvy]: market://search?q=com.biggu.shopsavvy
  [SL4A]: market://search?q=com.googlecode.android_scripting
  [VoiceMemo]: market://search?q=com.javacodeland.android.voicememo
