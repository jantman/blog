Title: The ultimate Geek alarm clock!
Date: 2007-01-16 22:55
Author: admin
Category: Ideas and Rants
Tags: alarm clock, embedded, geek, PoE
Slug: the-ultimate-geek-alarm-clock

So, here's an idea that I've been toying around with for a while.

I've been dong some development on a pair of
[Soekris](http://www.soekris.com) embedded Linix boards I bought to use
as a firewall/router and WAP. So, naturally, my interest in embedded
systems is piqued. I know that there are some smaller embedded Linux
devices out there. So, the idea is as follows:

Get an embedded Linux box that is either PoE or uses a hardwired
connection with a wall-wart, or better yet, uses both, so it can be
designed to have PoE as the primary power, with a 9v battery backup (ok,
it won't run too long, but can handle minor power losses if the PoE
switch isn't on a UPS).

Attach to it a clock-style LED display, or a matrix LED display, and an
additional really bright red LED, both controlled by software (serial or
GPIO).

The system has one RJ-45 connector for Ethernet (10-BaseT) and a serial
console. The console is a captive login to a setup program to define IP,
etc. but by default uses DHCP.

Plug it in, and it queries your DHCP server for an NTP server (or in the
absence of one, uses a default Stratum 2). We re-update the time every
day or so. Now, you have an accurate-to-the-second clock.

We add a speaker to the box, and have a few default built-in MP3s or
WAVs for alarm tones, and add a GPIO "snooze" and "off" button.

The serial console allows setting a daily alarm or two, as well as
selecting one of the default tones.

**The Geekier Part:**
The alarm clock is controlled by a script called by a Cron job. Now, we
add the miniserv web server and a PHP admin gateway. Login via a
password (user-selectable) and we can upload new audio files for alarms,
as well as adding alarms via the web as cron jobs - now I can program in
my class schedule, and automatically have an alarm at the right time
each day of the week!

**The Geekiest Part:**
Remember the matrix display and that additional really bright LED? We
setup simple communication between machines via SNMP or a script on the
clock (called with an Expect script on a remote machine) and we can
activate the super-bright LED, a custom sound, and even a scrolling
message on the LED display (alternates between message and time, of
course) for critical events. Now, when the servers go down, I have
another device (in addition to the SMS alerts on my cell) to tell me to
wake up and deal with it. If we want to get even more fancy, we can
enable a feature through the serial console or web interface that emits
a loud tone for a few seconds and blinks the LED if PoE is lost, or we
can't ping a user-selectable address for more than, say, one minute.

I guess I have too much free time on my hands..
