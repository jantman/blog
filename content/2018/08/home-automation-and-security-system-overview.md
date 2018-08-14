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

## Object Detection

- object detection from images, identification of motion zones, localization of objects to zones; pass off to AppDaemon via event
- yolov3-tiny; comparison and accuracy issues

## Tie-In with Alarm System

- processing of events by AppDaemon
- tie-in with alarm state
- notifications

# Alarm System

- overview

## Overall Functionality

- manual control; proximity
- door sensors

## Zooz Multi-Sensors

- why I got them, price, problems

## Control Panel

- project, hardware, photos, functionality

# Home Automation

- lights based on motion, door sensors and proximity; first morning
