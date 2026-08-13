import os
import random
import subprocess

from libqtile.config import Key
from libqtile.lazy import lazy

from .themes import SCRIPTS_DIR

def change_wallpaper(qtile):
    home = os.path.expanduser('~')
    wallpaper_dir = os.path.join(home, 'Pictures/Wallpapers')
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    
    if os.path.exists(wallpaper_dir):
        wallpapers = [
            os.path.join(wallpaper_dir, f) 
            for f in os.listdir(wallpaper_dir) 
            if f.lower().endswith(valid_extensions)
        ]
        if wallpapers:
            subprocess.Popen(['awww', 'img', random.choice(wallpapers), '--transition-type', 'outer'])

mod = "mod4"
terminal = "kitty"
browser = "brave"
explorer = "alacritty -e ranger"
htop = "kitty htop"

lock_cmd = os.path.expanduser("~/.local/share/quickshell-lockscreen/lock.sh")

keys = [
    # Change Wallpaper
    Key([mod, "control"], "e", lazy.function(change_wallpaper), desc="Randomize Wallpaper"),

    # Lockscreen
    Key([mod, "mod1"], "l", lazy.spawn(lock_cmd), desc="Lock Screen"),

    # Brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl +10"),
        desc="Increase Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl -10"),
        desc="Decreases Brightness",
    ),
    # Volume
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpactl set-volume @DEFAULT_AUDIO_SINK@ +10%"),
        desc="Increase Volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpactl set-volume @DEFAULT_AUDIO_SINK@ -10%"),
        desc="Decreases Volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
        desc="Toggles Volume",
    ),

    # Launch Apps
    Key([mod], "b", lazy.spawn(browser), desc="Spawn default browser"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch file explorer"),
    Key([mod], "m", lazy.spawn(f"{SCRIPTS_DIR}/wifi.sh"), desc="Opens wifi menu"),

    # Menus
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launches rofi drun"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),

    # Global
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
