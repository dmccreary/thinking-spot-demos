---
title: List of STEM Kits
description: A consolidated catalog of physical STEM kits developed across the intelligent-textbook family that could be sold in a bookstore or classroom.
---

# List of STEM Kits

This page consolidates every physical, buildable STEM kit found across the
intelligent-textbook family of repos (`src/kits/` and `docs/kits/` in each
book). It is a sales/inventory-planning reference — a candidate list of kits
that could be packaged and sold, grouped by the book that documents them.

Placeholder pages with no real content, pure comparison/survey pages with no
single buildable kit, and exact duplicates across repos have been left out.

**Total kits: 62**

## Clocks and Watches Kits

### Character LCD Clock

A clock built around a low-cost ($5) 16x2 I2C character LCD (LCD1602) and a
real-time-clock chip that shows the date, time, and temperature.

![Character LCD Clock](img/kits/clock-char-lcd.jpg)

### GC9A01 Round Display Clock

A smartwatch-style analog/digital clock face driven by the GC9A01, a 240x240
round color SPI display chip.

![GC9A01 Round Display Clock](img/kits/clock-gc9a01.png)

### ILI9341 Color TFT Clock

A clock face on a low-cost ($9) 240x320 color TFT display, chosen because the
driver can draw smooth circles for analog clock hands.

![ILI9341 Color TFT Clock](img/kits/clock-ili9341.jpg)

### TM1637 LED Clock Kit

An entry-level clock (under $10 total) built from a 4-digit 7-segment TM1637
LED module wired to a Raspberry Pi Pico over a simple 2-wire interface.

![TM1637 LED Clock Kit](img/kits/clock-tm1637-led.png)

### LILYGO T-Display RP2040 Clock

An all-in-one RP2040 board with a built-in 1.14" color LCD, two buttons, and
custom firmware to make a compact desk clock.

![LILYGO T-Display RP2040 Clock](img/kits/clock-lilygo-tdisplay.jpg)

### MAX7219 LED Clock

A digital clock driven by the low-cost MAX7219 LED driver chip, which runs a
row of seven-segment displays over a single serial interface.

![MAX7219 LED Clock](img/kits/clock-max7219.png)

### Large OLED Clock Kit

A versatile clock combining a 128x64 SSD1306 OLED, a Raspberry Pi Pico W, and
a DS3231 real-time clock (accurate to 2 seconds/month), with three buttons
for manual time and alarm adjustment.

![Large OLED Clock Kit](img/kits/clock-oled-large.png)

### SH1106 OLED Clock

A clock built around the SH1106 monochrome OLED driver over I2C, with custom
segment-mapping logic to render clock digits.

![SH1106 OLED Clock](img/kits/clock-sh1106.jpg)

### SSD1306 I2C OLED Clock

An entry-level clock using a $3-4 small SSD1306 OLED display connected over a
simple 4-wire I2C bus.

![SSD1306 I2C OLED Clock](img/kits/clock-ssd1306.jpg)

### ST7735 Color LCD Clock

A color clock kit using the low-cost (~$3.50) 1.8" ST7735 SPI LCD, covering
RGB565 color and screen rotation.

![ST7735 Color LCD Clock](img/kits/clock-st7735.jpg)

### Stopwatch Kit

A two-button OLED stopwatch (Start/Stop and Reset) built on a Raspberry Pi
Pico, with an interactive on-screen simulation of the display.

![Stopwatch Kit](img/kits/clock-stopwatch.png)

### Waveshare RP2040 SmartWatch Kit

A ~$18 all-in-one RP2040 development board with a 1.28" round IPS LCD, USB-C,
LiPo connector, and a built-in accelerometer/gyroscope for smartwatch
programming.

![Waveshare RP2040 SmartWatch Kit](img/kits/clock-waveshare-rp2040.jpg)

## FFT Benchmarking Kits

### FFT Lab Kit

A ~$19/student hardware kit for a 35-lab course on FFT and digital signal
processing, built on a Raspberry Pi Pico 2 (RP2350) with a 2.42" SPI OLED
display, two buttons, and an INMP441 I2S MEMS microphone.

![FFT Lab Kit](img/kits/fft-lab-kit.jpg)

## Learning MicroPython Kits

### Cytron Maker Pi Pico Kit

A $9.99 breakout board for the Raspberry Pi Pico that adds a speaker, stereo
headphone jacks, and an SD card reader.

### Cytron Maker Pi RP2040 Collision Avoidance Robot

A collision-avoidance robot (under $20 in parts) built around the Cytron
Maker Pi RP2040 and a time-of-flight distance sensor.

![Cytron Maker Pi RP2040 Collision Avoidance Robot](img/kits/lmp-maker-pi-rp2040-robot.jpg)

### Maker Pi RP2040 Robotics Kit

The base Cytron Maker Pi RP2040 board ($9.90) mounted on a standard smart-car
chassis, with 13 status LEDs, 2 NeoPixels, a LiPo connector, and buttons.

![Maker Pi RP2040 Robotics Kit](img/kits/lmp-maker-pi-rp2040.jpeg)

### NeoPixel Starter Kit

A low-cost (under $10) starter kit with a Raspberry Pi Pico, a half-size
breadboard, a WS2811B LED strip, two push buttons, and a USB cable.

![NeoPixel Starter Kit](img/kits/lmp-neopixel-kit.jpg)

### RFID Reader Kit

A kit for wiring and using the popular MFRC522 RFID reader module with a
Raspberry Pi Pico over SPI to read RFID cards and tags.

![RFID Reader Kit](img/kits/lmp-rfid-rc522.png)

### Spectrum Analyzer Kit

A kit that displays a live audio frequency spectrum on an OLED, using a
Raspberry Pi Pico, a microphone, and a Cooley-Tukey FFT with Hanning
windowing.

### Larson Scanner Pumpkin Kit

A "Cylon eye" scanning-LED effect built into a craft pumpkin (~$25 total)
using a 144-pixel/meter NeoPixel strip and a Raspberry Pi Pico.

![Larson Scanner Pumpkin Kit](img/kits/lmp-larson-pumpkin.gif)

### Cytron Maker Nano RP2040 Kit

A low-cost ($9) RP2040 board with 14 GPIO blue LEDs, 2 NeoPixel RGB LEDs, a
piezo buzzer, and Grove-compatible ports.

![Cytron Maker Nano RP2040 Kit](img/kits/lmp-maker-nano-rp2040.png)

## Moving Rainbow Kits

### Moving Rainbow Base Kit

The foundational kit for the whole course — a Raspberry Pi Pico, half-size
breadboard, 30-LED WS2812B strip, and two push buttons — typically under
$10/kit in classroom quantities.

### 8x8 NeoPixel Matrix Kit

An 8x8 (64-pixel) NeoPixel matrix panel (~$12) programmable with
MicroPython's built-in NeoPixel library.

![8x8 NeoPixel Matrix Kit](img/kits/mr-8x8-neopixel-matrix.png)

### BookStore Sign Kit

A 134-pixel NeoPixel sign spelling "Bookstore," with switchable display modes
controlled by back-mounted buttons.

![BookStore Sign Kit](img/kits/mr-bookstore-sign.jpg)

### Cylon Pumpkin Kit

A scanning "Cylon eye" LED effect built into a craft foam pumpkin (~$10 plus
LED strip) using a 144-pixel/meter NeoPixel strip and a USB power pack.

![Cylon Pumpkin Kit](img/kits/mr-cylon-pumpkin.gif)

### Digital Nightlight Kit

A Raspberry Pi Pico breadboard nightlight with a button, two potentiometers,
a power switch, and a photoresistor to control pattern, brightness, and
color/speed.

![Digital Nightlight Kit](img/kits/mr-digital-nightlight.png)

### Analog Nightlight Kit

An analog nightlight circuit with sensitivity and brightness controls, built
without a microcontroller.

### Halloween Party NeoPixel Kit

A "power-limited" Halloween-themed NeoPixel pattern kit (orange/purple
effects) that caps lit pixels at one-third of the strip to stay USB-safe.

### Holiday Hats Kit

A foam-core hat fitted with NeoPixel strips, reusable across holidays by
swapping the color pattern; built on the Moving Rainbow base kit.

### Jake's Fire Kit

A small color-changing tabletop "campfire" prop using programmable RGB LEDs,
wooden sticks, and cellophane.

### LED Candle Kit

A $10 kit using a NeoPixel ring, Raspberry Pi Pico, breadboard, and
battery/USB power to simulate a flickering candle.

### LED Dimmer Kit

A basic transistor-based LED dimmer circuit (potentiometer plus a 2N2222
NPN transistor).

![LED Dimmer Kit](img/kits/mr-led-dimmer.png)

### LED Noodle Nightlight Kit

A rope-light ("noodle") nightlight built from a simple LED driver circuit.

![LED Noodle Nightlight Kit](img/kits/mr-led-noodle-nightlight.png)

### Name Sign Night Light Kit

A NeoPixel sign spelling a name, with a photo sensor that triggers a
20-minute fading rainbow nightlight mode when the room lights go out.

![Name Sign Night Light Kit](img/kits/mr-name-sign-nightlight.jpg)

### Nightlight Circuit Kit

A simple LDR-and-transistor nightlight circuit with two potentiometers for
sensitivity and brightness adjustment.

## Robot Faces Kits

### OLED Robot Faces Kit

A lab series teaching MicroPython framebuffer graphics (pixels, lines,
shapes, text) on a 128x64 monochrome OLED, building up to animated robot
faces.

### 1.2" Smartwatch Robot Face Kit

Ports the OLED robot-face kit to a 240x240 round color GC9A01 display, the
same panel used in cheap smartwatches, for under $10 total.

### 2.1" Smartwatch Robot Face Kit (GC9B72)

A larger sibling kit using a 360x360 round color display driven by a
GC9B72 controller; the driver was reverse-engineered since GalaxyCore does
not publish documentation for it. Also sold as the [Thinking Spot Logo Smartwatch Kit](#thinking-spot-logo-smartwatch-kit) with a custom logo face.

![2.1" Smartwatch Robot Face Kit](img/kits/rf-smartwatch-gc9b72.png)

## STEM Robots Kits

### Base STEM Robot

The classic low-cost (~$19) collision-avoidance robot built on the Cytron
Maker Pi RP2040 and a 2WD smart-robot-car chassis; requires no soldering and
is the recommended first robot purchase.

![Base STEM Robot](img/kits/sr-base-bot.jpg)

### Adjustabot

A variant of the Display Bot with three potentiometers added so students can
"program" motor power, distance threshold, and turn time by turning knobs.

### Bump Switch Bot

A robot that uses cheap (under $1) microswitches instead of a distance
sensor for collision detection.

![Bump Switch Bot](img/kits/sr-bump-switch-bot.jpg)

### Display Bot

Adds a 2.42" OLED display to the base robot so status and distance readings
are visible while the robot runs.

![Display Bot](img/kits/sr-display-bot.png)

### 9-DOF IMU Kit

A standalone learning kit that wires a 9-axis motion sensor to a bare
Raspberry Pi Pico and streams live gyroscope/accelerometer/magnetometer data.

### Compass Kit (HMC5883L)

A standalone digital compass built from the HMC5883L magnetometer and a
Raspberry Pi Pico, drawing a live compass heading on an OLED.

### Motion Detection Explorer Kit

A standalone (non-robot) learning bench — Pico, breadboard, MPU6050 IMU
sensor, and OLED display — for teaching how an IMU works.

![Motion Detection Explorer Kit](img/kits/sr-motion-explorer.png)

### Line Follower Bot

A line-following robot variant of the base STEM robot.

### MAX98357A Audio Amplifier Kit

Adds a MAX98357A Class-D I2S audio amplifier (~$10) to a robot so it can play
recorded sounds and speech instead of simple piezo beeps.

### Rainbow Bot

Adds a colorful 8x8 NeoPixel matrix to the top of the base robot, changing
colors and patterns as the robot moves.

### Smartwatch Compass Kit

Combines an HMC5883L digital compass sensor with a round GC9A01 color screen
and a Raspberry Pi Pico to build a compass with a live needle display.

### Robot Sound Synthesizer Kit

Generates R2-D2-style expressive robot sounds using a single GPIO pin
(PWM pitch-shifting), with no audio chip or recorded sound files needed.

### Ultrasonic Bot

A collision-avoidance robot variant using an ultrasonic (ping) distance
sensor.

### WiFi Bot

Uses the Cytron Robo Pico board (a Raspberry Pi Pico W) for built-in
WiFi/Bluetooth, enabling wireless robot control.

![WiFi Bot](img/kits/sr-wifi-bot.jpg)

### WiFi Display Bot

Extends the WiFi Bot with an OLED display showing startup status, WiFi
connection state, and a driver web-server form.

![WiFi Display Bot](img/kits/sr-wifi-display-bot.jpg)

### Swarm Robot Kit

A heading-follower swarm robot using a 9-DOF IMU module ($5.96) on the
Cytron ROBO-PICO board. Still in the planning stage.

![Swarm Robot Kit](img/kits/sr-swarm-bot.png)

## Thinking Spot Demos Kits

### Thinking Spot Logo Smartwatch Kit

Reuses the 2.1" GC9B72 smartwatch kit's wiring, driver, and configuration to
display the Thinking Spot bookstore logo instead of a robot face; available
in a white-background and a black-background/white-lettering variant.

![Thinking Spot Logo Smartwatch Kit](img/kits/tsd-logo-smartwatch.jpg)

## Beginning Electronics Kits

### 5V Regulator Kit

A 7805 linear voltage regulator circuit with input/output filter capacitors
that produces a constant 5V output from a higher input voltage.

![5V Regulator Kit](img/kits/be-5v-regulator.png)

### Low-Cost Buck Converter Kit

A DIY guide and parts kit for building a basic buck (step-down) converter
using an inductor, MOSFET switch, Schottky diode, and smoothing capacitor.

![Low-Cost Buck Converter Kit](img/kits/be-buck-converter.png)

### Interactive Electronic Busy Board

A hands-on busy board for young children combining buttons, switches, knobs,
LEDs, and buzzers to teach cause-and-effect and basic circuit concepts.

![Interactive Electronic Busy Board](img/kits/be-busy-board.jpg)

### LED Dimmer Project Kit

A high-school-level dimmer circuit for one or more LEDs using a 5V supply, a
potentiometer, a 2N2222 NPN transistor, and current-limiting resistors.

### RGB LED Kit

A simple RGB LED circuit powered by 2 AA batteries with 3 current-limiting
resistors on a breadboard.

![RGB LED Kit](img/kits/be-rgb-led.png)

### Signal Generator Kit

An XR2206-based DIY function-generator kit producing sine, square, and
triangle waveforms from 1Hz to 1MHz; requires soldering to assemble.

### Variable Power Supply Kit

A DIY variable DC power supply (under $10) built from an LM317 adjustable
regulator kit, usable with any spare AC/DC transformer.

![Variable Power Supply Kit](img/kits/be-variable-power-supply.jpg)
