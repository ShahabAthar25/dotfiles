from libqtile.config import Screen
from libqtile import bar
from libqtile.lazy import lazy

from qtile_extras import widget

from .themes import colors
from .custom_widgets import Wlan
from .themes import SCRIPTS_DIR

CANDY_ICONS_PATH = "/usr/share/icons/candy-icons/apps/scalable/"

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono",
    fontsize=12,
    padding=10,
)
extension_defaults = widget_defaults.copy()

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
                    mouse_callbacks={"Button1": lazy.spawn(f"{SCRIPTS_DIR}/wifi.sh")},
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
