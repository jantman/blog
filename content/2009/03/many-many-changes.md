Title: Many Many Changes; Downtime
Date: 2009-03-07 19:05
Author: admin
Category: Projects
Tags: firewall, optimum, rack, router, wan
Slug: many-many-changes

Well, I don't have time to go into a lot of detail, but I thought I'd
give a recap of what's going on. I went down to Mount Holly, NJ
yestserday morning - about a 2-/12 hour drive each way, and picked up a
41U rack for the basement. Pretty damn heavy, took me two hours to
disassemble it, wrangle it down the stairs, and get it back together.
It's an old round-hole rack, which didn't seem to matter much until I
found that the tabs of the Dell Rapid Rails are just a bit too big to
fit in it, so neither my rack KMM nor the rails for my mail server will
fit. A bigger problem, though, is that the guy told me it was the
standard HP 29" deep, and I found it to be 28-1/4" deep when I started
racking things up. So, though I just spent $200 on rails for old
Proliants, they're all about 1/2" too long to fit.

Yesterday, I also had Cablevision show up to install the new Optimum
Business with 5 static IPs.

So, last night around 9:00, I started the arduous task of (for the first
time ever) powering down ALL of my machines, moving them to the new
rack, and re-cabling. That took about 2-1/2 hours, after which my intent
was to bring up the new Optimum connection, configure the Vyatta router,
and roll over mail and web. From what I'd read of the Vyatta docs it
seemed a relatively straightforward task, and being the stubborn jackass
that I am, I decied, "hey, it's my personal site, it's low traffic, and
I want it up before I go to sleep. I'll roll over DNS *before* I bring
everything up."

That was a **very bad idea**. Vyatta isn't nearly as
simple as it seems - especially for someone who isn't really a network
(or at least router/firewall) guy. When they say Enterprise, they mean
robust. They also mean that week-long bootcamps aren't for naught. It
took me about half an hour to figure out that even if no "firewall"
ruleset is associated with an interface, it still has an implicit drop
all. And if you only want to firewall what's coming in from the outside
world, and let everything out, you need to add explicit allow all rules
to the in and out sides of the LAN inteface and the out side of the WAN
interface.

To top all this off, I had some serious still-unexplained DHCP problems
on the LAN, a serious issue since I just set all my hosts to DHCP (which
I'll probably undo soon). So, Yesterday was network work from 7:30 AM to
3 AM today (including driving to pickup the rack). By the time 3 AM
rolled around, I was quite unhappy that I decided to roll over DNS in
order to force myself to get things working, as I ended up going back to
FiOS for client access only. Today started around 10 AM, and here I am -
6:30 PM, and I just got things working partially right. I have mail
working - arguably the most important - for jasonantman.com only, though
I have yet to setup any aliases.

On the web side, I'm working to setup name-based vhosts for all of the
subdomains, but for some reason, blog is showing up for everything.
Luckily it works right. So we'll see....
