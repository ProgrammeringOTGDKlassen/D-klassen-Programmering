import tkinter as tk


class My_GUI(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.build_GUI()

    def change(self):
        self.lbl_name.config(text = "Her er din mor kommet, AAAAAAAAAAAD!")


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.lbl_name = tk.Label(self, text = 'Her står der jeiner i en label')
        self.but_change = tk.Button(self, text = 'Hej med dig', command = self.change, background = '#DB0000' )
        self.lbl_name.pack(side = tk.TOP)
        self.but_change.pack(side = tk.TOP)

app = My_GUI()

app.mainloop()