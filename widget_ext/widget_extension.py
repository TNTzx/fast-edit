"""Module that contains the class for widget utilities."""


import tkinter as tk
import tkinter.font as tkf

from . import utils as ul


class WidgetExt(tk.Widget):
    """Class for widget extensions."""
    def __init__(self, master, widgetName, cnf=..., kw=..., extra=...) -> None:
        super().__init__(master, widgetName, cnf, kw, extra)


    def set_font(
            self,
            family=ul.df.FONT_FAMILY,
            size_mult=1,
            bold=False, italic=False, underline=False, overline=False
        ):
        """Sets the font of the widget."""
        self.configure(
            font = tkf.Font(
                family = family,
                size = ul.df.FONT_SIZE_BASE * size_mult,
                weight = "bold" if bold else "normal",
                slant = "italic" if italic else "roman",
                underline = underline,
                overstrike = overline
            )
        )
