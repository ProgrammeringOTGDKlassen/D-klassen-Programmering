import sqlite3
from cryptography.fernet import Fernet

import sys, os


def nav_to_folder_w_file(folder_path: str):
    abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
    file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
    parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
    new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
    sys.path.append(new_path)


# GUI--------------------------------------------------------
nav_to_folder_w_file('GUI')

# ------------------------------------------------------------


# APP---------------------------------------------------------
nav_to_folder_w_file('APP')

# ------------------------------------------------------------


# LOCAL_FOLDER (this folder)----------------------------------
nav_to_folder_w_file('DATA')
import password_manager

class User():

    def __init__(self, name: str, email: str, country: str, username: str, password: str, active_years: int):
        self.name = name
        self.email = email
        self.country = country
        self.username = username
        self.password = password
        self.active_years = active_years


    def set_id(self, id: int):
        self.id = id

    def __str__(self):
        return f'''
        Name: {self.name}
        Username: {self.username}
        Password: {self.password}
        Country: {self.country}
        Active Years: {self.active_years}'''


class Game():

    def __init__(self, name: str, description: str, icon: str, gamestats: int):
        self.name = name
        self.description = description
        self.icon = icon
        self.gamestats = gamestats


    def set_id(self, id: str):
        self.id = id


class DAMPData():

    def __init__(self):
        self.db = sqlite3.connect('./DATA/DAMPData.db')
        self.pass_key = password_manager.read_key()


    def add_user(self, user: User):
        c = self.db.cursor()
        c.execute("""INSERT INTO users (name, email, country, username, password, active_years) VALUES (?, ?, ?, ?, ?, ?);""", (user.name, user.email, user.country, user.username, user.password, user.active_years))
        userID = c.lastrowid
        self.db.commit()

        return userID


    def get_user_from_id(self, id: int):
        c = self.db.cursor()
        c.execute("""SELECT name, email, country, username, password, active_years FROM users WHERE id = ?""", (id,))
        u = c.fetchone()
        user = User(name = u[0], email = u[1], country = u[2], username = u[3], password = u[4], active_years = u[5])
        return user


    def encrypt_password(self, password: str):
        # encode password
        encoded = password.encode()

        # encrypt password
        f = Fernet(self.pass_key)
        encrypted = f.encrypt(encoded)

        return encrypted


    def decrypt_password(self, encrypted_password):
        f = Fernet(self.pass_key)
        decrypted = f.decrypt(encrypted_password)
        decoded = decrypted.decode()
        return decoded



    def create_tables(self):
        try:
            self.db.execute("""DROP TABLE IF EXISTS users;""")
            self.db.execute("""DROP TABLE IF EXISTS userLibrary;""")
            self.db.execute("""DROP TABLE IF EXISTS games;""")


            print('Tables dropped')
        except Exception as e:
            print(f'Error with deletion of tables: {e}')

        try:
            self.db.execute("""CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                country TEXT,
                username TEXT,
                password TEXT,
                active_years INTEGER);""")

            self.db.execute("""CREATE TABLE userLibrary (
                id INTEGER PRIMARY KEY,
                gamesID INTEGER,
                userID INTEGER,
                game_stat_file TEXT);""")

            self.db.execute("""CREATE TABLE games (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                icon TEXT,
                init_gamestats TEXT);""")

            print('Tables created')
        except Exception as e:
            print(f'Table already exists: {e}')

        first_password = '1234'
        second_password = '4321'

        first_password = self.encrypt_password(first_password)
        second_password = self.encrypt_password(second_password)

        self.db.execute("""INSERT INTO users (name, email, country, username, password, active_years) VALUES ('Andreas', 'andreasgdp@gmail.com', 'Denmark', 'TheLegend27', ?, 0);""", (first_password,))
        self.db.execute("""INSERT INTO users (name, email, country, username, password, active_years) VALUES ('Svend', 'din_mor@gmail.com', 'Denmark', 'Din mor', ?, 0);""", (second_password,))

        self.db.execute("""INSERT INTO userLibrary (gamesID, userID, game_stat_file) VALUES (1,1,'./DATA/user_gamestats/userID-1_gamesID-1.json');""")
        self.db.execute("""INSERT INTO userLibrary (gamesID, userID, game_stat_file) VALUES (1,1,'./DATA/user_gamestats/userID-1_gamesID-2.json');""")
        self.db.execute("""INSERT INTO userLibrary (gamesID, userID, game_stat_file) VALUES (1,1,'./DATA/user_gamestats/userID-2_gamesID-1.json');""")
        self.db.execute("""INSERT INTO userLibrary (gamesID, userID, game_stat_file) VALUES (1,1,'./DATA/user_gamestats/userID-2_gamesID-2.json');""")

        self.db.execute("""INSERT INTO games (name, description, icon, init_gamestats) VALUES ('Rocket League','A game with flying rocket cars','rocket_league.ico', './DATA/init_ganestats/rocket_league_init_gamestats.json');""")

        self.db.commit()
