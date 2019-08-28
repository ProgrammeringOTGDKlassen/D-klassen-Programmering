import tkinter as tk

class My_GUI(tk.Frame):

  def __init__(self, master = None):
    tk.Frame.__init__(self, master)

    self.build_GUI()


  def build_GUI(self):
    self.pack(side = tk.BOTTOM)
    self.v  = tk.Frame(self)
    self.h = tk.Frame(self)
    self.agF = tk.Frame(self.h)

    self.v.pack(side = tk.LEFT)
    self.h.pack(side = tk.RIGHT)
    self.agF.pack(side = tk.TOP)

    commands = tk.Label(text = 'COMMANDS FOR DATABASE')
    commands.pack(side = tk.TOP)

    ag = tk.Button(self.v, text = 'Add Guitar')
    ag.pack()
    ag.place(width = 100, height = 100)
    am = tk.Button(self.v, text = 'Add Manufacturer')
    am.pack()
    am.place(width = 100, height = 100)
    ud = tk.Button(self.v, text = 'Update Guitar')
    ud.pack()
    ud.place(width = 100, height = 100)
    dg = tk.Button(self.v, text = 'Delete Guitar')
    dg.pack()
    dg.place(width = 100, height = 100)
    

app = My_GUI()

app.mainloop()