# Demo: Thinking Spot Showcase
# Button A moves forward through the mode list, button B moves back --
# same pattern as sw-gc9b72's 18-modes.py. Rename this file to main.py
# (plus config.py, lib/, and the two *.rgb565 logo assets) to have it run
# automatically a few seconds after power-on.
#
# Modes:
#   0  Logo, dark background   (streamed from logo-dark.rgb565)
#   1  Logo, white background  (streamed from logo.rgb565)
#   2  Rainbow title card
#   3  Color wheel
#   4  Colorful gauge
#   5  Analog watch face (mockup)
#   6  Digital watch face (mockup)
#   7  5-day weather forecast (mockup)

import config
import shapes
from array import array
from math import sin, cos, atan2, pi, sqrt
from utime import sleep

display = config.init_display()
button_a, button_b = config.init_buttons()

WHITE = config.WHITE
BLACK = config.BLACK
FILL = config.FILL
NO_FILL = config.NO_FILL
SMALL_FONT = config.SMALL_FONT
BIG_FONT = config.BIG_FONT

CX = config.CENTER_X
CY = config.CENTER_Y

RED = config.RED
GREEN = config.GREEN
BLUE = config.BLUE
YELLOW = config.YELLOW
CYAN = config.CYAN
MAGENTA = config.MAGENTA
ORANGE = config.color565(255, 140, 0)

DEG_TO_RAD = pi / 180.0


def centered_text(font, text, y, color, background=BLACK):
    x = CX - (len(text) * font.WIDTH) // 2
    display.text(font, text, x, y, color, background)


# ---------------------------------------------------------------------
# Mode 0 / 1: the logo, streamed a few rows at a time so the whole image
# never has to fit in RAM at once (see 01-logo.py / 02-logo-dark.py).

ROWS_PER_CHUNK = 20
ROW_BYTES = config.WIDTH * 2


def stream_logo(filename, background):
    display.fill(background)
    with open(filename, "rb") as logo:
        y = 0
        while y < config.HEIGHT:
            rows = min(ROWS_PER_CHUNK, config.HEIGHT - y)
            chunk = logo.read(ROW_BYTES * rows)
            display.blit_buffer(chunk, 0, y, config.WIDTH, rows)
            y += rows


def draw_logo_dark():
    stream_logo("logo-dark.rgb565", BLACK)


def draw_logo_white():
    stream_logo("logo.rgb565", WHITE)


# ---------------------------------------------------------------------
# Mode 2: title card, one rainbow color per letter in the big line.

RAINBOW = (RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, MAGENTA)


def draw_rainbow_title():
    centered_text(SMALL_FONT, "Awesome STEM Kits at", 130, WHITE)

    text = "The Thinking Spot"
    x = CX - (len(text) * BIG_FONT.WIDTH) // 2
    y = 170
    for i, letter in enumerate(text):
        color = RAINBOW[i % len(RAINBOW)]
        display.text(BIG_FONT, letter, x, y, color, BLACK)
        x += BIG_FONT.WIDTH


# ---------------------------------------------------------------------
# Mode 3: color wheel. A cut-down, "fast" version of sw-gc9b72's
# 33-color-wheel.py: hue is the angle, saturation is the distance from
# the center, brightness is fixed at full. Colors are sampled once per
# BLOCK x BLOCK square, not once per pixel, to keep this readable on a
# chip with no floating-point unit.

INNER_R = 55
OUTER_R = 165
BLOCK = 3


def draw_color_wheel():
    _sqrt = sqrt
    _int = int
    _blit = display.blit_buffer

    for dy in range(-OUTER_R, OUTER_R + 1, BLOCK):
        last = dy + BLOCK - 1
        near = dy if abs(dy) < abs(last) else last
        near2 = near * near
        if near2 > OUTER_R * OUTER_R:
            continue

        outer_span = _int(_sqrt(OUTER_R * OUTER_R - near2))
        if near2 < INNER_R * INNER_R:
            inner_span = _int(_sqrt(INNER_R * INNER_R - near2))
            spans = ((-outer_span, -inner_span), (inner_span, outer_span))
        else:
            spans = ((-outer_span, outer_span),)

        for start_dx, end_dx in spans:
            width = end_dx - start_dx + 1
            if width <= 0:
                continue

            line = bytearray(width * 2)
            offset = 0
            dx = start_dx
            color = 0
            countdown = 0

            while dx <= end_dx:
                if countdown == 0:
                    countdown = BLOCK
                    radius = _sqrt(dx * dx + near2)
                    hue = _atan2_deg(near, dx)

                    sat = (radius - INNER_R) / float(OUTER_R - INNER_R)
                    if sat < 0.0:
                        sat = 0.0
                    elif sat > 1.0:
                        sat = 1.0

                    r, g, b = _hsv_to_255(hue, sat)
                    color = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

                line[offset] = color >> 8
                line[offset + 1] = color & 0xFF
                offset += 2
                dx += 1
                countdown -= 1

            height = BLOCK
            if CY + dy + height > config.HEIGHT:
                height = config.HEIGHT - (CY + dy)
            for strip_row in range(height):
                _blit(line, CX + start_dx, CY + dy + strip_row, width, 1)

    centered_text(SMALL_FONT, "Color", CY - 8, WHITE)
    centered_text(SMALL_FONT, "Wheel", CY + 8, WHITE)


def _atan2_deg(y, x):
    hue = atan2(y, x) * (180.0 / pi)
    if hue < 0:
        hue += 360.0
    return hue


def _hsv_to_255(hue, sat, val=1.0):
    sector = int(hue / 60.0) % 6
    ramp = (hue / 60.0) - int(hue / 60.0)

    low = val * (1.0 - sat)
    falling = val * (1.0 - ramp * sat)
    rising = val * (1.0 - (1.0 - ramp) * sat)

    if sector == 0:
        r, g, b = val, rising, low
    elif sector == 1:
        r, g, b = falling, val, low
    elif sector == 2:
        r, g, b = low, val, rising
    elif sector == 3:
        r, g, b = low, falling, val
    elif sector == 4:
        r, g, b = rising, low, val
    else:
        r, g, b = val, low, falling

    return int(r * 255), int(g * 255), int(b * 255)


# ---------------------------------------------------------------------
# Mode 4: a speedometer-style gauge. Angle 180 degrees points left,
# 270 up, 360 (=0) right, so sweeping 180 -> 360 draws a semicircle over
# the top with the opening at the bottom -- the classic gauge shape.

GAUGE_CX = CX
GAUGE_CY = 210
GAUGE_OUTER = 150
GAUGE_INNER = 120
GAUGE_VALUE = 0.68     # demo needle position, 0.0 - 1.0


def _point(radius, angle_deg, cx, cy):
    rad = angle_deg * DEG_TO_RAD
    return cx + int(radius * cos(rad)), cy + int(radius * sin(rad))


def draw_gauge():
    for angle in range(180, 361, 2):
        fraction = (angle - 180) / 180.0
        if fraction < 0.4:
            color = GREEN
        elif fraction < 0.75:
            color = YELLOW
        else:
            color = RED
        x0, y0 = _point(GAUGE_INNER, angle, GAUGE_CX, GAUGE_CY)
        x1, y1 = _point(GAUGE_OUTER, angle, GAUGE_CX, GAUGE_CY)
        display.line(x0, y0, x1, y1, color)

    needle_angle = 180 + GAUGE_VALUE * 180
    x1, y1 = _point(GAUGE_OUTER - 15, needle_angle, GAUGE_CX, GAUGE_CY)
    display.line(GAUGE_CX, GAUGE_CY, x1, y1, WHITE)
    shapes.circle(display, GAUGE_CX, GAUGE_CY, 8, WHITE, FILL)

    centered_text(BIG_FONT, str(int(GAUGE_VALUE * 100)), GAUGE_CY + 40, WHITE)
    centered_text(SMALL_FONT, "SPEED", GAUGE_CY + 80, WHITE)


# ---------------------------------------------------------------------
# Mode 5: analog watch face mockup. A fixed demo time (10:09:34) --
# a real clock would need a battery-backed RTC this kit does not have.

WATCH_R = 150
DEMO_HOUR = 10
DEMO_MINUTE = 9
DEMO_SECOND = 34


def draw_analog_watch():
    shapes.ring(display, CX, CY, WATCH_R, WHITE, 3)

    for hour in range(12):
        angle = hour * 30 - 90     # 0 -> straight up, then clockwise
        length = 18 if hour % 3 == 0 else 10
        x0, y0 = _point(WATCH_R - length, angle, CX, CY)
        x1, y1 = _point(WATCH_R - 4, angle, CX, CY)
        display.line(x0, y0, x1, y1, WHITE)

    hour_angle = (DEMO_HOUR % 12) * 30 + DEMO_MINUTE * 0.5 - 90
    minute_angle = DEMO_MINUTE * 6 - 90
    second_angle = DEMO_SECOND * 6 - 90

    hx, hy = _point(70, hour_angle, CX, CY)
    display.line(CX, CY, hx, hy, WHITE)
    mx, my = _point(105, minute_angle, CX, CY)
    display.line(CX, CY, mx, my, WHITE)
    sx, sy = _point(115, second_angle, CX, CY)
    display.line(CX, CY, sx, sy, RED)

    shapes.circle(display, CX, CY, 5, WHITE, FILL)


# ---------------------------------------------------------------------
# Mode 6: digital watch face mockup.

def draw_digital_watch():
    shapes.ring(display, CX, CY, WATCH_R, WHITE, 3)
    centered_text(BIG_FONT, "10:09", CY - 40, WHITE)
    centered_text(SMALL_FONT, "AM", CY, GREEN)
    centered_text(SMALL_FONT, "THU SEP 11", CY + 30, WHITE)


# ---------------------------------------------------------------------
# Mode 7: a sample 5-day weather forecast, with a raindrop icon on the
# rainiest of the three outlook days.

FORECAST = (
    ("TODAY", 82, 61),
    ("TUE", 78, 58),
    ("WED", 68, 52),   # the rainy day
    ("THU", 80, 60),
)


def draw_raindrop(x, y, color):
    shapes.circle(display, x, y + 6, 8, color, FILL)
    points = array('h', [0, -14, 7, 2, -7, 2])
    shapes.poly(display, x, y, points, color, FILL)


def draw_weather():
    centered_text(SMALL_FONT, "5-Day Forecast", 70, WHITE)

    width = config.WIDTH // len(FORECAST)
    y = 150
    for i, (day, hi, lo) in enumerate(FORECAST):
        x = width // 2 + i * width
        _draw_forecast_column(x, y, day, hi, lo, rainy=(day == "WED"))


def _draw_forecast_column(x, top_y, day, hi, lo, rainy):
    text = day
    tx = x - (len(text) * SMALL_FONT.WIDTH) // 2
    display.text(SMALL_FONT, text, tx, top_y, YELLOW, BLACK)

    if rainy:
        draw_raindrop(x, top_y + 34, CYAN)
    else:
        shapes.circle(display, x, top_y + 34, 10, YELLOW, FILL)

    hi_text = "H:" + str(hi)
    lo_text = "L:" + str(lo)
    hx = x - (len(hi_text) * SMALL_FONT.WIDTH) // 2
    lx = x - (len(lo_text) * SMALL_FONT.WIDTH) // 2
    display.text(SMALL_FONT, hi_text, hx, top_y + 58, WHITE, BLACK)
    display.text(SMALL_FONT, lo_text, lx, top_y + 76, config.color565(150, 150, 150), BLACK)


# ---------------------------------------------------------------------

MODES = (
    ("Logo (dark)", draw_logo_dark, True),
    ("Logo (white)", draw_logo_white, True),
    ("Rainbow Title", draw_rainbow_title, False),
    ("Color Wheel", draw_color_wheel, False),
    ("Gauge", draw_gauge, False),
    ("Analog Watch", draw_analog_watch, False),
    ("Digital Watch", draw_digital_watch, False),
    ("Weather", draw_weather, False),
)


def show_mode(index):
    name, draw, full_screen = MODES[index]
    if not full_screen:
        display.fill(BLACK)
    draw()


def pressed(button):
    if button.value() == 1:
        return False
    sleep(0.02)
    return button.value() == 0


def wait_for_release(button):
    while button.value() == 0:
        sleep(0.01)


mode_index = 0
show_mode(mode_index)

while True:
    if pressed(button_a):
        mode_index = (mode_index + 1) % len(MODES)
        show_mode(mode_index)
        wait_for_release(button_a)

    if pressed(button_b):
        mode_index = (mode_index - 1) % len(MODES)
        show_mode(mode_index)
        wait_for_release(button_b)

    sleep(0.01)
