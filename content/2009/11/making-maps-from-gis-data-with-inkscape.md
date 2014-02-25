Title: Making maps from GIS data with Inkscape
Date: 2009-11-25 09:24
Author: admin
Category: Tech HowTos
Tags: gis, inkscape, map, shapefile, svg
Slug: making-maps-from-gis-data-with-inkscape

**NOTE-** I more or less dropped this project, in favor of a more
precise approach, as outlined in [Using Google Maps to produce usable,
printable
maps](/2009/12/using-google-maps-to-produce-usable-printable-maps/).
This is being left just to give other people ideas.

**Background**

I was recently asked by one of the officers of our volunteer [fire
department](http://www.mpnj.com/mp_fd.asp) if I could come up with a
good map of our town that could be laminated and put in the trucks. We
currently have a really simple [PDF
map](http://www.mpnj.com/forms/TownMap.pdf) of our town, but it was done
by a for-profit entity and is only available as the single-size PDF. The
map itself looks like:

![town map](GFX/TownMap.png)

**Data**

With a little research, I was able to find quite a lot of GIS data on
the [NJ Department of Environmental Protection GIS
site](http://www.state.nj.us/dep/gis/). While the GIS viewer software by
[ESRI](http://www.esri.com) seems to be the usual choice, I found that
the GPL'ed [Quantum GIS](http://www.qgis.org/) project (available in the
OpenSuSE
[Application:Geo](http://download.opensuse.org/repositories/Application:/Geo/)
repository) displayed the data quite nicely. The only major issue was
with street names - there was no way to label lines with two fields from
the metadata (the TIGER/Line files have separate fields for the street
name and the st/rd/ln suffix). More importantly, I needed something that
both looked nice and included overlays (specifically of the fire
department's hydrant map).

**SVG**

A little research led me to the
[shptosvg](http://wiki.github.com/kbh3rd/shptosvg) perl script that
converts a shapefile to SVG. As the streets within our town won't change
any time soon, I figured it was the most logical solution, when
producing a map for print where I would need to re-scale and edit
overlay layers - to just get the data I needed into SVG and do the rest
there. I was able to export both the county roads shapefile and the
state municipal boundaries shapefile to an SVG drawing, and then open
that in [Inkscape](http://www.inkscape.org/). To export them, I used:

~~~~{.bash}
perl shptosvg.pl -x3300 -y5100 -p1 -d0.5 berrds00.shp muni_boundaries/nj_munis.shp > test2.svg
~~~~

where berrds00.shp is the TIGER/Line roads shapefile for our county
(from the 2000 census) and muni\_boundaries/nj\_munis.shp is the
shapefile for the NJ municipal boundaries. The x and y sizes (3300px and
5100px, respectively) were based on an 11x17" sheet printed at 300dpi.

**Initial Work**

The initial work was a real pain. I moved each group of objects (the
municipal boundaries and the county road lines) to a separate layer and
then ungrouped them. Next, I began the painstaking process of deleting
all of the objects outside of our town boundary, except the roads
directly around our town. Once this was done, I used File -\> Document
Properties -\> Fit to Page Selection to "crop" the canvas to the
remaining objects. Thanks to the nature of **S**VG, I was able to crop
the page down and then scale it up again to 11x17" without any loss of
data or quality. I then moved the roads outside of our town (luckily,
most of the roads from the TIGER data ended up being made up of a series
of line segments, with most of them having a break at the town boundary)
to another layer, so that they could be easily given a light gray color.
I also gave the down boundary a nice red color. Finally, as I neglected
to include a railroad shapefile when I did the original conversion to
SVG, and adding one would obviously not jive with the massive deletion
and re-scaling I'd done, I drew in the one railroad line running through
town by hand, and gave it a nice dashed line type.

At this point, I ended up with something that looked like:

![inkscape work version 1](GFX/inkscape.png)

**Cleaning Up**

I now had the following tasks to perform:

1.  Find a nicer way to show the street lines. The ideal would be a line
    made up of 1-2px lines on either side, with a white center. Second
    best would just be thinner lines.
2.  Cleanup the roads around the town boundary - make sure they're black
    within the town and gray outside. If need be. delete some lines and
    re-draw them to split at the town boundary.
3.  Add labels for the bordering towns.
4.  The big one - add street name labels.
5.  Perhaps add in icons/labels/boxes for churches, schools, municipal
    buildings, etc.
6.  Add in, once I get a copy of the map, the fire department hydrant
    locations as another layer.

And the added bonuses that I'd like to do:

1.  Add house numbering on a block level for each street.
2.  Add a grid overlay, with an index of streets by grid square on the
    back.

As of right now (about 9AM on November 25, 2009) this is where I stand.
I'll update a bit more when I get farther along.
