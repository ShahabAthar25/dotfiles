import os
import subprocess
import random

from libqtile import hook

from modules.groups import group_keys, groups
from modules.keys import keys
from modules.layouts import floating_layout, get_layout_settings, layouts
from modules.screens import extension_defaults, screens, widget_defaults
from modules.themes import colors

SCRIPT_DIR = os.path.expanduser("~/.config/rofi/scripts")

keys.extend(group_keys)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    wallpaper_dir = os.path.join(home, 'Pictures/Wallpapers')

    # Start swww daemon
    subprocess.Popen(['awww-daemon'])

    # Get a list of image files from the wallpaper directory
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    if os.path.exists(wallpaper_dir):
        wallpapers = [
            os.path.join(wallpaper_dir, f) 
            for f in os.listdir(wallpaper_dir) 
            if f.lower().endswith(valid_extensions)
        ]

        if wallpapers:
            random_wallpaper = random.choice(wallpapers)
            # Send wallpaper image to swww with a transition effect
            subprocess.Popen([
                'awww', 'img', random_wallpaper,
                '--transition-type', 'outer',
                '--transition-step', '30'
            ])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24
