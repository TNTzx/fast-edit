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
    cls_list: list[RegisteredClass] = []

    @classmethod
    def register_class(cls, registering_class: RegisteredClass):
        """Registers a class into the class list."""
        cls.cls_list.append(registering_class)

    @classmethod
    def get_cls_strs(cls):
        """Get strs of classes."""
        return [reg_class.cls_to_str() for reg_class in cls.cls_list]

    @classmethod
    def get_cls_from_str(cls, str_search: str):
        """Gets the class from a str."""
        for reg_class in cls.cls_list:
            if reg_class.cls_to_str() == str_search:
                return reg_class
        
        raise ValueError(f"Cannot find string {str_search} of class list.")


def bind_to_class_list(class_list: ClassList):
    """Bind a parent class to a class list."""
    def decorator(cls):
        class ParentClass(cls):
            """Parent class."""
            def __init_subclass__(cls) -> None:
                class_list.register_class(cls)

        return ParentClass

    return decorator
