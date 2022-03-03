"""Module that contains formats for representing speed."""


class SpeedFormat():
    """Base class for speed formats."""
    def __init__(self, value: int | float):
        self.name: str = None
        self.prefix: str = None
        self.value = value
    
    def __repr__(self):
        return f"{self.name} ({self.prefix})"


class Decimal(SpeedFormat):
    """Decimal."""
    def __init__(self, value: int | float):
        super().__init__(value)
        self.name = "Decimal"
        self.prefix = "."

    def from_nonstandard(self, data):
        """Function to call to convert other speed formats to this one."""
        if isinstance(data, Percent):
            self.value = data / 100


class Percent(SpeedFormat):
    """Percent."""
    def __init__(self, value: int | float):
        super().__init__(value)
        self.name = "Percent"
        self.prefix = "%"

    def from_standard(self, data):
        """Function to call to convert other speed formats to this one."""
        self.value = data * 100


DEFAULT = 0
SPEED_FORMATS = [Decimal(DEFAULT), Percent(DEFAULT)]
