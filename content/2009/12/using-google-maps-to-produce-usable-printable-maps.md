Title: Using Google Maps to produce usable, printable maps
Date: 2009-12-01 14:11
Author: admin
Category: Tech HowTos
Tags: catrography, emergency, EMS, google, maps, PHP
Slug: using-google-maps-to-produce-usable-printable-maps

This is a follow-up to my [Making maps from GIS data with
Inkscape](/2009/11/making-maps-from-gis-data-with-inkscape/) post. After
playing around with Inkscape for quite a while, and coming up with the
dismal results seen in that post, I decided there has to be an easier
way. A little Googling turned up [this video
tutorial](http://www.wipeout44.com/video/misc/google_maps_large.asp) on
how to print large scale maps from Google Maps. It turns out that the
Google Maps API will honor almost any pixel resolution that it's passed.
The [Screengrab](https://addons.mozilla.org/en-US/firefox/addon/1146)
add-on for Firefox has the wonderful capability of being able to capture
a screengrab of page content, at actual resolution, regardless of screen
resolution. So load up a 5000x5000 pixel Google Map, use the Screengrab
addon, and end up with a full 5000x5000 pixel image file.

After testing this a bit, I decided to go the Google Maps route. This
also has a lot of other added bonuses - I can store my overlay data in
simple XML files, add and remove layers on-the-fly, and also make it
available online (and, theoretically, to any Google Maps-equipped device
used by responders). This even opens up the possibility of using paper
maps as a last resort, and providing the Fire Department with live
hydrant maps on GPS-enabled handheld devices and phones.

The quirks, however, may need some serious photoshopping (err, rather,
[gimp](http://www.gimp.org/)ing) to fix:

1.  With all of the background color, how will this look when printed?
2.  How do I make the town borders easily defined? It would be a *lot*
    of raster editing to remove the background color of areas outside of
    town.
3.  How do I overlay a grid for a street name index?

The first step was to setup a large Google Map to develop with. I used
PHP and Monte Ohrt's
[GoogleMapAPI](http://www.phpinsider.com/php/code/GoogleMapAPI/) PHP
wrapper class. It was simple enough to setup a big (3300x5100px) map,
zoom out in Firefox, and start adding some stuff. My examples and
development pages, if you want to take a peek at the code, are
[here](http://www.jasonantman.com/indexed/googleMaps/).

The first step was to draw a polygon for the outline of the town. I
found some very detailed information on how to get zip code boundary
lines on Matt Cutts'
[blog](http://www.mattcutts.com/blog/fun-with-zip-codes/). Apparently,
he's a Google software engineer, heading up their webspam team. I
grabbed the files from the Census, as described, and came up with the
boundary for my zip code looking like:

~~~~{.text}
        60      -0.741427638843858E+02       0.409963180802469E+02
      -0.741375870000000E+02       0.410075970000000E+02
      -0.741308870000000E+02       0.410061970000000E+02
      -0.741308870000000E+02       0.410061970000000E+02
      -0.741307260000000E+02       0.410032600000000E+02
      -0.741326870000000E+02       0.409955970000000E+02
      -0.741278870000000E+02       0.409943970000000E+02
      -0.741280870000000E+02       0.409938970000000E+02
      -0.741327870000000E+02       0.409853970000000E+02
      -0.741352870000000E+02       0.409830970000000E+02
      -0.741369600000000E+02       0.409818620000000E+02
      -0.741410520000000E+02       0.409821940000000E+02
      -0.741412870000000E+02       0.409826970000000E+02
      -0.741412870000000E+02       0.409826970000000E+02
      -0.741417870000000E+02       0.409847970000000E+02
      -0.741427870000000E+02       0.409863970000000E+02
      -0.741482870000000E+02       0.409868970000000E+02
      -0.741536880000000E+02       0.409899970000000E+02
      -0.741510880000000E+02       0.409929970000000E+02
      -0.741531880000000E+02       0.409965970000000E+02
      -0.741571880000000E+02       0.409988970000000E+02
      -0.741557880000000E+02       0.410013970000000E+02
      -0.741461870000000E+02       0.410018970000000E+02
      -0.741400870000000E+02       0.410065970000000E+02

      -0.741375870000000E+02       0.410075970000000E+02
END
~~~~

As per Matt's instructions, I stripped off the first and last lines,
converted everything to normal decimal notation, and built it into a PHP
array:

~~~~{.php}
$MP_boundary = array();
$MP_boundary[] = array(-74.137587, 41.007597);
$MP_boundary[] = array(-74.130887, 41.006197);
$MP_boundary[] = array(-74.130887, 41.006197);
$MP_boundary[] = array(-74.130726, 41.003260);
$MP_boundary[] = array(-74.132687, 40.995597);
$MP_boundary[] = array(-74.127887, 40.994397);
$MP_boundary[] = array(-74.128087, 40.993897);
$MP_boundary[] = array(-74.132787, 40.985397);
$MP_boundary[] = array(-74.135287, 40.983097);
$MP_boundary[] = array(-74.136960, 40.981862);
$MP_boundary[] = array(-74.141052, 40.982194);
$MP_boundary[] = array(-74.141287, 40.982697);
$MP_boundary[] = array(-74.141287, 40.982697);
$MP_boundary[] = array(-74.141787, 40.984797);
$MP_boundary[] = array(-74.142787, 40.986397);
$MP_boundary[] = array(-74.148287, 40.986897);
$MP_boundary[] = array(-74.153688, 40.989997);
$MP_boundary[] = array(-74.151088, 40.992997);
$MP_boundary[] = array(-74.153188, 40.996597);
$MP_boundary[] = array(-74.157188, 40.998897);
$MP_boundary[] = array(-74.155788, 41.001397);
$MP_boundary[] = array(-74.146187, 41.001897);
$MP_boundary[] = array(-74.140087, 41.006597);
$MP_boundary[] = array(-74.137587, 41.007597);
~~~~

Though this data doesn't seem exactly 100% accurate (at least by my
knowledge of the town, and every map I can find) it's quite close and a
very good start.

I'll update later this week when I have some more done...
