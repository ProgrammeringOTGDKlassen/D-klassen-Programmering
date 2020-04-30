from econodata import Economy_data
import tkinter as tk
import tkinter.ttk as ttk

class EconomyLoginGui(ttk.Frame):
    pass


class EconomySignupGui(ttk.Frame):
    pass


class EconomyMainGUI(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = Economy_data()
        self.build_GUI()
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.statistics_panel = ttk.Frame(self)
        self.button_panel = ttk.Frame(self)

        self.button_panel.grid_columnconfigure()



root = tk.Tk()
root.geometry('1280x720')
root.state('zoomed')

app = Economy_GUI(root)
app.master.title('Economy')
app.mainloop()
