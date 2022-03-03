"""Custom messagebox."""


import typing as typ
import tkinter as tk

import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e


class MsgBox(w_e.window.Window):
    """Represents a message box."""
    def __init__(self, parent: wec.WidgetExt, title: str, description: str, borderless = False):
        super().__init__(parent)
        self.title(title)
        self.focus_set()
        self.overrideredirect(borderless)

        self.set_weights(y = (1, 1))


        self.value = None
        self.buttons: list[w_e.normal.Button] = []


        self.w_parent = parent

        self.w_description = self.Description(self, description)

        self.w_buttons = self.Buttons(self)
        self.w_buttons.place_on_grid(coords = (0, 1))


    class Description(w_e.normal.Label):
        """Description."""
        def __init__(self, parent: wec.WidgetExt, description: str):
            super().__init__(parent, text = description)


    class Buttons(w_e.contain.Frame):
        """Frame for buttons."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent)

        class Button(w_e.normal.Button):
            """Button."""
            def __init__(self, parent: wec.WidgetExt, text: str, command: typ.Callable = None):
                super().__init__(parent, text=text, command=command)
                self.text = text


    def set_value(self, value: str):
        """Sets the value and destroys the message box."""
        self.value = value
        self.destroy()

    def add_button(self, text: str):
        """Adds a button to the message box."""
        button = self.Buttons.Button(self.w_buttons, text, command=lambda: self.set_value(text))
        self.buttons.append(button)

    def show(self):
        """Shows the message box then waits for input."""
        for idx, button in enumerate(self.buttons):
            button.place_on_grid(coords = (idx, 0))

        self.w_buttons.set_weights(x = [1 for _ in self.buttons])

        self.w_parent.set_status(False)
        self.set_status(True)
        self.wait_window()
        self.w_parent.set_status(True)

        return self.value


class Options():
    """Contains the options available."""
    ok = "OK"
    exit = "Exit"

    yes = "Yes"
    no = "No"

    submit = "Submit"
    cancel = "Cancel"


def create_msgbox(parent: wec.WidgetExt, title: str, description: str, options: tuple[str] = (), borderless = False):
    """Shows a messagebox then returns the option."""
    msgbox = MsgBox(parent, title, description, borderless = borderless)
    for option in options:
        msgbox.add_button(option)

    return msgbox.show()
