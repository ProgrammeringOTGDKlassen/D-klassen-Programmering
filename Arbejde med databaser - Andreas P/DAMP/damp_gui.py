from damp_datalayer import DAMPData
from loading import loading_screen
import tkinter as tk
import tkinter.ttk as ttk


loading_screen()


class Damp_Gui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass

root = tk.Tk()
# sets the icon top left to e predefined icon
root.iconbitmap(r'C:\Users\andre\OneDrive - Syddansk Erhvervsskole\GitHub\D-klassen-Programmering\Arbejde med databaser - Andreas P\DAMP\Icons\DAMP_ICON.ico')
# defines the default windows size
root.geometry("1280x720")
# starts windows in maximized size
root.state('zoomed')

app = Damp_Gui(root)
app.master.title('DAMP')

app.mainloop()
