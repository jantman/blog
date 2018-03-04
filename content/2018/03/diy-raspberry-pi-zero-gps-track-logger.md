Title: DIY Raspberry Pi Zero GPS Track Logger
Date: 2018-03-04 11:00
Modified: 2018-03-04 11:00
Author: Jason Antman
Category: Tech HowTos
Tags: embedded, gps, hiking, logger, raspberrypi
Slug: diy-raspberry-pi-zero-gps-track-logger
Summary: Simple DIY Raspberry Pi Zero USB GPS logger, with code and instructions.
Status: draft

Last weekend I was out hiking with one of my dogs when I realized that I didn't know the exact length of the route we were taking. We were at the [Davidson-Arabia Nature Preserve](http://arabiaalliance.org/explore/plan-your-visit/visit-davidson-arabia-nature-preserve/), part of the Arabia Mountain National Heritage Area, only about 20 minutes from home. It's a wonderful afternoon hike for me since it's so close to home and the trails are easy. It's also a laid back hike - the area is only about 2.1 square miles (5.4 sq. km.) bordered on all sides by well-traveled roads or suburban neighborhoods and dominated by Arabia Mountain and a lake - with many trails and high traffic, so I'm less concerned about navigation than I would be in the backcountry. However, since my usual route covers portions of two trails and a cut-through between them, I don't know what the actual distance is.

At first it seemed like the logical solution to this would be tracking hikes on my phone using one of the many apps for this (or a similar) purpose. But that didn't seem like a good solution to me for a number of reasons. First, my current phone is an aging Samsung Galaxy S6 (I tend to buy the best phone available at the time, and keep it until it dies) and the battery life is far from what it used to be. I carry an external battery pack for it, but frequently polling GPS position is extremely power intensive on any phone; I'd rather leave my phone for tasks that actually require it  like communication, weather, and checking some of the great digital maps that are available. More importantly, the GPS antennas in most smartphones seem to be rather position sensitive and I haven't gotten very good results recording an accurate track with my phone in my pocket or belt holster, let alone in my pack (where it often is on more challenging terrain).

I started looking at the commercial GPS loggers available online, but few of them seemed like compelling choices for the cost. Then I realized that I could probably piece one together at no cost using parts that I already had, namely a [RaspberryPi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/), USB GPS, and the [10Ah external battery pack](https://www.amazon.com/gp/product/B01JIYWUBA/) I use for my phone. It turns out that the [Deluo 31-311-01 USB GPS](https://www.amazon.com/gp/product/B000FPILZG/) I bought a decade ago has been lost to time, likely thrown out in one of the electronics purges I've done over the past few years. But I was able to get a new SiRF Star IV-based [GlobalSat BU-353-S4 USB GPS](https://www.amazon.com/gp/product/B008200LHW/) on Amazon. The manufacturer's specifications sound quite nice and even though the [gpsd hardware list](http://www.catb.org/gpsd/hardware.html) rates it extremely poorly, once I received it in the mail I unboxed it and set it on the sill inside my window and was able to get a very accurate fix in about a minute.

## The Result

[![Photograph of finished hardware next to playing card deck for size comparison](/GFX/pizero_gpslogger_1_sm.jpg)](/GFX/pizero_gpslogger_1.jpg)

The solution I came up with uses the very stable and mature [gpsd daemon](http://www.catb.org/gpsd/) to handle communication with the GPS and caching the last position information, and a small Python daemon to read from ``gpsd`` and log to the RaspberryPi's SD card using gpsd's full JSON data format. The Pi itself is running the [Raspbian](https://www.raspbian.org/) Linux distribution with virtually no customization, and all of the default services (plus SSH) running out of laziness. I also added two status LEDs driven by the board's GPIO, to give visual indication of the position fix state and SD card writes. Unlike many of the commercial GPS loggers available which log data every 60 seconds, my code defaults to 5-second intervals (that, along with most other parameters, are configurable via environment variables). My code (along with detailed instructions, an installation script, and a script to convert from gpsd JSON format to standard [GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format)) is available at [https://github.com/jantman/pizero-gpslog](https://github.com/jantman/pizero-gpslog).

## Hardware

[![Photograph of finished hardware inside backpack](/GFX/pizero_gpslogger_2_sm.jpg)](/GFX/pizero_gpslogger_2.jpg)

This all fits conveniently in my hiking pack inside the mesh bag that the battery pack came in. I plan on putting the Pi and battery safely inside the main compartment (I can unzip it periodically to check that the GPS has a fix and is logging) and dangling the GPS receiver out the zipper, affixed between the zipper pulls of the smaller compartment (with a hair elastic...). This seems to be relatively horizontal, but I may also experiment with taping the GPS to the carry handle on top of the pack, or packing all of it into the top outside pocket.

[![Front angle pohotograph of GPS affixed to outside of pack](/GFX/pizero_gpslogger_3_sm.jpg)](/GFX/pizero_gpslogger_3.jpg)

[![Side angle photograph of GPS affixed to outside of pack](/GFX/pizero_gpslogger_4_sm.jpg)](/GFX/pizero_gpslogger_4.jpg)

It's worth mention that my hardware choice was largely dependent on what I already had or what I thought I could reuse for other projects. While the GPS receiver is small and lightweight - about 2" (5cm) around and about 2 ounces (57g) - I could have saved a fair amount of space and some weight by purchasing a component GPS to connect to the Pi via GPIO and mount directly to the Pi itself. I decided to get a USB model as it will be more useful to me for other projects as well. Some space and weight could also be saved by using a simpler microcontroller than the Pi Zero (this application certainly doesn't need the power of a Pi, or a full Linux system) but I used what I had handy.

The full system as I have it set up weighs 11.5 ounces (326g) which is quite heavy by the standards of serious hikers. However, 7 ounces (203g) of that is the 10,000mAh external battery pack which I already had for my cell phone. This battery can run the logger for >>>>TODO<<<<< continuously, which is definitely overkill for my purposes. I could likely cut the weight in half if I used a more appropriately-sized battery; Anker, a company whose products I really like, makes a $15 [3350mAh USB battery pack](https://www.amazon.com/dp/B005X1Y7I2) that weighs in at just 3oz (85g), to say nothing of the lighter Pi-specific options available.

As-is, this hardware allows me to continuously log GPS fixes every 5 seconds for >>>>TODO<<<<<. Each data point is approximately 1400 bytes, and the 8GB microSD card I use (5.6G free after OS and software) has space to log about __240 days__ of data at this interval.

## Initial Tests

My first test, as described above, was just a test of the "cold fix" speed for the BU-353-S4 GPS after unboxing. Sitting on the sill inside a residential window with a view of half the sky at best, I got a fix accurate to 3-4 meters within about a minute.

My next test was placing the GPS on the dash of my car during a quick five-mile trip to the grocery store and gas station. The results were shockingly accurate: not only did the unit perform perfectly as intended, but when I converted the logs to GPX format and used [gpsvisualizer.com](http://www.gpsvisualizer.com/) to overlay them on Google Maps, I could clearly see my route down to which side of the road I was driving on, the exact space I parked in, and which gas pump I used.

I also did a test of the total time that I can capture data using the 10Ah battery pack and 8GB SD card. This might be a very slight amount unrealistic, since the GPS was stationary most of the time. After doing the above driving test I set the GPS up on the inside sill of my bedroom window and let it run. And run. And drove to work the next day with it on the dashboard of my car, left it in the car during my work day (on the bottom floor of a 4-story parking deck, where a GPS fix is impossible to get) and... >>>>TODO<<<<

## Source Code

For code, detailed hardware information, and instructions see: [https://github.com/jantman/pizero-gpslog](https://github.com/jantman/pizero-gpslog).
