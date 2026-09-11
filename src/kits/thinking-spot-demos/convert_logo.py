#!/usr/bin/env python3
# Converts docs/img/thinking-spot-logo-on-white.jpg into raw RGB565 pixel
# dumps the GC9B72 driver can stream straight to the display.
#
# Run this on your computer (needs Pillow, NumPy, and SciPy), not on the
# Pico -- MicroPython has no JPEG decoder. It produces two files:
#
#   logo.rgb565       the logo as-is (white background) -- 01-logo.py
#   logo-dark.rgb565  a black-background, white-text variant with a
#                      lighter brown trunk -- 02-logo-dark.py
#
# The dark variant is built by re-segmenting the source JPEG's colors
# rather than hand-editing pixels, so it stays in sync if the source
# artwork changes. It also writes the full-resolution result to
# docs/img/thinking-spot-logo-on-black.png for use elsewhere in the book.
#
#   pip install pillow numpy scipy
#   python3 convert_logo.py

import struct
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

KIT_DIR = Path(__file__).resolve().parent
IMG_DIR = KIT_DIR / ".." / ".." / ".." / "docs" / "img"
SOURCE_IMAGE = IMG_DIR / "thinking-spot-logo-on-white.jpg"
DARK_PNG = IMG_DIR / "thinking-spot-logo-on-black.png"

# Matches config.WIDTH / config.HEIGHT for the GC9B72 panel.
DISPLAY_SIZE = 360

# The source artwork's flat colors, sampled from the JPEG. "purple" covers
# both the lettering and the tree trunk -- they're recolored differently
# below because a connected-component pass, not the color itself,
# distinguishes the trunk from each individual letter.
WHITE = np.array([255, 255, 255])
PURPLE = np.array([97, 38, 82])
GREEN = np.array([148, 212, 11])
YELLOW = np.array([252, 216, 0])
ORANGE = np.array([253, 103, 26])

DARK_BACKGROUND = np.array([0, 0, 0])
DARK_TEXT = np.array([255, 255, 255])
DARK_TRUNK = np.array([196, 138, 86])  # a lighter brown that reads against black


def rgb565(r, g, b):
    """Same packing as gc9b72.color565() and its big-endian wire format:
    5 bits red, 6 bits green, 5 bits blue, sent MSB-first (">H")."""
    return (r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3


def image_to_rgb565(image):
    image = image.resize((DISPLAY_SIZE, DISPLAY_SIZE), Image.LANCZOS)
    pixels = image.load()
    out = bytearray(DISPLAY_SIZE * DISPLAY_SIZE * 2)
    i = 0
    for y in range(DISPLAY_SIZE):
        for x in range(DISPLAY_SIZE):
            r, g, b = pixels[x, y]
            struct.pack_into(">H", out, i, rgb565(r, g, b))
            i += 2
    return out


def write_variant(image, name):
    data = image_to_rgb565(image)
    out_path = KIT_DIR / name
    out_path.write_bytes(data)
    print(f"Wrote {out_path} ({len(data):,} bytes, "
          f"{DISPLAY_SIZE}x{DISPLAY_SIZE} RGB565)")


def build_dark_variant(source):
    """Re-segments the source artwork by nearest flat color, then
    recolors each segment for a black background: white background ->
    black, letters -> white, tree trunk -> light brown. Everything else
    (leaves, book) keeps its original color.

    The trunk and the letters share the same purple in the source, so
    color alone can't tell them apart -- a connected-components pass
    does: the trunk is one large blob, each letter is its own small one,
    and the trunk is by far the largest purple region in the image.
    """
    arr = np.array(source).astype(int)
    anchors = {"white": WHITE, "purple": PURPLE, "green": GREEN,
               "yellow": YELLOW, "orange": ORANGE}
    names = list(anchors.keys())
    dists = np.stack(
        [np.sqrt(((arr - c) ** 2).sum(axis=2)) for c in anchors.values()],
        axis=-1)
    cls = np.argmin(dists, axis=-1)

    purple_mask = cls == names.index("purple")
    labeled, count = ndimage.label(purple_mask, structure=np.ones((3, 3)))
    sizes = ndimage.sum(purple_mask, labeled, range(1, count + 1))
    trunk_label = int(np.argmax(sizes)) + 1
    trunk_mask = labeled == trunk_label
    text_mask = purple_mask & ~trunk_mask

    out = np.zeros_like(arr)
    out[cls == names.index("white")] = DARK_BACKGROUND
    out[text_mask] = DARK_TEXT
    out[trunk_mask] = DARK_TRUNK
    out[cls == names.index("green")] = GREEN
    out[cls == names.index("yellow")] = YELLOW
    out[cls == names.index("orange")] = ORANGE

    return Image.fromarray(out.astype("uint8"), "RGB")


def main():
    source = Image.open(SOURCE_IMAGE).convert("RGB")
    write_variant(source, "logo.rgb565")

    dark = build_dark_variant(source)
    dark.save(DARK_PNG)
    print(f"Wrote {DARK_PNG}")
    write_variant(dark, "logo-dark.rgb565")


if __name__ == "__main__":
    main()
