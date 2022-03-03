"""Title."""


import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e


class Title(w_e.contain.Frame):
    """The title frame."""
    def __init__(self, parent: wec.WidgetExt):
        super().__init__(parent)

        self.w_title = self.Title(self)

        self.w_description = self.Description(self)
        self.w_description.set_grid(coords = (0, 1))


    class Title(w_e.normal.Label):
        """The title itself."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent, text="Fast Edit")
            self.set_font(size_mult=2, bold=True)

    class Description(w_e.normal.Label):
        """The description."""
        def __init__(self, parent: wec.WidgetExt):
            super().__init__(parent, text="A program enabling fast editing. Currently only supports speedup.")
