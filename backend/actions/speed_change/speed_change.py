"""Contains a class for speed changes."""


import typing as typ

import widget_ext.widget_ext_class as wec

from .. import action
from . import modes
from . import ui


class SpeedChange(action.ActionABC):
    """Contains information for changing the speed of the video."""
    def __init__(self, speed_mode: modes.SpeedMode):
        self.speed_mode = speed_mode

    def convert_to_decimal(self):
        """Converts the speed format to a decimal."""
        if not isinstance(self.speed_formatted, frm.Decimal):
            self.speed_formatted = frm.Decimal.from_sub(self.speed_formatted)


    @classmethod
    def from_ui(cls, parent: wec.WidgetExt, inst=None):
        ui.SpeedChange(parent)


    def execute_action(self, video_path):
        pass
