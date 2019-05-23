import math
global fra, til

# Startværdi
y0 = 0

# Her skrives hvor lang talrækken skal være. Fx y0 til y 10 skal være fra: 0 og til: 10
fra = 0
til = 10

# Hvis yn skal bruges, skal der stå True ellers False. Skal startværdien tælles med som det første element i talrækkken?
bruger_yn = True


def funktion(n=None, yn=None):  # Her skrives funktionen som skal bruges:
    funktion = yn + (n+1)**2

    return funktion

# Hertil og ikke længere
# -----------------------------------------------------------------------------------------------------------------------------------------------------------


talrækkeyn = []

talrækken = []


def yn(yn, talrække):  # Tager startværdien med i talrækken
    print("\nyn")
    talrække.append(yn)
    for n in range(fra, til):
        yn = funktion(n, yn)
        talrække.append(yn)
        yn = yn
    for i in range(len(talrække)):
        print("y{} er {}".format(i, talrække[i]))


def n(yn, talrække):  # Tager ikke startværdien med i talrækken
    print("\nn")
    for n in range(fra, til):
        yn = funktion(n, yn)
        talrække.append(yn)
        yn = yn
    for i in range(len(talrække)):
        print("y{} er {}".format(i, talrække[i]))

if bruger_yn:
    yn(y0, talrækkeyn)
else:
    n(y0, talrækken)
