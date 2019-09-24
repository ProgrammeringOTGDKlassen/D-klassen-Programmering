from flask import g
import sqlite3

import hashlib, binascii, os

class IdeaData():

    def __init__(self):
        self.DATABASE = 'ideahouse.db'

        self._create_db_tables()


    def _get_db(self):
        db = g.get('_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.DATABASE)
        return db


    def close_connection(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def hash_password(self, password):
        # Hash a password for storing.
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        # Verify a stored password against one provided by user
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                        provided_password.encode('utf-8'), 
                                        salt.encode('ascii'), 
                                        100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def get_number_of_ideas(self):
        c = self._get_db().cursor()
        c.execute("SELECT COUNT(rowid) FROM Ideas;")
        val = c.fetchone()
        if val is not None:
            return val[0]
        else:
            return None


    def get_idea_list(self, id):
        db = self._get_db()
        c = db.cursor()
        c.execute("""SELECT idea from Ideas WHERE userid = ?""",(id,))
        idea_list = []
        for i in c:
            idea_list.append(i[0])
        return idea_list


    def register_new_idea(self, idea, id):
        db = self._get_db()
        c = db.cursor()
        c.execute("""INSERT INTO Ideas (idea, userid) VALUES (?, ?);""",(idea, id))
        db().commit()


    def get_user_id(self, s):
        c = self._get_db().cursor()
        c.execute("SELECT id FROM UserProfiles WHERE username = ?", (s,))
        r = c.fetchone()
        #If the user doesn't exist, the result will be None
        if r is not None:
            return r[0]
        else:
            return None


    def register_user(self, user, password, email):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT * from UserProfiles WHERE username = ? OR email = ?", (user,email))
        r = c.fetchone()
        res = False
        if r is not None:
            #The username og email is already in use
            res = False
        else:
            c.execute("INSERT INTO UserProfiles (username, password, email) VALUES (?,?,?)", (user, password, email))
            db.commit()
            res = True
        return res


    def get_user_list(self):
        l = []
        c = self._get_db().cursor()
        c.execute('SELECT * FROM UserProfiles;')
        for u in c:
            l.append("Navn: {}, email: {}, pw: {}".format(u[1],u[2],u[3]))
        return l


    def login_success(self, user, password):
        c = self._get_db().cursor()
        c.execute("SELECT password FROM UserProfiles WHERE username = ?", (user,))
        r = c.fetchone()
        if r is not None:
            db_pw = r[0]
        else:
            return False
        return self.verify_password(stored_password = db_pw, provided_password = password)


    def _create_db_tables(self):
        db = self._get_db()
        c = db.cursor()
        try:
            c.execute("""CREATE TABLE UserProfiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                password TEXT);""")
        except Exception as e:
            print(e)

        try:
            c.execute("""CREATE TABLE Ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userid INTEGER,
                idea TEXT);""")
        except Exception as e:
            print(e)

        db.commit()
        return 'Database tables created'
