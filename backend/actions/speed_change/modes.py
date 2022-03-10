"""Defines the modes for the speed changes."""


import backend.misc.dataclass as dt
import backend.misc.class_registers as c_r

from . import formats as frm


speed_modes = c_r.ClassList()


class SpeedMode():
    """A mode for changing speeds."""
    def __init__(self, start_speed: frm.SpeedFormat, end_speed: frm.SpeedFormat):
        self.start_speed = start_speed
        self.end_speed = end_speed

    def convert_to_decimal(self):
        """Converts the speed formats to a decimal."""
        self.start_speed = frm.Decimal.from_sub(self.start_speed)
        self.end_speed = frm.Decimal.from_sub(self.end_speed)


class FromToMode(SpeedMode, dt.MainDataclass, c_r.RegisteredClass):
    """Describes a speed mode with an initial and end speed."""
    @classmethod
    def cls_to_str(cls):
        return "From Speed To Speed"

    @classmethod
    def from_sub(cls, data: SpeedMode):
        inst = cls(data.start_speed, data.end_speed)
        if isinstance(data, ApplySpeedMode):
            pass
        return inst

speed_modes.register_class(FromToMode)


class ApplySpeedMode(SpeedMode, dt.SubDataclass, c_r.RegisteredClass):
    """Describes a speed mode with a speed increase."""
    def __init__(self, new_speed: frm.SpeedFormat):
        super().__init__(frm.Decimal(1), new_speed)

    @classmethod
    def cls_to_str(cls):
        return "Apply Speed"


    @classmethod
    def from_main(cls, data: SpeedMode):
        inst = cls(data.end_speed)
        return inst

speed_modes.register_class(ApplySpeedMode)
