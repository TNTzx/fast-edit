"""Title."""


from widget_ext.widget_ext_class import WidgetExt as w_e
import widget_ext.extended_widgets as w_e


class Title(w_e.contain.Frame):
    """The title frame."""
    def __init__(self, parent: w_e):
        super().__init__(parent)
    

    class Title(w_e.normal.Label):
        """The title itself."""

        def __init__(self, parent: w_e):
            
