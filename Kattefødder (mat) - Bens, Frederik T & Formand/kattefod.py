from math import atan2
from math import sqrt
import cv2


img = cv2.imread('3_small.JPG')

count = 0
for y, line in enumerate(img):
    for x, pixel in enumerate(line):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
        brightness = (r + g + b)/3
        if (hue < 0.15 or hue > 6.28 - 0.15) and brightness < 120:
            img[y, x] = (255, 255, 255)
            count += 1
        else:
            img[y, x] = (0, 0, 0)

print(count)
cv2.imshow('image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
