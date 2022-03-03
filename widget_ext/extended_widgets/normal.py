"""Extended normal widgets."""


import tkinter as tk

from .. import widget_ext_class as w_e


class Label(tk.Label, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText):
    """Label."""

class Listbox(tk.Listbox, w_e.ExecuteInit, w_e.ExtGridable, w_e.ExtText):
    """Listbox."""

    def get_selected(self, _list: list):
        """Gets the selected items of the listbox. listbox and list must be synced."""
        str_items = [self.get(idx) for idx in self.curselection()]
        obj_items = [item for item in _list if item.__repr__() in str_items]
        return obj_items

    def update_listbox(self, _list: list):
        """Update contents of a listbox using a list."""
        self.delete(0, tk.END)
        for item in _list:
            self.insert(tk.END, item.__repr__())
    