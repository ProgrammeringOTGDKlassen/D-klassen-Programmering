import sqlite3

global conn, c

# establishing connection to database
conn = sqlite3.connect("guitars.db")

# trying to create table "guitars" with id, name, manufacturer and price
try:
  conn.execute("""CREATE TABLE IF NOT EXISTS guitars (id INTEGER PRIMARY KEY, name TEXT, manufacturer INTEGER, price INTEGER);""")
except Exception as err:
  print(err)

# trying to create table "manufacturers" with id and manufacturer
try:
  conn.execute("""CREATE TABLE IF NOT EXISTS manufacturers (id INTEGER PRIMARY KEY, manufacturer TEXT);""")
except Exception as err:
  print(err)

try:
  conn.execute("""CREATE TABLE IF NOT EXISTS guitarists (id INTEGER PRIMARY KEY, name TEXT, band TEXT);""")
except Exception as err:
  print(err)

try:
  # conn.execute("DROP TABLE guitaristsModels;")
  conn.execute("""CREATE TABLE IF NOT EXISTS guitaristsModels (id INTEGER PRIMARY KEY, guitarist_id INTEGER, model_id INTEGER);""")
except Exception as err:
  print(err)

# creating cursor
c = conn.cursor()


def add_guitar(name = None, manufacturer = None, price = None):
  c.execute("""INSERT INTO guitars (name, manufacturer, price) VALUES (?, ?, ?);""", (name, manufacturer, price))
  conn.commit()


def add_manufacturer(manufacturer = None):
  c.execute("""INSERT INTO manufacturers (manufacturer) VALUES (?);""", (manufacturer,))
  conn.commit()


def update_guitar(name = None, manufacturer = None, price = None, identifier = None):
  c.execute("""UPDATE guitars SET name = ?, manufacturer = ?, price = ? WHERE id = ?""", ((name, manufacturer, price, identifier)))
  conn.commit()


def delete_guitar(identifier = None):
  c.execute("""DELETE FROM guitars WHERE id = ?;""", (identifier,))
  conn.commit()


def add_guitarist_model(g_id = None, m_id = None):
  c.execute("""INSERT INTO guitaristsModels (guitarist_id, model_id) VALUES (?, ?);""", (g_id, m_id))
  conn.commit()


def add_guitarist(name = None, band = None):
  c.execute("""INSERT INTO guitarists (name, band) VALUES (?, ?);""", (name, band))
  conn.commit()


# commandsystem
while True:
  try:
    # get userinput
    cmd = input("Please enter a command: ")
    
    if cmd == 'add':
      name = str(input("What should the name be?: "))
      manufacturer = int(input("What should the manufacturer-ID be?: "))
      price = int(input("What should the price be?: "))
      add_guitar(name, manufacturer, price)
    
    elif cmd == 'add mfr':
      manufacturer = str(input("What should the manufacturer be?: "))
      add_manufacturer(manufacturer)

    elif cmd == 'update guitar':
      name = str(input("What should the name be?: "))
      manufacturer = int(input("What should the manufacturer be?: "))
      price = int(input("What should the price be?: "))
      identifier = int(input("What ID of guitar would you like to change?: "))
      update_guitar(name, manufacturer, price, identifier)
    
    elif cmd == 'delete guitar':
      c.execute("SELECT * FROM guitars;")
      for gui in c:
        print(gui)
      identifier = int(input("\nWhat guitar-ID should be deleted: "))
      delete_guitar(identifier)
    
    elif cmd == 'add guitarist':
      name = str(input("What should the name be?: "))
      band = str(input("What should the band be?: "))
      add_guitarist(name, band)

    elif cmd == 'add guitarist model':
      g_id = int(input("What should the guitar id be?: "))
      m_id = int(input("What should the model id be?: "))
      add_guitarist_model(g_id, m_id)

    elif cmd == 'show':
      c.execute("SELECT * FROM guitars;")
      for gui in c:
        print(gui)
    
    elif cmd == 'show right':
      c.execute("SELECT guitars.name, manufacturers.manufacturer, guitars.price FROM guitars JOIN manufacturers ON guitars.manufacturer = manufacturers.id;")
      for gui in c:
        print(gui)
    
    elif cmd == 'show bobs':
        print("""(oYo)""")
      
    elif cmd == 'test':
      c.execute("SELECT * FROM guitaristsModels;")
      for gui in c:
        print(gui)

    elif cmd == 'q' or cmd == 'quit':
      break
    
    else:
      print('It is not a recognized command')
  except Exception as err:
    print(err)