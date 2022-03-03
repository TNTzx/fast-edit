"""Program that quickly edits your previews."""


import tkinter as tk

import widget_ext.extended_widgets as w_e
import widget_ext.generated_widgets.msgbox as msgbox

import ui


class Main(w_e.window.Root):
    """The main window."""
    def __init__(self):
        super().__init__()
        self.set_size([x / 1.5 for x in (1280, 720)])
        self.center_window()

        # self.w_title = ui.title.Title(self)
        self.button = self.Button(self)


        self.mainloop()

    class Button(w_e.normal.Button):
        """Button???!?!!?"""
        def __init__(self, parent):
            super().__init__(parent, text="A", command=lambda: msgbox.create_msgbox(parent, "A", "AAAA", (msgbox.Options.exit, msgbox.Options.exit)))



def main():
    """Main."""
    Main()


if __name__ == "__main__":
    main()
