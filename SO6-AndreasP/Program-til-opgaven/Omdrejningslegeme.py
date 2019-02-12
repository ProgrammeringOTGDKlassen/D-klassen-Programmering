import math
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.pyplot import Polygon
import bezier
from geometri_bibliotek import Vector2D
from geometri_bibliotek import Point

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

def trapezPoint(pList):
    last = 0
    for i in range(0, len(pList) - 1):
        new = (pList[i + 1].x - pList[i].x)/2 * (pList[i].y + pList[i + 1].y)
        last += new
    return last

# def trapezPoint(pList):
#     last = 0
#     for i in pList:
#         new = last + (pList.index(i + 1).x - i.x)/2 * (i.y + pList.index(i + 1).y)
#         last += new
#     return last

# def area_solid_of_revolution(pList):
#     last = 0
#     for i in range(0, pList-1):
#         new = ???
#         last += new
#     return last

# def volume_solid_of_revolution(pList):
#     last = 0
#     for i in range(0, pList-1):
#             new = ???
#             last += new
#     return last

def pointify(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Tager en mængde punkter og retunerer dem i en liste af punktlister således [[p1x, p1y], [p2x, p2y]]
    '''
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)
    compiled = [p1, p2, p3, p4]
    return compiled

def bezier_control(p1, p2, p3, p4):
    p1c1p2 = Point(p1.x + (p2.x - p1.x)/5, p1.y + (abs(p2.y - p1.y))/2)
    p1c2p2 = Point(p2.x - (p2.x - p1.x)/2, p2.y)
    p2c1p3 = Point(p2.x + (p2.x - p1.x)/2, p2.y)
    p2c2p3 = Point(p3.x - (p3.x - p2.x)/4, p3.y)
    p3c1p4 = Point(p3.x + (p3.x - p2.x)/4, p3.y)
    p3c2p4 = Point(p4.x, p4.y - (p4.y - p3.y)/2)
    compiled = [p1c1p2, p1c2p2, p2c1p3, p2c2p3, p3c1p4, p3c2p4]
    return compiled

def bezier_part(p1, c1, c2, p2):
    compiled = []
    compiled.append(p1)
    compiled.append(c1)
    compiled.append(c2)
    compiled.append(p2)
    return compiled

def bezier_curve(pcList, index):
    tIndex = 1/index
    t = 0
    xList = []
    yList = []
    pList = []

    for p in pcList:
        for i in range(0, index):
            x = (1 - t)**3 * p[0].x + 3 * (1 - t)**2 * t * p[1].x + 3*(1-t) * t**2 * p[2].x + t**3 * p[3].x
            y = (1 - t)**3 * p[0].y + 3 * (1 - t)**2 * t * p[1].y + 3*(1-t) * t**2 * p[2].y + t**3 * p[3].y
            
            xList.append(x)
            yList.append(y)

            point = Point(x, y)
            pList.append(point)

            t += tIndex
        t = 0
    
    return pList, xList, yList


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
            '''
            How tall will the vase be?: 500

            What should the diameter of the vase's buttom be?: 100

            What should the diameter of the vase's top be?: 200

            What should the diameter of the vase's thinest spot be?: 60

            In which height should the thinest spot be placed?: 400

            What should the diameter of the vase's thickest spot be?: 300

            In which height should the thickest spot be placed?: 200
            '''

            # h = int(input("\nHow tall will the vase be?: "))
            # diaBund = int(input("\nWhat should the diameter of the vase's buttom be?: "))
            # diaBund /= 2
            # diaTop = int(input("\nWhat should the diameter of the vase's top be?: "))
            # diaTop /= 2
            # diaMin = int(input("\nWhat should the diameter of the vase's thinest spot be?: "))
            # diaMin /= 2
            # diaMinPlace = int(input("\nIn which height should the thinest spot be placed?: "))
            # diaMax = int(input("\nWhat should the diameter of the vase's thickest spot be?: "))
            # diaMax /=2
            # diaMaxPlace = int(input("\nIn which height should the thickest spot be placed?: "))

            h = 18
            diaBund = 10
            diaBund /= 2
            diaTop = 20
            diaTop /= 2
            diaMin = 12
            diaMin /= 2
            diaMinPlace = 12
            diaMax = 16
            diaMax /=2
            diaMaxPlace = 6

            ready = True
        msg = input("\nSkriv her: ")

        if not msg:
            break

        elif msg.startswith("q"):
            break
        
        elif msg.startswith("start"):
            if ready:
                pcList = []
                points = pointify(0, diaBund, diaMaxPlace, diaMax, diaMinPlace, diaMin, h, diaTop)
                # print(points[0], points[1], points[2], points[3])
                cPoints = bezier_control(points[0], points[1], points[2], points[3])
                # print(cPoints[0], cPoints[1], cPoints[2], cPoints[3], cPoints[4], cPoints[5])
                pcList.append(bezier_part(points[0], cPoints[0], cPoints[1], points[1]))
                pcList.append(bezier_part(points[1], cPoints[2], cPoints[3], points[2]))
                pcList.append(bezier_part(points[2], cPoints[4], cPoints[5], points[3]))
                # for i in pcList:
                #     for j in i:
                #         print(j)
                bezier = bezier_curve(pcList, 100)
                pList = bezier[0]
                xs = bezier[1]
                # print(xs)
                ys = bezier[2]
                # print(ys)

                # Numeric integration
                s = trapezPoint(pList)
                print(s)
        elif msg.startswith("plot"):
            plt.plot(xs, ys)
            for i in range(0, len(xs)-1):
                p = [[xs[i], 0], [xs[i], ys[i]], [xs[i+1], ys[i+1]], [xs[i+1], 0]]
                plt.gca().add_patch(Polygon(p, color = '0.8'))
            plt.show()
        else:
            print("\nDu skrev " + str(msg))
    except Exception as e:
        print(e)
        break
print("Tak for nu")