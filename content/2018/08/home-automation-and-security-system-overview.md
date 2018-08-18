Title: Home Automation and Security System Overview
Date: 2018-08-07 17:17
Modified: 2018-08-07 17:17
Author: Jason Antman
Category: Projects
Tags: amcrest, camera, security, surveillance, video, linux, IP camera, evaluation, alarm, IR, homeassistant, hass, automation, z-wave, darknet, yolo, machine learning, neural network, object detection
Slug: home-automation-and-security-system-overview
Summary: An overview of the current working state of my DIY home automation and security system.
Status: draft

<!--- remove this next line to disable Table of Contents -->
[TOC]

I've done a lot of work on my DIY HomeAssistant-based home automation and security system since my [last post on it](/2018/07/ip-camera-home-security-and-automation-update/) just over a month ago. While it was a lot of work and frustrating at times, I'm happy to say that I think I've finally gotten everything to a usable and working state, and I don't currently have anything left on my to-do list for this project. I have four working security cameras that run both motion detection and object detection and notify me if a person is detected, a functional alarm system for unauthorized entry, and a few home automation conveniences.

Virtually all of the code and configuration backing this is available in my [home-automation-configs GitHub repo](https://github.com/jantman/home-automation-configs) but I want to use this post to go over each of the major components as well as some of the difficulties I encountered.

# Security Cameras

About a month ago I purchased the two more security cameras I'd been thinking about, a pair of WiFi  [Amcrest IP2M-852W](https://amcrest.com/amcrest-prohd-outdoor-1080p-wifi-wireless-ip-security-bullet-camera-ip67-weatherproof-1080p-1920tvl-ip2m-852w-white.html) 1080P with a super-wide 128º field of view. After switching out the IPM-723W (960P / 92º FoV) on my front porch for one of them and mounting the other on the far side of the house, I now have a total of four cameras (three outside, one inside) and coverage of both entrances to my house and all meaningful approaches to the property.

One thing I didn't take into account, unfortunately, was the signal strength from my aged (in-service 24x7 for ) 2.4GHz Ubiquiti Networks access point at the far corners of the house. After a sweaty, hot summer afternoon up on a ladder mounting a camera at the back corner of the house and attempting in vain to aim it using the stream over WiFi, I realized that the construction of my (rental) house causes severe signal shadows at the back corners. I spent a fruitless few hours trying to set up a Netgear WN3000RP "WiFi Range Extender" that I picked up at Best Buy (the setup process was horribly frustrating and error-prone even for someone who worked as a wireless network engineer) only to realize that it was actually a layer 3 router and nothing connected to the extended network could be accessed from my LAN.

After spending another afternoon considering some options - moving my AP or adding another, neither very feasible in a rented house that I don't want to run permanent cabling in - I ended up using existing holes and wiring paths to hook up both cameras with wired Ethernet. In retrospect, I should have done either a proper wireless site survey or at least some spot tests with my phone or laptop beforehand. It would've been much faster if I'd known about the poor signal beforehand, and I also would've purchased PoE cameras instead of using the WiFi models which ended up requiring both Ethernet and power cables. On that note, my one complaint so far about the Amcrest cameras is that they are _either_ wired Ethernet with PoE _or_ WiFi with separate Ethernet and 12V DC power cables. I'm not quite sure why they were designed this way as opposed to all supporting PoE, but I assume there's a manufacturing or cost reason.

One thing that I have noticed in the past month of having both wireless and wired cameras is the difference in frame rate. While my one outdoor camera that's actually using the 2.4GHz WiFi works acceptably well, ZoneMinder is all too happy to show me that it runs at between five and nine FPS, whereas the indoor WiFi and outdoor wired cameras run at the full configured 10FPS rate. If I had to do the camera installation over again, I would've spent much more time assessing the 2.4GHz coverage around my house from my existing AP and likely considered PoE cameras for all of the outdoor locations.

## Neural Network Object Detection

In my last post, I [mentioned](/2018/07/ip-camera-home-security-and-automation-update/#neural-network-object-detection) how I started passing still images from motion events through [Joseph Redmon's Darknet yolo3](https://pjreddie.com/darknet/yolo/) neural network object detection library. With some caveats this has worked out extremely well. While I've decided that my cameras are mainly for remote monitoring and possible evidentiary value, and not really for use as an alarm, I'm still pushing notifications from them to my phone when my alarm is armed; I'm just not relying on them as a primary means of detecting a problem.

One down side to my current setup is the "tiny" version of the yolov3 model that I'm forced to use because of my poor choice of graphics card. I got the feeling that the performance of the tiny model was significantly worse than the full version and, sure enough, comparison tests on the same images proved that. It seems reasonably good at detecting people, but has a relatively high number of false positives. To compensate for this, I've built functionality to ignore certain objects in certain locations in to my image processing scripts; I can now easily log but ignore when yolo detects a stump in my front yard as a cow, or my porch railing as a bench.

My current code for handling ZoneMinder events, available [on github](https://github.com/jantman/home-automation-configs/tree/master/zoneminder) implements what seems to me to be a reasonable workflow for my needs. When events are detected by ZoneMinder a selection of frames - first, last, and a variable number of high-motion (high-score) frames - are passed through yolov3-tiny object detection. Using the tiny model and 1920x1080 frames, this takes about 1/4 second per frame on my GPU. Once a list of detections is obtained (category, confidence level, and bounding boxes for each detected object) it parses the Notes field on the ZoneMinder event to determine what zones motion was detected in, then retrieves the coordinates of each zone on the monitor form ZoneMinder and calculates which zones contain each detected object. All of that information is used to evaluate - via a configuration file - which objects should be ignored. All of this information - the ZoneMinder Event details, object detections and their containing zones, etc. - is passed to HomeAssistant as an event, where it's picked up by an AppDaemon app.

## Tie-In with Alarm System

Once the ZoneMinder events/alarms are sent to HomeAssistant as events they're picked up by an AppDaemon app, [zmevent_alarm_handler.py](https://github.com/jantman/home-automation-configs/blob/master/appdaemon/apps/zmevent_alarm_handler.py). This handles the logic behind whether or not to send me a notification for a given ZoneMinder alarm. The logic I'm currently using is as follows:

1. If my alarm system is disarmed, no notification.
2. If no objects were detected by YOLO3, no notification.
3. If the only motion was in the "Street" zones, no notification. I have distinct zones for the road in front of my property, and record motion there but don't alert on it.
4. Formulate a short string describing the objects detected and what zones they're in, for use in notifications.
5. If an ``input_boolean`` in HomeAssistant called "silence_cameras" is _not_ on, send a Pushover notification to my phone containing the description of the alert and the highest-motion frame containing the detected object(s).
6. Send an email containing all analyzed/detected frames as well as the full details of the event.

So far this is working quite well for me. I get _very_ few false positives with the above logic combined with object detection, only get notified if my alarm system is armed, and as far as I can tell get notified 100% of the time a person is on my property.

# Alarm System

My traditional alarm system hasn't changed much since my last post. I have door/window sensors on both entry doors to the house as well as the gate to my fenced yard and the door on the crawlspace under the house. I've added motion detectors in most rooms, but because of problems with the sensors I chose (more on that below) I only have one in use as a trigger for the alarm, a more reliable model than the other four I purchased. With the addition of a physical control panel near the front door (more on that below as well) it's working quite well for me. I've had zero false positives so far, and a 100% detection rate based on HomeAssistant's logs of the sensors (and my own occasional forgetting to disarm the system before I open a door). There's still something to be desired in terms of reliability of notifications as it relies on my cable Internet connection, but I _do_ get notified within five minutes by offsite monitoring if my Internet connection goes down. If I really wanted more than that, I'd look into some sort of cellular backup connection.

The overall functionality of the system is incredibly basic: when armed (``input_select`` in HomeAssistant) and one of the sensors is tripped, it pushes a loud high-priority notification to my phone via Pushover. I opted not to use HomeAssistant's state machine-based [manual alarm control panel](https://www.home-assistant.io/components/alarm_control_panel.manual/) component and rather implement my own logic in AppDaemon. I have an ``input_select`` with three options: Disarmed, Home and Away. The alarm does nothing in "Disarmed" state. The "Home" state uses only external (door/window) sensors for trigger and the "Away" state also includes interior motion sensors. This trinary state is also used to control whether ZoneMinder events notify me, as described previously. My logic doesn't include any "triggered" state or delay; I get one notification for every sensor trigger. It also doesn't include any arming delay, but since I built and installed a real physical control panel near the door, it includes a configurable delay (currently 10 seconds) to give me time to disarm before triggering the alarm if it's currently in the Away state.

One added bit of fancy-ness that I put into the alarm is integration with ZoneMinder and my cameras. All of the doors (as well as the fence gate) have external coverage by outdoor cameras, and the front and back doors also share internal coverage from a PTZ camera mounted in view of both of them. When the alarm is armed and a door sensor trips, the AppDaemon app that handles the alarm captures images from whatever cameras have a view of the door that opened (including panning the indoor camera if needed). Those images are included in the Pushover notification that I receive, making it much more informative than just knowing that a particular door opened.

## Zooz Multi-Sensors

In my last post I [mentioned](/2018/07/ip-camera-home-security-and-automation-update/#doorwindow-and-motion-sensors) that I'd purchased some Z-Wave security sensors, including a $40 [EcoLink PIRZWAVE2.5-ECO](https://www.amazon.com/gp/product/B01MQXXG0I/) Z-Wave Plus PIR motion sensor "with PET immunity" (I'm pretty sure they mean domestic animals, not Positron Emission Tomography). I originally just set it to lowest sensitivity (via a physical jumper) and balanced it on top of the blinds in my living room to see how it worked. I was pleasantly surprised to find that it seemed to work perfectly - it triggered every time I moved in the room, and never when no person was in the room. After a week or so I decided that it was working well enough to order some more for full coverage of my house. I put the EcoLink PIR sensor in the back room that I use for storage and the cats' food and litter boxes, and in the month-plus since then it's had a 100% accuracy rate.

When I began shopping for four more sensors, though, I was tempted to see if I could find something a bit less expensive. As I'd just gotten my Z-Wave thermostat working, I was really intrigued by the $36 [ZOOZ ZSE40 4-in-1 sensor, version 2.0](https://www.amazon.com/gp/product/B01AKSO80O/) which combines a PIR motion sensor with sensors for light, temperature, and humidity. I figured these would let me save a tiny bit of money while also getting the bonus of temperature sensors in every room, and the PIR motion sensors have seven levels of sensitivity - settable over Z-Wave - which I figured would be more than enough to get them to ignore my cats.

The Zooz sensors only had a 3.5 star rating on Amazon and lots of negative reviews, but it seemed that most of the reviews were for the older (non-2.0) version. Unfortunately I didn't heed my concerns and bought four of them, and I've regretted that ever since. 

## Control Panel

- project, hardware, photos, functionality

Here are a few photos of the finished unit currently hanging out on top of the entertainment center in my living room, just a few feet inside the front door:

[![photo of finished touchscreen control panel in place](/GFX/doorpanel_installed1_480x320.jpg)](/GFX/doorpanel_installed1_1920x1080.jpg)

[![photo of finished touchscreen control panel in place](/GFX/doorpanel_installed2_480x320.jpg)](/GFX/doorpanel_installed2_1920x1080.jpg)

[![photo of finished touchscreen control panel in place](/GFX/doorpanel_installed3_480x320.jpg)](/GFX/doorpanel_installed3_1920x1080.jpg)

[![photo of finished touchscreen control panel in place](/GFX/doorpanel_installed4_480x320.jpg)](/GFX/doorpanel_installed4_1920x1080.jpg)

And some screenshots of the 480x320 touchscreen display:

Disarmed:

![screenshot of touchscreen in disarmed mode](/GFX/doorpanel_disarmed_480x320.png)

Arming Away (exit delay):

![screenshot of touchscreen in arming away mode](/GFX/doorpanel_arming-away_480x320.png)

Armed Away:

![screenshot of touchscreen in armed away mode](/GFX/doorpanel_armed-away_480x320.png)

Armed home:

![screenshot of touchscreen in armed home mode](/GFX/doorpanel_armed-home_480x320.png)

# Home Automation

- lights based on motion, door sensors and proximity; first morning
