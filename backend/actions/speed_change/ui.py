"""The UI shown for speed changes."""


import tkinter as tk

import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e

from . import formats as frm
from . import modes


class SpeedChange(w_e.window.Window):
    """The Speed Change window."""
    def __init__(self, parent: wec.WidgetExt):
        super().__init__(parent)
        self.set_size([x / 1.5 for x in (1280, 720)])
        self.center_window()


        self.w_frame = self.Frame(self)

    class Frame(w_e.contain.Frame):
        """The main frame."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent)
            self.set_weights(y = (1, 1))

            self.w_start_speed = generate_speed_definition(self, "Starting speed")
            self.w_start_speed.set_grid(coords = (0, 1))
        
        class Title(w_e.contain.Frame):
            """The title."""
            def __init__(self, parent: wec.WidgetExt):
                super().__init__(parent)

            class Text(w_e.normal.Label):
                """Title text."""
                def __init__(self, parent: wec.WidgetExt):
                    super().__init__(parent, text = "Speed Change")
                    self.set_font(size_mult = 3, bold = True)

        class Parameters(w_e.contain.Frame):
            """Parameters."""
            def __init__(self, parent: wec.WidgetExt):
                super().__init__(parent)


                self.w_select_type = self.SelectType(self)

            class SelectType(w_e.contain.Frame):
                """Select the type of conversion."""
                def __init__(self, parent: wec.WidgetExt):
                    super().__init__(parent)


                    self.w_title = self.Title(self)

                class Title(w_e.normal.Label):
                    """Title text."""
                    def __init__(self, parent: wec.WidgetExt):
                        super().__init__(parent, text = "Select Mode")
                        self.set_font(size_mult = 2, bold = True)

                class Dropdown(w_e.normal.Dropdown):
                    """The dropdown."""
                    def __init__(self, parent: wec.WidgetExt):
                        self.variable = tk.StringVar
                        super().__init__(parent, textvariable = self.variable)

                        [self.list.append(speed_mode()) for speed_mode in modes.SpeedModes.speed_modes]


def generate_speed_definition(parent: wec.WidgetExt, title: str):
    """Generates the UI for a speed definition."""
    class SpeedDefinition(w_e.contain.Frame):
        """Contains a speed definition."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent)
            self.set_weights(x = (1, 3))


            self.w_title = self.Title(self)

            self.w_input_frame = self.InputFrame(self)
            self.w_input_frame.set_grid(coords = (1, 0))

        class Title(w_e.normal.Label):
            """Title."""
            def __init__(self, parent: wec.WidgetExt):
                super().__init__(parent, text = title)

        class InputFrame(w_e.contain.Frame):
            """Frame for inputting stuff."""
            def __init__(self, parent: wec.WidgetExt):
                super().__init__(parent)
                self.set_weights(x = (1, 3))


                self.w_entry = self.Entry(self)

                self.w_formats = self.Formats(self)
                self.w_formats.set_grid(coords = (1, 0))

            class Entry(w_e.normal.Entry):
                """The entry box."""
                def __init__(self, parent: wec.WidgetExt):
                    self.variable = tk.StringVar()
                    super().__init__(parent, textvariable = self.variable)

            class Formats(w_e.normal.Dropdown):
                """The dropdown to select the formats."""
                def __init__(self, parent: wec.WidgetExt):
                    self.variable = tk.StringVar()
                    super().__init__(parent, self.variable)


    return SpeedDefinition(parent)
