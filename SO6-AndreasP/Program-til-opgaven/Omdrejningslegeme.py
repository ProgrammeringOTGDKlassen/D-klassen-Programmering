import math
# import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.pyplot import Polygon
# import bezier
from geometri_bibliotek import Point
from geometri_bibliotek import Vector2D


def linespace(n, a, b):
    liste = []
    interval = (b - a) / n
    for i in range(n):
        liste.append(a + interval)
        a += interval
        i = i
    return liste


def trapez(n, a, b, f):
    s = 0
    x = linespace(n, a, b)

    for i in range(0, n-1):
        dx = x[i + 1] - x[i]
        h = 0.5 * (f(x[i + 1]) + f(x[i]))
        s += dx * h
    return s


def trapezPoint(pList):
    '''
    Takes a list of points and calculates the integral using the trapez-method in the space between each point.
    '''
    last = 0
    for i in range(0, len(pList) - 1):
        new = (pList[i + 1].x - pList[i].x)/2 * (pList[i].y + pList[i + 1].y)
        last += new
    return last


def area_solid_of_revolution(pList):
    '''
    Left cylinder
    Takes a list of points and calculates the area solid of revolution in the space between each point.
    '''
    last = 0
    for i in range(0, len(pList)-1):
        new = 2 * math.pi * pList[i].y * (pList[i + 1].x - pList[i].x)
        last += new
    return last


def area_solid_of_revolution_right(pList):
    '''
    Right cylinder
    Takes a list of points and calculates the area solid of revolution in the space between each point.
    '''
    last = 0
    for i in range(0, len(pList)-1):
        new = 2 * math.pi * pList[i+1].y * (pList[i + 1].x - pList[i].x)
        last += new
    return last

# def area_solid_of_revolution_trapez(pList):
#     '''
#     Trapez
#     Takes a list of points and calculates the area solid of revolution in the space between each point.
#     '''
#     last = 0
#     for i in range(0, len(pList)-1):
#         fv = Vector2D.forbindende_vektor(pList[i].x, pList[i].y, pList[i+1].x, pList[i+1].y)
#         lenFV = Vector2D.length(fv)
#         new = math.pi * (pList[i].y + pList[i+1].y) * lenFV
#         last += new
#     return last


def area_solid_of_revolution_trapez(pList):
    '''
    Trapez
    Takes a list of points and calculates the area solid of revolution in the space between each point.
    '''
    last = 0
    for i in range(0, len(pList)-1):
        new = math.pi * (pList[i].y + pList[i+1].y) * (
            math.sqrt((pList[i + 1].x - pList[i].x)**2 + (pList[i+1].y - pList[i].y)**2))
        last += new
    return last

# def volume_solid_of_revolution(pList):
#     last = 0
#     for i in range(0, len(pList)-1):
#             new = ???
#             last += new
#     return last


def pointify(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Takes an amount of points and returns them in a list of pointlists like this: [[p1x, p1y], [p2x, p2y]].
    '''
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)
    compiled = [p1, p2, p3, p4]
    return compiled


def vectify(p):
    return Vector2D.stedvektor(p)


def bezier_control(p1, p2, p3, p4):
    '''
    Creates controlpoints for 3 cubic bezier curves. The points are predetermined to create a specific kind of vase.
    '''
    p1c1p2 = Point(p1.x + (p2.x - p1.x)/5, p1.y + (p2.y - p1.y)/2)
    p1c2p2 = Point(p2.x - (p2.x - p1.x)/2, p2.y)
    p2c1p3 = Point(p2.x + (p2.x - p1.x)/2, p2.y)
    p2c2p3 = Point(p3.x - (p3.x - p2.x)/4, p3.y)
    p3c1p4 = Point(p3.x + (p3.x - p2.x)/4, p3.y)
    p3c2p4 = Point(p4.x, p4.y - (p4.y - p3.y)/2)
    compiled = [p1c1p2, p1c2p2, p2c1p3, p2c2p3, p3c1p4, p3c2p4]
    return compiled


def bezier_part(p1, c1, c2, p2):
    '''
    Takes two points and the two controlpoints between them and makes it a set in a list.
    '''
    compiled = []
    compiled.append(p1)
    compiled.append(c1)
    compiled.append(c2)
    compiled.append(p2)
    return compiled


def bezier_curve(pcList, index):
    '''
    Takes a list of bezier parts and a index for how many points of the curve to create and returns a pointlist and a list of x- and y-koordinates.
    It is using the formula for the cubic bezier curve.
    '''
    tIndex = 1/index
    t = 0
    xList = []
    yList = []
    pList = []

    for p in pcList:
        for i in range(0, index):
            x = (1 - t)**3 * p[0].x + 3 * (1 - t)**2 * t * \
                p[1].x + 3*(1-t) * t**2 * p[2].x + t**3 * p[3].x
            y = (1 - t)**3 * p[0].y + 3 * (1 - t)**2 * t * \
                p[1].y + 3*(1-t) * t**2 * p[2].y + t**3 * p[3].y

            xList.append(x)
            yList.append(y)

            point = Point(x, y)
            pList.append(point)

            t += tIndex
        t = 0

    return pList, xList, yList


ready = False

# Dictionary
cmd = {}
cmd["Quits the program."] = "q"
cmd["Gets a list of commands."] = "help"
cmd["Takes your dimensions for a vase to prepare for calculating."] = "setup"
cmd["Calculates the mass of the vase based on the setup."] = "start"
cmd["Plots a graf of half of the vase."] = "plot"
cmd["Resets the setup."] = "reset"

print("\nWrite 'help' for a list of commands!")

while True:
    try:
        msg = input("\nSkriv her: ")

        if not msg:
            break

        elif msg.startswith("q"):
            break

        elif msg.startswith("help"):
            print("")
            counter = 1
            for name in cmd:
                print(counter, "-", "command: " + cmd[name], " - ", name)
                counter += 1

        elif msg.startswith("setup"):
            '''
            How tall will the vase be?: 500

            What should the diameter of the vase's buttom be?: 100

            What should the diameter of the vase's top be?: 200

            What should the diameter of the vase's thinest spot be?: 60

            In which height should the thinest spot be placed?: 400

            What should the diameter of the vase's thickest spot be?: 300

            In which height should the thickest spot be placed?: 200
            '''

            # unit = input(
            # "\nWhat unit will you be using for the measurements?: ")

            # h = int(input("\nHow tall will the vase be?: "))
            # diaBund = int(
            #     input("\nWhat should the diameter of the vase's buttom be?: "))
            # diaBund /= 2
            # diaTop = int(
            #     input("\nWhat should the diameter of the vase's top be?: "))
            # diaTop /= 2
            # diaMin = int(
            #     input("\nWhat should the diameter of the vase's thinest spot be?: "))
            # diaMin /= 2
            # diaMinPlace = int(
            #     input("\nIn which height should the thinest spot be placed?: "))
            # diaMax = int(
            #     input("\nWhat should the diameter of the vase's thickest spot be?: "))
            # diaMax /= 2
            # diaMaxPlace = int(
            #     input("\nIn which height should the thickest spot be placed?: "))

            h = 18
            diaBund = 10
            diaBund /= 2
            diaTop = 20
            diaTop /= 2
            diaMin = 12
            diaMin /= 2
            diaMinPlace = 12
            diaMax = 16
            diaMax /= 2
            diaMaxPlace = 6

            ready = True

        elif msg.startswith("start"):
            if ready:
                pcList = []
                # Takes the requirements from the user and converts it to points.
                points = pointify(0, diaBund, diaMaxPlace,
                                  diaMax, diaMinPlace, diaMin, h, diaTop)
                # Creates the bezier controlpoints for the 4 points above
                cPoints = bezier_control(
                    points[0], points[1], points[2], points[3])
                # Adds the 3 bezier parts to a list of them
                pcList.append(bezier_part(
                    points[0], cPoints[0], cPoints[1], points[1]))
                pcList.append(bezier_part(
                    points[1], cPoints[2], cPoints[3], points[2]))
                pcList.append(bezier_part(
                    points[2], cPoints[4], cPoints[5], points[3]))
                # Gets the list of bezier parts and creates a list of points on the bezier curve of the vase.
                bezier = bezier_curve(pcList, 1000)
                pList = bezier[0]
                xs = bezier[1]
                ys = bezier[2]

                # # Numeric integration
                # ni = trapezPoint(pList)
                # print(ni)

                # Something
                a = area_solid_of_revolution(pList)
                a1 = area_solid_of_revolution_right(pList)
                forskelVH = abs(a1-a)
                a2 = area_solid_of_revolution_trapez(pList)
                forskelVT = abs(a-a2)
                forskelHT = abs(a1-a2)
                gennemsnitForskel = (forskelHT + forskelVT)/2
                # aTotal = a + math.pi * diaBund**2
                # a1Total = a1 + math.pi * diaBund**2
                # a2Total = a2 + math.pi * diaBund**2
                # thickness = float(input("\nHow thick should the vase be?: "))
                # aTotal *= thickness
                # a1Total *= thickness
                # a2Total *= thickness
                # print("\nThe volume of the material is {} {}^2".format(aTotal, unit))
                # print("\nThe volume of the material is {} {}^2".format(a1Total, unit))
                # print("\nThe volume of the material is {} {}^2".format(a2Total, unit))

                print("\nThe volume of the material with left is {}".format(a))
                print("\nThe volume of the material with right is {}".format(a1))
                print("\nThe volume of the material with trapez is {}".format(a2))
                print("\nForskel på venstre og højre {}".format(forskelVH))
                print("Forskel på gennemsnit højre og venstre og trapez {}".format(
                    gennemsnitForskel))
            else:
                print("\nPlease setup first!")

        elif msg.startswith("plot"):
            # Plots the points of the bezier curve using matplotlib.pyplot
            plt.plot(xs, ys)
            for i in range(0, len(xs)-1):
                p = [[xs[i], 0], [xs[i], ys[i]], [
                    xs[i+1], ys[i+1]], [xs[i+1], 0]]
                plt.gca().add_patch(Polygon(p, color='0.8'))
            plt.show()

        elif msg.startswith("reset"):
            ready = False
            print("\nThe setup has been reset.")

        else:
            print("\nDu skrev " + str(msg))

    except Exception as e:
        print(e)
        break


print("Tak for nu")
