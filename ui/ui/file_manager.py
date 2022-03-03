"""File manager for opening and outputting files."""


import tkinter as tk
import tkinter.filedialog as tkfd

import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e


class FileManagerFrame(w_e.contain.Frame):
    """File Manager."""
    def __init__(self, parent: wec.WidgetExt, title: str):
        super().__init__(parent)


        self.w_title = self.Title(self, title)

        self.w_entry = self.Entry(self)
        self.w_entry.place_on_grid(coords = (1, 0))

        self.w_browse = self.Browse(self)
        self.w_browse.place_on_grid(coords = (2, 0))
        self.w_browse.configure(command = self.browse_for_file)


    class Title(w_e.normal.Label):
        """Title."""
        def __init__(self, parent: wec.WidgetExt, title: str):
            super().__init__(parent, text=title)
            self.set_font(size_mult = 2, bold = True)

    class Entry(w_e.normal.Entry):
        "Entry box."
        def __init__(self, parent: wec.WidgetExt):
            self.variable = tk.StringVar()
            super().__init__(parent, textvariable = self.variable)

    class Browse(w_e.normal.Button):
        """Browse button."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent, text="Browse...")


    def browse_for_file(self, default_file_name: str = ""):
        """Asks for a file directory."""
        file_path = tkfd.asksaveasfilename(
            parent = self,
            initialfile = default_file_name,
            filetypes = [("All Files", ".*")] + [("mp4", ".mp4")]
        )

        self.w_entry.variable.set(file_path)
