Title: New Project
Date: 2008-06-04 10:34
Author: admin
Category: Miscellaneous
Tags: 1wire, automation, home control, linux, thermostat
Slug: new-project

Well, TuxTruck has been temporarily put on the back burner. I priced out
the hardware, and it looks like a minimum of $1000, more like $1000 if I
get what I had originally wanted. This is complicated by the fact that
my roommates and I were just hit with a $220 electric bill. Mostly,
that's due to the central air conditioning in our apartment, and the
horrible inefficiencies with it.

Inefficient? Yes. At the moment, I'm the only person in the apartment.
I'm home for the weekend from 18:00 Friday through about 15:00 Monday. I
have class Monday-Thursday night 18:00-21:45. I work Tuesday-Friday
0900-1700. Even though the thermostat we have is "programmable", it can
only be set for 4 time periods per day, weekdays and weekends. So, I
figured that a little added efficiency in calculating when the A/C
should run would go a long way towards energy savings.

My idea - tuxOstat - is to have a Linux box that has temperature sensors
placed around the apartment, and a bank of relays to control the
heating/cooling systems. So, even though I only got the idea last
Thursday, version 1 should be up and running next week.

In terms of hardware:

1.  Originally I had planned on using a [Soekris
    net4526](http://www.soekris.com/net4526.htm) that I had lying
    around. However, the added cost of a MiniPCI USB card seemed
    prohibitive for a one-off project. Instead, I'm using an old HP
    OmniBook laptop that was already lying behind my servers. It's
    running Debian 4.0.
2.  I've ordered (just 15 minutes ago) a [Phidgets InterfaceKit
    0/0/4](http://www.phidgets.com/products.php?product_id=1014), which
    connects via USB and provides 4 relays. One will control the fan,
    one for the A/C compressor, one for the heat, and one unused (for
    now).
3.  I already had a
    [DS9490](http://www.hobby-boards.com/catalog/product_info.php?cPath=23&products_id=1503)
    Dallas 1-wire USB adapter from
    [Hobby-Boards.com](http://www.hobby-boards.com/) along with five
    [DS18S20P](http://www.hobby-boards.com/catalog/product_info.php?products_id=93)
    1-wire parasite power temperature sensors. I've wired those up with
    one in the living room near the existing thermostat, one in my
    bedroom, and one stuck about five feet up one of the A/C conduits,
    to sense when the system is actually putting out cold air. I've had
    them logging to MySQL since 0200 today.
4.  I decided to bite the bullet and order a beautiful [CrystalFontz
    XES635BK-TMF-KU](http://www.crystalfontz.com/products/635xes/index.html)
    for the physical interface. It's a little backlit LCD display, in a
    surface-mount box, along with four bi-color LEDs and a 6-button
    keypad. That should handle the interface for anyone who doesn't want
    to grab a console.
5.  I'll be looking for a eight-pin header so that the relays will plug
    right in to the screw-terminal block that the thermostat uses, to
    make for easy switching to the original thermostat if needed (or
    when moving out in a year).

Now, in terms of software:

1.  A Python text-based configuration/administration program. Will be
    accessed via SSH or KVM for the actual machine.
2.  Lots of state data stored in files under /var.
3.  A python script, run via cron every 2 minutes, that checks
    temperatures from the 1-wire bus, logs them to MySQL (on a remote
    host) and updates the temperature files in /var.
4.  A master control script, run via cron every minute, that looks at
    the temperatures, the current system state, any manual overrides
    that exist, and decides what relays should be on or off.
5.  A daemon to handle relay control.
6.  A daemon to handle the LCD display output and keypad input
    (including immediate manual overrides).
7.  A method of providing overrides of the programmed schedule on a
    single-instance basis, i.e. "system completely off from 2008-06-06
    18:00 to 2008-06-08 15:00".

