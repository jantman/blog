Title: Using wireshark to capture packets from a remote host
Date: 2011-04-26 10:50
Author: admin
Category: Tech HowTos
Tags: ethereal, linux, sysadmin, tcpdump, troubleshooting, wireshark
Slug: using-wireshark-to-capture-packets-from-a-remote-host

I spend a fair amount of my time debugging network and service problems
on a few racks of Linux servers. Of course, they're located in a data
center (yes, just downstairs, but still not quite as comfortable as my
office), and they're all command-line only - no sense in using up RAM
and CPU to run a graphical UI on a box that should just be serving
remote clients. I used to go through the arduous task of running a
command line [`tcpdump`](http://www.tcpdump.org/) session on the server
until I thought I had enough packets, then SCPing it over to my
workstation and opening the file in
[wireshark](http://www.wireshark.org/) (formerly Ethereal). Fortunately,
thanks to a
[post](http://linuxexplore.wordpress.com/2010/05/30/remote-packet-capture-using-wireshark-tcpdump/)
on Rahul Panwar's [Linux Explore
blog](http://linuxexplore.wordpress.com/) (which seems to be sadly
neglected), I found a much easier way to do it. I've summarized that
post here, added a little explanation, and also made some useful
comments for people working on Red Hat/CentOS and OpenSuSE.

**What you need:**

1.  Source system (the server you want to capture packets on) that you
    have SSH access to, with tcpdump installed, and available to your
    user (either directly, or via sudo without password).
2.  Destination system (where you run graphical Wireshark) with
    wireshark installed and working, and `mkfifo` available.

**Procedure:**

1.  On the destination system, if you haven't already done so,

~~~~{.bash}
mkfifo /tmp/packet_capture
~~~~

    <p>
    This creates a [named pipe](http://en.wikipedia.org/wiki/Named_pipe)
    where the source packet data (via ssh) will be written and Wireshark
    will read it from. You can use any name or location you want, but
    `/tmp/packet_capture` is pretty logical.

2.  On your destination system, open up Wireshark (we do this now, since
    on many systems it required the root password to start). In the
    "Capture" menu, select "Options". In the "Interface" box, type in
    the path to the FIFO you created (`/tmp/packet_capture`). You should
    press the Start button before running the next command - I recommend
    typing the command in a terminal window, pressing start, then
    hitting enter in the terminal to run the command.
3.  On the destination system, run

~~~~{.bash}
ssh user@source-hostname "sudo /usr/sbin/tcpdump -s 0 -U -n -w - -i eth0 not port 22" > /tmp/packet_capture
~~~~

    <p>
    This will SSH to the source system (`source-hostname`, either by
    hostname or IP) as the specified user (`user`) and execute
    `sudo /usr/sbin/tcpdump`. Omit the "sudo" if you don't need it,
    though if you do, you'll need passwordless access. Options passed to
    tcpdump are: "-s 0" snarf entire packets, no length limit; "-U"
    packet-buffered output - write each complete packet to output once
    it's captured, rather than waiting for a buffer to fill up; "-n"
    don't convert addresses to hostnames; "-w -" write raw packets to
    STDOUT (which will be passed through the SSH tunnel and become
    STDOUT of the "ssh" command on the destination machine); "-i eth0"
    capture on interface eth0; "not port 22" a tcpdump filter expression
    to prevent capturing our own SSH packets (more on this below). The
    final "\> /tmp/packet\_capture" redirects the STDOUT of the ssh
    program (the raw packets from tcpdump on the source machine) to the
    `/tmp/packet_capture` FIFO.

4.  When you're ready to stop the capture, just Ctrl+C the SSH command
    in the terminal window. Wireshark will automatically stop capturing,
    and you can save the capture file or play around with it. To capture
    again, you'll need to restart the capture in Wireshark and then run
    the ssh command again.

**A note on network usage and tcpdump filters**

This is a relatively bandwidth intensive procedure. If you use the "not
port 22" tcpdump filter (shown above) on the source machine, all traffic
over eth0 (other than SSH) on that machine will be duplicated within an
SSH tunnel. So you have double the traffic, plus the overhead of
tunneling all that within SSH to the destination machine. If you're
capturing data from a busy machine this way, you could easily saturate
the uplink and wreak all sorts of havoc. As a result, I'd recommend
making the tcpdump filter as specific as you can while still retaining
the data you need. If you can replace it with a filter for specific
ports (i.e. `'(port 67 or port 68)'` for DHCP) or specific hosts, that
should cut down on the amount of data you actually have to pass through
the tunnel.
