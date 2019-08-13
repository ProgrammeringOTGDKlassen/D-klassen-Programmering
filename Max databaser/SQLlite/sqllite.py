import sqlite3

run = True

conn = sqlite3.connect("guitarer.db")

try:
    conn.execute("""CREATE TABLE IF NOT EXISTS guitarer (id INTEGER PRIMARY KEY, navn TEXT, pris INTEGER, producent INTEGER);""")
    conn.commit()
    conn.execute("""CREATE TABLE IF NOT EXISTS producenter (id INTEGER PRIMARY KEY, navn TEXT, lokation TEKST);""")
except Exception as e:
    print(f'FEJL: Fejl ved oprettelse af tabel. {e}')


c = conn.cursor()
'''
c.execute("""UPDATE guitarer SET navn = 'Jens', pris = 1000 WHERE id = 2;""")

conn.commit()

c.execute("SELECT * FROM guitarer;")

for gui in c:
    print(gui)
'''
while(run):
    try:

        inp = input("> ")

        if inp == "ny":
            navn1 = input("Navn > ")
            pris1 = input("Pris > ")
            prod = input("Producent > ")
            prod_loka = input("Producentens lokation > ")
            pris1 = int(pris1)

            c.execute("""INSERT INTO guitarer (navn, pris) VALUES (?, ?);""",(navn1, pris1))
            conn.commit()
            c.execute("""INSERT INTO producenter (navn, lokation) VALUES (?, ?);""",(prod, prod_loka))

            conn.commit()

            c.execute("SELECT guitarer.navn, producenter.navn, guitarer.pris, producenter.lokation FROM guitarer JOIN producenter ON guitarer.producent = producenter.id;")

            for gui in c:
                print(gui)
        elif inp == "Vis":
            c.execute("SELECT guitarer.navn, producenter.navn, guitarer.pris, producenter.lokation FROM guitarer JOIN producenter ON guitarer.producent = producenter.id;")
            
            for gui in c:
                print(gui)
        elif inp == "Luk":
            break
        else:
            print(f'{inp} er ikke en kommando!')
            
    except Exception as e:
        print(e)