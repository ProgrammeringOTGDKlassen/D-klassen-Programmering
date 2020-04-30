from econodata import Economy_data
import tkinter as tk
import tkinter.ttk as ttk

class Economy_GUI(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = Economy_data()
        self.build_GUI()
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)

root = tk.Tk()
root.geometry('1280x720')
root.state('zoomed')

app = Economy_GUI(root)
app.master.title('Economy')
app.mainloop()
