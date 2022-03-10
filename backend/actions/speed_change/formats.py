"""Module that contains formats for representing speed."""


import backend.misc.dataclass as dt
import backend.misc.class_registers as c_r


speed_formats = c_r.ClassList()


class SpeedFormat(c_r.RegisteredClass):
    """Base class for speed formats."""
    name: str = None
    prefix: str = None

    def __init__(self, value: int | float = 0):
        self.value = value

    def __repr__(self):
        return f"{self.name} ({self.prefix}): {self.value}"

    @classmethod
    def cls_to_str(cls):
        """Gets the class string."""
        inst = cls()
        return f"{inst.name} ({inst.prefix})"


class Decimal(SpeedFormat, dt.MainDataclass):
    """Decimal."""
    name = "Decimal"
    prefix = "."

    @classmethod
    def from_sub(cls, data: SpeedFormat):
        inst = cls()

        if isinstance(data, Percent):
            inst.value = data.value / 100

        return inst

speed_formats.register_class(Decimal)


class Percent(SpeedFormat, dt.SubDataclass):
    """Percent."""
    name = "Percent"
    prefix = "%"

    @classmethod
    def from_main(cls, data: SpeedFormat):
        inst = cls()

        inst.value = data.value * 100

        return inst

speed_formats.register_class(Percent)
