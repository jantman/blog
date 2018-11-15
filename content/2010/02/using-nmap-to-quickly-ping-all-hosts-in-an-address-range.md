Title: Using nmap to quickly ping all hosts in an address range
Date: 2010-02-08 09:10
Author: admin
Category: Miscellaneous
Tags: dhcp, nmap, ping, sysadmin
Slug: using-nmap-to-quickly-ping-all-hosts-in-an-address-range

At $WORK, the subnet we use for some of our workstations and test boxes
was only recently setup with DHCP. Previously, we'd used
IP-by-Whiteboard in the office. As a result, most of the recent machines
use DHCP, but there are a few older ones still around using static
addresses. I recently had to add a new machine, so I had to go through
the process of finding out which IPs are in use and which aren't (since
some aren't in DHCP).

I decided to be good and update DHCP with records for all machines in
the subnet, whether they're actually using DHCP or not. There's a quick
way to do this with `nmap` using the options for ping scan (`-sP`) and
always resolve DNS (`-R`):

~~~~{.console}
# nmap -sP -R 172.16.43.129-159
Host ar01-hill-hill.example.com (172.16.43.129) appears to be up.
MAC Address: 00:11:BC:7D:28:0A (Cisco Systems)
Host ccf-hill019-1.example.com (172.16.43.130) appears to be up.
MAC Address: 00:00:AA:63:54:BB (Xerox)
Host ccf-hill019-2.example.com (172.16.43.131) appears to be down.
Host ccf-hill019-3.example.com (172.16.43.132) appears to be down.
Host ccf-hill019-4.example.com (172.16.43.133) appears to be down.
Host ccf-hill019-5.example.com (172.16.43.134) appears to be down.
Host ccf-hill019-6.example.com (172.16.43.135) appears to be down.
Host ccf-hill019-7.example.com (172.16.43.136) appears to be up.
Host speakeasy.example.com (172.16.43.137) appears to be up.
MAC Address: 00:17:A4:13:EB:57 (Global Data Services)
Host ccf-hill019-9.example.com (172.16.43.138) appears to be up.
MAC Address: 00:17:A4:13:E8:17 (Global Data Services)
Host ccf-hill019-10.example.com (172.16.43.139) appears to be down.
Host testmac01.example.com (172.16.43.140) appears to be down.
Host ccf-hill019-12.example.com (172.16.43.141) appears to be down.
Host ccf-hill019-13.example.com (172.16.43.142) appears to be up.
MAC Address: 00:0D:29:59:58:00 (Cisco)
Host ccf-hill019-14.example.com (172.16.43.143) appears to be down.
Host ccf-hill019-15.example.com (172.16.43.144) appears to be down.
Host ccf-hill019-16.example.com (172.16.43.145) appears to be down.
Host ccf-hill019-17.example.com (172.16.43.146) appears to be down.
Host ccf-hill019-18.example.com (172.16.43.147) appears to be up.
MAC Address: 00:1E:C2:0D:C1:98 (Unknown)
Host ccf-hill019-19.example.com (172.16.43.148) appears to be down.
Host ccf-hill019-20.example.com (172.16.43.149) appears to be down.
Host ccf-hill019-21.example.com (172.16.43.150) appears to be down.
Host lordkris.example.com (172.16.43.151) appears to be down.
Host ccf-hill019-23.example.com (172.16.43.152) appears to be down.
Host ccf-hill019-24.example.com (172.16.43.153) appears to be down.
Host ccf-hill019-25.example.com (172.16.43.154) appears to be down.
Host ccf-hill019-26.example.com (172.16.43.155) appears to be down.
Host ccf-hill019-27.example.com (172.16.43.156) appears to be down.
Host ccf-hill019-28.example.com (172.16.43.157) appears to be down.
Host ccf-hill019-29.example.com (172.16.43.158) appears to be down.
Host ccf-hill019-30.example.com (172.16.43.159) appears to be down.
Nmap finished: 31 IP addresses (7 hosts up) scanned in 0.892 seconds
~~~~

As you can see, the results also (very usefully) include MAC addresses,
so it's pretty easy to update DHCP as needed.
