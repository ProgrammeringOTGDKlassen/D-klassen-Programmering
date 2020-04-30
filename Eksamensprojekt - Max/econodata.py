import sqlite3, hashlib, binascii, os

class User():
    
    def __init__(selv, first_name: str, last_name: str, username: str, password: str, email: str, last_login: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.last_login = last_login

    def set_id(self, id):
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
        # self.create_tables()

    def hash_password(self, password):
        # https://www.vitoshacademy.com/hashing-passwords-in-python/
        # Hash a password for storing.
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwdhash = hashlib.pbkdf2_hmac(
            "sha512", 
            password.encode("utf-8"), 
            salt, 
            100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode("ascii")

    def verify_password(self, stored_password, provided_password):
        # Verify a stored password against one provided by user
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac(
            "sha512", 
            provided_password.encode("utf-8"), 
            salt.encode("ascii"), 
            100000)
        pwdhash = binascii.hexlify(pwdhash).decode("ascii")
        return pwdhash == stored_password

    def add_user(self, user: User):
        c = self.db.cursor()
        hashed_password = self.hash_password(user.password)
        c.execute("""INSERT INTO users (
            username, 
            first_name, 
            last_name, 
            email, 
            password) VALUES (?, ?, ?, ?, ?);""", user.username, user.first_name, user.last_name, user.email, user.password)
        userID = c.lastrowid
        self.db.commit()

        return userID

    def create_tables(self):
        c = self.db.cursor()

        try:
            c.execute("""DROP TABLE IF EXISTS users;""")
            c.execute("""DROP TABLE IF EXISTS used_economy;""")
            c.execute("""DROP TABLE IF EXISTS optained_economy;""")
            c.execute("""DROP TABLE IF EXISTS catagory;""")
            c.execute("""DROP TABLE IF EXISTS job;""")
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
                money_optained FLOAT,
                date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);""")

            c.execute("""CREATE TABLE IF NOT EXISTS catagory (
                id INTEGER PRIMARY KEY,
                catagory TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS job (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                salary FLOAT,
                payday TEXT );""")
            
            print('All tables created successfully')
        except Exception as e:
            print(f'Error when creating tables: {e}')

        test_password1 = "DinMor"
        test_password2 = "DinFar"
        test_password1 = self.hash_password(test_password1)
        test_password2 = self.hash_password(test_password2)
        print(test_password1)
        print(len(test_password2))
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester1', 'Jens', 'Tester','jenstester@gmail.com',?);""", (test_password1,))
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester2', 'Tester', 'Jens','testerjens@gmail.com',?);""", (test_password2,))

        self.db.commit()

