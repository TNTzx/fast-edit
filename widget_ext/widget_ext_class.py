"""Module that contains the class for widget utilities."""


from __future__ import annotations

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf

from . import utils as ul



def quick_wrap(funcs: list):
    """Quickly wraps functions and executes them in order."""
    def wrapper(*args, **kwargs):
        for func in funcs:
            func(*args, **kwargs)

    return wrapper

class ExecuteInit():
    """Executes the __init__ functions of the classes."""
    def __init_subclass__(cls):
        def end_init(*args, **kwargs):
            for cls_init in cls.__bases__[2:]:
                cls_init.__init__(*args, **kwargs)

        cls.__init__ = quick_wrap([cls.__init__, end_init])



class WidgetExt(tk.Widget):
    """Class for widget extensions."""
    def set_visibility(self, state: bool = True):
        """Makes a widget visible or not."""
        if state:
            self.grid()
        else:
            self.grid_remove()

    def set_status(self, state: bool = True):
        """Enables or disables the widget and its children."""
        configure = {
            "state": tk.NORMAL if state else tk.DISABLED
        }

        def edit_state(widget: WidgetExt):
            children = widget.winfo_children()
            if len(children) > 0:
                for child in children:
                    edit_state(child)
            else:
                if not issubclass(widget.__class__, (tk.Scrollbar, ttk.Progressbar)):
                    widget.configure(**configure)

        edit_state(self)


class ExtGridable(WidgetExt):
    """Inherited to when widget can be placed on a grid."""
    def __init__(self, *args, **kwargs):
        self.set_grid()


    def set_grid(
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
    def __init__(self, *args, **kwargs):
        self.set_weights()


    def set_weights(self, x=(1,), y=(1,)):
        """Sets the row and column weights for this widget."""
        for idx, weight in enumerate(x):
            self.columnconfigure(idx, weight=weight)
        for idx, weight in enumerate(y):
            self.rowconfigure(idx, weight=weight)


class ExtFrame(WidgetExt):
    """Inherited to when widget is a frame."""
    def __init__(self, *args, **kwargs):
        self.configure(**ul.df.FRAME)


class ExtWindow(WidgetExt):
    """Inherited to when widget is a window."""
    def __init__(self, *args, **kwargs):
        self.center_window()


    def set_size(self: tk.Tk | tk.Toplevel, size: tuple[float, float]):
        """Set size of the window."""
        def to_int(num: float):
            return int(round(num))
        self.geometry(f"{to_int(size[0])}x{to_int(size[1])}")

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
    def __init__(self, *args, **kwargs):
        self.set_font()


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


class ExtList(WidgetExt):
    """Inherited to when a widget contains some sort of list."""
    def __init__(self, *args, **kwargs):
        self._list = []

    @property
    def list(self):
        """The list."""
        self.update_from_list()
        return self._list

    def get_selected(self: ExtList | tk.Listbox):
        """Gets the selected items of the ExtList."""
        ...

    def update_from_list(self: tk.Listbox):
        """Update contents."""
        ...
