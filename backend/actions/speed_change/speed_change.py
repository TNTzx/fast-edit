"""Contains a class for speed changes."""


import widget_ext.widget_ext_class as wec

from .. import action
from . import modes
from . import ui


class SpeedChange(action.ActionABC):
    """Contains information for changing the speed of the video."""
    def __init__(self, speed_mode: modes.SpeedMode):
        self.speed_mode = speed_mode

    def execute_action(self, video_path):
        pass


def from_ui(parent: wec.WidgetExt, speed_change: SpeedChange = None):
    """Creates a UI then returns the speed change."""
    ui.SpeedChange(parent)

