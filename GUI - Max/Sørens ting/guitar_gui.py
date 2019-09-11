from guitar_datalag import GuitarData, Guitar
import tkinter as tk
import tkinter.ttk as ttk

class My_guitar_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = GuitarData()

        self.build_GUI()
        self.update_label()

    def update_label(self):

        l = self.data.get_guitar_list()
        self.lblGuitarer.config(text = 'Der er {} guitarer i databasen'.format(len(l)))
        self.db_view.delete(*self.db_view.get_children())
        for g in l:
            self.db_view.insert("", tk.END, values=(g.navn, g.maerke, g.pris, g.id))

    def on_guitar_selected(self, event):
        curItem = self.db_view.item(self.db_view.focus())['values']
        
        if len(curItem) > 0:
            self.lblCurrentName.config(text = 'Navn: {}'.format(curItem[0]))
            self.lblCurrentMaerke.config(text = 'Mærke: {}'.format(curItem[1]))
            self.lblCurrentPris.config(text = 'Pris: {}'.format(curItem[2]))

    def add_new(self):
        g = Guitar(self.enName.get(), int(self.scPris.scale.get()), self.cbProducenter.get(), 0)
        self.data.add_new_guitar(g)
        self.update_label()

    def delete_current_guitar(self):
        curItem = self.db_view.focus()
        if len(self.db_view.item(curItem)['values']) >= 4:
            self.data.delete_guitar(self.db_view.item(curItem)['values'][3])
        self.update_label()

    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.knap_panel = ttk.Frame(self)
        self.lblGuitarer = ttk.Label(self.knap_panel, text = 'Der er {} guitarer i databasen'.format(None))
        self.lblGuitarer.grid(row = 0, column = 0)
        self.butUpdate = ttk.Button(self.knap_panel, text = 'Opdater', command=self.update_label)
        self.butUpdate.grid(row = 1, column = 0)

        self.lblName = ttk.Label(self.knap_panel, text = 'Navn')
        self.lblName.grid(row = 0, column = 1)
        self.enName = ttk.Entry(self.knap_panel)
        self.enName.grid(row = 0, column = 2)
        self.lblPris = ttk.Label(self.knap_panel, text = 'Pris')
        self.lblPris.grid(row = 1, column = 1)
        self.scPris = ttk.LabeledScale(self.knap_panel, from_ = 0, to = 30000)
        #self.scPris.config(showvalue=1)
        self.scPris.grid(row = 1, column = 2)
        producenter = self.data.get_producent_liste()
        lblProducenter = ttk.Label(self.knap_panel, text = 'Producenter')
        lblProducenter.grid(row = 2, column = 1)
        self.cbProducenter = ttk.Combobox(self.knap_panel, values = producenter)
        self.cbProducenter.grid(row = 2, column = 2)
        self.butNew = ttk.Button(self.knap_panel, text = 'Tilføj ny guitar', command = self.add_new)
        self.butNew.grid(row=3, column=1, columnspan = 2)

        self.lblCurrentName = ttk.Label(self.knap_panel, text = 'Navn: ')
        self.lblCurrentName.grid(row = 0, column = 3)
        self.lblCurrentMaerke = ttk.Label(self.knap_panel, text = 'Mærke: ')
        self.lblCurrentMaerke.grid(row = 1, column = 3)
        self.lblCurrentPris = ttk.Label(self.knap_panel, text = 'Pris: ')
        self.lblCurrentPris.grid(row = 2, column= 3)
        self.butDelete = ttk.Button(self.knap_panel, text = 'Fjern guitar', command = self.delete_current_guitar)
        self.butDelete.grid(row=3, column = 3)

        self.db_view = ttk.Treeview(self.data_panel, column=("column1", "column2", "column3", "column4"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_guitar_selected)
        self.db_view.heading("#1", text="Navn")
        self.db_view.heading("#2", text="Mærke")
        self.db_view.heading("#3", text="Pris")
        self.db_view.heading("#4", text="id")
        self.db_view["displaycolumns"]=("column1", "column2", "column3")
        ysb = ttk.Scrollbar(self.data_panel, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.data_panel.pack(side = tk.TOP)
        self.knap_panel.pack(side = tk.LEFT)
        self.pack()

root = tk.Tk()
root.geometry("600x400")

app = My_guitar_gui(root)
app.master.title('Guitarer')
app.mainloop()
