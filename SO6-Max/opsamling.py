import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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
    return x**2
    # return 3*math.sin(0.3*x)+4

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

def bedre_trapez_sum(f, a, b, n):
    s = 0
    x = linspace(a, b, n)
    for i in range(0, n - 1):
        dx = x[i + 1] - x[i]
        h = 0.5 * (f(x[i + 1]) + f(x[i]))
        s += dx * h
    return s
diff = 1
last = 0
a = 0
b = 3
n = 5000000
while diff > 0.0001:
    s = bedre_trapez_sum(f, a, b, n)
    diff = abs(last - s)
    last = s
    n *= 2

print(s)
xs = linspace(a,b,n)
ys = f_liste(f,xs)
#print(ys)
plt.plot(xs, ys)
for i in range(0, len(xs) - 1):
    p = [[xs[i], 0], [xs[i], ys[i]], [xs[i + 1], ys[i]], [xs[i + 1], 0]]
    plt.gca().add_patch(Polygon(p, color = '0.8'))
plt.show()
#print(trapez_sum(xs,ys))