Title: Galaxy S10 / Android 9 alarm app broken by battery optimization
Date: 2019-04-02 07:46
Modified: 2019-04-02 07:46
Author: Jason Antman
Category: Software
Tags: android, samsung, s10, galaxy s10, android 9, pie, battery optimization, app
Slug: galaxy-s10--android-9-alarm-app-broken-by-battery-optimization
Summary: How to fix the Galaxy S10 / Android 9 "Pie" phones from putting alarm apps to sleep.

A few weeks ago I finally replaced my four-year-old Samsung Galaxy S6 with a brand new Galaxy S10. All in all I've been liking it aside from a few differences in the last four years of Android development that annoy me. By far the biggest issue I've had was my alarm clock not going off two morings, and going off seventeen minutes late another morning. At first I thought maybe I was shutting my alarm off, but that doesn't seem likely... I use [Alarm Clock Plus](https://play.google.com/store/apps/details?id=com.vp.alarmClockPlusDock), and have been using it for almost ten years, because it allows me to set an alarm that requires correctly solving some algebra to snooze or dismiss it. I tend to be a very heavy sleeper, and the "math to snooze" / "math to dismiss" requirement ensures that I actually wake up, yet eliminates the harsh "alarm clock on the other side of the room" solution.

So I was right, I didn't suddenly start sleeping so deeply that I could do the algebra and disable my alarm without even remembering it. On the third day of no alarm, I saw the pattern: if I had my phone on the charger, the alarm went off. If my phone wasn't on the charger overnight - as I'd started doing because I now had a phone that lasted _two_ days on a charge - the alarm wouldn't go off. I figured it had to be something with power management or putting apps to sleep.

Sure enough, this was caused by the new "AI-based" battery optimization, which by default limits background usage - not just data, but processor cycles - of apps that it thinks you don't use often.

To solve this on my Samsung Galaxy S10 running Android 9 / OneUI 1.1:

1. Open the Android Settings app.
2. Scroll to and tap on "Apps".
3. Tap on the app in question (Alarm Clock Plus for me).
4. Tap on "Battery" in the "Usage" menu.
5. Ensure the "Allow background activity" slider is ON.
6. Tap the "Optimize battery usage" button.
7. Near the top left, change the dropdown from "Apps not optimized" to "All".
8. Find the app in question, and tap it to turn the slider OFF.

This should let the app use background resources as it desires, such as ensuring that your alarm goes off when scheduled.

