"""Main UI frame."""


import widget_ext.widget_ext_class as wec
import widget_ext.extended_widgets as w_e

from . import widgets_main as w_m


class MainFrame(w_e.contain.Frame):
    """Main frame."""
    def __init__(self, parent: wec.WidgetExt):
        super().__init__(parent)


        self.set_weights(y = (1, 1))


        self.title = w_m.title.Title(self)

        self.input_path = w_m.file_manager.FileManagerFrame(self, "Input path:")
        self.input_path.set_grid(coords = (0, 1))
