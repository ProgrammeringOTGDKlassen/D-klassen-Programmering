import sqlite3

class User():
    
    def __init__(selv, first_name: str, last_name: str, username: str, password: str, email: str, last_login: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.last_login = last_login

    def set_id(self, id:):
        self.id = id

    def __str__(self):
        return f'''
        Fist name: {self.first_name}
        Last name: {self.last_name}
        Username: {self.username}
        Password: {self.password}
        Email: {self.email}
        Last time logged in: {self.last_login}
        '''


class Economy_data():
    def __init__(self):
        self.db = sqlite3.connect('economy.db')

    def add_user(self, user: User, date: str):
        c = self.db.cursor()
        date = date
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password, last_login) VALUES (?, ?, ?, ?, ?, ?);""", user.username, user.first_name, user.last_name, user.email, user.password, date)
        userID = c.lastrowid
        self.db.commit()

        return userID

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
                last_login TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS used_economy (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                catagory INTEGER,
                money_spent INTEGER,
                date TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS optained_economy (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                catagory INTEGER,
                money_optained FLOAT,
                date TEXT);""")

            c.execute("""CREATE TABLE IF NOT EXISTS catagory (
                id INTEGER PRIMARY KEY,
                catagory TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS job (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                salary FLOAT,
                payday TEXT );""")