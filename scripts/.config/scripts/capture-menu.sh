#!/usr/bin/env bash

# Directory setup
TARGET_DIR="$HOME/Pictures/Screenshots"
mkdir -p "$TARGET_DIR"

TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')
FILE="$TARGET_DIR/screenshot_${TIMESTAMP}.png"

# Define menu options
OPT_SCREEN="1. Fullscreen (Save & Copy)"
OPT_WINDOW="2. Active Window (Save & Copy)"
OPT_SELECT="3. Selected Area (Save & Copy)"
OPT_CLIP_SELECT="4. Selected Area (Clipboard Only)"

# Launch Rofi menu
CHOSEN=$(printf "%s\n%s\n%s\n%s" \
    "$OPT_SCREEN" \
    "$OPT_WINDOW" \
    "$OPT_SELECT" \
    "$OPT_CLIP_SELECT" | rofi -dmenu -p "miam screenshot" -theme "$HOME/.config/rofi/menu.rasi" -i)

case "$CHOSEN" in
    "$OPT_SCREEN")
        grim "$FILE" && wl-copy < "$FILE"
        ;;
    "$OPT_WINDOW")
        GEOMETRY=$(slurp -b "#00000088")
        [ -n "$GEOMETRY" ] && grim -g "$GEOMETRY" "$FILE" && wl-copy < "$FILE"
        ;;
    "$OPT_SELECT")
        GEOMETRY=$(slurp)
        [ -n "$GEOMETRY" ] && grim -g "$GEOMETRY" "$FILE" && wl-copy < "$FILE"
        ;;
    "$OPT_CLIP_SELECT")
        GEOMETRY=$(slurp)
        [ -n "$GEOMETRY" ] && grim -g "$GEOMETRY" - | wl-copy
        ;;
    *)
        exit 0
        ;;
esac
