from flask import g, Flask
import sqlite3, hashlib, binascii, os, time

ABS_FILEPATH = os.path.dirname(os.path.abspath(__file__))


class User:
    def __init__(self, username, firstname, lastname, email, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def set_id(self, ID):
        self.id = ID

    def __str__(self):
        return f"""
        username: {self.username}
        email: {self.email}
        password: {self.password}
        rank: {self.rank}"""


class Database:
    def __init__(self):
        self.DATABASE = fr"{ABS_FILEPATH}\main.db"

        # self._create_tables()

    def _get_db(self):
        db = g.get("_database", None)
        if db is None:
            db = g._database = sqlite3.connect(self.DATABASE)
        return db

    def close_connection(self):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    def get_user_id(self, username):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT id FROM userprofiles WHERE username = ?", (username,))
        r = c.fetchone()
        # If the user doesn't exist, the result will be None
        if r is not None:
            return r[0]
        else:
            return None

    def hash_password(self, password):
        # https://www.vitoshacademy.com/hashing-passwords-in-python/
        # Hash a password for storing.
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwdhash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode("ascii")

    def verify_password(self, stored_password, provided_password):
        # Verify a stored password against one provided by user
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac(
            "sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000
        )
        pwdhash = binascii.hexlify(pwdhash).decode("ascii")
        return pwdhash == stored_password

    def login_success(self, username, password):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT password FROM userprofiles WHERE username = ?", (username,))
        r = c.fetchone()
        if r is not None:
            db_pw = r[0]
        else:
            return False
        return self.verify_password(stored_password=db_pw, provided_password=password)

    def check_existing_username(self, username):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT username from userprofiles WHERE username=?", (username,))
        r = c.fetchone()
        if r == None:
            return False
        return True

    def signup_success(self, user: User):
        db = self._get_db()
        c = db.cursor()
        fullname = f"{user.firstname};{user.lastname}"
        if not self.check_existing_username(user.username):
            c.execute(
                "INSERT INTO userprofiles (username, email, password, rank, fullname) VALUES (?, ?, ?, ?, ?)",
                (user.username, user.email, user.password, user.rank, fullname),
            )
            db.commit()
            return True
        return False

    def get_username(self, user_id):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT username FROM userprofiles WHERE id = ?", (user_id,))
        r = c.fetchone()
        # If the user doesn't exist, the result will be None
        if r is not None:
            return r[0]
        else:
            return None

    def get_fullname(self, user_id):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT fullname FROM userprofiles WHERE id = ?", (user_id,))
        r = c.fetchone()
        # If the user doesn't exist, the result will be None
        if r is not None:
            fullname = r[0].replace(";", " ")
            return fullname
        else:
            return None


    def _drop_tables(self):
        db = self._get_db()
        c = db.cursor()

        try:
            c.execute("""DROP TABLE IF EXISTS userprofiles;""")
            c.execute("""DROP TABLE IF EXISTS ranks;""")
            c.execute("""DROP TABLE IF EXISTS help_stats;""")
            c.execute("""DROP TABLE IF EXISTS user_favorites;""")
            c.execute("""DROP TABLE IF EXISTS recents;""")
            c.execute("""DROP TABLE IF EXISTS rooms;""")
            c.execute("""DROP TABLE IF EXISTS room_que;""")
        except Exception as e:
            print(e)
        db.commit()

    def _create_tables(self):
        db = self._get_db()
        c = db.cursor()

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS userprofiles (
                id INTEGER PRIMARY KEY, 
                username TEXT, 
                email TEXT, 
                password TEXT,
                rank INTEGER,
                fullname VARCHAR(128) NOT NULL);"""
            )
        except Exception as e:
            print(e)

        # ? Template to use to alter tables in future----------------------------------------------------------
        # adding fullname to userprofiles table in database
        # try:
        #     c.execute(
        #         """ALTER TABLE userprofiles ADD fullname VARCHAR(128) NOT NULL DEFAULT 'none';"""
        #     )
        # except Exception as e:
        #     print(e)
        # ?----------------------------------------------------------------------------------------

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS ranks (
                id INTEGER PRIMARY KEY,
                rank TEXT);"""
            )

        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS help_stats (
                id INTEGER PRIMARY KEY,
                stat TEXT);"""
            )

        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS user_favorites (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                room_id INTEGER);"""
            )
        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS recents (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                room_id INTEGER,
                timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);"""
            )
        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY,
                room_name INTEGER,
                room_code TEXT,
                creator_id INTEGER);"""
            )
        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS room_que (
                id INTEGER PRIMARY KEY,
                room_id INTEGER,
                user_id INTEGER,
                need_help BIT, 
                help_stat INTEGER,
                timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);"""
            )
            # BIT stores eather 1, 0 or None
        except Exception as e:
            print(e)

        db.commit()

        # Create ranks
        try:
            c.execute(
                """
                INSERT INTO ranks (rank) 
                SELECT "Student"
                WHERE NOT EXISTS (SELECT 1 FROM ranks WHERE rank = "Student");
                """
            )
            c.execute(
                """
                INSERT INTO ranks (rank) 
                SELECT "Teacher"
                WHERE NOT EXISTS (SELECT 1 FROM ranks WHERE rank = "Teacher");
                """
            )
            c.execute(
                """
                INSERT INTO ranks (rank) 
                SELECT "Admin"
                WHERE NOT EXISTS (SELECT 1 FROM ranks WHERE rank = "Admin");
                """
            )
        except Exception as e:
            print(e)

        # Create testing profiles
        pass1 = self.hash_password("1234")

        try:
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, rank, fullname)
                SELECT "user", "andreasgdp@gmail.com", ?, 1, "Andreas;Petersen"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "user" AND email = "andreasgdp@gmail.com" AND rank = 1 AND fullname = "Andreas;Petersen");
                """,
                (pass1,),
            )
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, rank, fullname) 
                SELECT "teacher", "andreasgdp@gmail.com", ?, 2, "Mande;Manden"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "teacher" AND email = "andreasgdp@gmail.com" AND rank = 2 AND fullname = "Mande;Manden");
                """,
                (pass1,),
            )
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, rank, fullname) 
                SELECT "admin", "andreasgdp@gmail.com", ?, 3, "Big;Boss"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "admin" AND email = "andreasgdp@gmail.com" AND rank = 3 AND fullname = "Big;Boss");
                """,
                (pass1,),
            )
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, rank, fullname) 
                SELECT "user2", "andreasgdp@gmail.com", ?, 1, "Anden;Bruger"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "user2" AND email = "andreasgdp@gmail.com" AND rank = 1 AND fullname = "Anden;Bruger");
                """,
                (pass1,),
            )
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, rank, fullname)
                SELECT "kurt", "andreasgdp@gmail.com", ?, 1, "Kurt;Cobain"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "kurt" AND email = "andreasgdp@gmail.com" AND rank = 1 AND fullname = "Kurt;Cobain");
                """,
                (pass1,),
            )
        except Exception as e:
            print(e)

        # Create a testrooms for the test teacher
        try:
            c.execute(
                """
                INSERT INTO rooms (room_name, room_code, creator_id)
                SELECT "test room 1", "SEJKODE1", 2
                WHERE NOT EXISTS (SELECT 1 FROM rooms WHERE room_name = "test room 1" AND room_code = "SEJKODE1" AND creator_id = 2);
                """
            )
            c.execute(
                """
                INSERT INTO rooms (room_name, room_code, creator_id) 
                SELECT "test room 2", "SEJKODE2", 2 
                WHERE NOT EXISTS (SELECT 1 FROM rooms WHERE room_name = "test room 2" AND room_code = "SEJKODE2" AND creator_id = 2);
                """
            )
            c.execute(
                """
                INSERT INTO rooms (room_name, room_code, creator_id) 
                SELECT "test room 3", "SEJKODE3", 2 
                WHERE NOT EXISTS (SELECT 1 FROM rooms WHERE room_name = "test room 3" AND room_code = "SEJKODE3" AND creator_id = 2);
                """
            )
        except Exception as e:
            print(e)

        # Create helpstats
        try:
            c.execute(
                """
                INSERT INTO help_stats (stat) 
                SELECT "Beginning"
                WHERE NOT EXISTS (SELECT 1 FROM help_stats WHERE stat = "Beginning");
                """
            )
            c.execute(
                """
                INSERT INTO help_stats (stat) 
                SELECT "Middle"
                WHERE NOT EXISTS (SELECT 1 FROM help_stats WHERE stat = "Middle");
                """
            )
            c.execute(
                """
                INSERT INTO help_stats (stat) 
                SELECT "Almost done"
                WHERE NOT EXISTS (SELECT 1 FROM help_stats WHERE stat = "Almost done");
                """
            )
        except Exception as e:
            print(e)

        # Create a que for the test user
        try:
            c.execute(
                """
                INSERT INTO room_que (room_id, user_id, need_help, help_stat) 
                SELECT 1, 1, 0, 1
                WHERE NOT EXISTS (SELECT 1 FROM room_que WHERE room_id = 1 AND user_id = 1 AND need_help = 0 AND help_stat = 1);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO room_que (room_id, user_id, need_help, help_stat) 
                SELECT 2, 1, 0, 1
                WHERE NOT EXISTS (SELECT 1 FROM room_que WHERE room_id = 2 AND user_id = 1 AND need_help = 0 AND help_stat = 1);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO room_que (room_id, user_id, need_help, help_stat) 
                SELECT 3, 1, 0, 1
                WHERE NOT EXISTS (SELECT 1 FROM room_que WHERE room_id = 3 AND user_id = 1 AND need_help = 0 AND help_stat = 1);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO room_que (room_id, user_id, need_help, help_stat) 
                SELECT 1, 4, 1, 3
                WHERE NOT EXISTS (SELECT 1 FROM room_que WHERE room_id = 1 AND user_id = 4 AND need_help = 1 AND help_stat = 3);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO room_que (room_id, user_id, need_help, help_stat) 
                SELECT 1, 5, 0, 1
                WHERE NOT EXISTS (SELECT 1 FROM room_que WHERE room_id = 1 AND user_id = 5 AND need_help = 0 AND help_stat = 1);
                """
            )
            time.sleep(1)
        except Exception as e:
            print(e)

        # Create a favorite for the test user
        try:
            c.execute(
                """
                INSERT INTO user_favorites (user_id, room_id)
                SELECT 1, 1
                WHERE NOT EXISTS (SELECT 1 FROM user_favorites WHERE user_id = 1 AND room_id = 1);
                """
            )
            c.execute(
                """
                INSERT INTO user_favorites (user_id, room_id)
                SELECT 1, 2
                WHERE NOT EXISTS (SELECT 1 FROM user_favorites WHERE user_id = 1 AND room_id = 2);
                """
            )
            c.execute(
                """
                INSERT INTO user_favorites (user_id, room_id)
                SELECT 1, 3
                WHERE NOT EXISTS (SELECT 1 FROM user_favorites WHERE user_id = 1 AND room_id = 3);
                """
            )
            c.execute(
                """
                INSERT INTO user_favorites (user_id, room_id)
                SELECT 5, 1
                WHERE NOT EXISTS (SELECT 1 FROM user_favorites WHERE user_id = 5 AND room_id = 1);
                """
            )
        except Exception as e:
            print(e)

        # Create a recent for the test user
        try:
            c.execute(
                """
                INSERT INTO recents (user_id, room_id) 
                SELECT 1, 1
                WHERE NOT EXISTS (SELECT 1 FROM recents WHERE user_id = 1 AND room_id = 1);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO recents (user_id, room_id)
                SELECT 1, 2
                WHERE NOT EXISTS (SELECT 1 FROM recents WHERE user_id = 1 AND room_id = 2);
                """
            )
            time.sleep(1)
            c.execute(
                """
                INSERT INTO recents (user_id, room_id)
                SELECT 1, 3
                WHERE NOT EXISTS (SELECT 1 FROM recents WHERE user_id = 1 AND room_id = 3);
                """
            )
        except Exception as e:
            print(e)

        db.commit()
        print("Database tables created")

    def _update_database_new_data(self):
        db = self._get_db()
        c = db.cursor()
        pass_teach = self.hash_password("OTGLÆRER2020")
        c.execute(
            """
                INSERT INTO userprofiles (username, email, password, rank, fullname)
                SELECT "betalærer", "andreasgdp@gmail.com", ?, 2, "Beta;Lærer"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "teacher" AND email = "andreasgdp@gmail.com" AND rank = 2 AND fullname = "Beta;Lærer");
                """,
            (pass_teach,),
        )
        db.commit()
        print("Database tables updated")


if __name__ == "__main__":
    app = Flask(__name__)
    key = "very secret string"
    app.secret_key = key
    with app.app_context():
        data = HelpData()
        data._drop_tables()
        data._create_tables()
