import tkinter as tk
import tkinter.ttk as ttk
from EconomyGui

def loginGui():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width/6)
    height = int(screen_height/6)
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (width/2))
    root.geometry(f'{width}x{height}+{x}+{y}')

    app = EconomyLoginGui(root)
    app.master.title('Economy Login')
    app.mainloop()

def mainGui():
    EconomyLoginGui().master.destroy()
    root = tk.Tk()
    root.geometry('1920x1080')
    root.state('zoomed')
    app = EconomyMainGUI(root)
    app.master.title('Economy logged in')
    app.mainloop()

loginGui()