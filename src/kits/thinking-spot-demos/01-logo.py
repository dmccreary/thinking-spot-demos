# Lab 01: The Thinking Spot Logo
# Streams docs/img/thinking-spot-logo-on-white.jpg to the 360x360 GC9B72
# round display.
#
# The Pico has no JPEG decoder, so the image can't be loaded as-is.
# convert_logo.py (run on your computer, not the Pico) resizes the logo
# to 360x360 and dumps it as raw RGB565 pixels -- logo.rgb565, 259,200
# bytes -- which is what this script actually reads.
#
# 259,200 bytes is also most of the RP2040's 264 KB of RAM (see the note
# in ../sw-gc9b72/09-blit.py), so the whole image is never held in memory
# at once. Instead this reads ROWS_PER_CHUNK rows at a time from the file
# and blits each chunk before reading the next -- a small, constant
# amount of RAM no matter how big the image is.
#
# Rename this file to main.py and copy it (plus config.py, lib/, and
# logo.rgb565) to the board's root to have the logo appear a few seconds
# after power-on with no computer attached.

import config

ROWS_PER_CHUNK = 20  # 360 * 20 * 2 = 14,400 bytes per chunk
ROW_BYTES = config.WIDTH * 2

display = config.init_display()
display.fill(config.WHITE)

with open("logo.rgb565", "rb") as logo:
    y = 0
    while y < config.HEIGHT:
        rows = min(ROWS_PER_CHUNK, config.HEIGHT - y)
        chunk = logo.read(ROW_BYTES * rows)
        display.blit_buffer(chunk, 0, y, config.WIDTH, rows)
        y += rows
