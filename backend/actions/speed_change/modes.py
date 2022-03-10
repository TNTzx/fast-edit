"""Defines the modes for the speed changes."""


import backend.misc.dataclass as dt

from . import formats as frm


class SpeedMode(dt.Dataclass):
    """A mode for changing speeds."""
    def __init__(self, start_speed: frm.SpeedFormat, end_speed: frm.SpeedFormat):
        self.start_speed = start_speed
        self.end_speed = end_speed

    def __init_subclass__(cls) -> None:
        SpeedModes.register_mode(cls)


    def convert_to_decimal(self):
        """Converts the speed format to a decimal."""
        ...


class SpeedModes():
    """Contains all speed modes."""
    speed_modes: list[SpeedMode] = []

    @classmethod
    def register_mode(cls, speed_mode: SpeedMode):
        """Register a mode."""
        cls.speed_modes.append(speed_mode)


class FromToMode(SpeedMode, dt.MainDataclass):
    """Describes a speed mode with an initial and end speed."""
    name = "From Speed To Speed"

    @classmethod
    def from_sub(cls, data: SpeedMode):
        ...


class ApplySpeedMode(SpeedMode, dt.SubDataclass):
    """Describes a speed mode with a speed increase."""
    name = "Apply Speed"

    def __init__(self, new_speed: frm.SpeedFormat):
        super().__init__(frm.Decimal(1), new_speed)


    @classmethod
    def from_main(cls, data: SpeedMode):
        ...
