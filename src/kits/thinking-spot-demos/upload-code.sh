#!/usr/bin/env bash
# Upload the Thinking Spot logo demo to a connected Raspberry Pi Pico
# wired to a 2.1" 360x360 GC9B72 round display, using mpremote. Run from
# within this directory or from anywhere -- the script resolves its own
# location.
#
# Everything in lib/ goes to :lib/ first -- the GC9B72 driver and the two
# font modules config.py imports. Then config.py, then every *.rgb565
# asset (the raw pixel dumps 01-logo.py and 02-logo-dark.py read), then
# the labs.
#
# convert_logo.py runs on your computer, not the Pico -- MicroPython has
# no JPEG decoder -- so it is deliberately left off the board.
#
# IMPORTANT: Quit (or "Stop/Disconnect" from) Thonny before running this.
# Only one program can use the Pico's serial port at a time. If Thonny is
# connected, mpremote fails with:
#   "failed to access /dev/cu.usbmodem... (it may be in use by another program)"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if ! command -v mpremote >/dev/null 2>&1; then
    echo "Error: mpremote is not installed. Install with: pip install mpremote" >&2
    exit 1
fi

shopt -s nullglob
asset_files=( *.rgb565 )
shopt -u nullglob
if (( ${#asset_files[@]} == 0 )); then
    echo "Error: no .rgb565 files found. Generate them first:" >&2
    echo "  python3 convert_logo.py" >&2
    exit 1
fi

echo "NOTE: Quit or disconnect Thonny first — only one program can use the"
echo "      Pico's serial port at a time."
echo

echo "Checking for connected Pico..."
# We pass the exact serial port to mpremote rather than using "connect auto",
# which only matches a fixed list of vendor/product IDs and silently reports
# "no device found" for boards it does not recognize.
#
# You can force a specific port:  PORT=/dev/cu.usbmodem14301 ./upload-code.sh
if [[ -n "${PORT:-}" ]]; then
    echo "Using device from PORT environment variable: $PORT"
else
    # macOS uses /dev/cu.usbmodem* (preferred for outgoing connections);
    # Linux uses /dev/ttyACM* or /dev/ttyUSB*.
    shopt -s nullglob
    serial_devs=(
        /dev/cu.usbmodem*
        /dev/tty.usbmodem*
        /dev/ttyACM*
        /dev/ttyUSB*
    )
    shopt -u nullglob
    if (( ${#serial_devs[@]} == 0 )); then
        echo "Error: No Pico detected (no usbmodem/ttyACM/ttyUSB device). Plug it in and try again." >&2
        exit 1
    fi
    PORT="${serial_devs[0]}"
    if (( ${#serial_devs[@]} > 1 )); then
        echo "Multiple serial devices found; using the first:"
        printf '  %s\n' "${serial_devs[@]}"
        echo "Override with: PORT=/dev/your-device ./upload-code.sh"
    fi
    echo "Using device: $PORT"
fi

# Interrupt any running program before copying files.
mpremote connect "$PORT" soft-reset >/dev/null 2>&1 || true

shopt -s nullglob
lab_files=( *.py )
lib_files=( lib/*.py )
shopt -u nullglob

# convert_logo.py is a host-side tool (needs Pillow, decodes JPEG) -- it
# never runs on the Pico and has no reason to take up flash there.
lab_files=( "${lab_files[@]/convert_logo.py}" )

if (( ${#lab_files[@]} == 0 && ${#lib_files[@]} == 0 )); then
    echo "No .py files found in $SCRIPT_DIR" >&2
    exit 1
fi

# Upload lib/ first (display driver and fonts config.py imports), then
# config.py, then every .rgb565 asset (the pixel data the logo labs
# read), then everything else.
if (( ${#lib_files[@]} > 0 )); then
    echo "Uploading ${#lib_files[@]} file(s) to Pico :lib/ ..."
    mpremote connect "$PORT" mkdir :lib >/dev/null 2>&1 || true
    for f in "${lib_files[@]}"; do
        name="$(basename "$f")"
        echo "  -> lib/$name"
        if ! mpremote connect "$PORT" cp "$f" ":lib/$name"; then
            echo >&2
            echo "Error: could not write to the Pico." >&2
            echo "If the port is 'in use by another program', QUIT or DISCONNECT" >&2
            echo "Thonny (or any other serial monitor) and run this script again." >&2
            exit 1
        fi
    done
fi

files=()
if [[ -f config.py ]]; then
    files+=( config.py )
fi
files+=( "${asset_files[@]}" )
for f in "${lab_files[@]}"; do
    [[ -z "$f" ]] && continue
    [[ "$f" == "config.py" ]] && continue
    files+=( "$f" )
done

echo "Uploading ${#files[@]} file(s) to Pico..."
for f in "${files[@]}"; do
    echo "  -> $f"
    if ! mpremote connect "$PORT" cp "$f" ":$f"; then
        echo >&2
        echo "Error: could not write to the Pico." >&2
        echo "If the port is 'in use by another program', QUIT or DISCONNECT" >&2
        echo "Thonny (or any other serial monitor) and run this script again." >&2
        exit 1
    fi
done

echo "Done. Files on Pico:"
mpremote connect "$PORT" ls
mpremote connect "$PORT" ls :lib 2>/dev/null || true
