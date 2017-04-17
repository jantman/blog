Title: Python script to check xfinity data usage
Date: 2017-04-17 16:11
Author: Jason Antman
Category: Tech HowTos
Tags: comcast, xfinity, data, usage, bandwidth, cap, python, selenium
Slug: python-script-to-check-xfinity-data-usage
Summary: Python/selenium script to check your Xfinity data usage

Yesterday I got one of those invasive, abusive, utterly awful (and idiotic) [injected popups from Xfinity](https://www.techdirt.com/articles/20161123/10554936126/comcast-takes-heat-injecting-messages-into-internet-traffic.shtml) that I'm at 75% of my monthly bandwidth allocation. Nevermind the fact that I have a bunch of automated scripts running on my computer and injected HTML might never be seen by a human, or that I work from home and every once in a while I'll find myself pulling and pushing multi-GB Docker images, which completely kills my 1TB bandwidth limit. But it's only half way through the month and, frankly, I'm pretty mystified how I could have used so much data this quickly. I went to Xfinity's site to check my usage meter - after rummaging around in my password manager to find my credentials - and realized that while it shows a graph of the past three months and a progress bar for the current month, it doesn't show me any detailed (i.e. daily or hourly) data that would help me figure out the cause.

So, I wrote a little [script](https://github.com/jantman/xfinity-usage) using Python and Selenium to log in to their My Account site and screen-scrape the [usage meter](http://www.xfinity.com/usagemeter). Why Comcast would require me to log in to view my usage when I'm accessing their site from the IP address *they* gave me, on *their* network, I have no idea... unless it's to provide a disincentive for customers to be aware of their usage. But I wrote the script, and it seems to be working. For the time being, I'm both pushing the results into Graphite so I can see usage over time, and sending myself a daily email so I can keep on top of usage.

Apparently Comcast used to have [a desktop app](http://usmapp-qa.comcast.net/) to track usage but it's since been completely shut down, along with the API that backed it (which an enterprising fellow reverse-engineered in [this script](https://github.com/WTFox/comcastUsage)). I can only assume this is another indication that, though the bandwidth cap was introduced citing "network performance", they really don't want people lowering network load (and avoiding fees).

I don't remember anything about screen-scraping in the Xfinity terms of service - and if they're f-ing injecting elements into *my* web traffic, I sure as hell hope they don't complain about me checking my own usage - but use this at your own risk. Also be aware that it's screen-scraping, so it may well break with a site redesign or element ID changes.

If anyone would find this useful, please see [https://github.com/jantman/xfinity-usage](https://github.com/jantman/xfinity-usage).
