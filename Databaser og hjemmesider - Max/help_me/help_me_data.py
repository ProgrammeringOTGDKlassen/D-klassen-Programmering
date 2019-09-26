from flask import g
import sqlite3


class HelpData():

    def __init__(self):
        self.DATABASE = 'help_me.db'
        
        self._create_tables()
        
    def _get_db(self):
        db = g.get('_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.DATABASE)
        return db

    def close_connection(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
    
    def get_number_of_students(self):
        c = self.db_get_db().cursor()
        c.execute("SELECT COUNT(rowid) FROM needing_help;")
        val = c.fetchone()
        if val is not None:
            return val[0]
        else:
            return "0"

    #def get_student_list(self, id)

    def register_new_user(self, username, email, password, class_name):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT * FROM userprofiles WHERE username = ? OR email = ?", (username,email))
        r = c.fetchone()
        res = False
        if r is not None:
            res = False
        else:
            c.execute("INSERT INTO userprofiles (username, email, password, class) VALUES (?,?,?,?)",(username, email, password, class))
            db.commit()
            res = True
        return res

    def _create_tables(self):
        db = self._get_db()
        c = db.cursor()
        try:
            c.execute("""CREATE TABLE userprofiles (
                id INTEGER PRIMARY KEY, 
                username TEXT, 
                email TEXT, 
                password TEXT,
                access INTEGER
                class INTEGER
                needs_help BIT);""")
        except Exception as e:
            print(e)

        try:
            c.execute("""CREATE TABLE accesspoint (
                id INTEGER PRIMARY KEY,
                access BIT);""")
            # BIT stores eather 1, 0 or None
        except Exception as e:
            print(e)

        try:
            c.excute("""CREATE TABLE needing_help (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                class INTEGER);""")
        except Exception as e:
            print(e)

        try:
            c.execute("""CREATE TABLE classes (
                id INTEGER PRIMARY KEY,
                class_name TEXT,
                
                
            );""")
        except Exception as e:
            print(e)
        
        db.commit()
        
        print('Database tables created')
