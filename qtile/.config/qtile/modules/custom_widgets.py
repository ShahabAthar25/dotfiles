import iwlib

from libqtile.widget import base

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
