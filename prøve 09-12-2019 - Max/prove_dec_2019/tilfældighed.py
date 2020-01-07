from flask import Flask
from flask import render_template
from flask import g
import sqlite3
import random

app = Flask(__name__)

def _get_db():
    db = g.get('_database', None)
    if db is None:
        db = g._databdase = sqlite3.connect('terningekast.db')
    return db

def create_db_table():
    c = _get_db().cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS terninger(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tal INTEGER);""")
    _get_db().commit()

def gem(tal):
    db = _get_db()
    c = db.cursor()
    c.execute("""INSERT INTO terninger (tal) VALUES (?);""",(tal,))
    db.commit()
    print(antal())
    gennemsnit()

def antal():
    antal = []
    db = _get_db()
    c = db.cursor()
    for i in range(1,7):
        c.execute("""SELECT COUNT(tal) FROM terninger WHERE tal = ?;""", (i,))
        for j in c:
            antal.append(j[0])
    return antal

def gennemsnit():
    db = _get_db()
    c = db.cursor()
    c.execute("""SELECT COUNT(id), tal FROM terninger;""")
    t = antal()
    for count, tal in c:
        gennemsnit = tal / count
        print(gennemsnit)

@app.route("/")
@app.route("/home")
def home():
    tal = random.randint(1,6)
    gem(tal)
    return render_template('home.html', tal = tal)


if __name__ == "__main__":
    with app.app_context():
        create_db_table()

    app.run(debug=True)
