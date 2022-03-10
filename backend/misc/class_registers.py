"""Contains frameworks for creating class registration systems."""


from __future__ import annotations

import abc


class RegisteredClass(abc.ABC):
    """A class to be registered to a ClassList."""
    @classmethod
    @abc.abstractmethod
    def cls_to_str(cls):
        """Turns the class into a string."""


class ClassList():
    """A class list."""
    def __init__(self):
        self.cls_list: list[RegisteredClass] = []
    

    def register_class(self, reg_class: RegisteredClass):
        """Register class."""
        self.cls_list.append(reg_class)


    def get_cls_strs(self):
        """Get strs of classes."""
        return [reg_class.cls_to_str() for reg_class in self.cls_list]

    def get_cls_from_str(self, str_search: str):
        """Gets the class from a str."""
        for reg_class in self.cls_list:
            if reg_class.cls_to_str() == str_search:
                return reg_class

        raise ValueError(f"Cannot find string {str_search} of class list.")
