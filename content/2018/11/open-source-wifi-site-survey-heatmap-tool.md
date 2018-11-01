Title: Open Source WiFi Site Survey Heatmap Tool
Date: 2018-11-01 18:07
Modified: 2018-11-01 18:07
Author: Jason Antman
Category: Projects
Tags: wifi, survey, wireless, heatmap, python
Slug: open-source-wifi-site-survey-tool
Summary: A bit about a Python project I wrote to plot floorplan heatmaps of wireless site surveys.

This week I finally bought myself a new wireless access point (AP) to replace my current ones, a pair of older Ubiquiti models that have been continually in service without issue for [nine years](https://twitter.com/j_antman/status/1029135879695228929) and five years, respectively. I bought another Ubiquiti, of course, but wanted to be a bit more methodical and scientific in figuring out the best placement of it in my house.

Years ago when part of my job was supporting an extremely large wireless network, we used some expensive proprietary Windows software (I'm pretty sure it was [Ekahau Site Survey](https://www.ekahau.com/products/ekahau-site-survey/overview/)) for performing site surveys to
determine AP location. Essentially you temporarily rig up a running AP where you propose locating one, load a floorplan of the building into the site survey software, and then walk around the area tapping on the floorplan at your current location. At each tap, the software performs some measurements through the AP (I don't remember what the specific software we used did, but generally it's some bandwidth measurement like [iperf](https://software.es.net/iperf/)) and ends up plotting a (predictive, interpolated) heatmap of signal strength or data transfer speeds over the floorplan.

I wanted to do something similar for my new AP, but was rather surprised that I couldn't find any existing F/OSS solution; only a handful of proprietary options costing anywhere from "more than I'd pay for a one-time thing" to astronomical prices, and none of them clearly with Linux support. The closest I was able to find - and I'm very thankful that I found it - was a [GitHub repository from Beau Gunderson](https://github.com/beaugunderson/wifi-heatmap) that plots a heatmap superimposed on a floorplan using a CSV file of WiFi signal strength measurements. This was enough to get me started on a similar project to automate the process.
