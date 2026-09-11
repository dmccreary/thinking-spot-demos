# Lab 02: The Thinking Spot Logo -- Dark Variant
# Same idea as 01-logo.py, but streams logo-dark.rgb565: a black
# background, white lettering, and a lighter brown tree trunk so it
# stands out against the dark background instead of the original
# white-background artwork.
#
# convert_logo.py builds this variant from the same source JPEG by
# re-segmenting its flat colors, so both logos stay in sync if the
# source artwork changes -- see build_dark_variant() there for how the
# trunk gets told apart from the letters (they share the same purple in
# the original).
#
# Rename this file to main.py (instead of 01-logo.py) and copy it (plus
# config.py, lib/, and logo-dark.rgb565) to the board's root to have this
# variant appear a few seconds after power-on with no computer attached.

import config

ROWS_PER_CHUNK = 20  # 360 * 20 * 2 = 14,400 bytes per chunk
ROW_BYTES = config.WIDTH * 2

display = config.init_display()
display.fill(config.BLACK)

with open("logo-dark.rgb565", "rb") as logo:
    y = 0
    while y < config.HEIGHT:
        rows = min(ROWS_PER_CHUNK, config.HEIGHT - y)
        chunk = logo.read(ROW_BYTES * rows)
        display.blit_buffer(chunk, 0, y, config.WIDTH, rows)
        y += rows
