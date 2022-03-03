"""Module that contains the class for widget utilities."""


import tkinter as tk
import tkinter.font as tkf

from matplotlib.widgets import Widget

from . import utils as ul


class WidgetExt(tk.Widget):
    """Class for widget extensions."""
    def __init__(self, master, widgetName, cnf=..., kw=..., extra=...) -> None:
        super().__init__(master, widgetName, cnf, kw, extra)
        self.place_on_grid()


    def place_on_grid(
            self,
            coords = (0, 0),
            span_set = (1, 1), ipad_set = (0, 0), pad_set = ul.df.PAD_SET,
            sticks = ("N", "S", "E", "W")
        ):
        """Places a widget on a grid."""
        self.grid(
            column = coords[0],
            row = coords[1],
            columnspan = span_set[0],
            rowspan = span_set[1],
            ipadx = ipad_set[0],
            ipady = ipad_set[1],
            padx = pad_set[0],
            pady = pad_set[1],
            sticky = "".join(sticks)
        )


class ExtContainer(WidgetExt):
    """Inherited to when widget is a container."""
    def set_weights(self, x=(1,), y=(1,)):
        """Sets the row and column weights for this widget."""
        for idx, weight in enumerate(x):
            self.columnconfigure(idx, weight=weight)
        for idx, weight in enumerate(y):
            self.rowconfigure(idx, weight=weight)


class ExtWindow(WidgetExt):
    """Inherited to when widget is a window."""
    def __init__(self, master, widgetName, cnf=..., kw=..., extra=...) -> None:
        super().__init__(master, widgetName, cnf, kw, extra)
        self.center_window()


    def set_size(self: tk.Tk | tk.Toplevel, size: tuple[float, float]):
        """Set size of the window."""
        self.geometry(f"{size[0]}x{size[1]}")

    def center_window(self: tk.Tk | tk.Toplevel):
        """Center the window to the screen."""
        self.update_idletasks()

        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width

        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = round(self.winfo_screenwidth() / 2 - win_width / 2)
        y = round(self.winfo_screenheight() / 2 - win_height / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")


class ExtText(WidgetExt):
    """Inherited to when widget contains text."""
    def set_font(
        self,
        family=ul.df.FONT_FAMILY, size_mult=1,
        bold=False, italic=False, underline=False, overline=False
    ):
        """Sets the font of this widget."""
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
