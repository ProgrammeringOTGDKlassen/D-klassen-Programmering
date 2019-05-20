import cv2
from math import atan2
from math import sqrt
import math
import numpy as np


img = cv2.imread('4_small.JPG')

def afstand():
    white_pixels = np.array(np.where(img == (255,255,255)))
    first_white_pixel = white_pixels[:,0]
    last_white_pixel = white_pixels[:,-1]
    difference = float(last_white_pixel[0]-first_white_pixel[0])
    print(difference)
    area(difference)
    return first_white_pixel, last_white_pixel

def area(difference):
    radius = difference/2
    areaOfCircle = float(math.pi*radius**2)
    print("Arealet af cirklen er "+str(areaOfCircle))
count = 0
for y,line in enumerate(img):
    for x,pixel in enumerate(line):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
        brightness = (r+g+b)/3
        if (hue < 0.25 or hue > 6.28 - 0.25) and brightness < 95:
            img[y,x] = (255,255,255)
            count += 1
        else:
            img[y,x] = (0,0,0)

print(afstand())

print("Antal pixels i cirklen " + str(count))

cv2.imshow('image', img)
cv2.waitKey(7000)
cv2.destroyAllWindows()

'''
import cv2
from math import atan2
from math import sqrt

img = cv2.imread('58380085_426570451453404_6094751866552320000_n.PNG')

#Punkt på billedet
print(img[10,20])
count = 0
for y,line in enumerate(img):
    for x,pixel in enumerate(line):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
        brightness = (r+g+b)/3
        ran = 1*2*3.1415/360
        if x == 70 and y == 80:
            print(r,g,b,hue)
        if x== 34 and y == 43:
            print(r,g,b,hue)
        if hue < ran and hue > - ran:
            img[y,x] = (255, 255, 255)
            count += 1
        else:
            img[y,x] = (0, 0, 0)
print(count)
cv2.imshow('image', img)
cv2.waitKey(7000)
cv2.destroyAllWindows()

        '''
            
