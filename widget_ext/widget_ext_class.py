"""Module that contains the class for widget utilities."""


import tkinter as tk
import tkinter.font as tkf

from matplotlib.widgets import Widget

from . import utils as ul


def quick_wrap(funcs: list):
    """Quickly wraps functions and executes them in order."""
    def wrapper(*args, **kwargs):
        for func in funcs:
            func(*args, **kwargs)
        
    return wrapper


class WidgetExt(tk.Widget):
    """Class for widget extensions."""


class ExtGridable(WidgetExt):
    """Inherited to when widget can be placed on a grid."""
    def __init_subclass__(cls) -> None:
        def init_end(self: ExtGridable, *args, **kwargs):
            self.place_on_grid()
        cls.__init__ = quick_wrap([cls.__init__, init_end])


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
    def __init_subclass__(cls) -> None:
        def init_end(self: ExtContainer, *args, **kwargs):
            self.set_weights()
        cls.__init__ = quick_wrap([cls.__init__, init_end])


    def set_weights(self, x=(1,), y=(1,)):
        """Sets the row and column weights for this widget."""
        for idx, weight in enumerate(x):
            self.columnconfigure(idx, weight=weight)
        for idx, weight in enumerate(y):
            self.rowconfigure(idx, weight=weight)


class ExtWindow(WidgetExt):
    """Inherited to when widget is a window."""
    def __init_subclass__(cls) -> None:
        def init_end(self: ExtWindow, *args, **kwargs):
            self.center_window()
        cls.__init__ = quick_wrap([cls.__init__, init_end])


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
    def __init_subclass__(cls) -> None:
        def init_end(self: ExtText, *args, **kwargs):
            self.set_font()
        cls.__init__ = quick_wrap([cls.__init__, init_end])


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
