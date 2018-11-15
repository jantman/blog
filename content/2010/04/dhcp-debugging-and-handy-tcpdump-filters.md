Title: DHCP Debugging and Handy TCPdump filters
Date: 2010-04-14 09:21
Author: admin
Category: Software
Tags: dhcp, tcpdump, wireshark
Slug: dhcp-debugging-and-handy-tcpdump-filters

Recently at $WORK we've been having some strange issues with a
particular Xen VM not getting DHCP. Traditional (tail -f dhcpd.log)
debugging hasn't turned up much, other than the server is getting the
DISCOVER but not sending out an OFFER. I've turned to packet captures to
try and track down the problem. Of course, this is where
[tcpdump](http://www.tcpdump.org/) and
[wireshark](http://www.wireshark.org/) come into play. So I thought I'd
share some of the filters that I've been using, and a few that I
developed.

tcpdump filter for CDP (I should have this memorized by now) from
[SWeidner](http://sidewynder.blogspot.com/2005/07/tcpdump-filter-for-capturing-only.html):

~~~~{.bash}
tcpdump -nn -v -i eth0 -s 1500 -c 1 'ether[20:2] == 0x2000'
~~~~

Wireshark display filter for a specific DHCP client (by MAC):

~~~~{.text}
bootp.hw.mac_addr == 00:11:22:33:44:55
~~~~

tcpdump filter to match DHCP packets including a specific Client MAC
Address:

~~~~{.bash}
tcpdump -i br0 -vvv -s 1500 '((port 67 or port 68) and (udp[38:4] = 0x3e0ccf08))'
~~~~

tcpdump only allows matching on a maximum of 4 bytes (octets), not the 6
bytes of a MAC address. So, in the above example, we match the last 4
bytes (presumably the most unique) - our original MAC address was
`00:16:3e:0c:cf:08`, so we match on `3e0ccf08`. The `udp[38:4]` matches
from the 38th octet after the start of the UDP header (so the comparison
starts on the 39th octet) and compares a chunk 4 octets long. The [UDP
header](http://www.networksorcery.com/enp/protocol/udp.htm) is 8 octets
long, followed immediately by the [DHCP
header](http://www.networksorcery.com/enp/protocol/dhcp.htm), and the
Client MAC Address field is composed of octets 29-35 of the DHCP header.
Therefore, 8 octets for UDP header + 28 octets until Client MAC Address
+ 2 octets offset (drop the first 2 octets of MAC address to allow a 4
octet comparison) = 38 (our total offset).

This can also be modified as a Wireshark display filter:

~~~~{.text}
udp[38:4]==3e:0c:cf:08
~~~~

Using the same logic, a tcpdump filter to capture packets sent by the
client (DISCOVER, REQUEST, INFORM):

~~~~{.bash}
tcpdump -i br0 -vvv -s 1500 '((port 67 or port 68) and (udp[8:1] = 0x1))'
~~~~

Finally, a tcpdump filter for DHCPDISCOVER packets (this makes the
possibly flawed ass-umption that Option 53 will be the first option set:

~~~~{.text}
udp[247:4] = 0x63350101
~~~~

and a wireshark display filter:

~~~~{.text}
udp[247:4]==63:35:01:01
~~~~

And the same thing for DHCPREQUEST packets:

~~~~{.text}
udp[247:4] = 0x63350103
~~~~

and a wireshark display filter:

~~~~{.text}
udp[247:4]==63:35:01:03
~~~~
