Title: OctoPrint Power Outage Handling
Date: 2021-03-28 08:44
Modified: 2021-03-28 08:44
Author: Jason Antman
Category: DIY / Home Automation / Security
Tags: printing, 3d printing, octoprint, octopi, diy
Slug: octoprint-power-outage-handling
Summary: My simple method of handling power outages during OctoPrint 3d printing.

One of my recent interests has been 3D printing. A few months ago I obtained a used [Creality CR-10S](https://www.creality.com/goods-detail/cr-10s-3d-printer) 3d printer and started doing some work with it. I even [designed](https://www.thingiverse.com/jantman/designs) and [printed](https://www.thingiverse.com/jantman/makes) some parts for it, and designed my new workbench around it. However, about eighteen hours into a twenty-hour print, my neighborhood suffered a power outage. It only lasted about twenty minutes, but the print was ruined and I had to start over. This was clearly a problem.

I'm using the absolutely wonderful [OctoPrint](https://octoprint.org/) project to drive my printer, running on a RaspberryPi-based [OctoPi](https://github.com/guysoft/OctoPi). I did a bunch of research online, but it turns out that solving the general case of handling power outages is quite difficult, and not likely to be supported any time soon. However, I've been able to come up with a workable solution made up of a few common tools. I thought I'd share it with anyone else it may benefit.

I had an extra UPS lying around - an APC BackUPS 1000 (1000VA) - so that seemed like an ideal solution to the problem. Unfortunately, when a print is in progress, the 1000VA UPS will only power the OctoPi (Raspberry PI 4) and printer for about six minutes. This is mainly because of the immense power needs of the stepper motors and bed and extruder heaters. Luckily, there's a solution.

After spending some time in the OctoPrint documentation and forums, I was able to come up with a pair of GCode scripts that move the hotend off the print and disable the heaters when a print is paused, and then revert those changes when the print is resumed. It's worth noting that this is far from foolproof, as disabling the heaters and moving the head around in the middle of a print can cause all sorts of problems... but it's better than nothing. The following scripts are set in OctoPrint settings on the GCODE scripts tab:

After print job is paused:

```gcode
; from https://docs.octoprint.org/en/master/features/gcode_scripts.html#gcode-scripts
; and https://community.octoprint.org/t/better-pause-function-in-octoprint/5331/4
M117 Print Paused ; comment
{% if pause_position.x is not none %}
M117 Print Paused and pause_position.x is not none ; Comment
G91 ; set XYZ relative  positioning
M83 ; set E relative positioning

G1 Z+15 E-5 F4500 ; retract filament, move Z slightly upwards

M82 ; set E absolute positioning
G90 ; set XYZ absolute positioning

G1 X0 Y0 ; move to a safe rest position

; disable all heaters
{% snippet 'disable_hotends' %}
{% snippet 'disable_bed' %}
; note - I disabled the heaters but not the fan, because I don't know how to restore the fan speed
{% else %}
M117 Print Paused but pause_position.x is none ; Comment
M117 pause_position {{ pause_position }} ; Comment
{% endif %}
```

Before print job is resumed:

```gcode
; from https://docs.octoprint.org/en/master/features/gcode_scripts.html#gcode-scripts
; and https://community.octoprint.org/t/better-pause-function-in-octoprint/5331/4
M117 Print Unpaused ; comment
{% if pause_position.x is not none %}
M117 pause_position.x is not none ; comment
{% for tool in range(printer_profile.extruder.count) %}
    {% if pause_temperature[tool] and pause_temperature[tool]['target'] is not none %}
        {% if tool == 0 and printer_profile.extruder.count == 1 %}
            M109 T{{ tool }} S{{ pause_temperature[tool]['target'] }}
        {% else %}
            M109 S{{ pause_temperature[tool]['target'] }}
        {% endif %}
    {% else %}
        {% if tool == 0 and printer_profile.extruder.count == 1 %}
            M104 T{{ tool }} S0
        {% else %}
            M104 S0
        {% endif %}
    {% endif %}
{% endfor %}

{% if printer_profile.heatedBed %}
    {% if pause_temperature['b'] and pause_temperature['b']['target'] is not none %}
        M190 S{{ pause_temperature['b']['target'] }}
    {% else %}
        M140 S0
    {% endif %}
{% endif %}

M83 ; set E relative positioning

; prime nozzle
G1 E-5 F4500
G1 E5 F4500
G1 E5 F4500

M82 ; set E absolute positioning
G90 ; set XYZ absolute positioning

G92 E{{ pause_position.e }} ; reset E to pre-pause position

G1 X{{ pause_position.x }} Y{{ pause_position.y }} Z{{ pause_position.z }} F4500 ; move back to pause position XYZ

; reset to feed rate before pause if available
{% if pause_position.f is not none %}G1 F{{ pause_position.f }}{% endif %}
{% else %}
M117 pause_position.x is none ; comment
{% endif %}
```

Testing those manually via the "Pause" button, they work for me... at least for relatively short pause durations.

The final piece of the solution is relatively simple: I have a script that runs as a daemon and monitors the UPS status (actually via [Network UPS Tools](https://networkupstools.org/)). If the UPS is on battery and drops to 50% charge or less than 4 minutes remaining, the script calls OctoPrint's ReST API to pause the print and then sends me a notification. If power returns within a reasonable amount of time, I can resume the print and hopefully save it.
