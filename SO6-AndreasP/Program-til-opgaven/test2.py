import math
# import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.pyplot import Polygon
# import bezier
from geometri_bibliotek import Point
from geometri_bibliotek import Vector2D


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

def area_solid_of_revolution_trapez(pList):
    '''
    Trapez
    Takes a list of points and calculates the area solid of revolution in the space between each point.
    '''
    last = 0
    for i in range(0, len(pList)-1):
        fv = Vector2D.forbindende_vektor(pList[i].x, pList[i].y, pList[i+1].x, pList[i+1].y)
        lenFV = Vector2D.length(fv)
        new = math.pi * (pList[i].y + pList[i+1].y) * lenFV
        last += new
    return last

# def area_solid_of_revolution_trapez(pList):
#     '''
#     Trapez
#     Takes a list of points and calculates the area solid of revolution in the space between each point.
#     '''
#     last = 0
#     for i in range(0, len(pList)-1):
#         new = math.pi * (pList[i].y + pList[i+1].y) * (math.sqrt((pList[i + 1].x - pList[i].x)**2 + (pList[i+1].y - pList[i].y)**2))
#         last += new
#     return last

pList = [Point(3, 4), Point(5, 7)]

a = area_solid_of_revolution(pList)
a1 = area_solid_of_revolution_right(pList)
a2 = area_solid_of_revolution_trapez(pList)

print(a)
print(a1)
print(a2)