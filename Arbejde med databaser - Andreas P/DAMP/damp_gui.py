from damp_datalayer import DAMPData
from damp_applicationlayer import *
import tkinter as tk
import tkinter.ttk as ttk


loading_screen()


class DampLoginGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass


class DampAddUserGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass


class DampGui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass


root = tk.Tk()
# sets the icon top left to e predefined icon
root.iconbitmap('./Icons/DAMP_ICON.ico')
# defines the default windows size
root.geometry("1280x720")
# starts windows in maximized size
root.state('zoomed')


# defines the app inheriting root as base
app = DampGui(root)
# sets the title of the app
app.master.title('DAMP')
# starts the app
app.mainloop()
