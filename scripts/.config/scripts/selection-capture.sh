#!/usr/bin/env bash

TARGET_DIR="$HOME/Pictures/Screenshots"
mkdir -p "$TARGET_DIR"

FILE="$TARGET_DIR/screenshot_$(date +'%Y-%m-%d_%H-%M-%S').png"

# Select region and capture
GEOMETRY=$(slurp)

# If user cancelled selection (pressed Esc), exit cleanly
if [ -z "$GEOMETRY" ]; then
    exit 0
fi

grim -g "$GEOMETRY" "$FILE"
wl-copy < "$FILE"

notify-send "Screenshot Captured" "Saved to $FILE" -i "$FILE" -a "Screenshot"
