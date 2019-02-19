import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import Polygon

def linespace(n, a, b):
    liste = []
    interval = (b - a) / n
    for i in range(n):
        liste.append(a + interval)
        a += interval
        i = i
    return liste

def f_liste(f,xs):
    ys = []
    for x in xs:
        result = f(x)
        ys.append(result)
    return ys

def f(x):
    return x**4+x**3+x**2+x+4

def fx(lx, lp):
    '''
    1 p = f(x) = p
    2 p = f(x) = p + p*x
    3 p = f(x) = p + p*x + p*x^2
    4 p = f(x) = p + p*x + p*x^2 + p*x^3
    '''
    f = 0
    final = []
    for x in lx:
        for p in lp:
            f += p * x**lp.index(p)
        final.append(f)
    return final


def trapez(n, a, b, f):
    s = 0
    x = linespace(n, a, b)

    for i in range(0,n-1):
        dx = x[i + 1] - x[i]
        h = 0.5 * (f(x[i + 1]) + f(x[i]))
        s += dx * h
    return s

diff = 1
last = 0
n = 100
a = -10
b = 10

# while diff > 0.00001:
#     s = trapez(n, a, b, f)
#     diff = abs(last - s)
#     last = s
#     n *= 2

polyList = [4, 7, 7, 3]

xs = linespace(n, a, b)
ys = f_liste(f, xs)

plt.plot(xs, ys)
for i in range(0, len(xs)-1):
    p = [[xs[i], 0], [xs[i], ys[i]], [xs[i+1], ys[i+1]], [xs[i+1], 0]]
    plt.gca().add_patch(Polygon(p, color = '0.8'))
plt.show()