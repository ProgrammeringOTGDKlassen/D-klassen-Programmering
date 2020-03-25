import sqlite3



class Economy_data():
    def __init__(self):
        self.db = sqlite3.connect('economy.db')
    
