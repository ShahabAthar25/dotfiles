#!/bin/bash

# Extract wifi SSIDs cleanly, stripping ANSI codes and formatting markers
wifi_names=$(iwctl station wlan0 get-networks | sed '1,4d; s/[[0-9;]*m//g; s/^[[:space:]]*//; s/\x1B//g; s/>//; s/psk//; s/*//g; s/[[:space:]]*$//; s/^ \{5\}//')


# Show menu in Rofi
selected_wifi=$(echo "$wifi_names" | rofi -dmenu -i -p "Select Wifi")

# Connect if a network was selected
if [[ -n "$selected_wifi" ]]; then
    # Spawn in terminal or prompt for passphrase if needed
    iwctl station wlan0 connect "$selected_wifi"
fi
