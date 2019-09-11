import sqlite3


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
