Title: Consolidation of nmap port scan results to HTML table
Date: 2011-01-30 20:00
Author: admin
Category: Tech HowTos
Tags: nmap, security
Slug: consolidation-of-nmap-port-scan-results-to-html-table

I spent a good part of the weekend auditing the security of my
infrastructure at home, since I haven't given it much attention lately.
One of my first steps was doing a port scan with
[nmap](http://www.nmap.org) of my public IPs from a remote host, both to
make sure there's nothing showing up that shouldn't be and to get an
idea of what a potential attacker might see. However, given all of
nmap's options for different TCP scans, it seemed like a lot of data to
sort through. Without finding any good solution in my cursory search, I
wrote up a little PHP script that takes any number of XML nmap scan
files on the command line, parses out the hosts and ports found in each
of them, and presents a nice table showing the result for each host/port
for each scan file.

The current version of the script can be found at
[https://github.com/jantman/misc-scripts/blob/master/nmap-xml-to-table.php](https://github.com/jantman/misc-scripts/blob/master/nmap-xml-to-table.php),
and simply called as `./nmap-xml-to-table.php file1.xml file2.xml [...]`
and outputs HTML to stdout.
