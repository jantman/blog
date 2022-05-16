Title: Adding a BLTouch to a Creality CR-10S running Marlin 2 Firmware
Date: 2022-05-15 16:54
Modified: 2022-05-15 16:54
Author: Jason Antman
Category: DIY / Home Automation / Security
Tags: printing, 3d printing, octoprint, octopi, diy, creality, cr-10s
Slug: adding-a-bltouch-to-a-creality-cr-10s-running-marlin-2-firmware
Summary: How to add a BLTouch probe to a Creality CR-10S 3d printer running Marlin 2 firmware.

I have a Creality CR-10S 3d printer that I purchased used, with many previous upgrades, in September 2020 (currently about 1.75 years ago). The printer has an original Creality v2.2 board in it. I've been *extremely* happy with it, especially with all of the existing upgrades that I didn't have to deal with. However, the printer did not have a bed leveling sensor and also had third-party (TH3D U1.R2.B5) Marlin-based firmware installed but no configuration file for that firmware. Recently I started having some printing issues that I believed were related to bed leveling issues (specifically a sagging bed) and I decided to add a [BLTouch](https://www.antclabs.com/bltouch) and see if that helped. So, I ordered an off-brand BLTouch from Amazon, listed as [Creality Upgraded BLTouch V1 Auto Bed Leveling Sensor Kit Accessories for Creality Ender 3/ Ender 3 Pro/Ender 5/CR -10/CR-10S4/S5/CR20/20Pro](https://smile.amazon.com/gp/product/B088KLFPNV/) (**note:** This product has been updated, and is now a BLTouch V2).

The process of both installing the sensor and updating my firmware to work with it were quite a bit more difficult than I'd hoped or thought. The former because the installation instructions for the third-party BLTouch v1 clone were flat-out wrong for my CR-10S with a V2.2 board. The latter because with a printer with third-party firmware but no configuration file, I had to start from scratch determining what configuration options I had to use.

To try to prevent anyone else from going through the same headaches, here is the process that I used.

## Sensor Preparation

The sensor that I purchased was a BLTouch v1 clone. It came with a cable that had a small 5-pin JST connector on the probe end and two separate connectors on the board end, a 3-pin DuPont-style connector and a 2-pin JST connector. The first thing to do is disconnect your control box from your printer and confirm the correct wiring and connectors for your printer (see next section). Then if you (like me) have cable management on your extruder, you'll want to order or make extension cables for the BLTouch; the cables that come with it are far too short to use with any cable management.

## Hardware Installation

Attach the probe to its bracket and the bracket to your extruder carriage. The bracket that came with mine works fine with a Micro-Swiss direct-drive extruder.

Then route the cables to your main board and attach them. This was a big point of confusion to me, as my CR-10S has a Creality original V2.2 main board. The process for connecting the BLTouch v1 to this board is as follows:

1. Throw out the instructions that came with the probe.
2. Throw out the auxiliary adapter board that came with the probe.
3. Disconnect the Z-axis limit switch (2-pin JST connector) from the main board (this is `Z-Min` on the board) and connect the 2-pin JST connector from the probe in place of it.
4. Find the `D11` 3-pin header on the board; this is in a block of four 3-pin headers just inboard of the `EXP2` ribbon going to the LCD display. Connect the 3-pin DuPont plug from the probe to `D11`. The wires on this shoild be Red, Blue, Yellow; Red goes towards the outboard side of the main board, closest to `EXP2`.

That's it. No adapter boards or anything else crazy needed. Once you know that the instructions that came with the probe are **not** for the V2 board, and find the correct instructions, it's easy. My process here is based on instructions that I found at [iFixIt](https://www.ifixit.com/Guide/CR-10S+BL+Touch+Install/128525).

## Firmware

The most difficult part of this process, by far, was configuring my firmware for the BLTouch. I bought my printer second-hand and it came to me with third-party TH3D firmware on it (U1.R2.B5) but no configuration file for the firmware. After a bunch of research and trying to find the exact firmware that my printer had running, I decided that the best option would be to re-flash with [Marlin 2 firmware](https://marlinfw.org/), most especially so that I could take advantage of the new [Unified Bed Leveling (UBL)](https://marlinfw.org/docs/features/unified_bed_leveling.html) system. I've never flashed firmware on a 3D printer before, or even worked with AVR microcontrollers. It took quite a bunch of research, but here's what I came up with.

### Preparation

Just in case, I wanted to be able to revert back to what I currently had running. Note that I'm running OctoPrint on an [OctoPi](https://github.com/guysoft/OctoPi), and that already includes [avrdude](https://www.nongnu.org/avrdude/) for working with the firmware on AVR microcontrollers.

1. In OctoPrint's terminal, run [M115](https://marlinfw.org/docs/gcode/M115.html) to show information about the current firmware and capabilities; save this output somewhere.
2. In OctoPrint's terminal, run [M503](https://marlinfw.org/docs/gcode/M503.html) to report the current settings; save this output somewhere.
3. On your OctoPrint machine, perform a backup of the current firmware/flash with ``avrdude -p m2560 -c wiring -P /dev/ttyUSB0 -b 115200 -v -U flash:r:printerbackup.hex:i`` and a backup of the EEPROM using ``avrdude -p m2560 -c wiring -P /dev/ttyUSB0 -b 115200 -v -U eeprom:r:printereeprom.hex:i``.

### Compiling and Flashing

Note that the Creality V2.2 board doesn't need any adapter to flash; it can be flashed directly over USB.

1. Follow [Installing Marlin (Arduino)](https://marlinfw.org/docs/basics/install_arduino.html) to set up the Arduino IDE; also install your distro's `arduino-cli` package. Launch the IDE and install the `U8glib-HAL` library.
2. Clone the [Marlin GitHub repo](https://github.com/MarlinFirmware/Marlin) and check out the `2.0.9.3` tag (the latest release at this time).
3. Set up a configuration file for your printer. I started with the [Marlin CR-10S example configuration for 2.0.9.3](https://github.com/MarlinFirmware/Configurations/tree/2.0.9.3/config/examples/Creality/CR-10S/CrealityV1) and then made a few rounds of changes based on trial and error. You can see my current configurations [here](https://github.com/jantman/3d-printed-things/tree/master/my-cr10s/marlin-configs) and the changes that I made from the examples [here](https://github.com/jantman/3d-printed-things/compare/f546693de8de80a013b9e9aaaf2cbdb52dbe1175..bea951bc1a23f3d135ab831b52a8c6f2d92a2efa).
4. Copy all of those configuration files to the Marlin source repo clone.
5. Build the firmware with `arduino-cli compile --fqbn arduino:avr:mega --export-binaries --verbose --clean Marlin.ino`; this should generate `build/arduino.avr.mega/Marlin.ino.hex`
6. Copy that file to your OctoPrint machine.
7. In OctoPrint, disconnect from the printer if connected.
8. Flash that to the printer with: `avrdude -p m2560 -c wiring -P /dev/ttyUSB0 -b 115200 -v -U flash:w:Marlin.ino.mega.hex:i`
9. When the printer reboots, connect OctoPrint.
10. In OctoPrint terminal, reset the EEPROM to factory defaults with [M502](https://marlinfw.org/docs/gcode/M502.html) and then write that to EEPROM with [M500](https://marlinfw.org/docs/gcode/M500.html).

From there, we can go on to configure automatic bed leveling (see next section).

Note that I had some issues because I accidentally swapped the X and Y endstop (limit switch) connectors during all of this. To troubleshoot that, [M119](https://marlinfw.org/docs/gcode/M119.html) will log the current state of all endstop sensors to the terminal.

### Leveling and Finishing Touches

The rest of the bed leveling configuration was done according to the Marlin [Automatic Bed Leveling](https://marlinfw.org/docs/features/auto_bed_leveling.html) documentation. In short:

1. Send [M420](https://marlinfw.org/docs/gcode/M420.html) to turn off bed leveling.
2. Send [M111 247](https://marlinfw.org/docs/gcode/M111.html) to turn on debug logging via the terminal.
3. Send [G28](https://marlinfw.org/docs/gcode/G028.html) to auto-home.
4. Send [G29](https://marlinfw.org/docs/gcode/G029.html) to begin bed leveling.
5. Send [G29 P0](https://marlinfw.org/docs/gcode/G029.html) to zero the mesh data and then [G29 P1](https://marlinfw.org/docs/gcode/G029.html) to start Phase 1 bed leveling; this may take a while, as it probes up to 100 points.
6. Send [G29 P3](https://marlinfw.org/docs/gcode/G029.html) to interpolate the rest of the points. Repeat as needed until the mesh is complete.
7. Set the Z Offset using the Probe Offset Wizard in Marlin:
    1. Heat build plate to 55 and nozzle to 210 (about average temperatures for me).
    2. Use the Probe Offset Wizard on the LCD:
        1. Go to Configuration – Advanced Settings – Probe Offsets – Z Prob Wizard
        2. Select Move 0.1mm
        3. Lower the z-axis by 0.1mm until you get to paper height from the build plate
        4. Closeout of that Move 0.1mm window
        5. Select Done
    3. That gets me to a probe offset of -3.72. Running `M503` confirms that: `Recv: echo:  M851 X-44.00 Y-9.00 Z-3.72 ; (mm)`
    4. Ok, let's save those settings: [M500](https://marlinfw.org/docs/gcode/M500.html)
8. Home the machine ([G28](https://marlinfw.org/docs/gcode/G028.html)), set it back to relative positioning ([G91](https://marlinfw.org/docs/gcode/G091.html)), and try a test print. Maybe the best print to do is the Marlin built-in Mesh Validation pattern, which can be printed with [G26](https://marlinfw.org/docs/gcode/G026.html).
9. Update OctoPrint and Cura scripts (see below). Install the [Bed Visualizer](https://plugins.octoprint.org/plugins/bedlevelvisualizer/) plugin in OctoPrint, update its GCode as shown below, and run it to see what your bed mesh looks like.

Note that I experienced an issue where after homing, the print would start with the middle of the build plate as the origin. I fixed this in my slicer (Cura) as shown below.

### Cura Updates

My printer profile in Cura had the following near the middle of its Start G-Code:

```gcode
G28 ;Home

G92 E0 ;Reset Extruder
```

This just needs to be changed to enable Automatic Bed Leveling after homing:

```gcode
G28 ;Home
G29 A ; enable UBL
G92 E0 ;Reset Extruder
```

### OctoPrint Updates

In OctoPrint Settings -> Printer -> GCODE Scripts set the "Before print job starts" script to load the mesh from slot 0 and enable automatic leveling:

```gcode
G29 L0 ; load UBL mesh from slot 0
```

In the Bed Visualizer plugin, we want it to just show the existing mesh, not re-calculate anything. Set its GCode to:

```gcode
M155 S30  ; reduce temperature reporting rate to reduce output pollution
@BEDLEVELVISUALIZER    ; tell the plugin to watch for reported mesh
G29 T           ; View the Z compensation values.
M155 S3   ; reset temperature reporting
```

### Re-Calculating the Mesh

You'll want to re-calculate the bed mesh from time to time to make sure it's accurate. To do this, use the following GCode:

```gcode
G28       ; home all axes
M420 S0   ; Turning off bed leveling while probing, if firmware is set to restore after G28
M190 S55  ; (optional) wait for the bed to get up to temperature
G29 P1    ; automatically populate mesh with all reachable points
G29 P3 T   ; infer the rest of the mesh values
G29 P3 T  ; infer the rest of the mesh values again, keep running until mesh complete

G29 S0 ; enabled leveling and report the new mesh, saving it to slot 0
G29 F 10.0 ; Set Fade Height for correction at 10.0 mm.
G29 A     ; Activate the UBL System.
M420 S1 ; enable bed leveling
M500      ; save the current setup to EEPROM
M140 S0   ; cooling down the bed
```
