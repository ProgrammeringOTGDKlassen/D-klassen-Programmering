import math
import tkinter as tk
import matplotlib.pyplot as plt
import bezier
from geometri_bibliotek import Vector2D

def linespace(n, a, b):
    liste = []
    interval = (b - a) / n
    for i in range(n):
        liste.append(a + interval)
        a += interval
        i = i
    return liste

def y_liste(f,xs):
    ys = []
    for x in xs:
        result = f(x)
        ys.append(result)
    return ys

def f(x):
    return x**4+x**3+x**2+x+4

def trapez(n, a, b, f):
    s = 0
    x = linespace(n, a, b)

    for i in range(0,n-1):
        dx = x[i + 1] - x[i]
        h = 0.5 * (f(x[i + 1]) + f(x[i]))
        s += dx * h
    return s

def pointify(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Tager en mængde punkter og retunerer dem i en liste af punktlister således [[p1x, p1y], [p2x, p2y]]
    '''
    p1 = [x1, y1]
    p2 = [x2, y2]
    p3 = [x3, y3]
    p4 = [x4, y4]
    compiled = [p1, p2, p3, p4]
    return compiled

def vectors(p):
    '''
    Tager en liste af punkter, som vist over, og retunerer dem som en retningsvektor for kontrolpunkterne som skal styre bezierkueven senere
    '''
    v1 = Vector2D.connecting_vector(p[0][0], p[0][1], p[0][0] + 50, p[0][1] + 50)
    v2 = Vector2D.connecting_vector(p[1][0], p[1][1], p[1][0] + 50, p[1][1])
    v3 = Vector2D.connecting_vector(p[2][0], p[2][1], p[2][0] + 50, p[2][1])
    v4 = Vector2D.connecting_vector(p[3][0], p[3][1], p[3][0] + 50, p[3][1] + 50)
    return [v1, v2, v3, v4]

def bezier_vectors(p, v):
    '''
    Tager punkt-listen og listen med vektorer og laver stedvektorer til hver.
    '''
    v1 = Vector2D.sumvektor(p[0], v[0])
    v2 = Vector2D.sumvektor(p[1], v[1])
    v3 = Vector2D.sumvektor(p[2], v[2])
    v4 = Vector2D.sumvektor(p[3], v[3])
    return [v1, v2, v3, v4]

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

def generate_vase():
    pass

# diff = 1
# last = 0
# n = 100
# a = 0
# b = 3

# while diff > 0.0001:
#     s = trapez(n, a, b, f)
#     diff = abs(last - s)
#     last = s
#     n *= 2
# print(s)



# Eksempel:
# xs = [1, 2, 3, 4, 5, 6]
# ys = [1, 4, 9, 16, 25, 36]
# plt.plot(xs,ys, 'b*')
# plt.xlabel("x")
# plt.ylabel("y=x^2")
# plt.title("Plot of y=x^2")
# plt.show()


ready = False

while True:
    try:
        if not ready:
            h = int(input("\nHvor høj skal vasen være?: "))
            diaBund = int(input("\nHvad skal diameteren for vasen være i bunden?: "))
            diaBund /= 2
            diaTop = int(input("\nHvad skal diameteren for vasen være i toppen?: "))
            diaTop /= 2
            diaMin = int(input("\nHvad skal diameteren, hvor vasen er tyndest?: "))
            diaMin /= 2
            diaMinPlace = int(input("\nHvor højt skal det tyndeste punkt placeres?: "))
            diaMax = int(input("\nHvad skal diameteren, hvor vasen er tykkest?: "))
            diaMax /=2
            diaMaxPlace = int(input("\nHvor højt skal det tykkeste punkt placeres?: "))
            allPoints = pointify(0, diaBund, diaMinPlace, diaMin, diaMaxPlace, diaMax, h, diaTop)
            ready = True
        msg = input("\nSkriv her: ")

        if not msg:
            break

        elif msg.startswith("q"):
            break
        
        elif msg.startswith("start"):
            if ready:
                pass
        elif msg.startswith("test"):
            vectors = vectors(allPoints)
            print(vectors[0], vectors[1], vectors[2], vectors[3])

        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
print("Tak for nu")