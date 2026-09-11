# thinking-spot-demos Kit (Thinking Spot Logo on GC9B72)

A Raspberry Pi Pico wired to the same 2.1" round GC9B72 SPI display as the
[sw-gc9b72 kit](../sw-gc9b72/README.md), showing
[the Thinking Spot logo](../../../docs/img/thinking-spot-logo-on-white.jpg)
instead of a face. The wiring, driver, and `config.py` are identical to
that kit -- see its README for pinout and troubleshooting.

Two variants ship: the logo as-is on a white background, and a
dark variant with a black background, white lettering, and a lighter
brown trunk so it stands out.

## Files

| File | Purpose |
|---|---|
| `convert_logo.py` | Host-side tool (needs Pillow, NumPy, SciPy). Resizes the logo JPEG to 360x360 and dumps it as raw RGB565 pixels, and builds the dark variant by re-segmenting the source artwork's colors. Run this on your computer, not the Pico. |
| `logo.rgb565` | The white-background logo, resized to 360x360 RGB565 -- 259,200 bytes, checked in so the kit works without re-running the converter. |
| `logo-dark.rgb565` | The dark variant at 360x360 RGB565, same size, also checked in. |
| `01-logo.py` | Reads `logo.rgb565` back a few rows at a time and blits it to the display. |
| `02-logo-dark.py` | Same as `01-logo.py` but reads `logo-dark.rgb565` and fills the screen black first instead of white. |
| `config.py`, `lib/` | Copied from `sw-gc9b72` -- same board, same driver, same fonts. |
| `upload-code.sh` | Uploads everything above (except `convert_logo.py`, which never runs on the Pico) to a connected Pico via `mpremote`. |

Rename whichever lab you want to run automatically to `main.py` before
uploading -- MicroPython always runs `main.py` a few seconds after
power-on.

## How the dark variant is built

`docs/img/thinking-spot-logo-on-black.png` (and `logo-dark.rgb565`, its
360x360 RGB565 encoding) are generated, not hand-drawn. `convert_logo.py`
re-segments the source JPEG by its five flat colors (white, purple,
green, yellow, orange), then recolors: white background -> black,
green/yellow/orange leaves and book -> unchanged.

The tricky part is the purple: the lettering and the tree trunk are the
*same* purple in the source artwork, so color alone can't tell them
apart. A connected-components pass over the purple pixels does -- the
trunk is one large connected blob, each letter is its own small,
separate blob, and the trunk is by a wide margin the largest purple
region in the image. The trunk's component becomes the lighter brown
`(196, 138, 86)`; every other purple pixel (the letters) becomes white.

## Why the image is streamed instead of loaded whole

The Pico's RP2040 has 264 KB of RAM total. A full 360x360 RGB565 frame is
259,200 bytes -- 98% of every byte on the chip, before MicroPython's own
interpreter and heap take their share. Neither lab holds the whole image
in memory: each reads `ROWS_PER_CHUNK` rows (14,400 bytes) from its
`.rgb565` file at a time and blits each chunk before reading the next, so
memory use stays small and constant regardless of image size.

## Regenerating the logo assets

If `docs/img/thinking-spot-logo-on-white.jpg` changes, regenerate both
on-device assets (and the dark-variant PNG):

```bash
pip install pillow numpy scipy
python3 convert_logo.py
```

## Running it

```bash
./upload-code.sh
```

Then, on the Pico (via Thonny or `mpremote run 01-logo.py` /
`mpremote run 02-logo-dark.py`), run whichever lab you want.
