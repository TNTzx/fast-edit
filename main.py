"""Program that quickly edits your previews."""


import tkinter as tk

import widget_ext.widget_ext_class as w_e


class Main(tk.Tk, w_e.WidgetExt):
    """The main window."""
    def __init__(self):
        super().__init__()
        self.label = self.Label(self)

        self.mainloop()

    class Label(tk.Label, w_e.WidgetExt):
        """Label."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, text="AAAAAA")
            self.set_font(size_mult=10)



def main():
    """Main."""
    Main()


if __name__ == "__main__":
    main()