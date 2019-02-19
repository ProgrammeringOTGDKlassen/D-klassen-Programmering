import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.integrate import quad

def linspace(a, b, n):
    xs = []
    interval = (b - a) / n
    for i in range(n):
        #xs.append(a + i * interval)
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

'''
print(s)
xs = linspace(a,b,n)
ys = f_liste(f,xs)
#print(ys)
plt.plot(xs, ys)
for i in range(0, len(xs) - 1):
    p = [[xs[i], 0], [xs[i], ys[i]], [xs[i + 1], ys[i]], [xs[i + 1], 0]]
    plt.gca().add_patch(Polygon(p, color = '0.8'))
plt.show()
'''
while True:
    try:
        msg = input("\nHvilken sum vil du have regnet? ")
        
        if msg == "venstresum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f,xs)
            Venstre_result = venstre_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            Venstre_sammenligning = Venstre_result - integral_værdi
            Højre_result = højre_sum(xs, ys)
            Højre_sammenligning = Højre_result - integral_værdi
            Mid_result = midt_sum(xs,ys2)
            Mid_sammenligning = Mid_result - integral_værdi
            Trapez_result = trapez_sum(xs, ys)
            Trapez_sammenligning = Trapez_result - integral_værdi
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            Mindsteværdi = min(Absolut_liste)
            for i in range(0,len(Absolut_liste)):
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
            print('Venstre summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Venstre_result, Venstre_sammenligning, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} fra det eksakte integral som er {}.'.format(Bedste_sum, Listeelement, integral_værdi))
        elif msg == "midsum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_midliste(f, xs)
            ys2 = f_liste(f,xs)
            Mid_result = midt_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            Mid_sammenligning = Mid_result - integral_værdi
            Højre_result = højre_sum(xs, ys2)
            Højre_sammenligning = Højre_result - integral_værdi
            Venstre_result = venstre_sum(xs,ys2)
            Venstre_sammenligning = Venstre_result - integral_værdi
            Trapez_result = trapez_sum(xs,ys2)
            Trapez_sammenligning = Trapez_result - integral_værdi
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            Mindsteværdi = min(Absolut_liste)
            for i in range(0,len(Absolut_liste)):
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
            print('Mid summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Mid_result, Mid_sammenligning, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} fra det eksakte integral som er {}.'.format(Bedste_sum, Listeelement, integral_værdi))

        elif msg == "højresum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f, xs)
            Højre_result = højre_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            Højre_sammenligning = Højre_result - integral_værdi
            Venstre_result = venstre_sum(xs, ys)
            Venstre_sammenligning = Venstre_result - integral_værdi
            Mid_result = midt_sum(xs,ys2)
            Mid_sammenligning = Mid_result - integral_værdi
            Trapez_result = trapez_sum(xs,ys)
            Trapez_sammenligning = Trapez_result - integral_værdi
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            Mindsteværdi = min(Absolut_liste)
            for i in range(0,len(Absolut_liste)):
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
            print('Højre summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Højre_result, Højre_sammenligning, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} fra det eksakte integral som er {}.'.format(Bedste_sum, Listeelement, integral_værdi))

        elif msg == "trapezsum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split(" ")
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            ys2 = f_midliste(f, xs)
            Trapez_result = trapez_sum(xs,ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            Trapez_sammenligning = Trapez_result - integral_værdi
            Højre_result = højre_sum(xs, ys)
            Højre_sammenligning = Højre_result - integral_værdi
            Mid_result = midt_sum(xs,ys2)
            Mid_sammenligning = Mid_result - integral_værdi
            Venstre_result = venstre_sum(xs, ys)
            Venstre_sammenligning = Venstre_result - integral_værdi
            Sammenlignings_liste = [Venstre_sammenligning, Højre_sammenligning, Mid_sammenligning, Trapez_sammenligning]
            Absolut_liste = [abs(Venstre_sammenligning), abs(Højre_sammenligning), abs(Mid_sammenligning), abs(Trapez_sammenligning)]
            Mindsteværdi = min(Absolut_liste)
            for i in range(0,len(Absolut_liste)):
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
            print('Trapez summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Trapez_result, Trapez_sammenligning, integral_værdi, integral_fejl))
            print('Den bedste sum er {} som er {} fra det eksakte integral som er {}.'.format(Bedste_sum, Listeelement, integral_værdi))

        if msg == ("quit"): #Hvis msg == quit så stopper programmet
            break
    except Exception as e:
        print(e)
        print("[ERROR] Except was runned! Check your code!!!")
print("Tak for nu")