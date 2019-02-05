import math
import matplotlib.pyplot as plt

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

xs = linspace(1,50,100)
ys = f_liste(f,xs)
#print(ys)
#plt.plot(xs, ys)
#plt.show()
print(trapez_sum(xs,ys))