Title: IP Camera, Home Security and Automation Update
Date: 2018-06-27 17:49
Modified: 2018-06-27 17:49
Author: Jason Antman
Category: Projects
Tags: amcrest, camera, security, surveillance, video, linux, IP camera, evaluation, alarm, IR, homeassistant, hass, automation, z-wave
Slug: ip-camera-home-security-and-automation-update
Summary: An update on my IP camera and home security project, now branching out into home automation and machine learning as well.
Status: draft

[TOC]

Last month I posted about my [Linux Surveillance Camera Software Evaluation](/2018/05/linux-surveillance-camera-software-evaluation/) and my plans for turning some Amcrest IP cameras into a home security system. I've made a lot of progress and some big changes since then and decided that I had better post an update before the effort of doing so becomes overwhelming. There are a lot of changes and new information, and some really cool plans for the future (this has become my new obsession, albeit a prohibitively expensive one), so I'll break this up into a number of sections.

## Amcrest Cameras

I'm extremely happy with the two Amcrest cameras I purchased, and am planning to add two more at some point in the near future to cover the rest of the exterior of my house. The one I currently have outside is an Amcrest [IPM-723W](https://amcrest.com/amcrest-1-3mp-bullt-wifi-video-security-ip-camera-pt-ipm-723w.html) WiFi camera with a 1.3MP 1280x960 resolution and a 92º field of view. It's a decent camera and the resolution is perfectly adequate but I wouldn't mind a bit more, and more importantly, both sides of my house would benefit a lot from a winder field of view. I believe I've settled on two Amcrest [IP2M-852W](https://amcrest.com/amcrest-prohd-outdoor-1080p-wifi-wireless-ip-security-bullet-camera-ip67-weatherproof-1080p-1920tvl-ip2m-852w-white.html), which are similar outdoor WiFi cameras but with 1920x1080 resolution and a super-wide 128º field of view.

I received some questions via email after writing this post about the Amcrest cameras with Linux as well as the security of them. I think I'm quite happy with both, but both with some caveats. First of all, regarding security, I'm skeptical of the security of any proprietary software (especially from a small vendor or one not in the software business) and generally expect all IoT devices to have abysmal security. When I originally purchased the devices, I blocked all Internet-bound traffic from them at my router before even plugging them in. For the time being at least, I'm going to assume that to be enough for my needs. I certainly wouldn't expose these directly to the Internet or allow them to access both the Internet and my home network, as is the case for any consumer-oriented devices.

I've also received some questions about the Linux support for Amcrest cameras. My experience so far has been consistent with my [Amcrest IP Camera First Impressions - Jason Antman's Blog](/2018/05/amcrest-ip-camera-first-impressions/). The cameras certainly work fine under Linux in general; they can be fully controlled and configured via any browser and you can view the low-resolution MJPEG stream in any browser. Viewing the full-resolution RTSP stream requires either the Amcrest Web View Chrome app or a viewer that supports RTSP streams (VLC or any common surveillance camera software). Aside from watching the stream in VLC or Amcrest Web View while I was outside aiming the camera, I've been using either the low-res MJPEG stream in a browser or, more recently ZoneMinder and HomeAssistant, to view it. Unless you want a closed-source native desktop app, I can't find any meaningful difference between how the cameras work on Linux vs Mac or presumably Windows.

### IR Illuminator

My first step in attempting to reduce false-positive motion detection caused by flying bugs at night was purchasing an external IR illuminator. I opted for a 12V DC model on amazon that uses the same power supply as the camera (I purchased a splitter for them), the
[Univivi 850nm 12 LED Wide Angle IR Illuminator](https://www.amazon.com/gp/product/B01G6EDOO2/). It's a large-ish unit that looks much like a LED floodlight, except that when on it emits only a barely-visible red glow from the LEDs. This has helped immensely; I have it placed about a foot and a half away from the camera and it has dramatically cut down on (but not eliminated) the number of times that the motion detection is triggered at night by moths and other light-seeking insects. That being said, with some of the advances I've made in other areas (read on) I probably won't be replicating this for my other cameras, at least not initially. I _will_ also remark that the light output from this unit isn't wide enough to cover the camera's whole field of view, and it does suffer from some definite hot spots.

Here's a view of the camera and IR illuminator during the day:

[![camera and IR illuminator as installed, during the day](/GFX/ir_illuminator_day_sm.jpg)](/GFX/ir_illuminator_day.jpg)

And here's a view of it at night. Note that this was taken in almost total darkness and to the human eye the illuminator only emits a barely-visible red glow; unfortunately this photo does more to illustrate how sensitive my phone camera is to IR than what it actually looks like.

[![camera and IR illuminator at night](/GFX/ir_illuminator_night_sm.jpg)](/GFX/ir_illuminator_night.jpg)

## Surveillance Software - ZoneMinder

When I last posted I'd done an [evaluation](/2018/05/linux-surveillance-camera-software-evaluation/) of a number of options for Linux-based video surveillance, discounted ZoneMinder mainly because of its age, resource requirements, and difficulty getting it running in Docker. I ended up settling on the [Motion Project](https://motion-project.github.io/) (``motion``) because of its simplicity and low resource requirements. Unfortunately, that path ended up being a dead end.

I spent quite a bit of time tuning motion and developing a horribly simple proof-of-concept web interface for it (the defunct project lives at [https://github.com/jantman/motion-pipeline](https://github.com/jantman/motion-pipeline) if anyone is interested) and playing with masks and various values to get reliable motion detection at 1920x1080 10fps on a RaspberryPi 3B+. While I eventually got that working including notifications with images, it failed completely when I installed the camera in its final environment - the exterior of my house. No matter how hard I tried, I couldn't get the motion detection to capture legitimate events but ignore the large amounts of shadow motion when wind caught the trees around my house. I hadn't considered this relatively obvious issue when I did my initial tests at my former (and relatively tree-free) apartment complex. It's also worth noting that when running motion detection at 1920x1080 10fps, the RaspberryPi 3B+ was essentially at its limits; if I wanted to add another camera of equal resolution and frame rate I'd need a Pi per camera.

After that non-starter I remembered that the motion detection algorithm in ``motion`` only takes luminance into account (effectively a black-and-white image) but ZoneMinder uses full color in its motion detection. So, I decided to take another look at ZoneMinder. After some initial hiccups I decided to just install the ``zoneminder`` package on the RaspberryPi 3B+ running Debian 9. After a bit of setup, I had it running and processing 1920x1080 10fps on the Pi. This taxed the system quite a bit and the web UI was almost unusably sluggish, but it was enough for me to get ZM up and running and to prove that its motion detection algorithm handles clouds and shadows *much* better than ``motion``.

It was apparent that if I wanted to make use of ZM with multiple cameras and also have it be useful and reliable, I needed significantly better hardware than the RaspberryPi. After some searching on Amazon, I found a [refurbished HP Elite 8200 small-form-factor desktop](https://www.amazon.com/gp/product/B01KWP82CK/) on Amazon for $300. It was quite a bit more money than I'd wanted to put into this system, but with an Intel Core i7-2600 with four cores (plus hyper-threading) at 3.4GHz, 16GB memory and a 2TB spinning disk, I figured it would be more than adequate for four or more cameras (in fact the specs are shockingly close to my desktop computer, which was quite beefy when I built it three or four years ago).

That machine arrived two weeks ago and I installed Debian 9 on it along with the official ZoneMinder package, and it's performing amazingly well. With one camera at 1920x1080 10fps in monitor mode and another at 1280x960 10fps in motion detection (Modect) mode, the system barely breaks a sweat with half of its memory free and half or three-quarters of the CPU cores idle. ZM is performing exceedingly well, with the web UI fast and streaming working very well. I'm still having some false positives from shadows when it gets very windy, but I have a plan for addressing that as well. Overall I'm really glad I switched to ZoneMinder with decent hardware, and plan on further improving and expanding this set-up in the future.

### Notifications

One thing that ZoneMinder completely lacks is the built-in ability to notify immediately on new events/alarms. The closest that it has are "filters", which run at a configurable interval (usually 60 seconds) and can be set to send email or execute an external command for new alarms. Unfortunately there are some issues around how they're configured that result in either notification storms or severe delays when multiple short events happen in rapid succession. After using this method for a few days and researching other possibilities, I found the [zmeventserver](https://github.com/pliablepixels/zmeventserver) project, a daemon written in Perl that polls the ZoneMinder shared memory map for new events at a short interval and pushes them to clients via a websocket server. After some initial experimentation, I unashamedly hacked up the Perl source, ripped out the websocket server, and modified it to execute a shell command with the event ID as an argument (backgrounded with ``&`` so as not to tie up the Perl code).

For my event handler script I wrote something in Python that grabs the details of the event directly from ZoneMinder's database, along with the first and best (most motion) frames, and sends them to me via email and Pushover. I've added a bit more to the script but it's still quite a hack-ish proof-of-concept and too rough to share, but there's really nothing terribly complicated about it: it gets called with ZoneMinder's EventId, looks up that event and a bunch of related stuff in the database, and then generates an email and Pushover notification. I'm not sure if I'm going to keep using this or try to push most of the logic into HomeAssistant (see below); if I do stick with this script, I'll make an effort to clean it up and publish the code.

### Image Processing - IR Switch Detection

Once I got ZoneMinder relatively well tuned for motion detection in my environment and notifications up and running, my first bit of intelligence in the alerting process was disregarding events when the camera switched from visible light to infra-red mode. This IR switch occurs twice a day - visible to IR around dusk and IR to visible around dawn - and was a bit of an annoyance to me. When the switch-over happens, virtually all pixels in the image go white for a frame or two and the image switches between color and black and white. My gut reaction was to ignore events with a massive percentage of changed pixels around dawn or dusk, but that seemed too uncertain. With a bit of thought, I realized that detecting a change from color to black-and-white (or vice-versa) should be rather straightforward.

As the script was already written in Python, I installed [pillow](https://pillow.readthedocs.io/), a modern fork of the Python Imaging Library, and came up with the following snippet to tell whether a specific Frame from ZoneMinder is color or black-and-white (note this is a partial snippet with a lot of unrelated code removed):

```python
from PIL import Image

class Frame(object):

    def __init__(self, **kwargs):
      # lots of internals redacted here...

    @property
    def filename(self):
        return self.event.frame_fmt % self.FrameId

    @property
    def path(self):
        return os.path.join(self.event.path, self.filename)

    @property
    def is_color(self):
        img = self.image
        logger.debug('Finding if image is color or not for %s', self)
        bands = img.split()
        histos = [x.histogram() for x in bands]
        if histos[1:] == histos[:-1]:
            return False
        return True

    @property
    def image(self):
        if self._image is not None:
            return self._image
        logger.debug('Loading image for %s from: %s', self, self.path)
        self._image = Image.open(self.path)
        return self._image
```

This loads the JPEG image (frame) from ZoneMinder as a PIL ``Image``, splits the image
into its color-component bands (red, green, and blue), and then checks if the histograms
of the three color bands are identical. If so, the image is black-and-white.

My notification script simply looks at each event, checks if the first frame is color
and the last is black and white or vice-versa, and if so suppresses the notification
and renames the Event in ZoneMinder for later cleanup.

### Monitoring

At this point I decided that I was sufficiently close to having a minimally-usable system that
I should turn my attention to monitoring it, and making sure I'm alerted if it stops working.
Since I've moved all of my personal services to AWS, I didn't have an existing monitoring
infrastructure for anything running in my home. Not wanting anything too heavy-weight or
complicated, and having an existing Lambda function to handle re-notification of CloudWatch
alarms, I hacked a "monitoring system" together using that Lambda function and API Gateway
in a few hours.

The functionality is relatively simple: every five minutes a Python script runs on my ZoneMinder
system that does a bunch of checks and POSTS them to API Gateway as a JSON array of results. The
POSTed data for each check includes the timestamp, a check name, a boolean ``is_ok`` field, and
an optional string with additional information. API Gateway writes this information to DynamoDB,
and triggers a Lambda function if any of the ``is_ok`` fields changed from true to false. The
Lambda is also run every 30 minutes, and notifies me via email or text message if any of the
check ``is_ok`` fields is False _or_ if any of the timestamp values are more than 10 minutes old.
For now, this should suffice as a really simple monitoring system. I also have a quick and simple
single-page web view of the current Dynamo contents.

The checks that I'm currently running are:

* System load average
* Disk free space as reported by ZoneMinder
* ZoneMinder daemon status as reported by API
* ZoneMinder Run State (one of my custom values, not "stopped")
* ZoneMinder SHM free
* ZoneMinder status as reported by ``zmpkg.pl`` ("running")
* ZoneMinder UI - page loads and has a link to my primary camera
* zmdc process running
* zmwatch process running
* My custom event server process running (based on zmeventnotification.pl; see above)
* For each camera:
  * Direct image check against the Amcrest camera
  * Camera enabled
  * Image check via ZoneMinder
  * zmu frame rate
  * zmu last frame time
  * zmc process running
  * zma process running if Monitor is set to a motion-detecting state

For the "Image check" tests, I do the following:

1. Retrieve the binary image from the camera or ZM
2. Use the python ``imghdr.what()`` function to ensure it's a JPEG image
3. Ensure that the size of the image matches what ZM thinks the monitor size is
4. Use the PIL ``getextrema()`` function to ensure that there's more than one color in the image (i.e. fail if it's an all-blue "signal lost" or an all-black image).
5. Ensure that the histogram of the image has more than 20 distinct buckets / pixel values.

### Neural Network Object Detection

[I wrote an object-detection add-on for ZM - ZoneMinder Forums](https://forums.zoneminder.com/viewtopic.php?f=36&t=26222)

https://www.amazon.com/gp/product/B00BLTE8HK/

https://groups.google.com/forum/#!topic/darknet/tVMLWKDqXNM

## HomeAssistant and Z-Wave

### Door/Window and Motion Sensors

https://www.amazon.com/gp/product/B01MQXXG0I/

https://www.amazon.com/gp/product/B00X0AWA6E/

https://www.amazon.com/gp/product/B01N5HB4U5/

### Thermostat

https://github.com/jantman/RPyMostat

https://github.com/jantman/tuxostat

https://www.amazon.com/gp/product/B0095P7B80/

## What's Next

* GPU and image analysis to reduce false positives
* More cameras
* Door and motion sensors
* Actual alarm alerts and possibly lights/siren
