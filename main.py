"""Program that quickly edits your previews."""


import tkinter as tk

import widget_ext.extended_widgets as w_e


class Main(w_e.root.ExtRoot):
    """The main window."""
    def __init__(self):
        super().__init__()
        self.label = self.Label(self)

        self.mainloop()

    class Label(w_e.normal.ExtLabel):
        """Label."""
        def __init__(self, parent: tk.Widget):
            super().__init__(parent, text="AAAAAA")
            self.set_font(size_mult=10)
            self.place_on_grid()



def main():
    """Main."""
    Main()


if __name__ == "__main__":
    main()
