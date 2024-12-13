#################################
#            Imports            #
#################################


from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import subprocess, time


#################################
#           Constants           #
#################################


mod = "mod4"
terminal = "alacritty"
browser = "firefox"

colors = {
    "bg": "#1E1F27",
    "fg": "#727691",
    "fg-light": "#424452",
    "active": "#168ECA",
    "blue": "#1ba3e7",
    "red": "#ef4444",
    "yellow": "#eab308",
    "purple": "#9333ea",
    "green": "#22c55e"
}


#################################
#           Functions           #
#################################


# NONE as of now


#################################
#         Key Bingdings         #
#################################


keys = [
    # Layout Management
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resizing Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"), desc="Increases volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"), desc="Decreases volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mutes volume"),

    # Maximize Window In Selected Stact
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Spawn Application
    Key([mod, "shift"], "b", lazy.spawn("feh --bg-scale --randomize /home/shahab/Pictures/Wallpapers/*"), desc="Changes tp random background"),

    # Spawn Application
    Key([mod], "r", lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh drun"), desc="Opens rofi drun"),

    # Switch Application
    Key([mod, "shift"], "Tab", lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh window"), desc="Opens rofi window switcher"),

    # File Explorer
    Key([mod], "e", lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh filebrowser"), desc="Opens rofi file explorer"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),

    # Switch Layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    # Toggle Between Floating And Tiled Layouts
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Toggle Fullscreen
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    # General Settings
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]


#################################
#      Group Key Bingdings      #
#################################


groups = [
    Group("1", label="󰈹"),
    Group("2", label="󰨞"),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label=""),
    Group("6", label="")
]

for i in groups:
    keys.extend(
        [
            # Switch to group (mod + group number)
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),

            # Switch To & Move Focused Window To Group (mod + shift + group number)
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),

            # move focused window to group (mod + control + group number)
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
            ),
        ]
    )


#################################
#            Layouts            #
#################################

layout_properties = {
    "border_width": 2,
    "margin": 10,
    "border_normal": colors["bg"],
    "border_focus": colors["blue"],

}


layouts = [
    layout.Columns(**layout_properties),
    layout.Max(margin = 10),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#################################
#        Custom Widgets         #
#################################


class WifiIconWidget(widget.TextBox):
    def __init__(self, **config):
        widget.TextBox.__init__(self, **config)
        self.update_icon()

    def update_icon(self):
        try:
            result = subprocess.run(["iwconfig"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            wifi_strength = int(output.split('\n')[5].split('Link Quality=')[1].split("/70")[0])

            if wifi_strength >= 60:
                icon = ''
            elif wifi_strength >= 50:
                icon = '󰤥'
            elif wifi_strength >= 40:
                icon = '󰤢'
            elif wifi_strength >= 30:
                icon = '󰤟'
            else:
                icon = '󰤯'

            self.text = icon
        except Exception as e:
            print(f"Error updating WiFi icon: {e}")

    def hook(self):
        qtile.hook.subscribe.screen_change(self.update_icon)

class WifiNameWidget(widget.TextBox):
    def __init__(self, **config):
        widget.TextBox.__init__(self, **config)
        self.update_icon()

    def update_icon(self):
        try:
            result = subprocess.run(["iwconfig"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            wifi_name = output.split('\n')[0].split('ESSID:')[1].replace('\"', "").replace("  ", "")

            self.text = wifi_name
        except Exception as e:
            print(f"Error updating WiFi icon: {e}")

    def hook(self):
        qtile.hook.subscribe.screen_change(self.update_icon)

class BatteryIconWidget(widget.TextBox):
    def __init__(self, **config):
        widget.TextBox.__init__(self, **config)
        self.update_icon()

    def update_icon(self):
        try:
            result = subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            battery_percent = int(output)

            if battery_percent == 100:
                icon = '󰁹'
            elif battery_percent >= 90:
                icon = '󰂂'
            elif battery_percent >= 80:
                icon = '󰂀'
            elif battery_percent >= 70:
                icon = '󰂀'
            elif battery_percent >= 60:
                icon = '󰁿'
            elif battery_percent >= 50:
                icon = '󰁾'
            elif battery_percent >= 40:
                icon = '󰁽'
            elif battery_percent >= 30:
                icon = '󰁼'
            elif battery_percent >= 20:
                icon = '󰁻'
            elif battery_percent >= 10:
                icon = '󰁺'
            else:
                icon = ''

            self.text = icon
        except Exception as e:
            print(f"Error updating WiFi icon: {e}")

    def hook(self):
        qtile.hook.subscribe.screen_change(self.update_icon)

class BatteryPercentWidget(widget.TextBox):
    def __init__(self, **config):
        widget.TextBox.__init__(self, **config)
        self.update_icon()

    def update_icon(self):
        try:
            result = subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            battery_percent = int(output)

            self.text = str(battery_percent)
        except Exception as e:
            print(f"Error updating WiFi icon: {e}")

    def hook(self):
        qtile.hook.subscribe.screen_change(self.update_icon)


#################################
#      Widget And Screens       #
#################################


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(colour=colors["bg"], radius=10, filled=True, padding_y=4, group=True)
    ],
    "padding": 10,
}

decoration_group_no_padding = {
    "decorations": [
        RectDecoration(colour=colors["bg"], radius=10, filled=True, padding_y=4, group=True)
    ],
}

screens = [
    Screen(
        top=bar.Bar(
            [
                # Arch Icon (Rofi menu open on click)
                widget.TextBox(
                    "󰣇",
                    fontsize=20,
                    foreground=colors["active"],
                    **decoration_group,
                    mouse_callbacks={
                        'Button1': lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh drun")
                    }
                ),
                
                # Search and Workspaces
                widget.Spacer(15),
                widget.TextBox(
                    "Arch Linux",
                    fontsize=10,
                    foreground=colors["fg"],
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh window")
                    },
                    **decoration_group
                ),
                widget.Spacer(
                    40,
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/shahab/.config/rofi/launchers/type-7/launcher.sh window")
                    },
                    **decoration_group
                ),
                widget.GroupBox(
                    active=colors["fg"],
                    fontsize=20,
                    highlight_method='text',
                    disable_drag=True,
                    inactive=colors["fg-light"],
                    padding_x=5,
                    scroll=True,
                    **decoration_group
                ),

                # User Management Section
                widget.Spacer(15),
                widget.TextBox("", fontsize=20, foreground=colors["blue"], **decoration_group),
                widget.QuickExit(
                    default_text="⏻",
                    fontsize=18,
                    foreground=colors["red"],
                    countdown_format="{}",
                    countdown_start=3,
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/shahab/.config/rofi/powermenu/type-2/powermenu.sh")
                    },
                    **decoration_group
                ),
                widget.TextBox("", fontsize=14, foreground=colors["yellow"], **decoration_group),
                widget.CheckUpdates(distro="Arch", no_update_string="0", foreground=colors["yellow"], initial_text="?", **decoration_group),
                widget.CurrentLayout(fmt=" {}", foreground=colors["fg"], **decoration_group),

                # Music
                widget.Spacer(15),
                widget.TextBox("", fontsize=14, foreground=colors["purple"], **decoration_group),
                widget.Systray(**decoration_group),

                widget.Spacer(15),

                widget.Spacer(),

                # Memory
                widget.Spacer(10, **decoration_group_no_padding),
                widget.TextBox("", fontsize=20, foreground=colors["red"], **decoration_group_no_padding, padding=4),
                widget.Memory(format="{MemUsed: .0f}{mm} / {MemTotal: .0f}{mm}", **decoration_group_no_padding, padding=4),
                # Battery
                widget.Spacer(10, **decoration_group_no_padding),
                BatteryIconWidget(fontsize=20, foreground=colors["green"], **decoration_group_no_padding, padding=4),
                BatteryPercentWidget(**decoration_group_no_padding, padding=4),
                # Wifi
                widget.Spacer(10, **decoration_group_no_padding),
                WifiIconWidget(fontsize=16, foreground=colors["yellow"], **decoration_group_no_padding),
                widget.Wlan(**decoration_group),
                # Volume
                widget.Spacer(10, **decoration_group_no_padding),
                widget.TextBox("󰜟", fontsize=16, foreground=colors["purple"], **decoration_group_no_padding, padding=4),
                widget.PulseVolume(**decoration_group_no_padding),
                widget.Spacer(10, **decoration_group_no_padding),

                widget.Spacer(15),

                # Clock
                widget.Spacer(6, **decoration_group_no_padding),
                widget.TextBox("󰥔", fontsize=22, foreground=colors["blue"], **decoration_group_no_padding, padding=4),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", **decoration_group_no_padding),
                widget.Spacer(10, **decoration_group_no_padding),
            ],
            50,
            background = "#00000000",
            margin=[0, 10, -6, 10]
        ),
        # # Enable if floating windows lag
        # x11_drag_polling_rate = 60,
    ),
]


#################################
#   Drag and Floating Layout    #
#################################


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    **layout_properties,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
