"""Module that contains a class of functionable lists."""


import typing as typ


class EventList(list):
    """A list with a callable function when modified."""
    def __init__(self, func: typ.Callable, *args, **kwargs):
        self.func = func
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        super(EventList, self).__setitem__(key, value)
        self.func()

    def __delitem__(self, value):
        super(EventList, self).__delitem__(value)
        self.func()

    def __add__(self, value):
        super(EventList, self).__add__(value)
        self.func()

    def __iadd__(self, value):
        super(EventList, self).__iadd__(value)
        self.func()

    def append(self, value):
        super(EventList, self).append(value)
        self.func()

    def remove(self, value):
        super(EventList, self).remove(value)
        self.func()
