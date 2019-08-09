import sqlite3

global conn, c

# establishing connection to database
conn = sqlite3.connect("guitars.db")

# trying to create table "guitars" with id, name, manufacturer and price
try:
  conn.execute("""CREATE TABLE guitars (id INTEGER PRIMARY KEY, name TEXT, manufacturer INTEGER, price INTEGER);""")
except:
  print('Fejl ved oprettelse af tabel')

# trying to create table "manufacturers" with id and manufacturer
try:
  conn.execute("""CREATE TABLE manufacturers (id INTEGER PRIMARY KEY, manufacturer TEXT);""")
except:
  print('Fejl ved oprettelse af tabel')

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
    
    if cmd == 'add mfr':
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

    elif cmd == 'show':
      c.execute("SELECT * FROM guitars;")
      for gui in c:
        print(gui)
    
    elif cmd == 'show right':
      c.execute("SELECT guitars.name, manufacturers.manufacturer, guitars.price FROM guitars JOIN manufacturers ON guitars.manufacturer = manufacturers.id;")
      for gui in c:
        print(gui)
    
    elif cmd == 'q' or cmd == 'quit':
      break
  except Exception as err:
    print(err)

