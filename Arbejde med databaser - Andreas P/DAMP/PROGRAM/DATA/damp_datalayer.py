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

    def __init__(self, name, username, country, userstats, gamestats, password):
        self.name = name
        self.username = username
        self.country = country
        self.userstats = userstats
        self.gamestats = gamestats
        self.password = password


    def set_id(self, id):
        self.id = id


class User():

    def __init__(self, name: str, description: str, icon, gamestats):
        self.name = name
        self.description = description
        self.icon = icon
        self.gamestats = gamestats


    def set_id(self, id):
        self.id = id


class DAMPData():

    def __init__(self):
        self.db = sqlite3.connect('DAMPData.db')

    
    def add_user(self, user: User):
        pass


    def check_correct_password(self, user: User):
        pass

    
    def create_tables(self):
        pass
