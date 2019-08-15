import sqlite3

run = True

conn = sqlite3.connect("guitarer.db")
#SECONDARY KEY OG TJEK I PROGRAMMET!
try:
    conn.execute("""CREATE TABLE IF NOT EXISTS guitarer (id INTEGER PRIMARY KEY, navn TEXT, pris INTEGER, producent INTEGER);""")
except Exception as e:
    print(f'FEJL: Fejl ved oprettelse af tabel. {e}')

try:
    conn.execute("""CREATE TABLE IF NOT EXISTS producenter (id INTEGER PRIMARY KEY, navn TEXT, lokation TEKST);""")
except Exception as e:
    print(f'FEJL: Fejl ved oprettelse af tabel. {e}')

try:
    conn.execute("""CREATE TABLE IF NOT EXISTS guitarister (id INTEGER PRIMARY KEY, navn TEXT, band TEXT);""")
except Exception as e:
    print(f'FEJL: Fejl ved oprettelse af tabel. {e}')

try:
    conn.execute("""CREATE TABLE IF NOT EXISTS guitaristmodel (id INTEGER PRIMARY KEY, guitarist_id INTEGER, model_id INTEGER);""")
except Exception as e:
    print(f'FEJL: Fejl ved oprettelse af tabel. {e}')

c = conn.cursor()


def add_guitar(navn = None, producent = None, pris = None):
    c.execute("""INSERT INTO guitarer (navn, producent, pris) VALUES (?, ?, ?);""", (navn, producent, pris))
    conn.commit()


def add_producent(navn = None, lokation = None):
    c.execute("""INSERT INTO producenter (navn, lokation) VALUES (?, ?);""", (navn, lokation))
    conn.commit()


def add_guitarist(navn = None, band = None):
    c.execute("""INSERT INTO guitarister (navn, band) VALUES (?, ?);""", (navn, band))
    conn.commit()


def add_guitaristmodel(guitarist_ident = None, guitar_model = None):
    c.execute("""INSERT INTO guitaristmodel (guitarist_id, model_id), VALUES (?, ?);""", (guitarist_ident, guitar_model))
    conn.commit()


def update_guitar(navn = None, producent = None, pris = None, identifier = None):
    c.execute("""UPDATE guitarer SET navn = ?, producent = ?, pris = ?, WHERE id = ?;""", (navn, producent, pris, identifier))
    conn.commit()


def update_producent(navn = None, lokation = None, identifier = None):
    c.execute("""UPDATE producenter SET navn = ?, lokation = ? WHERE id = ?;""", (navn, lokation, identifier))
    conn.commit()


def update_guitarist(navn = None, band = None, identifier = None):
    c.execute("""UPDATE guitarister SET navn = ?, band = ? WHERE id = ?;""", (navn, band, identifier))
    conn.commit()


def update_guitaristmodel(guitarist_identifier = None, guitar_identifier = None, identifier = None):
    c.execute("""UPDATE guitaristmodel SET guitarist_id = ?, model_id = ? WHERE id = ?;""", (guitar_identifier, guitar_identifier, identifier))
    conn.commit()


def delete_guitar(identifier = None):
    c.execute("""DELETE FROM guiterer WHERE id = ?;""", (identifier))
    conn.commit()


def delete_producenter(identifier = None):
    c.execute("""DELETE FROM producenter WHERE id = ?;""", (identifier))
    conn.commit()


def delete_guitarist(identifier = None):
    c.execute("""DELETE FROM guitarister WHERE id = ?;""", (identifier))
    conn.commit()


def delete_guitaristmodel(identifier = None):
    c.execute("""DELETE FROM guitaristmodel WHERE id = ?;""", (identifier))
    conn.commit()


while(run):
    try:
        inp = input("> ")

        if inp == "Ny guitar":
            guit_navn = input("Navn > ")
            guit_pris = input("Pris > ")
            guit_pris = int(guit_pris)
            guit_prod = input("Producent > ")
            guit_prod = int(guit_prod)

            add_guitar(guit_navn, guit_prod, guit_pris)

            print("Guitaren er blevet tilføjet til systemet!")
        
        elif inp == "Ny producent":
            prod_navn = input("Producentens navn > ")
            prod_loka = input("Producentens lokation > ")
            
            add_producent(prod_navn, prod_loka)

            print("Producenten er blevet tilføjet til systemet!")

        elif inp == "Ny guitarist":
            guitarist_navn = input("Guitaristens navn > ")
            guitarist_band = input("Guitaristens band > ")

            add_guitarist(guitarist_navn, guitarist_navn)

            print("Guitaristen er blevet tilføjet til systemet!")

        elif inp == "Ny guitarist model":
            guitarist = input("Guitaristens id > ")
            guitarist = int(guitarist)
            guitar_model = input("Guitar id > ")
            guitar_model = int(guitar_model)

            add_guitaristmodel(guitarist, guitar_model)

            print("Guitaristens guitar er blevet registreret!")

        elif inp == "Opdater guitar":
            guit_navn = input("Navn > ")
            guit_pris = input("Pris > ")
            guit_pris = int(guit_pris)
            guit_prod = input("Producent > ")
            guit_prod = int(guit_prod)
            guit_ident = input("Guitarens id > ")
            guit_ident = int(guit_ident)

            update_guitar(guit_navn, guit_prod, guit_pris, guit_ident)

            print("Guitaren er blevet opdateret!")

        elif inp == "Opdater producent":
            prod_navn = input("Producentens navn > ")
            prod_loka = input("Producentens lokation > ")
            prod_ident = input("Producentens id > ")
            prod_ident = int(prod_ident)

            update_producent(prod_navn, prod_loka, prod_ident)

            print("Producenten er blevet opdateret!")

        elif inp == "Opdater guitarist":
            guitarist_navn = input("Guitaristens navn > ")
            guitarist_band = input("Guitaristens band > ")
            guitarist_id = input("Guitaristens id > ")

            update_guitarist(guitarist_navn, guitarist_band, guitarist_id)
            print("Guitaristens informationer er blevet opdateret!")
        
        elif inp == "Opdater guitarist model":
            guitarist_id = input("Guitaristens id > ")
            guitarist_model = input("Guitaristens model > ")
            model_id = input("Guitarist model id > ")

            update_guitaristmodel(guitarist_id, guitarist_model, model_id)
            print("Guitaristens guitarmodel er blevet opdateret!")
            
        elif inp == "Slet guitar":
            guit_ident = input("Guitarens id > ")
            guit_ident = int(guit_ident)

            delete_guitar(guit_ident)

            print("Guitaren er blevet slettet!")
        
        elif inp == "Slet producent":
            prod_ident = input("Producentens id > ")
            prod_ident = int(prod_ident)

            delete_producenter(prod_ident)

            print("Producenten er blevet slettet!")

        elif inp == "Vis":
            c.execute("SELECT g.navn, p.navn, g.pris, p.lokation FROM guitarer g JOIN producenter p ON g.producent = p.id;")
            
            for gui in c:
                print(gui)

        elif inp == "Luk":
            break
        else:
            print(f'{inp} er ikke en kommando!')
            
    except Exception as e:
        print(e)