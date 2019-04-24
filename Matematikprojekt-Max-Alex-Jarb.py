import cv2
from math import atan2
from math import sqrt
'''
img = cv2.imread('filename.jpg')

print(img[width,height])

count = 0
for y,line in enumerate(img):
    for x,pixel in enumerate(line):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
        if hue < 0.5 or hue > 6.28 - 0.5:
            img[y,x] = (255, 255, 255)
        else:
            img[y,x] = (0, 0, 0)
            count += 1
print(count)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''