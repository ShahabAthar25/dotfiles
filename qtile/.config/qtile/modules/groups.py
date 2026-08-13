from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .keys import mod

groups = [
    Group("1", label="󰈹"),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label=""),
    Group("6", label=""),
]

group_keys = []

for i in groups:
    group_keys.extend(
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
