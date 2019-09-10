import sqlite3


class Guitar():
    def __init__(self, navn, pris, maerke, aarstal):
        self.navn = navn
        self.pris = pris
        self.maerke = maerke
        self.aarstal = aarstal

    def set_id(self, id):
        self.id = id

class GuitarData():

    def __init__(self):
        self.db = sqlite3.connect('guitarer.db')


    def get_producent_liste(self):
        c = self.db.cursor()
        c.execute('SELECT navn, lokation FROM producenter;')
        p_liste = []
        for p in c:
            p_liste.append((p[0], p[1]))
        return p_liste

    def get_guitar_list(self):
        c = self.db.cursor()
        c.execute('SELECT gm.navn, p.navn, gm.pris, gm.årstal, gm.id FROM guitarmodeller gm INNER JOIN producenter p ON gm.producent = p.id;')
        g_liste = []
        for g in c:
            guitar = Guitar(g[0],g[2],g[1],g[3])
            guitar.set_id(g[4])
            g_liste.append(guitar)
        return g_liste

    def delete_guitar(self, id):
        c = self.db.cursor()
        c.execute('DELETE FROM guitarmodeller WHERE id = ?;', (id,))
        self.db.commit()

    def get_producent_id(self, p):
        c = self.db.cursor()
        c.execute('SELECT id FROM producenter WHERE navn = ?', (p.split(' ')[0],))
        p = c.fetchone()
        return p[0]

    def add_new_guitar(self, g):
        p = self.get_producent_id(g.maerke)
        c = self.db.cursor()
        c.execute('INSERT INTO guitarmodeller (navn, pris, producent) VALUES (?,?,?);',(g.navn, g.pris, p))
        self.db.commit()
    
    def edit_guitar(self, g):
        c = self.db.cursor()
        g_id = g.id

        navn, pris, producent, årstal = c.execute('SELECT FROM guitarmodeller (navn, pris, producent, årstal) WHERE id = ?', (g_id,))

        if navn != g.navn:
            pass

        if pris != g.pris:
            pass

        if producent != g.producent:
            pass

        if årstal != g.årstal:
            pass

    def create_tables(self):
        try:
            self.db.execute("""DROP TABLE IF EXISTS guitarmodeller;""")
            self.db.execute("""DROP TABLE IF EXISTS guitarister;""")
            self.db.execute("""DROP TABLE IF EXISTS guitaristmodeller;""")
            self.db.execute("""DROP TABLE IF EXISTS producenter;""")

            print('Tabel slettet')
        except Exception as e:
            print('Fejl ved sletning af tabel')

        try:
            self.db.execute("""CREATE TABLE guitarmodeller (
        		id INTEGER PRIMARY KEY,
        		navn TEXT,
                producent INT,
                pris INT,
                årstal INTEGER);""")

            self.db.execute("""CREATE TABLE guitarister (
        		id INTEGER PRIMARY KEY,
        		navn TEXT);""")

            self.db.execute("""CREATE TABLE guitaristmodeller (
        		id INTEGER PRIMARY KEY,
        		guitarist_id INTEGER,
                model_id INTEGER,
                pris INTEGER);""")

            self.db.execute("""CREATE TABLE producenter (
        		id INTEGER PRIMARY KEY,
        		navn TEXT,
                lokation TEXT);""")



            print('Tabel oprettet')
        except Exception as e:
            print('Tabellen findes allerede')

        self.db.execute("""INSERT INTO guitarmodeller (navn, producent, årstal, pris) VALUES ('Stratocaster', 1, '1954', 6999);""")
        self.db.execute("""INSERT INTO guitarmodeller (navn, producent, årstal, pris) VALUES ('ES-335', 3, '1954', 23000);""")
        self.db.execute("""INSERT INTO guitarmodeller (navn, producent, årstal, pris) VALUES ('N-20', 2, '1969', 12000);""")
        self.db.execute("""INSERT INTO guitarmodeller (navn, producent, årstal, pris) VALUES ('Telecaster', 1, '1950', 8000);""")

        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Wes Montgomery');""")
        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Willie Nelson');""")
        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Tom Morello');""")

        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (1,2);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (2,3);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,2);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,4);""")

        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Fender','USA');""")
        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Martin','USA');""")
        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Gibson','USA');""")

        #Efter at have ændret i databasen skal man kalde funktionen commit.
        self.db.commit()
