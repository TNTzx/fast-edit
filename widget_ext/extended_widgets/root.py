"""Extended Widgets."""


import tkinter as tk

from .. import widget_ext_class as w_e


class ExtRoot(tk.Tk, w_e.ExtContainer, w_e.ExtWindow):
    """Extended Root."""
    