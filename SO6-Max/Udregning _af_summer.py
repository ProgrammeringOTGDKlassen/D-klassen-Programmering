import math

def linspace(a, b, n):
    xs = []
    interval = (b - a) / (n-1)
    for i in range(0, n):
        xs.append(a + i * interval)
    return xs

def f(x):
    return 3*math.sin(0.3*x)+4

def f_liste(f,xs):
    ys = []
    for x in xs:
        result = f(x)
        ys.append(result)
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
        s = s + ys[i + 1] * (xs[i + 1] - xs[i])
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

while True:
    try:
        msg = input("\n Hvilken sum vil du have regnet? ")
        
        if msg == "venstresum":
            Funktion = input("")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = list1[0]
            b = list1[1]
            n = list1[2]
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            Result = venstre_sum(xs, ys)
            print('Venstre summen af __ i intervallet {} til {} med {} inddelinger er {}'.format(a, b, n, Result))
        
        elif msg == "midsum":
            Funktion = input("")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = list1[0]
            b = list1[1]
            n = list1[2]
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            Result = midt_sum(xs, ys)
            print('Mid summen af __ i intervallet {} til {} med {} inddelinger er {}'.format(a, b, n, Result))
        
        elif msg == "højresum":
            Funktion = input("")
            Inddeling = input("Indtast start, slut og antal inddelinger i formatet [a b n]: ")
            list1 = Inddeling.split()
            a = list1[0]
            b = list1[1]
            n = list1[2]
            xs = linspace(a, b, n)
            ys = f_liste(f, xs)
            Result = højre_sum(xs, ys)
            print('Højre summen af __ i intervallet {} til {} med {} inddelinger er {}'.format(a, b, n, Result))