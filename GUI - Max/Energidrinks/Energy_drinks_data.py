import sqlite3

class Energy_drink():
    def __init__(self, name, price, brand, e_type):
        self.name = name
        self.price = price
        self.brand = brand
        self.e_type = e_type

        
    def set_id(self,id):
        self.id = id
        

class Energy_drink_data():
    def __init__(self):
        self.db = sqlite3.connect('energy_drinks.db')

    def get_producer_list(self):
        c = self.db.cursor()
        c.execute('SELECT name, location FROM producers;')
        p_list = []
        for p in c:
            p_list.append((p[0], p[1]))
        return p_list

    def get_energy_drink_list(self):
        c = self.db.cursor()
        c.execute('SELECT d.name, p.name, d.price, dd.types, d.id FROM drinks d INNER JOIN producers p ON d.producers = p.id INNER JOIN drink_types dd ON d.type = dd.id;')
        d_list = []
        for d in c:
            drink = Energy_drink(d[0], d[2], d[1], d[3])
            drink.set_id(d[4])
            d_list.append(drink)
        return d_list

    def delete_drink(self, id):
        c = self.db.cursor()
        c.execute('DELETE FROM drinks WHERE id = ?;', (id,))
        self.db.commit()

    def get_producer_id(self, p):
        c = self.db.cursor()
        c.execute('SELECT id FROM producers WHERE name = ?;', (p.split(' ')[0],))
        p = c.fetchone()
        return p[0]

    def add_new_drink(self, d):
        p = self.get_producer_id(d.brand)
        c = self.db.cursor()
        c.execute('INSERT INTO drinks (name, price, producer, type) VALUES (?, ?, ?, ?);', (d.name, d.price, p, d.type))
        self.db.commit()

    def edit_drink(self, d):
        c = self.db.cursor()
        d_id = d.id
        name, price, producer, e_type = c.execute('SELECT FROM drinks (name, price, producer, type) WHERE id = ?;', (d.id,))
        if name != d.name:
            pass
        if price != d.price:
            pass
        if producer != d.producer:
            pass
    
    def create_tables(self):
        try:
            self.db.execute("""DROP TABLE IF EXISTS drinks;""")
            self.db.execute("""DROP TABLE IF EXISTS producers;""")
            self.db.execute("""DROP TABLE IF EXISTS drink_types;""")

            print('Table deleted')
        except Exception as e:
            print('ERROR while deleting table!')
            print(e)
        
        try:
            self.db.execute("""CREATE TABLE IF NOT EXISTS drinks (id INTEGER PRIMARY KEY, name TEXT, producers INTEGER, price INTEGER, type INTEGER);""")
            self.db.execute("""CREATE TABLE IF NOT EXISTS producers (id INTEGER PRIMARY KEY, name TEXT, location TEXT);""")
            self.db.execute("""CREATE TABLE IF NOT EXISTS drink_types (id INTEGER PRIMARY KEY, types TEXT);""")

            print('Tables created succesfully')
        except Exception as e:
            print('ERROR while creating tables!')
            print(e)
        
        self.db.execute("""INSERT INTO drinks (name, producers, price, type) VALUES (?, ?, ?, ?);""", ('Monster Energy', 1, 20, 1))
        
        self.db.execute("""INSERT INTO producers (name, location) VALUES (?, ?);""", ('Monster Energy', 'USA')) 

        self.db.execute("""INSERT INTO drink_types (types) VALUES (?);""", ("Standard",))

        self.db.commit()