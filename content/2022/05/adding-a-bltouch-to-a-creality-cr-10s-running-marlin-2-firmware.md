Title: Adding a BLTouch to a Creality CR-10S running Marlin 2 Firmware
Date: 2022-05-15 16:54
Modified: 2022-05-15 16:54
Author: Jason Antman
Category: DIY / Home Automation / Security
Tags: printing, 3d printing, octoprint, octopi, diy, creality, cr-10s
Slug: adding-a-bltouch-to-a-creality-cr-10s-running-marlin-2-firmware
Summary: How to add a BLTouch probe to a Creality CR-10S 3d printer running Marlin 2 firmware.
Status: draft

I have a Creality CR-10S 3d printer that I purchased used, with many previous upgrades, in September 2020 (currently about 1.75 years ago). The printer has an original Creality v2.2 board in it. I've been *extremely* happy with it, especially with all of the existing upgrades that I didn't have to deal with. However, the printer did not have a bed leveling sensor and also had third-party (TH3D) Marlin-based firmware installed but no configuration file for that firmware. Recently I started having some printing issues that I believed were related to bed leveling issues (specifically a sagging bed) and I decided to add a [BLTouch](https://www.antclabs.com/bltouch) and see if that helped. So, I ordered an off-brand BLTouch from Amazon, listed as [Creality Upgraded BLTouch V1 Auto Bed Leveling Sensor Kit Accessories for Creality Ender 3/ Ender 3 Pro/Ender 5/CR -10/CR-10S4/S5/CR20/20Pro](https://smile.amazon.com/gp/product/B088KLFPNV/) (**note:** This product has been updated, and is now a BLTouch V2).

The process of both installing the sensor and updating my firmware to work with it were quite a bit more difficult than I'd hoped or thought. The former because the installation instructions for the third-party BLTouch v1 clone were flat-out wrong for my CR-10S with a V2.2 board. The latter because with a printer with third-party firmware but no configuration file, I had to start from scratch determining what configuration options I had to use.

To try to prevent anyone else from going through the same headaches, here is the process that I used.

## Preparation

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

The most difficult part of this process, by far, was configuring my firmware for the BLTouch. I bought my printer second-hand and it came to me with third-party TH3D firmware on it ()
