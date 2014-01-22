Title: SunSPOT Update
Date: 2008-05-15 16:04
Author: admin
Category: Miscellaneous
Tags: sensor, sun, sunspot
Slug: sunspot-update

Well, I got the SPOTs working on my system. It was a bit of a pain, but
it worked.

1.  Uninstall ALL of java, jdk, netbeans, and remove user's SunSPOT
    directory.
2.  Totally remove /usr/java /usr/lib/ /usr/lib/java-1.4.0
    /usr/lib/java-1.4.1 /usr/lib/java-1.4.2 /usr/lib/java-1.5.0
    /usr/lib/java-ext /usr/lib/jvm /usr/lib/jvm-exports
    /usr/lib/jvm-private
3.  Totally remove your .netbeans
4.  Install the jdk6
5.  Install netbeans6.1
6.  Login as your normal user, run Netbeans. Install the SunSPOT plugins
    from Bruno Ghisi's blog -
    http://weblogs.java.net/blog/brunogh/archive/2008/04/starting\_with\_s.html
7.  Install ant
8.  Symlink /usr/local/netbeans to /usr/local/netbeans-6.1
9.  Here, ant -version failed for me. I had to run ant --execdebug many
    many times and do a \*lot\* of symlinking.
10. Install SunSPOT sdk through SPOTManager.
11. To install demos, under "Preferences" select "Beta Update Center",
    change Network Timeout, go back to SDKs and install Purple demos.
12. cd into \~/SunSPOT/sdk, ln -s ../Demos Demos
13. Go back to NetBeans (exit SPOTManager) and open the
    TelemetryDemo-onSpot.
14. Now it WORKS!

Also, I tried my hand at a first demo - horribly simple, it just reads
light, temperature, and accelerometer data from a USB-connected SPOT.
The code is in my [CVS repository][], as a netbeans project (NB 6.1).

  [CVS repository]: http://cvs.jasonantman.com/SunSPOTs/AllSensorsOnSpot/
