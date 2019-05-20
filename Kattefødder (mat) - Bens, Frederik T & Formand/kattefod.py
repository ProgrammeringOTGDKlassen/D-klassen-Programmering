from math import atan2
from math import sqrt
from math import pi
import cv2

img = cv2.imread('new pictures/Vinkler/Vinkler cropped/DSC_0067.JPG')

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


def afstand1(pixels):
    return 631.72*(1/(pixels)**0.46956)


def afstand(pixels):  # Den funktion vi går med!
    return 536.22*(1/(pixels)**0.47936)


def afstand3(pixels):
    return 476.63*(1/(pixels)**0.46544)


def areal_af_cirkel(hvideKoordinater):  # Den metode vi går med!
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


afstandTilVinkel = afstand(areal_af_cirkel(hvideKoordinater))


print('Afstand med højde: {}'.format(afstandTilVinkel))
print('Antal pixels beregnet: {}'.format(areal_af_cirkel(hvideKoordinater)))
print('Standard afstand: {}'.format(afstand(count)))
print('Antal pixels: {}'.format(count))
cv2.imshow('image', img)
cv2.waitKey(4000)
cv2.destroyAllWindows()
