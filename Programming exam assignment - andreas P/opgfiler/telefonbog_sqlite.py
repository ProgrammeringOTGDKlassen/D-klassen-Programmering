import tkinter as tk
import tkinter.ttk as ttk
import sqlite3


class Telefonbog(tk.Frame):
    def __init__(self, master=None):
        self.db = sqlite3.connect("telefonbog.db")

        tk.Frame.__init__(self, master)

        self.selected_element = None
        self.selected_element_id = ""

        self.build_GUI()

        # Kald funktionen self.create_db_tables() herunder for at genstarte med en tom database.
        # self.create_db_tables()

        self.update_table()

    def create_db_tables(self):
        c = self.db.cursor()
        self.db.execute("""DROP TABLE IF EXISTS kontakter;""")
        c.execute(
            """CREATE TABLE kontakter (
            id INTEGER PRIMARY KEY,
            navn TEXT,
            telefonnummer TEXT,
            note TEXT);"""
        )

    def update_table(self):
        self.db_view.delete(*self.db_view.get_children())
        c = self.db.cursor()
        c.execute("""SELECT * FROM kontakter;""")
        for kontakt in c:
            self.db_view.insert(
                "", tk.END, values=(kontakt[1], kontakt[2], kontakt[3], kontakt[0])
            )

    def find_kontakt(self, navn):
        for k in self.kontakter:
            if k.navn == navn:
                return k
        return None

    def on_select(self, event):
        # !Change-------------------------------------------------------------------------------------------------------------------
        print(f"Event {event=}")
        cur_item = self.db_view.focus()
        print(f"Curitem{cur_item=}")
        if not cur_item == "":
            self.selected_element = self.db_view.item(cur_item)
            self.selected_element_id = self.selected_element["values"][3]
            print(f"Focus {self.selected_element=}")
        # !Change-------------------------------------------------------------------------------------------------------------------

    def tilfoj_kontakt(self):
        def tilfoj():
            if not enNavn.get() == '':
                c = self.db.cursor()
                c.execute(
                    """INSERT INTO kontakter (navn, telefonnummer, note) VALUES (?,?,?)""",
                    (enNavn.get(), int(enNummer.get()), enNote.get()),
                )
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
        butOk.grid(column=0, row=3)
    
    # ! Change-------------------------------------------------------------------------------------------------------------------
    def edit_contact(self, contact):
        def edit():
            c = self.db.cursor()
            c.execute(
                """UPDATE kontakter SET navn=?, telefonnummer=?, note=? WHERE id == ?""",
                (enNavn.get(), enNummer.get(), enNote.get(), contact_id),
            )
            self.db.commit()

            self.update_table()
            dlg.destroy()
            dlg.update()
        if not contact == None:
            contact_values = contact["values"]
            contact_id = contact_values[3]
            dlg = tk.Toplevel()
            lblNavn = tk.Label(dlg, text="Navn")
            enNavn = tk.Entry(dlg)
            enNavn.insert(0, contact_values[0])
            lblNavn.grid(column=0, row=0)
            enNavn.grid(column=1, row=0)
            lblNummer = tk.Label(dlg, text="Telefonnummer")
            enNummer = tk.Entry(dlg)
            enNummer.insert(0, contact_values[1])
            lblNummer.grid(column=0, row=1)
            enNummer.grid(column=1, row=1)
            lblNote = tk.Label(dlg, text="Note")
            enNote = tk.Entry(dlg)
            enNote.insert(0, contact_values[2])
            lblNote.grid(column=0, row=2)
            enNote.grid(column=1, row=2)

            butOk = tk.Button(dlg, text="Rediger", command=edit)
            butOk.grid(column=0, row=3)

    def rem_contact(self, contact_id):
        if not contact_id == "":
            c = self.db.cursor()
            c.execute(
                """DELETE FROM kontakter WHERE id == ?""", (contact_id,),
            )
            self.db.commit()

            self.update_table()
    # ! Change-------------------------------------------------------------------------------------------------------------------

    def build_GUI(self):
        self.pack(side=tk.BOTTOM)
        self.db_view = ttk.Treeview(
            self, column=("column1", "column2", "column3", "column4"), show="headings"
        )
        self.db_view.bind("<ButtonRelease-1>", self.on_select)
        self.db_view.heading("#1", text="Navn")
        self.db_view.heading("#2", text="Telefonnummer")
        self.db_view.heading("#3", text="Note")
        self.db_view.heading("#4", text="id")
        self.db_view["displaycolumns"] = ("column1", "column2", "column3")
        ysb = ttk.Scrollbar(self, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side=tk.TOP)

        self.but_tilfoj = tk.Button(
            self, text="Tilføj kontakt", command=self.tilfoj_kontakt
        )
        self.but_tilfoj.pack(side=tk.TOP)
        # !Change-------------------------------------------------------------------------------------------------------------------
        self.but_rem = tk.Button(
            self,
            text="Slet kontakt",
            command=lambda: self.rem_contact(self.selected_element_id),
        )
        self.but_rem.pack(side=tk.TOP)

        self.but_edit = tk.Button(
            self,
            text="Rediger kontakt",
            command=lambda: self.edit_contact(self.selected_element),
        )
        self.but_edit.pack(side=tk.TOP)
        # !Change-------------------------------------------------------------------------------------------------------------------


app = Telefonbog()
app.mainloop()
