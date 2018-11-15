Title: dashsnap.py - A Script to Snapshot a Graphite Dashboard
Date: 2014-05-07 21:58
Author: Jason Antman
Category: Software
Tags: graphite, monitoring
Slug: dashsnap-a-script-to-snapshot-a-graphite-dashboard
Summary: dashsnap.py, a script to snapshot a Graphite dashboard at various intervals

As we push more and more and more metrics into [Graphite](http://graphite.wikidot.com/)
at work, we've found the need to preserve data from an incident or outage to be quite
important. Especially now that we're feeding a _lot_ of our data at 10-second intervals,
and our storage schemas generally start aggregating that past 24 hours (God only knows
how many spikes are gone if you look a week later), it's important to capture as much
data as we think we'll need as soon after the incident as possible.

To this end, a few days (and nights) into a relatively major crisis, I wrote a little
python script, [dashsnap.py](https://github.com/jantman/misc-scripts/blob/master/dashsnap.py).
It's horribly simple; pass it the hostname to your graphite server (if "graphite" doesn't
resolve to what you want), the name of a dashboard, optionally a height and width for images
(the default is currently 1024x768), and either a from and to date/time or a list of graphite
URL-style intervals (the default is a ginormous "-10minutes,-30minutes,-1hours,-2hours,-4hours,-6hours,-12hours,-24hours,-36hours").
It will find all graphs on your dashboard, and locally save (in a horribly named directory)
both PNGs of all the graphs, as well as the _raw JSON data_ for them. It'll also write
(2 AM-simple) HTML index files to all of the intervals and graphs within them.

Here's a view of the index page using the default intervals:

[![screenshot of rendered index page](/GFX/dashsnap_index_sm.png)](/GFX/dashsnap_index.png)

And here's the page showing graphs and JSON links for an individual dashboard for one interval:

[![screenshot of one interval page](/GFX/dashsnap_page_sm.png)](/GFX/dashsnap_page.png)

I'll quickly admit right now that this is alpha software, if you can even call it that.
I guess in reality it's a late-night fix to a problem that deserves more. But, if it can
save someone else a few hours late at night, it's worth mentioning. PRs are welcome, as
are issues and suggestions on GitHub for bugs, or for where I should take this; I like
the handy little CLI script (though the output could use quite a bit of visual work),
but I'm also toying around with the idea of creating a service to take the snapshots
and store them, mostly thinking about it being part of something like
[Etsy's Morgue](https://github.com/etsy/morgue).

The latest version of the source for dashsnap will (within the forseeable future)
be available at:

[https://github.com/jantman/misc-scripts/blob/master/dashsnap.py](https://github.com/jantman/misc-scripts/blob/master/dashsnap.py)
