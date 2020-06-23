import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

class Telefonbog(tk.Frame):

    def __init__(self, master=None):
        self.db = sqlite3.connect('telefonbog.db')

        tk.Frame.__init__(self, master)

        self.build_GUI()

        #Kald funktionen self.create_db_tables() herunder for at genstarte med en tom database.
        #self.create_db_tables()

        self.update_table()

    def create_db_tables(self):
        c = self.db.cursor()
        self.db.execute("""DROP TABLE IF EXISTS kontakter;""")
        c.execute("""CREATE TABLE kontakter (
            id INTEGER PRIMARY KEY,
            navn TEXT,
            telefonnummer TEXT,
            note TEXT);""")

    def update_table(self):
        self.db_view.delete(*self.db_view.get_children())
        c = self.db.cursor()
        c.execute("""SELECT * FROM kontakter;""")
        for kontakt in c:
            self.db_view.insert("", tk.END, values=(kontakt[1], kontakt[2], kontakt[3], kontakt[0]))


    def find_kontakt(self, navn):
        for k in self.kontakter:
            if k.navn == navn:
                return k
        return None
    
    def edit_kontakt(self):
        
        def edit():
            curKontakt = self.db_view.focus()
            kontakt = self.db_view.item(curKontakt)['values']
            id = kontakt[3]
            c = self.db.cursor()
            c.execute("""UPDATE kontakter SET navn = ?, telefonnummer = ?, note = ? WHERE id = ?;""", (enNavn.get(), enNummer.get(), enNote.get(), id))
            self.db.commit()
            self.update_table()
            dlg.destroy()
            dlg.update()
        
        curKontakt = self.db_view.focus()
        kontakt = self.db_view.item(curKontakt)['values']
        navn = kontakt[0]
        nummer = kontakt[1]
        note = kontakt[2]
        # id = kontakt[3]

        dlg = tk.Toplevel()
        lblNavn = tk.Label(dlg, text="Navn",)
        enNavn = tk.Entry(dlg)
        enNavn.insert(0,navn)
        lblNavn.grid(column=0, row=0)
        enNavn.grid(column=1, row=0)
        lblNummer = tk.Label(dlg, text="Telefonnummer")
        enNummer = tk.Entry(dlg)
        enNummer.insert(0,nummer)
        lblNummer.grid(column=0, row=1)
        enNummer.grid(column=1, row=1)
        lblNote = tk.Label(dlg, text="Note")
        enNote = tk.Entry(dlg)
        enNote.insert(0,note)
        lblNote.grid(column=0, row=2)
        enNote.grid(column=1, row=2)

        butOk = tk.Button(dlg, text="Rediger", command=edit)
        butOk.grid(column=0,row=3)

    def on_select(self, event):
        curKontakt = self.db_view.focus()
        item = self.db_view.item(curKontakt)['values']

        return item
    
    def fjern_kontakt(self):
        def fjern(id):
            c = self.db.cursor()
            #Fjerner kontakten med det givne id.
            c.execute("""DELETE FROM kontakter WHERE id = ?;""", (id,))
            self.db.commit()
        
        #Finder den kontakt som er i fokus af brugeren
        curKontakt = self.db_view.focus()
        #Tjekker at det er en korrekt kontakt man har valgt. Når man tilføjer en kontakt
        #Så er der 4 kolonner i tabellen, men kolonne 4 kan ikke ses.
        if len(self.db_view.item(curKontakt)['values']) >= 4:
            #Kører funktionen fjern, hvor id'et på kontakten sendes med
            fjern(self.db_view.item(curKontakt)['values'][3])
        #Opdaterer tabellen
        self.update_table()

    def tilfoj_kontakt(self):
        def tilfoj():
            c = self.db.cursor()
            c.execute("""INSERT INTO kontakter (navn, telefonnummer, note) VALUES (?,?,?)""",(enNavn.get(), enNummer.get(), enNote.get()))
            self.db.commit()

            self.update_table()
            dlg.destroy()
            dlg.update()

        dlg = tk.Toplevel()
        lblNavn = tk.Label(dlg, text="Navn")
        enNavn = tk.Entry(dlg)
        lblNavn.grid(column=0, row=0)
        enNavn.grid(column=1, row=0)
        lblNummer = tk.Label(dlg, text="Telefonnummer")
        enNummer = tk.Entry(dlg)
        lblNummer.grid(column=0, row=1)
        enNummer.grid(column=1, row=1)
        lblNote = tk.Label(dlg, text="Note")
        enNote = tk.Entry(dlg)
        lblNote.grid(column=0, row=2)
        enNote.grid(column=1, row=2)

        butOk = tk.Button(dlg, text="Tilføj", command=tilfoj)
        butOk.grid(column=0,row=3)


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.db_view = ttk.Treeview(self, column=("column1", "column2", "column3", "column4"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_select)
        self.db_view.heading("#1", text="Navn")
        self.db_view.heading("#2", text="Telefonnummer")
        self.db_view.heading("#3", text="Note")
        self.db_view.heading("#4", text="id")
        self.db_view["displaycolumns"]=("column1", "column2", "column3")
        ysb = ttk.Scrollbar(self, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP)

        self.but_tilfoj = tk.Button(self, text="Tilføj kontakt", command=self.tilfoj_kontakt)
        
        self.but_fjern = tk.Button(self, text="Fjern kontakt", command=self.fjern_kontakt)
        
        self.but_edit = tk.Button(self, text="Rediger kontakt", command = self.edit_kontakt)
       
        self.but_tilfoj.pack(side=tk.TOP)

        self.but_fjern.pack(side=tk.TOP)

        self.but_edit.pack(side=tk.TOP)
app = Telefonbog()
app.mainloop()
