import sqlite3, hashlib, binascii, os

class User():
    
    def __init__(self, first_name: str, last_name: str, username: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return f'''
        Fist name: {self.first_name}
        Last name: {self.last_name}
        Username: {self.username}
        Email: {self.email}
        Password: {self.password}
        '''


class EconomyData():
    def __init__(self):
        self.db = sqlite3.connect('economy.db')
        self.create_tables()
    
    def check_username(self, username: str):
        c = self.db.cursor()
        c.execute("""SELECT username FROM users;""")
        usernames = c.fetchall()
        print(f'Usernames: {usernames}')
        for u in usernames:
            print(f'U: {u}\n Usernames: {usernames}')
            if username == u[0]:
                return False
            else:
                return True

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
            password) VALUES (?, ?, ?, ?, ?);""", (user.username, user.first_name, user.last_name, user.email, hashed_password))
        self.db.commit()

    def get_userID(self, username: str):
        c = self.db.cursor()
        c.execute("""SELECT id FROM users WHERE username = ?; """, (username,))
        ui = c.fetchone()
        return ui[0]

    def user_login(self, username: str, password: str):
        c = self.db.cursor()
        c.execute("""SELECT password FROM users WHERE username = ?;""", (username,))
        p = c.fetchone()
        if self.verify_password(p[0], password):
            return True
        else:
            return False

    def remove_time(self, datetime):
        datetime = datetime
        date = datetime.split()
        return date[0]

    def get_optained(self, userID):
        userID = userID
        c = self.db.cursor()
        c.execute("""SELECT money_optained, date FROM optained_economy WHERE user_id = ?;""", (userID,))
        optained = c.fetchall()
        print(optained)
        money = 0
        money_date_list = []
        testmoney = 0
        for i in range(0, len(optained)):
            money = optained[i][0]
            date = self.remove_time(optained[i][1])
            money_date = (money, date)
            print(money_date)
            money_date_list.append(money_date)
            print(money_date_list)
        
        
        return money_date_list

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

        test_password1 = "1234"
        test_password2 = "4321"
        test_password1 = self.hash_password(test_password1)
        test_password2 = self.hash_password(test_password2)
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester1', 'Jens', 'Tester','jenstester@gmail.com',?);""", (test_password1,))
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester2', 'Tester', 'Jens','testerjens@gmail.com',?);""", (test_password2,))
        c.execute("""INSERT INTO optained_economy (user_id, catagory, money_optained) VALUES (1, 1, 2000);""")
        c.execute("""INSERT INTO optained_economy (user_id, catagory, money_optained) VALUES (1, 1, 3000);""")
        c.execute("""INSERT INTO catagory (catagory) VALUES ('TEST');""")
        c.execute("""INSERT INTO used_economy (user_id, catagory, money_spent) VALUES (1, 1, 1000);""")

        self.db.commit()

