import sqlite3, hashlib, binascii, os, datetime

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
        # self.create_tables()
    
    def check_username(self, username: str):
        c = self.db.cursor()
        c.execute("""SELECT username FROM users;""")
        usernames = c.fetchall()
        for u in usernames:
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
    
    def add_cat(self, catagory: str):
        catagory = catagory
        c = self.db.cursor()
        c.execute("""INSERT INTO catagory (catagory) VALUES (?);""", (catagory,))
        self.db.commit()

    def add_money_obtained(self, userID: str, catagoryID: int, money_obtained: float):
        userID = userID
        catagoryID = catagoryID
        money_obtained = money_obtained
        c = self.db.cursor()
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained) VALUES (?, ?, ?);""", (userID, catagoryID, money_obtained))
        self.db.commit()
        return True

    def add_money_used(self, userID: str, catagoryID: int, money_used: float):
        userID = userID
        catagoryID = catagoryID
        money_used = money_used
        c = self.db.cursor()
        c.execute("""INSERT INTO used_economy (user_id, catagory, money_spent) VALUES (?, ?, ?);""", (userID, catagoryID, money_used))
        self.db.commit()
        return True

    def add_job(self, userID: int, job_name: str, job_salary: float, job_payday: str):
        userID = userID
        job_name = job_name
        job_salary = job_salary
        job_payday = job_payday
        current_date = datetime.date.today()
        next_payment = current_date + datetime.timedelta(days = job_payday)
        c = self.db.cursor()
        c.execute("""INSERT INTO job (user_id, job_name, salary, payday, next_payment) VALUES (?, ?, ?, ?, ?);""", (userID, job_name, job_salary, job_payday, next_payment))
        self.db.commit()
        return True

    def calc_optained(self, userID: int):
        userID = userID
        m = self.get_obtained(userID)
        optained = 0
        for date in m:
            optained += m[date]
        
        return optained

    def calc_used(self, userID: int):
        userID = userID
        m = self.get_obtained(userID)
        used = 0
        for date in m:
            used += m[date]
        
        return used
    
    def calc_current_balance(self, userID):
        optained = self.calc_optained(userID)
        used = self.calc_used(userID)
        balance = optained - used

        return balance
        
    def convert_str_to_date(self, string: str):
        return datetime.datetime.strptime(string, "%Y-%m-%d").date()

    def get_obtained(self, userID):
        userID = userID
        c = self.db.cursor()
        c.execute("""SELECT money_obtained, date FROM obtained_economy WHERE user_id = ?;""", (userID,))
        obtained = c.fetchall()
        obtained_money = 0
        obtained_money_date_dict = {}
        for i in range(0, len(obtained)):
            obtained_money = obtained[i][0]
            date = self.remove_time(obtained[i][1])
            if not date in obtained_money_date_dict:
                obtained_money_date_dict[date] = obtained_money
            else:
                obtained_money_date_dict[date] += obtained_money
        return obtained_money_date_dict
    
    def get_used(self, userID):
        userID = userID
        c = self.db.cursor()
        c.execute("""SELECT money_spent, date FROM used_economy WHERE user_id = ?;""", (userID,))
        used = c.fetchall()
        used_money = 0
        used_money_date_dict = {}
        for i in range(0, len(used)):
            used_money = used[i][0]
            date = self.remove_time(used[i][1])
            if not date in used_money_date_dict:
                used_money_date_dict[date] = used_money
            else:
                used_money_date_dict[date] += used_money
        return used_money_date_dict

    def get_cat_list(self):
        c = self.db.cursor()
        c.execute("""SELECT catagory FROM catagory;""")
        cat_list = []
        for cat in c:
            cat_list.append(cat[0])
        return cat_list

    def get_cat_id(self, catagory: str):
        catagory = catagory
        c = self.db.cursor()
        c.execute("""SELECT id FROM catagory WHERE catagory = ?;""", (catagory,))
        p = c.fetchone()
        return p[0]


    def get_userID(self, username: str):
        c = self.db.cursor()
        c.execute("""SELECT id FROM users WHERE username = ?; """, (username,))
        ui = c.fetchone()
        return ui[0]

    def get_job(self, userID: int):
        userID = userID
        c = self.db.cursor()
        c.execute("""SELECT job_name, salary, payday, next_payment FROM job WHERE user_id = ?;""", (userID,))
        j = c.fetchone()
        return j

    def has_job(self, userID: int):
        userID = userID
        c = self.db.cursor()
        c.execute("""SELECT * FROM job WHERE user_id = ?;""", (userID,))
        if len(c.fetchall()) < 1:
            return False
        else: 
            return True

    def update_date(self, username: str):
        current_date = datetime.date.today()
        userID = self.get_userID(username)
        c = self.db.cursor()
        c.execute("""UPDATE users SET last_login = ? WHERE id = ?;""", (current_date, userID))
        self.db.commit()

    def user_login(self, username: str, password: str):
        c = self.db.cursor()
        c.execute("""SELECT password FROM users WHERE username = ?;""", (username,))
        p = c.fetchone()
        if self.verify_password(p[0], password):
            self.update_date(username)
            return True
        else:
            return False

    def remove_time(self, datetime):
        datetime = datetime
        date = datetime.split()
        return date[0]

    def remove_job(self, userID):
        userID = userID
        c = self.db.cursor()
        c.execute("""DELETE FROM job WHERE user_id = ?;""",(userID,))
        self.db.commit()

    def create_tables(self):
        c = self.db.cursor()

        try:
            c.execute("""DROP TABLE IF EXISTS users;""")
            c.execute("""DROP TABLE IF EXISTS used_economy;""")
            c.execute("""DROP TABLE IF EXISTS obtained_economy;""")
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
            
            c.execute("""CREATE TABLE IF NOT EXISTS obtained_economy (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                catagory INTEGER,
                money_obtained FLOAT,
                date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);""")

            c.execute("""CREATE TABLE IF NOT EXISTS catagory (
                id INTEGER PRIMARY KEY,
                catagory TEXT);""")
            
            c.execute("""CREATE TABLE IF NOT EXISTS job (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                job_name TEXT,
                salary FLOAT,
                payday TEXT, 
                next_payment DATETIME NOT NULL
                );""")
            
            
            print('All tables created successfully')
        except Exception as e:
            print(f'Error when creating tables: {e}')

        test_password1 = "1234"
        test_password2 = "4321"
        test_password1 = self.hash_password(test_password1)
        test_password2 = self.hash_password(test_password2)
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester1', 'Jens', 'Tester','jenstester@gmail.com',?);""", (test_password1,))
        c.execute("""INSERT INTO users (username, first_name, last_name, email, password) VALUES ('Tester2', 'Tester', 'Jens','testerjens@gmail.com',?);""", (test_password2,))
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained) VALUES (1, 1, 2000);""")
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained) VALUES (1, 1, 3000);""")
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained, date) VALUES (1, 1, 3000, '2020-05-02 17:43:04');""")
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained, date) VALUES (1, 1, 4000, '2020-05-02 17:43:04');""")
        c.execute("""INSERT INTO obtained_economy (user_id, catagory, money_obtained, date) VALUES (1, 1, 500, '2020-05-01 17:43:04');""")
        c.execute("""INSERT INTO catagory (catagory) VALUES ('TEST');""")
        c.execute("""INSERT INTO catagory (catagory) VALUES ('HEJ');""")
        c.execute("""INSERT INTO used_economy (user_id, catagory, money_spent) VALUES (1, 1, 1000);""")
        self.db.commit()

