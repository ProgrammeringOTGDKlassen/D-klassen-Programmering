import sqlite3



class Economy_data():
    def __init__(self):
        self.db = sqlite3.connect('economy.db')
    

    def create_tables():
        c = self.db.cursor()

        try:
            pass
        except Exception as e:
            print(f'Din mor fejlede i at fjerne tabellerne: {e}')

        try:
            c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                password TEXT,
                last_login DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS used_economy (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                catagory INTEGER,
                money_spent INTEGER,
                date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS optained_economy (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                catagory INTEGER,
                money_optained INTEGER,
                date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);""")

            c.execute("""CREATE TABLE IF NOT EXISTS catagory (
                id INTEGER PRIMARY KEY,
                catagory TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS job (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                salary FLOAT,
                payday DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            );""")