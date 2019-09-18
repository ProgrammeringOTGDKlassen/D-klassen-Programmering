from Energy_drinks_data import Energy_drink, Energy_drink_data
import tkinter as tk
import tkinter.ttk as ttk
class Energy_drink_gui(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = Energy_drink_data()
        self.build_GUI()
        self.update_label()

    def update_label(self):
        l = self.data.get_energy_drink_list()
        self.drinks_label.config(text = 'Der er {} registrede energidrikke i databasen'.format(len(l)))
        self.db_view.delete(*self.db_view.get_children())
        for e in l:
            self.db_view.insert("", tk.END, values = (e.name, e.brand, e.price, e.e_type, e.id))
        
    def on_drink_selected(self, event):
        cur_item = self.db_view.item(self.db_view.focus())['values']
        if len(cur_item) > 0:
            self.label_current_name.config(text = 'Navn: {}'.format(cur_item[0]))
            self.label_current_producer.config(text = 'Producent: {}'.format(cur_item[1]))
            self.label_current_price.config(text = 'Pris: {}'.format(cur_item[2]))
            self.label_current_type.config(text = 'Type: {}'.format(cur_item[3]))

    def clear_drink_entry(self):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.cb_producers.set('')
        self.cb_type.set('')

    def clear_producer_entry(self):
        self.entry_producer_name.delete(0, tk.END)
        self.entry_producer_location.delete(0, tk.END)
    
    def clear_current_drink_label(self):
        self.label_current_name = ttk.Label(self.button_panel, text = 'Navn: ')
        self.label_current_name.grid(row = 0, column = 3)
        self.label_current_producer = ttk.Label(self.button_panel, text = 'Producent: ')
        self.label_current_producer.grid(row = 1, column = 3)
        self.label_current_price = ttk.Label(self.button_panel, text = 'Pris: ')
        self.label_current_price.grid(row = 2, column = 3)
        self.label_current_type = ttk.Label(self.button_panel, text = 'Type: ')
        self.label_current_type.grid(row = 3, column = 3)

    def add_new_drink(self):
        e = Energy_drink(self.entry_name.get(), int(self.entry_price.get()), self.cb_producers.get(), self.cb_type.get())
        self.data.add_new_drink(e)
        self.update_label()
        self.clear_drink_entry()

    def add_new_producer(self):
        self.data.add_new_producer(self.entry_producer_name.get(), self.entry_producer_location.get())
        producers = self.data.get_producer_list()
        self.cb_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_producers.grid(row = 2, column = 2, pady = (0,5))
        self.cb_delete_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_delete_producers.grid(row = 9, column = 2)
        self.clear_producer_entry()

    def delete_current_drink(self):
        cur_item = self.db_view.focus()
        if len(self.db_view.item(cur_item)['values']) >=4:
            self.data.delete_drink(self.db_view.item(cur_item)['values'][4])
        self.update_label()
        self.clear_current_drink_label()

    def delete_producer(self):
        self.data.delete_producer(self.cb_delete_producers.get())
        self.update_label()
        producers = self.data.get_producer_list()
        self.cb_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_producers.grid(row = 2, column = 2, pady = (0,5))
        self.cb_delete_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_delete_producers.grid(row = 9, column = 2)
        self.cb_delete_producers.set('')
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.button_panel = ttk.Frame(self)

        self.button_panel.grid_columnconfigure(3, minsize = 200)
        self.drinks_label = ttk.Label(self.button_panel, text = 'Der er {} registrede energidrikke i databasen'.format(None))
        self.drinks_label.grid(row = 0, column = 0)
        self.button_update = ttk.Button(self.button_panel, text = 'Opdater', command = self.update_label)
        self.button_update.grid(row = 1, column = 0)

        self.label_name = ttk.Label(self.button_panel, text = 'Navn')
        self.label_name.grid(row = 0, column = 1)
        self.entry_name = ttk.Entry(self.button_panel, width = 23)
        self.entry_name.grid(row = 0, column = 2, pady = (0,5))
        self.label_price = ttk.Label(self.button_panel, text = 'Pris')
        self.label_price.grid(row = 1, column = 1)
        self.entry_price = ttk.Entry(self.button_panel, width = 23)
        self.entry_price.grid(row = 1, column = 2, pady = (0,5))
        producers = self.data.get_producer_list()
        label_producers = ttk.Label(self.button_panel, text = 'Producenter')
        label_producers.grid(row = 2, column = 1)
        self.cb_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_producers.grid(row = 2, column = 2, pady = (0,5))
        types = self.data.get_type_list()
        label_type = ttk.Label(self.button_panel, text = 'Type')
        label_type.grid(row = 3, column = 1)
        self.cb_type = ttk.Combobox(self.button_panel, values = types, state = 'readonly') 
        self.cb_type.grid(row = 3, column = 2, pady = (0,5))
        self.button_add = ttk.Button(self.button_panel, text = 'Tilføj energidrik', command = self.add_new_drink)
        self.button_add.grid(row = 4, column = 2, pady = (0,10))

        self.label_producer_name = ttk.Label(self.button_panel, text = 'Producentens navn')
        self.label_producer_name.grid(row = 6, column = 1)
        self.entry_producer_name = ttk.Entry(self.button_panel, width = 23)
        self.entry_producer_name.grid(row = 6, column = 2, pady = (0,5))
        self.label_producer_location = ttk.Label(self.button_panel, text = 'Producentens lokation')
        self.label_producer_location.grid(row = 7, column = 1, padx = (0,17))
        self.entry_producer_location = ttk.Entry(self.button_panel, width = 23)
        self.entry_producer_location.grid(row = 7, column = 2, pady = (0,5))
        self.button_add_producer = ttk.Button(self.button_panel, text = 'Tilføj producent', command = self.add_new_producer)
        self.button_add_producer.grid(row = 8, column = 2, pady = (0,20))
        
        self.label_current_name = ttk.Label(self.button_panel, text = 'Navn: ')
        self.label_current_name.grid(row = 0, column = 3)
        self.label_current_producer = ttk.Label(self.button_panel, text = 'Producent: ')
        self.label_current_producer.grid(row = 1, column = 3)
        self.label_current_price = ttk.Label(self.button_panel, text = 'Pris: ')
        self.label_current_price.grid(row = 2, column = 3)
        self.label_current_type = ttk.Label(self.button_panel, text = 'Type: ')
        self.label_current_type.grid(row = 3, column = 3)
        self.button_delete = ttk.Button(self.button_panel, text = 'Fjern energidrik', command = self.delete_current_drink)
        self.button_delete.grid(row = 4, column = 3)

        self.label_producer = ttk.Label(self.button_panel, text = 'Producent')
        self.label_producer.grid(row = 9, column = 1)
        self.cb_delete_producers = ttk.Combobox(self.button_panel, values = producers, state = 'readonly')
        self.cb_delete_producers.grid(row = 9, column = 2)
        self.button_delete_producer = ttk.Button(self.button_panel, text = 'Fjern producent', command = self.delete_producer)
        self.button_delete_producer.grid(row = 10, column = 2)

        self.db_view = ttk.Treeview(self.data_panel, column = ('column1', 'column2', 'column3', 'column4', 'column5'), show = 'headings', height = 49)
        self.db_view.bind("<ButtonRelease-1>", self.on_drink_selected)
        self.db_view.heading('#1', text = 'Navn')
        self.db_view.heading('#2', text = 'Producent')
        self.db_view.heading('#3', text = 'Pris')
        self.db_view.heading('#4', text = 'Type')
        self.db_view.heading('#5', text = 'id')
        self.db_view['displaycolumns'] = ('column1', 'column2', 'column3', 'column4')
        scroll_bar_y = ttk.Scrollbar(self.data_panel, command = self.db_view.yview, orient = tk.VERTICAL)
        self.db_view.configure(yscrollcommand = scroll_bar_y.set)
        self.db_view.pack(side = tk.RIGHT)
        self.data_panel.pack(side = tk.RIGHT)
        self.button_panel.pack(side = tk.TOP)
        self.pack()

root = tk.Tk()
root.iconbitmap('./Icon/icon_AQK_icon.ico')
root.geometry('1280x720')
root.state('zoomed')

app = Energy_drink_gui(root)
app.master.title('Energidrikke')
app.mainloop()