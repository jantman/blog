Title: How to Find Network Settings in various operating systems
Date: 2011-02-16 21:34
Author: admin
Category: Tech HowTos
Tags: linux, mac, networking, troubleshooting, windows
Slug: how-to-find-network-settings-in-various-operating-systems

Since I'm occasionally asked these things, here's how to find some
commonly needed network information in various operating systems - for
now, Windows, Mac OS X and Linux, as well as Android and iOS
(iPhone/iPad/etc.). My assumption is that the people running BSD,
Solaris, etc. (and yes, all of those have visited my blog) know this
stuff. I won't go into descriptions of what these "strange" things are.

First off, I know that most desktop computer users are used to doing
everything graphically. If you know what you want to do, the command
line is a lot faster. There's no reason to fear it. Watching a cooking
show might be wonderful if you have no idea how to cook a meal, but it's
not very efficient if you just need the list of ingredients.

First off, how to get a command prompt:

-   **Windows**: For XP and before, Start -\> Run -\> type "cmd", click
    Ok. For Vista, Start -\> type "cmd", click it.
-   **Mac OS X**:Applications -\> Utilities -\> Terminal
-   **Linux/Unix**: Konsole, Xterm, whatever else you use, or just drop
    to command line/runlevel 3

In the following examples, anything in `monospace font` should be typed
exactly as is at the command prompt. *Note: some of this may need to be
run as Administrator/root. If you're using Windows Vista or newer, once
"cmd" appears under Programs, right-click it and select Run as
Administrator. On Mac or Linux, you may have to run as sudo, and you may
have to specify an absolute (full) path.*

**Default Gateway** - on a simple home network, this is the IP address
of your router.

-   **Windows**: `route PRINT`, look for the line beginning with
    "Default Gateway:"
-   **Mac OS X**: `route get default`, look for the "gateway:" line.
-   **Linux**: `sudo /sbin/route`, look for the line beginning with
    "default", it will be the in the "Gateway" column. If your system
    uses iproute2, `ip route show`.

**MAC Address** - The (more or less) globally unique address of your
computer's network adapter. Each network adapter (wired, wireless, etc.)
has its own. Looks like xx-xx-xx-xx-xx-xx or xx:xx:xx:xx:xx:xx or
xxxxxx:xxxxxx where each "x" is a number from 0 to 9 or a letter from a
to f.

-   **Windows**: `ipconfig /all`, look for the name of your network
    connection and then the indented line starting with "Physical
    Address".
-   **Mac OS X**: `ifconfig`, look for your network adapter (en0 is
    wired ethernet, en1 is your AirPort), the address will be on a line
    after "ether".
-   **Linux**: `ifconfig`, look for "HWaddr" for the right interface.

**WAN (Internet or External) IP Address)** - Go to
[whatismyip.jasonantman.com](http://whatismyip.jasonantman.com).

**Ping another host** - A ping test shows (simple explanation) how long
it takes packets to get from your computer to another. (For you Warcraft
players, this isn't the same as the ping times shown in-game, and you
can't ping the realm servers).

-   **Windows**: `ping -t IPaddress`, the `-t` makes it run until you
    type Control-C to stop it.
-   **Everything else**: `ping IPaddress`Ctrl-C (or whatever your OS
    uses) to stop it.

I'll update this with more when I get time...
