"""File manager for opening and outputting files."""


import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e


class FileManagerFrame(w_e.contain.Frame):
    """File Manager."""
    def __init__(self, parent: wec.WidgetExt, title: str):
        super().__init__(parent)


        self.w_title = self.Title(self)

        self.w_entry = self.Entry(self)
        self.w_entry.place_on_grid(coords = (1, 0))

        self.w_browse = self.Browse(self)
        self.w_browse.place_on_grid(coords = (2, 0))


    class Title(w_e.normal.Label):
        """Title."""
        def __init__(self, parent: wec.WidgetExt, title: str):
            super().__init__(parent, text=title)
            self.set_font(size_mult = 2, bold = True)

    class Entry(w_e.normal.Entry):
        "Entry box."
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent)

    class Browse(w_e.normal.Button):
        """Browse button."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent, text="Browse...")


    def browse_for_file(self):
        """Asks for a file directory."""

