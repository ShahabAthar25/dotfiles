from libqtile import layout
from libqtile.config import Match

from .themes import colors

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
