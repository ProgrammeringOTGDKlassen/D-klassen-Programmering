from math import atan2
from math import sqrt
from math import pi
import cv2


img = cv2.imread('red and white/3.png')

hvideKoordinater = []
centrumLinje = []
startVinkel = 90

count = 0
for y, line in enumerate(img):
    for x, pixel in enumerate(line):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        hue = atan2(sqrt(3)*(g-b), 2*r-g-b)
        brightness = (r + g + b)/3
        if (hue < 0.15 or hue > 6.28 - 0.15) and brightness < 186:
            img[y, x] = (255, 255, 255)
            count += 1
            hvideKoordinater.append([x, y])
        else:
            img[y, x] = (0, 0, 0)


def afstand(pixels):
    return 631.72*(1/(pixels)**0.46956)


def areal_af_cirkel(hvideKoordinater):
    førsteHvideKoordinat = hvideKoordinater[0]
    sidsteHvideKoordinat = hvideKoordinater[-1]
    cirkelHøjde = sidsteHvideKoordinat[1] - førsteHvideKoordinat[1]
    radius = cirkelHøjde/2
    return pi * radius**2


def forhold_fra_koordinater(hvideKoordinater):
    førsteHvideKoordinat = hvideKoordinater[0]
    sidsteHvideKoordinat = hvideKoordinater[-1]
    cirkelHøjde = sidsteHvideKoordinat[1] - førsteHvideKoordinat[1]
    centrum = int(førsteHvideKoordinat[1] + cirkelHøjde/2)

    for i in hvideKoordinater:
        if i[1] == centrum:
            centrumLinje.append(i)

    førstePixelBredde = centrumLinje[0]
    andenPixelBredde = centrumLinje[-1]
    cirkelBredde = andenPixelBredde[0] - førstePixelBredde[0]

    forhold = cirkelHøjde/cirkelBredde
    return forhold


def vinkel_fra_forhold(forhold):
    pass


afstandTilVinkel = afstand(areal_af_cirkel(hvideKoordinater))


print(afstandTilVinkel)
cv2.imshow('image', img)
cv2.waitKey(4000)
cv2.destroyAllWindows()
