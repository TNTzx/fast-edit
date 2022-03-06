"""Module that contains formats for representing speed."""


import typing as typ

import backend.misc.dataclass as dt


class SpeedFormat():
    """Base class for speed formats."""
    def __init__(self, value: int | float = 0):
        self.name: str = None
        self.prefix: str = None
        self.value = value

    def __repr__(self):
        return f"{self.name} ({self.prefix})"

    def __init_subclass__(cls):
        SpeedFormats.register_format(cls)

class SpeedFormats():
    """Contains all speed formats."""
    speed_formats = []

    @classmethod
    def register_format(cls, speed_format: typ.Type[SpeedFormat]):
        """Registers the SpeedFormat."""
        cls.speed_formats.append(speed_format)


class Decimal(SpeedFormat, dt.MainDataclass):
    """Decimal."""
    def __init__(self, value: int | float = 0):
        super().__init__(value)
        self.name = "Decimal"
        self.prefix = "."

    @classmethod
    def from_sub(cls, data: SpeedFormat):
        inst = cls()

        if isinstance(data, Percent):
            inst.value = data.value / 100

        return inst


@dt.SetMainDataclass(Decimal)
class Percent(SpeedFormat, dt.SubDataclass):
    """Percent."""
    def __init__(self, value: int | float = 0):
        super().__init__(value)
        self.name = "Percent"
        self.prefix = "%"

    @classmethod
    def from_main(cls, data: SpeedFormat):
        inst = cls()

        inst.value = data.value * 100

        return inst
