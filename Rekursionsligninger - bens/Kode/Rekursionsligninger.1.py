import math
global fra, til, funktion

# Test

def f(n=None, yn=None):
    funktion_fixed = funktion.replace("yn", str(yn)).replace("n", str(n))
    return eval(funktion_fixed)


def yn(yn, talrække):  # Tager startværdien med i talrækken
    talrække.append(yn)
    for n in range(fra, til):
        yn = f(n, yn)
        talrække.append(yn)
        yn = yn
    for i in range(len(talrække)):
        print("y{} er {}".format(i, talrække[i]))


def n(yn, talrække):  # Tager ikke startværdien med i talrækken
    for n in range(fra, til):
        yn = f(n, yn)
        talrække.append(yn)
        yn = yn
    for i in range(len(talrække)):
        print("y{} er {}".format(i, talrække[i]))


print('Der er følgende kommandoer: \nq for at lukke programmet \nr for at bruge Rekursionsligninger \nn for newton ting ting')
while True:
    try:
        msg = input("\nSkriv her: ")

        if not msg:
            break

        elif msg.startswith('q'):
            break

        elif msg.startswith('r'):
            # Startværdi
            y0 = input('\nHvad skal startværdien være (y0)?: ')

            # Her skrives hvor lang talrækken skal være. Fx y0 til y 10 skal være fra: 0 og til: 10
            fraTil = input(
                'Hvad skal det være fra og til (fx y0 til y10)? (adskilles med komma. 0,10): ')
            fraTil = fraTil.split(',')
            fra = int(fraTil[0])
            til = int(fraTil[1])

            # Hvis yn skal bruges, skal der stå True ellers False. Skal startværdien tælles med som det første element i talrækkken?
            startMed = input(
                'Skal startværdien tælles med som det første element i talrækkken? (y/n): ')

            if startMed == 'y':
                bruger_yn = True
            else:
                bruger_yn = False

            funktion = input(
                'Hvilken funktion skal der bruges (yn & n som variable)?: ')

            talrækkeyn = []

            talrækken = []

            if bruger_yn:
                yn(y0, talrækkeyn)
            else:
                n(y0, talrækken)
        elif msg.startswith('n'):

        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
print("Tak for nu")
