"""Extended normal widgets."""


import tkinter as tk
import tkinter.ttk as ttk

from .. import widget_ext_class as w_e


class Label(tk.Label, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText):
    """Label."""


class Button(tk.Button, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText):
    """Button."""


class Listbox(tk.Listbox, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText, w_e.ExtList):
    """Listbox."""

    def get_selected(self):
        str_items = [self.get(idx) for idx in self.curselection()]
        obj_items = [item for item in self._list if item.__repr__() in str_items]
        return obj_items

    def update_from_list(self):
        self.delete(0, tk.END)
        for item in self._list:
            self.insert(tk.END, item.__repr__())


class Dropdown(ttk.Combobox, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText, w_e.ExtList, w_e.ExtVariabled):
    """Dropdown."""
    def get_selected(self):
        ...

    def update_from_list(self):
        self["values"] = self.list


class Entry(tk.Entry, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText):
    """Entry box."""
