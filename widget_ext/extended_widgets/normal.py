"""Extended Widgets."""


import tkinter as tk

from .. import widget_ext_class as w_e


class ExtLabel(tk.Label, w_e.ExtText, w_e.ExtGridable):
    """Extended Label."""

    