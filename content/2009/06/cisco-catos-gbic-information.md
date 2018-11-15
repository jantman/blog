Title: Cisco CatOS GBIC Information
Date: 2009-06-20 11:35
Author: admin
Category: Hardware
Tags: catos, cisco, gbic, networking
Slug: cisco-catos-gbic-information

I have a Cisco WS-G4912 (12-port Gigabit aggregation switch) that I'm
using to bring my network up to Gig-E. It's about all that I could
afford, and works fine. Most of my older servers are running 1000BASE-SX
multimode fiber, but I decided to use copper GBICs for the new boxes
that have onboard Gig-E ports. Unfortunately, $100+ for Cisco GBICs was
way too much for me, so I found some third-party GBICs on Ebay from
[TNet
USA](http://members.ebay.com/ws/eBayISAPI.dll?ViewUserPage&userid=tnetusa)
right in Fairfield, NJ.

I wanted to make sure the GBICs work right, so I happened to find out
about the undocumented CatOS command \`show sprom [mod/port]\` which
shows the serial PROM information.
