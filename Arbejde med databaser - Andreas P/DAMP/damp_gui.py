from damp_datalayer import DAMPData
import tkinter as tk
import tkinter.ttk as ttk



class Damp_Gui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass

root = tk.Tk()
# defines the default windows size
root.geometry("1280x720")
# starts windows in maximized size
root.state('zoomed')

app = Damp_Gui(root)
app.master.title('DAMP')

app.mainloop()
