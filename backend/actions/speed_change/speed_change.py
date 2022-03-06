"""Contains a class for speed changes."""


import typing as typ

from .. import action
from . import formats as frm


class SpeedChange(action.ActionABC):
    """Contains information for changing the speed of the video."""
    def __init__(self, speed_formatted: frm.SpeedFormat):
        self.speed_formatted = speed_formatted

    def convert_to_decimal(self):
        """Converts the speed format to a decimal."""
        if not isinstance(self.speed_formatted, frm.Decimal):
            self.speed_formatted = frm.Decimal.from_sub(self.speed_formatted)


    @classmethod
    def show_ui(cls, inst=None):
        ...


    def execute_action(self, video_path):
        pass
