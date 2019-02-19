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

def bedre_trapez_sum(f, a, b, n):
    s = 0
    x = linspace(a, b, n)
    for i in range(0, n - 1):
        dx = x[i + 1] - x[i]
        h = 0.5 * (f(x[i + 1]) + f(x[i]))
        s += dx * h
    return s

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
            Result = venstre_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            sammenligning = Result - integral_værdi
            print('Venstre summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Result, sammenligning, integral_værdi, integral_fejl))
        
        elif msg == "midsum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_midliste(f, xs)
            Result = midt_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            sammenligning = Result - integral_værdi
            print('Mid summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Result, sammenligning, integral_værdi, integral_fejl))
        
        elif msg == "højresum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            Result = højre_sum(xs, ys)
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            sammenligning = Result - integral_værdi
            print('Højre summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, Result, sammenligning, integral_værdi, integral_fejl))

        elif msg == "trapezsum":
            Funktion = input("Indtast funktionen du vil have en sum af [Der skal være * mellem et tal og x som fx 3x -> 3*x. Opløftninger skal gøres med **]: ")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split(" ")
            a = int(list1[0])
            b = int(list1[1])
            n = int(list1[2])
            diff = 1
            last = 0
            xs = linspace(a, b, n)
            while diff > 0.0001:
                s = bedre_trapez_sum(f, a, b, n)
                diff = abs(last - s)
                last = s
                n *= 2
            integral = quad(f, a, b)
            integral_værdi = integral[0]
            integral_fejl = integral[1]
            sammenligning = s - integral_værdi
            print('Trapez summen af {} i intervallet {} til {} med {} inddelinger er {}. Det er {} fra det eksakte integral som er {} med en fejl på {}'.format(Funktion, a, b, n, s, sammenligning, integral_værdi, integral_fejl))

        if msg == ("quit"): #Hvis msg == quit så stopper programmet
            break
    except Exception as e:
        print(e)
        print("[ERROR] Except was runned! Check your code!!!")
        
print("Tak for nu")