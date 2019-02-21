import math as m
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.integrate import quad

def linspace(a, b, n):
    xs = []
    interval = (b - a) / n
    for i in range(n):
        xs.append(a + interval)
        a += interval
        i = i
    return xs

def f(x):
    global Funktion
    return eval(Funktion)

def f_liste(f,xs):
    ys = []
    for x in xs:
        result = f(x)
        ys.append(result)
    return ys

def f_midliste(f,xs):
    ys = []
    for i in range(0,len(xs)-1):
        y = f((xs[i]+xs[i+1])/2)
        ys.append(y)
    return ys

def venstre_sum(xs, ys):
    s = 0
    for i in range(0, len(xs) - 1):
        s = s + ys[i] * (xs[i + 1] - xs[i])
    return s

def højre_sum(xs, ys):
    s = 0
    for i in range(0, len(xs) - 1):
        s = s + ys[i + 1] * (xs[i + 1] - xs[i])
    return s

def midt_sum(xs, ys):
    s = 0
    for i in range(0, len(xs) - 1):
        s = s + ys[i] * (xs[i + 1] - xs[i])
    return s

def trapez_sum(xs, ys):
    s = 0
    s1 = 0
    s2 = 0
    for i in range(0, len(xs) - 1):
        s = s + ys[i] * (xs[i + 1] - xs[i])
        s1 = s1 + ys[i + 1] * (xs[i + 1] - xs[i])
        s2 = (s + s1)/2
    return s2

CMD = {}
CMD["Lukker programmet"] = "quit"
CMD["Liste af kommandoer"] = "hjælp"
CMD["Udregning af venstresum"] = "venstresum"
CMD["Udregning af midsum"] = "midsum"
CMD["Udregning af højresum"] = "højresum"
CMD["Udregning af trapezsum"] = "trapezsum"

while True:
    try:
        msg = input("\nHvilken sum vil du have regnet? ")
        
        if msg == "venstresum":
            print("\nNår du skal indskrive funktioner er der en følgende regler for indskrivningen:")
            print("Der skal være * mellem et tal og x som fx 3x -> 3*x")
            print("Operatører: Plus = + Minus = - Gange = * Dividere = /")
            print("Opløftninger skal gøres med **")
            print("Skal du bruge sin, cos eller tan, samt arc sin, cos eller tan så skal du skrive m.sin(funktionen), m.cos(funktionen), m.tan(funktionen). Arc: m.asin(funktion), m.acos(funktion), m.atan(funktion)")
            print("Logaritmer bruges med m.log(funktion)")
            Funktion = input("\nIndtast funktionen du vil have en sum af: ")

            if Funktion == "quit":
                break

            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            
            if Inddeling == "quit":
                break

            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f,xs)
            
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            
            Venstre_result = venstre_sum(xs, ys)
            Højre_result = højre_sum(xs, ys)
            Mid_result = midt_sum(xs, ys2)
            Trapez_result = trapez_sum(xs, ys)

            Venstre_sammenligning = Venstre_result - integral_værdi
            Højre_sammenligning = Højre_result - integral_værdi
            Mid_sammenligning = Mid_result - integral_værdi
            Trapez_sammenligning = Trapez_result - integral_værdi
            
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            
            Mindsteværdi = min(Absolut_liste)
            
            for i in range(0, len(Absolut_liste)):
                if Mindsteværdi == Absolut_liste[i]:
                    Listeelement = Sammenlignings_liste[i]
            
            if Listeelement == Venstre_sammenligning:
                Bedste_sum = "Venstresum"
            elif Listeelement == Højre_sammenligning:
                Bedste_sum = "Højresum"
            elif Listeelement == Mid_sammenligning:
                Bedste_sum = "Midsum"
            elif Listeelement == Trapez_sammenligning:
                Bedste_sum = "Trapezum"
            
            if Venstre_sammenligning > 0:
                Over_under = "over"
            elif Venstre_sammenligning < 0:
                Over_under = "under"

            if Listeelement > 0:
                Over_under2 = "over"
            elif Listeelement < 0:
                Over_under2 = "under"

            print('Venstresummen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Funktion, a, b, n, Venstre_result, abs(Venstre_sammenligning), Over_under, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Bedste_sum, abs(Listeelement), Over_under2, integral_værdi, integral_fejl))
        
        elif msg == "midsum":
            print("\nNår du skal indskrive funktioner er der en følgende regler for indskrivningen:   ")
            print("Der skal være * mellem et tal og x som fx 3x -> 3*x")
            print("Operatører: Plus = + Minus = - Gange = * Dividere = /")
            print("Opløftninger skal gøres med **")
            print("Skal du bruge sin, cos eller tan, samt arc sin, cos eller tan så skal du skrive m.sin(funktionen), m.cos(funktionen), m.tan(funktionen). Arc: m.asin(funktion), m.acos(funktion), m.atan(funktion)")
            print("Logaritmer bruges med m.log(funktion)")
            Funktion = input("Indtast funktionen du vil have en sum af: ")

            if Funktion == "quit":
                break

            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            
            if Inddeling == "quit":
                break

            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_midliste(f, xs)
            ys2 = f_liste(f,xs)
            
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            
            Venstre_result = venstre_sum(xs,ys2)
            Mid_result = midt_sum(xs, ys)
            Højre_result = højre_sum(xs, ys2)
            Trapez_result = trapez_sum(xs, ys2)

            Venstre_sammenligning = Venstre_result - integral_værdi
            Mid_sammenligning = Mid_result - integral_værdi
            Højre_sammenligning = Højre_result - integral_værdi     
            Trapez_sammenligning = Trapez_result - integral_værdi
            
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            
            Mindsteværdi = min(Absolut_liste)
            
            for i in range(0, len(Absolut_liste)):
                if Mindsteværdi == Absolut_liste[i]:
                    Listeelement = Sammenlignings_liste[i]
            
            if Listeelement == Venstre_sammenligning:
                Bedste_sum = "Venstresum"
            elif Listeelement == Højre_sammenligning:
                Bedste_sum = "Højresum"
            elif Listeelement == Mid_sammenligning:
                Bedste_sum = "Midsum"
            elif Listeelement == Trapez_sammenligning:
                Bedste_sum = "Trapezum"
            
            if Mid_sammenligning > 0:
                Over_under = "over"
            elif Mid_sammenligning < 0:
                Over_under = "under"

            if Listeelement > 0:
                Over_under2 = "over"
            elif Listeelement < 0:
                Over_under2 = "under"

            print('Midsummen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Funktion, a, b, n, Mid_result, abs(Mid_sammenligning), Over_under, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Bedste_sum, abs(Listeelement), Over_under2, integral_værdi, integral_fejl))

        elif msg == "højresum":
            print("\nNår du skal indskrive funktioner er der en følgende regler for indskrivningen:   ")
            print("Der skal være * mellem et tal og x som fx 3x -> 3*x")
            print("Operatører: Plus = + Minus = - Gange = * Dividere = /")
            print("Opløftninger skal gøres med **")
            print("Skal du bruge sin, cos eller tan, samt arc sin, cos eller tan så skal du skrive m.sin(funktionen), m.cos(funktionen), m.tan(funktionen). Arc: m.asin(funktion), m.acos(funktion), m.atan(funktion)")
            print("Logaritmer bruges med m.log(funktion)")
            Funktion = input("Indtast funktionen du vil have en sum af: ")

            if Funktion == "quit":
                break

            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            
            if Inddeling == "quit":
                break
            
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f, xs)
            
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            
            Venstre_result = venstre_sum(xs, ys)
            Mid_result = midt_sum(xs, ys2)
            Højre_result = højre_sum(xs, ys)
            Trapez_result = trapez_sum(xs, ys)

            Venstre_sammenligning = Venstre_result - integral_værdi
            Mid_sammenligning = Mid_result - integral_værdi
            Højre_sammenligning = Højre_result - integral_værdi
            Trapez_sammenligning = Trapez_result - integral_værdi
            
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            
            Mindsteværdi = min(Absolut_liste)
            
            for i in range(0, len(Absolut_liste)):
                if Mindsteværdi == Absolut_liste[i]:
                    Listeelement = Sammenlignings_liste[i]
            
            if Listeelement == Venstre_sammenligning:
                Bedste_sum = "Venstresum"
            elif Listeelement == Højre_sammenligning:
                Bedste_sum = "Højresum"
            elif Listeelement == Mid_sammenligning:
                Bedste_sum = "Midsum"
            elif Listeelement == Trapez_sammenligning:
                Bedste_sum = "Trapezum"
            
            if Højre_sammenligning > 0:
                Over_under = "over"
            elif Højre_sammenligning < 0:
                Over_under = "under"

            if Listeelement > 0:
                Over_under2 = "over"
            elif Listeelement < 0:
                Over_under2 = "under"

            print('Højresummen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Funktion, a, b, n, Højre_result, abs(Højre_sammenligning), Over_under, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Bedste_sum, abs(Listeelement), Over_under2, integral_værdi, integral_fejl))


        elif msg == "trapezsum":
            print("\nNår du skal indskrive funktioner er der en følgende regler for indskrivningen:   ")
            print("Der skal være * mellem et tal og x som fx 3x -> 3*x")
            print("Operatører: Plus = + Minus = - Gange = * Dividere = /")
            print("Opløftninger skal gøres med **")
            print("Skal du bruge sin, cos eller tan, samt arc sin, cos eller tan så skal du skrive m.sin(funktionen), m.cos(funktionen), m.tan(funktionen). Arc: m.asin(funktion), m.acos(funktion), m.atan(funktion)")
            print("Logaritmer bruges med m.log(funktion)")
            Funktion = input("Indtast funktionen du vil have en sum af: ")

            if Funktion == "quit":
                break

            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            
            if Inddeling == "quit":
                break
            
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f, xs)
            
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            
            Venstre_result = venstre_sum(xs, ys)
            Mid_result = midt_sum(xs, ys2)
            Højre_result = højre_sum(xs, ys)
            Trapez_result = trapez_sum(xs, ys)
            
            Venstre_sammenligning = Venstre_result - integral_værdi
            Mid_sammenligning = Mid_result - integral_værdi
            Højre_sammenligning = Højre_result - integral_værdi
            Trapez_sammenligning = Trapez_result - integral_værdi
            
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            
            Mindsteværdi = min(Absolut_liste)
            
            for i in range(0, len(Absolut_liste)):
                if Mindsteværdi == Absolut_liste[i]:
                    Listeelement = Sammenlignings_liste[i]
            
            if Listeelement == Venstre_sammenligning:
                Bedste_sum = "Venstresum"
            elif Listeelement == Højre_sammenligning:
                Bedste_sum = "Højresum"
            elif Listeelement == Mid_sammenligning:
                Bedste_sum = "Midsum"
            elif Listeelement == Trapez_sammenligning:
                Bedste_sum = "Trapezum"
            
            if Trapez_sammenligning > 0:
                Over_under = "over"
            elif Trapez_sammenligning < 0:
                Over_under = "under"

            if Listeelement > 0:
                Over_under2 = "over"
            elif Listeelement < 0:
                Over_under2 = "under"

            print('Trapezsummen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Funktion, a, b, n, Trapez_result, abs(Trapez_sammenligning), Over_under, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} {} det eksakte integral som er {} som er udregnet med Scipy med en usikkerhed på {}.'.format(Bedste_sum, abs(Listeelement), Over_under2, integral_værdi, integral_fejl))


        elif msg == ("quit"):
            break
        
        elif msg == ("hjælp"):
            for name in CMD:
                print("Kommando: "+ CMD[name], "- "+ name)
        else:
            print("{} er ikke en registreret kommando, skriv 'hjælp' for en liste af kommandoer".format(msg))

    except Exception as e:
        print(e)
        print("[ERROR] Except was runned! Check your code!!!")

print("Tak for nu")