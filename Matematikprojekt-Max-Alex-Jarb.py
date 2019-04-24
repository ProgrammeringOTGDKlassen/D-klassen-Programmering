import cv2
from math import atan2
from math import sqrt

img = cv2.imread('Udklip.JPG')

#Punkt på billedet
print(img[10,20])
count = 0
while True:
    try:
        msg = input("Spurgt: ")
        if msg == "start":
            for y,line in enumerate(img):
                for x,pixel in enumerate(line):
                    r = int(pixel[0])
                    g = int(pixel[1])
                    b = int(pixel[2])
                    hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
                    brightness = (r+g+b)/3
                    if hue < 0.15 or hue > 6.28 - 0.15 and brightness < 100:
                        img[y,x] = (255, 255, 255)
                        count += 1
                    else:
                        img[y,x] = (0, 0, 0)
            print(count)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            msg = input("Spurgt: ")
        if msg == "quit":
            break
    except Exception as e:
        print(e)
print("Sut min dut")
            
