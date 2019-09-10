import sqlite3


class User():

    def __init__(self, name, username, country, userstats, gamestats):
        self.name = name
        self.username = username
        self.country = country
        self.userstats = userstats
        self.gamestats = gamestats


    def set_id(self, id):
        self.id = id


class DAMPData():

    def __init__(self):
        self.db = sqlite3.connect('DAMPData.db')
