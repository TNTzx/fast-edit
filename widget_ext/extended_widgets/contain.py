"""Extended container widgets."""


import tkinter as tk

from .. import widget_ext_class as w_e


class Frame(tk.Frame, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtContainer, w_e.ExtFrame):
    """Frame."""

class LabelFrame(tk.Frame, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtContainer, w_e.ExtFrame, w_e.ExtText):
    """Frame, but with a label."""
    