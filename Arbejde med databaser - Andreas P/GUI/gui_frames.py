import tkinter as tk

class My_GUI(tk.Frame):


  def __init__(self, master = None):
    tk.Frame.__init__(self, master)

    self.build_GUI()


  def change(self):
    self.lbl_name.config(text = 'Her står der noget nyt tekst.')


  def build_GUI(self):
    self.pack(side = tk.BOTTOM)
    self.v = tk.Frame(self)
    self.h = tk.Frame(self)
    self.ht = tk.Frame(self.h)
    self.hb = tk.Frame(self.h)

    self.v.pack(side = tk.LEFT)
    self.h.pack(side = tk.RIGHT)
    self.ht.pack(side = tk.TOP)
    self.hb.pack(side = tk.BOTTOM)

    for i in range(4):
      b = tk.Button(self.v)
      b.pack(side = tk.TOP)
    for i in range(2):
      b = tk.Button(self.ht)
      b.pack(side = tk.LEFT)
    c = tk.Canvas(self.hb)

app = My_GUI()

app.mainloop()