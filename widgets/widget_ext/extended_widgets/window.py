"""Extended window widgets."""


import tkinter as tk

from .. import widget_ext_class as w_e


class Root(tk.Tk, w_e.ExecuteInit, w_e.ExtContainer, w_e.ExtWindow):
    """Root."""

class Window(tk.Toplevel, w_e.ExecuteInit, w_e.ExtContainer, w_e.ExtWindow):
    """Window."""
    