import tkinter as tk


class My_GUI(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.build_GUI()

    def change(self):
        self.lbl_name.config(text = "Her er din mor kommet, AAAAAAAAAAAD!")


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.V = tk.Frame(self)
        self.H = tk.Frame(self)
        self.HT = tk.Frame(self.H)
        self.HB = tk.Frame(self.H)

        self.V.pack(side = tk.LEFT)
        self.H.pack(side = tk.RIGHT)
        self.HT.pack(side = tk.TOP)
        self.HB.pack(side = tk.BOTTOM)

        for i in range(4):
            b = tk.Button(self.V, text = 'Du er fucking grim luder')
            b.pack(side = tk.TOP)
        
        for i in range(2):
            b = tk.Button(self.HT, text = 'hej med dig, hej med dig, hej')
            b.pack(side = tk.TOP)

        c = tk.Canvas(self.HB, width = 500, height = 500)
        # self.lbl_name = tk.Label(self, text = 'Her står der jeiner i en label')
        # self.but_change = tk.Button(self, text = 'Hej med dig', command = self.change, background = '#DB0000' )
        # self.lbl_name.pack(side = tk.TOP)
        # self.but_change.pack(side = tk.TOP)

app = My_GUI()

app.mainloop()