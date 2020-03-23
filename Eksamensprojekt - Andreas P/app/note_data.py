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
                "INSERT INTO userprofiles (username, email, password, fullname) VALUES (?, ?, ?, ?)",
                (user.username, user.email, user.password, fullname),
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
            c.execute("""DROP TABLE IF EXISTS classes;""")
            c.execute("""DROP TABLE IF EXISTS notes;""")
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
                fullname VARCHAR(128) NOT NULL);"""
            )
        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY, 
                classname TEXT, 
                img_path TEXT);"""
            )
        except Exception as e:
            print(e)

        try:
            c.execute(
                """CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                user_id INT,
                class_id INT,
                subject TEXT, 
                body TEXT,
                timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);"""
            )
        except Exception as e:
            print(e)

        db.commit()

        # Create testing profiles
        pass1 = self.hash_password("1234")

        try:
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, fullname)
                SELECT "user", "andreasgdp@gmail.com", ?, "Andreas;Petersen"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "user" AND email = "andreasgdp@gmail.com" AND fullname = "Andreas;Petersen");
                """,
                (pass1,),
            )
            c.execute(
                """
                INSERT INTO userprofiles (username, email, password, fullname) 
                SELECT "user2", "mand@gmail.com", ?, "Mande;Manden"
                WHERE NOT EXISTS (SELECT 1 FROM userprofiles WHERE username = "teacher" AND email = "mand@gmail.com" AND fullname = "Mande;Manden");
                """,
                (pass1,),
            )
        except Exception as e:
            print(e)

        # Create testing classes
        try:
            c.execute(
                """
                INSERT INTO classes (classname, img_path) VALUES ("Dansk", "./static/Images/dansk.png");
                """
            )
            c.execute(
                """
                INSERT INTO classes (classname, img_path) VALUES ("Matematik", "./static/Images/matematik.png");
                """
            )
            c.execute(
                """
                INSERT INTO classes (classname, img_path) VALUES ("Byggeri & Energi", "./static/Images/byggeri & energi.png");
                """
            )
        except Exception as e:
            print(e)

        # Create testing notes
        try:
            # ? Dansk
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1, 
                    1, 
                    "Romantikken", 
                    "Romantikkens afgørende dyder er Intuition(For at der rent faktisk er nogen, der går i gang med at finde ud af, hvordan det hele hænger sammen.) og Fantasi (For at kunne tænke ud af boksen og ud over den livskultur, som tidligere var.) Med “det væsentlige er usynligt for øjet” menes der, at man er nødt til at tænke på en anden måde for at kunne finde frem til det væsentlige, hvilket man altså ikke bare kan se med øjet. Det er en åndelig ting, man ikke kan se. Man kan opnå den romantiske universaloplevelse når de skriver/finder på tekster (Den oplevelse, når de sidder og finder på (digter eller andet) og får oplevelsen at være et med alt, i det man skriver). Det er ikke en nødvendighed, at digterne opnår denne universaloplevelse. Romantikken forholder sig også til organismetanken: “En organisme er en helhed, hvor delene kun kan forklares ud fra deres plads og funktion i helheden. Den såkaldte organicisme eller organismetanke går ud på, at ikke kun biologiske væsener, men også"
                    );
                """
            )
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1, 
                    1, 
                    "Romantikken", 
                    "Den såkaldte organicisme eller organismetanke går ud på, at..."
                    );
                """
            )
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1, 
                    1, 
                    "Dokumentar", 
                    "Dokumentaren handler om MKs barndom, hans forældre og..."
                    );
                """
            )
            # ? Matematik
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1, 
                    2, 
                    "Differentialligninger", 
                    "En eller anden tekst om differentialligninger"
                    );
                """
            )
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1, 
                    2, 
                    "Simpel matematik", 
                    "2 + 2 er 4 minus 1 er 3 hurtig matematik 😎"
                    );
                """
            )
            # ? Byggeri & Energi
            c.execute(
                """
                INSERT INTO notes (user_id, class_id, subject, body) VALUES (
                    1,
                    3, 
                    "Dimensionering", 
                    "Det er matematik men i byg"
                    );
                """
            )

        except Exception as e:
            print(e)

        db.commit()
        print("Database tables created")


if __name__ == "__main__":
    app = Flask(__name__)
    key = "very secret string"
    app.secret_key = key
    with app.app_context():
        data = Database()
        data._drop_tables()
        data._create_tables()