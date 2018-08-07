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

Virtually all of the code and configuration backing this is available in my [home-automation-configs GitHub repo](https://github.com/jantman/home-automation-configs). Below, I'll go over each of the major components as well as some of the difficulties I encountered.
