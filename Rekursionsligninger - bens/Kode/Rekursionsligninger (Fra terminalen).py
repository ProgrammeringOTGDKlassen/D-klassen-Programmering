import math
import sympy
from math import e
global fra, til, funktion


def f(n=None, yn=None):
    funktion_fixed = funktion.replace("yn", str(yn)).replace("n", str(n))
    return eval(funktion_fixed)


def newton(talrække):
    nFunk = input(
        'Hvilken funktion, f(x), skal der bruges (fx "x**2")?: ')

    x = sympy.Symbol('x')
    nDifFunk = str(sympy.diff(eval(nFunk), x))

    x = float(
        input('Hvad gætter du på, at nulpunktet er for f(x)={}?: '.format(nFunk)))

    nTil = int(
        input('Hvor mange gange skal der løbes igennem newton funktionen?: '))

    nFunk_fixed = nFunk.replace('x', str(x))
    nDifFunk_fixed = nDifFunk.replace('x', str(x))

    for n in range(0, nTil+1):
        x = x - ((eval(nFunk_fixed))/(eval(nDifFunk_fixed)))
        nFunk_fixed = nFunk.replace('x', str(x))
        nDifFunk_fixed = nDifFunk.replace('x', str(x))
        talrække.append(x)

    for i in range(1, len(talrække)):
        print("{}. gæt-beregning er {}".format(i, talrække[i]))


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

        # Brug af Rekursionsligninger----------------------------------------------------------------------------------------------------------------------
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

        # Newtons funktion----------------------------------------------------------------------------------------------------------------------------------
        elif msg.startswith('n'):
            nTalrække = []

            newton(nTalrække)

        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
print("DAK for i dag")
