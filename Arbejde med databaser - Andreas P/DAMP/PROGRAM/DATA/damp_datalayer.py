import sqlite3

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


class User():

    def __init__(self, name: str, username: str, country: str, userstats: int, gamestats: int, password: str):
        self.name = name
        self.username = username
        self.country = country
        self.userstats = userstats
        self.gamestats = gamestats
        self.password = password


    def set_id(self, id: int):
        self.id = id


class User():

    def __init__(self, name: str, description: str, icon, gamestats):
        self.name = name
        self.description = description
        self.icon = icon
        self.gamestats = gamestats


    def set_id(self, id: str):
        self.id = id


class DAMPData():

    def __init__(self):
        self.db = sqlite3.connect('./DATA/DAMPData.db')

    
    def add_user(self, user: User):
        pass


    def check_correct_password(self, user: User):
        pass

    
    def create_tables(self):
        try:
            self.db.execute("""DROP TABLE IF EXISTS users;""")
            self.db.execute("""DROP TABLE IF EXISTS games;""")
            self.db.execute("""DROP TABLE IF EXISTS usersStats;""")
            self.db.execute("""DROP TABLE IF EXISTS userLibrary;""")
            self.db.execute("""DROP TABLE IF EXISTS usersGamestats;""")


            print('Table dropped')
        except Exception as e:
            print(f'Error with deletion of tables: {e}')

        try:
            self.db.execute("""CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                password TEXT,
                country TEXT,
                gamesLibrary INTEGER,
                userstats INTEGER,
                gamestats INTEGER);""")

            self.db.execute("""CREATE TABLE games (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                icon TEXT,
                initGamestats INTEGER,);""")

            self.db.execute("""CREATE TABLE usersStats (
                id INTEGER PRIMARY KEY,
                gamesOwned INTEGER,
                activeYears INTEGER);""")
            
            self.db.execute("""CREATE TABLE userLibrary (
                id INTEGER PRIMARY KEY,
                games LIST);""")

            self.db.execute("""CREATE TABLE usersGamestats (
                id INTEGER PRIMARY KEY,
                userID INTEGER,
                gameID INTEGER,
                playtime INTEGER);""")



            print('Tables created')
        except Exception as e:
            print(f'Table already exists: {e}')

        self.db.execute("""INSERT INTO users (name, username, password, country, gamesLibrary, userstats, gamestats) VALUES ('Andreas', 'TheLegend27', '1234', 'Denmark', 1, 1, 1);""")
        self.db.execute("""INSERT INTO users (name, username, password, country, gamesLibrary, userstats, gamestats) VALUES ('Svend', 'Din mor', '4321', 'Denmark', 2, 2, 2);""")

        self.db.execute("""INSERT INTO userLibrary (navn) VALUES ('Wes Montgomery');""")

        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Wes Montgomery');""")
        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Willie Nelson');""")
        self.db.execute("""INSERT INTO guitarister (navn) VALUES ('Tom Morello');""")

        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (1,2);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (2,3);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,2);""")
        self.db.execute("""INSERT INTO guitaristmodeller (guitarist_id, model_id) VALUES (3,4);""")

        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Fender','USA');""")
        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Martin','USA');""")
        self.db.execute("""INSERT INTO producenter (navn, lokation) VALUES ('Gibson','USA');""")


        self.db.commit()
