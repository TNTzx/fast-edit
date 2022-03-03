"""Program that quickly edits your previews."""


import tkinter as tk

import widget_ext.extended_widgets as w_e
import ui


class Main(w_e.window.Root):
    """The main window."""
    def __init__(self):
        super().__init__()
        self.label = self.Label(self)
        self.title = ui.title.Title()
        self.mainloop()



def main():
    """Main."""
    Main()


if __name__ == "__main__":
    main()
