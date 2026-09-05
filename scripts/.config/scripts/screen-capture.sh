#!/usr/bin/env bash

# Define output directory and ensure it exists
TARGET_DIR="$HOME/Pictures/Screenshots"
mkdir -p "$TARGET_DIR"

# Generate timestamped filename
FILE="$TARGET_DIR/screenshot_$(date +'%Y-%m-%d_%H-%M-%S').png"

# Take fullscreen shot
grim "$FILE"

# Optional: Copy to clipboard as well
wl-copy < "$FILE"

notify-send "Screenshot Captured" "Saved to $FILE" -i "$FILE" -a "Screenshot"
