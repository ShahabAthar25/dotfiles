import iwlib
import toml
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.widget import base
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

############################
#      Custom Widgets      #
############################


def get_quality(interface_name):
    interface = iwlib.get_iwconfig(interface_name)
    if "stats" not in interface:
        return None, None
    quality = interface["stats"]["quality"]
    return quality


class Wlan(base.InLoopPollText):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("interface", "wlan0", "The interface to monitor"),
        ("update_interval", 1, "The update interval."),
        (
            "disconnected_message",
            "Disconnected",
            "String to show when the wlan is diconnected.",
        ),
        (
            "use_ethernet",
            False,
            "Activate or deactivate checking for ethernet when no wlan connection is detected",
        ),
        (
            "format",
            "{icon}",
            'Display format. For percents you can use "{essid} {percent:2.0%}"',
        ),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Wlan.defaults)

    def poll(self):
        try:
            quality = get_quality(self.interface)

            if quality >= 60:
                icon = ""
            elif quality >= 50:
                icon = "󰤥"
            elif quality >= 40:
                icon = "󰤢"
            elif quality >= 30:
                icon = "󰤟"
            else:
                icon = "󰤯"

            return self.format.format(
                icon=icon,
            )
        except:
            logger.error(
                "Probably your wlan device is switched off or "
                " otherwise not present in your system."
            )

    def button_press(self, num, x, y):
        if num in self.mouse_callbacks:
            self.mouse_callbacks[num]()


############################
#          Config          #
############################

SCRIPT_DIR = "/home/shahab/.config/rofi/scripts"

colors = toml.load("/home/shahab/.config/colors.toml")["colors"]
colors["custom"] = {"white": "#ffffff"}

mod = "mod4"
terminal = "kitty"
browser = "brave"
explorer = "alacritty -e ranger"
htop = "kitty htop"

keys = [
    # Brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("xbacklight +10"),
        desc="Increase Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -10"),
        desc="Decreases Brightness",
    ),
    # Volume
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
        desc="Increase Volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
        desc="Decreases Volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Toggles Volume",
    ),
    # Launch Apps
    Key([mod], "b", lazy.spawn(browser), desc="Spawn default browser"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch file explorer"),
    Key([mod], "m", lazy.spawn(f"{SCRIPT_DIR}/wifi.sh"), desc="Opens wifi menu"),
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
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [
    Group("1", label="󰈹"),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label=""),
    Group("6", label=""),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )


def get_layout_settings(exclude=[], values={}):
    layout_settings = {
        "border_focus": colors["primary"]["foreground"],
        "border_normal": colors["primary"]["background"],
        "border_width": 2,
        "margin": [7, 10, 10, 10],
    }

    for key in exclude:
        if key in layout_settings:
            del layout_settings[key]

    for key, value in values.items():
        if key in values:
            layout_settings[key] = value

    return layout_settings


layouts = [
    layout.Columns(**get_layout_settings()),
    layout.Max(**get_layout_settings(exclude=["border_width"])),
    layout.MonadWide(**get_layout_settings(values={"margin": 10})),
    layout.Stack(num_stacks=2, **get_layout_settings()),
    layout.Matrix(**get_layout_settings()),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(**get_layout_settings()),
    # layout.MonadTall(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono",
    fontsize=12,
    padding=10,
)
extension_defaults = widget_defaults.copy()

powerline = {"decorations": [PowerLineDecoration(path="arrow_right")]}

CANDY_ICONS_PATH = "/usr/share/icons/candy-icons/apps/scalable/"

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(10),
                widget.TextBox(
                    "󰣇", fontsize=35, padding=5, foreground=colors["bright"]["cyan"]
                ),
                widget.TextBox(
                    "", fontsize=15, foreground=colors["primary"]["foreground"]
                ),
                widget.GroupBox(
                    active=colors["primary"]["foreground"],
                    highlight_method="text",
                    disable_drag=True,
                    inactive=colors["normal"]["black"],
                    padding_x=4,
                    fontsize=35,
                ),
                widget.TextBox(
                    "", fontsize=15, foreground=colors["primary"]["foreground"]
                ),
                widget.Spacer(-10),
                widget.LaunchBar(
                    progs=[
                        (
                            f"{CANDY_ICONS_PATH}/firefox-icon.svg",
                            "firefox",
                            "Launches Firefox",
                        ),
                        (
                            f"{CANDY_ICONS_PATH}/Alacritty.svg",
                            "alacritty",
                            "Launches Alacritty",
                        ),
                        (
                            f"{CANDY_ICONS_PATH}/file-manager.svg",
                            "alacritty -e ranger",
                            "Launches Ranger",
                        ),
                    ],
                    padding=20,
                    icon_size=26,
                ),
                widget.Systray(padding=10),
                widget.Prompt(),
                widget.WindowName(width=500),
                widget.Spacer(foreground=colors["cursor"]["cursor"]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    "", fontsize=30, padding=0, foreground=colors["bright"]["green"]
                ),
                widget.CurrentLayout(foreground=colors["cursor"]["cursor"]),
                widget.TextBox(
                    "", fontsize=15, foreground=colors["primary"]["foreground"]
                ),
                widget.TextBox(
                    "󰥔", fontsize=30, foreground=colors["bright"]["blue"], padding=0
                ),
                widget.Clock(
                    format="%I:%M %p %a, %Y/%m/%d",
                    foreground=colors["cursor"]["cursor"],
                ),
                widget.TextBox(
                    "", fontsize=15, foreground=colors["primary"]["foreground"]
                ),
                widget.TextBox(
                    "",
                    fontsize=33,
                    foreground=colors["bright"]["magenta"],
                    mouse_callbacks={
                        "Button1": lazy.spawn("pavucontrol"),
                    },
                ),
                Wlan(
                    fontsize=33,
                    foreground=colors["bright"]["yellow"],
                    mouse_callbacks={"Button1": lazy.spawn(f"{SCRIPT_DIR}/wifi.sh")},
                ),
                widget.QuickExit(
                    fmt="⏻", fontsize=30, foreground=colors["bright"]["red"]
                ),
            ],
            35,
            background=colors["primary"]["background"],
            margin=[-3, 10, 4, 10],
            border_width=10,  # Draw top and bottom borders
            border_color=colors["primary"]["background"],  # Borders are magenta
        ),
        x11_drag_polling_rate=60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    **get_layout_settings(),
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
