Title: My Android Apps
Date: 2010-02-28 12:39
Author: admin
Category: Miscellaneous
Tags: android, apps, droid
Slug: my-android-apps

**Update 2010-08-15** - I've also added some new apps to an [updated
post](/2010/08/updated-android-app-list/).

The past 48 hours has been very eventful in my Android world. Thanks to
the instructions on [rootyourdroid.info](http://rootyourdroid.info)
(hey, it's an expensive phone and locked hardware - I'm not fooling
around the way I would with something [more
common](http://blog.jasonantman.com/2009/11/root-on-a-cyclades-acs-console-server/)),
I rooted my droid and did a few minor hacks. Though, I must say, it
pains me to see all of the post-rooting instructions based on access via
adb, instead of using a terminal emulator on the phone. Also, last
night, my mother (definitely *not* a technical person) for a Droid - and
loves it! (My dad got one a month or two ago).

Anyway, in the last 24 hours, I've gone app-crazy. I thought I'd share
some of my findings here. Unfortunately, while a few of the app/file
managers out there do dump a list of applications, I can't find one that
dumps a list including the package names (which are required to create
an effective link to the app). If any of you know of one, please
enlighten me. For now, I'll construct this list by hand (using the list
from [ASTRO](market://details?id=com.metago.astro) 2.2.4), and maybe
write an app to do it in the future.

*(Note: These links all use the market:// URI scheme, so they're only
useful if clicked on an Android device with the Market app.)*

-   [AndFTP](market://details?id=lysesoft.andftp) (1.3) - A good
    FTP/SFTP client for Android, includes pubkey-based authentication
    and host storage.
-   [Android Battery
    Dog](market://details?id=net.sf.andbatdog.batterydog) (0.1.2) - An
    app that runs as a service and collects *detailed* statistics on
    battery usage, including temperature, charge percent, voltage,
    discharge rate, battery technology and external power status. While
    it can display a graph or formatted data, its' real shining point is
    the ability to export timestamped semicolon-delimited data files for
    external graphing and analysis.
-   [Any Cut](market://details?id=com.appdroid.anycut) (1.0) - Allows
    you to create shortcuts on your home screen to almost anything,
    including Android OS Acitvities, direct calls or direct text
    messages.
-   [ASTRO](market://details?id=com.metago.astro) (2.2.4) - File manager
    that allows copying of files on the device (both internal memory and
    SD card), image and file viewing, listing/management of apps
    (including finding out the package name of an App), reading of tar
    and tgz files, etc.
-   [Battery
    Widget](market://details?id=com.geekyouup.android.widgets.battery)
    (1.5.2, by mippin) - Very simple widget for the home screen that
    takes up one square and shows current battery level. When clicked,
    provides shortcuts to settings screens for display, GPS, WiFi and
    Bluetooth.
-   [Compass](market://details?id=com.apksoftware.compass) (1.1) -
    Simple compass app. Shows a compass which seems to be accurate,
    current lat/long and current street address. Has extensive settings
    and some nice skins for the compass.
-   [ConnectBot](market://details?id=org.connectbot) (1.6.2) - A very
    good SSH client for Android. Allows storage of multiple hosts,
    pubkey-based authentication (with a master password), etc.
    Unfortunately, doesn't seem to have any way (that I can find) to
    enter certain characters, such as tab and pipe (|).
-   [Dolphin
    Browser](market://details?id=com.mgeek.android.DolphinBrowser.Browser)
    (2.5.0) - An alternate browser for Android. I haven't used it
    extensively yet, but it shows multiple tabs at the top of the screen
    like Firefox (easier to switch between tabs than the stock browser's
    Menu -\> Windows) and **supports iPhone-like multitouch on the
    Droid**.
-   [drocap2](market://details?id=com.gmail.nagamatu.drocap2) (2.07) -
    Screen capture program (requires root). Allows you to trigger a
    capture from the notifications bar and stores captures on the SD
    card.
-   [DroidLight](market://details?id=com.motorola.dlight) (3.0) - Nice
    twist on the usual flashlight app. By Motorola, this app triggers
    the camera's flash LED in a steady burn mode, providing very good
    light output. Probably a real battery killer.
-   [FoxyRing](market://details?id=com.levelup.foxyring) (1.12) - This
    was an ANdroid Developer Challenge winner and, among other things,
    it claims to monitor ambient sound levels and adjust your ringer
    volume to match them. Unfortunately, due to the overly restrictive
    End User License Agreement (EULA), specifically the strong
    provisions against reverse engineering and redistribution, I was
    forced to uninstall the app before even trying it.
-   [GPS Status](market://details?id=com.eclipsim.gpsstatus2) (3.0.3) -
    Very nice app. Provides a display like a real GPS, showing the
    location and status of various satellites (in a rotating compass),
    heading and orientation, number of fixes, estimated error (DoP),
    signal strength graph for stelites, speed, altitude, pitch/tilt of
    phone, magnetic field, acceleration, coordinates and time of last
    fix.
-   [iPerf](market://details?id=com.magicandroidapps.iperf) (1.07) - An
    iPerf client for Android that seems to work fine. How cool! Seems to
    be a wrapper around the binary, lets you specify CLI arguments,
    shows console output.
-   [Meebo IM](market://details?id=com.meebo) (22) - A simple, good,
    multi-protocol IM application.
-   [Metal Detector](market://details?id=com.imkurt.metaldetector)
    (1.2-RELEASE) - Maybe not that useful, but way cool. The Droid (and
    perhaps other phones?) uses the compass to detect magnetic fields to
    trigger the modes for car dock and multimedia dock. This turns it
    into a metal detector. Wonderful cool-ness factor.
-   [Nagroid](market://details?id=de.schoar.nagroid) (0.0.7) - A Nagios
    watcher for Android. Can be configured with only one URL, but can do
    HTTP Basic Auth and handle self-signed SSL certs. Options to hide
    everything that's OK, and show only unhandled (un-acknowledged)
    problems. Also can start a service to poll and alert at regular
    intervals. Only down side is that it only handles one Nagios URL.
-   [Network Discovery](market://details?id=info.lamatricexiste.network)
    (0.2.7.1) - Intersting little app that I haven't played around with
    much. Does port scans of IPs and runs a "network discovery" of the
    LAN, though it doesn't say whether it is active (ping/port scanning)
    or passive (ARP). Displays info on devices (IP, MAC address, decodes
    MAC manufacturer name from address) and a button to run a port scan.
-   [OSMonitor](market://details?id=com.eolwral.osmonitor) (1.1.0) -
    Good process monitor for Android - shows running processes. load
    from each process, total CPU usage, network information for all NICs
    (WiFi, BT, cellular/PPP), active TCP connections, battery status,
    storage status (of ALL filesystems), and internal log.
-   [Ping](market://details?id=com.mm.network) (1.5.3) - Simple ping
    app. Lets you enter an IP and select how many pings to send out.
    Shows console output.
-   [Shazam](market://details?id=com.shazam.android) (1.3) - Yup, same
    thing that was the killer app for iPhone.
-   [SMS Backup &
    Restore](market://details?id=com.riteshsahu.SMSBackupRestore) (2.1)
    - Allows backup and restore of SMS data to/from SD card, as an XML
    file. Good for Droid users who experience the [disappearing
    SMS](http://code.google.com/p/android/issues/detail?id=5669) bug.
-   [Speed Test](market://details?id=org.zwanoo.android.speedtest)
    (1.7.0) - A simple speed test app for Android from speedtest.net.
    Not sure how accurate it is, but it does upload and download tests
    over WiFi or cellular/PPP.
-   [Spirit Level Plus](market://details?id=com.wasserwaage) (1.2) -
    Simple but cool. Spirit level for the phone, using the builtin
    accelerometer. Seems relatively accurate.
-   [StopWatch](market://details?id=com.sportstracklive.stopwatch)
    (1.07) - AWFUL. It's a stopwatch app, but I could *not* get it to
    stop displaying stuff in the notifications bar.
-   [Terminal Emulator](market://details?id=jackpal.androidterm) (1.0.4)
    - Terminal emulator for Android. It feels so wonderful to be able to
    pull up an app, pop open the keyboard, and type "su" on my phone. On
    the down side, once again, I can't figure out how to enter the pipe
    or tab characters, and I don't know what shell the phone has on it.
-   [Wifi Analyzer](market://details?id=com.farproc.wifi.analyzer)
    (2.2.9) - **REALLY COOL**. Vaguely
    [WiSpy](http://www.metageek.net/products/wi-spy-24x) like, but I
    doubt it's accurate. Shows a graph of spectrum utilization with
    SSIDs and signal strength, a time-based graph of signal strength per
    SSID, a simple list of APs with channel number, BSSID, frequency,
    signal strength and encryption, and a simple "signal meter". Looks
    like it could be pretty useful.
-   [WifiScanner](market://details?id=gr.androiddev.WifiScanner) (1.7) -
    Simple WiFi scanner app. Shows all detected WiFi APs along with
    SSID, BSSID/MAC, signal level, channel and encryption.

