"""Module that contains formats for representing speed."""


from re import L


class SpeedFormat():
    """Base class for speed formats."""
    def __init__(self, value: int | float):
        self.name: str = None
        self.value = value


class SubSpeedFormat(SpeedFormat):
    """The sub-speed formats."""

class MainDecimal(SpeedFormat):
    """The main speed format."""
    def __init__(self, value: SubSpeedFormat | int | float):
        super().__init__(value)
        

