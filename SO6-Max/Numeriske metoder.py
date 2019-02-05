import math
import matplotlib.pyplot as plt
'''
print('___________________________')
print('Øvelse 1')
print('___________________________')
print(math.ceil(5.7))
print(math.ceil(1.3))
print(math.ceil(-5.7))
print(math.ceil(-1.3))
print(math.floor(5.7))
print(math.floor(1.3))
print(math.floor(-5.7))
print(math.floor(-1.3))

print('___________________________')
print('Øvelse 2')
print('___________________________')
print(math.exp(0))
print(math.exp(1))
print(math.exp(10))

print('___________________________')
print('Øvelse 3')
print('___________________________')
print(math.log10(100))
print(math.log(math.e**2))
print(math.log2(8))
print(math.log10(1000))
print(math.log2(256))
print(math.log(54.598))

print('___________________________')
print('Øvelse 4')
print('___________________________')
print(7*math.tan(math.radians(27.5)))

print('___________________________')
print('Øvelse 5')
print('___________________________')
def rum(h, r):
    return math.pi * h * r ** 2
print(rum(5, 2))

print('___________________________')
print('Øvelse 6')
print('___________________________')
def function(x, a, b, c):
    return a * x ** 2 + b * x + c
print(function(5, 1, 3, 4))

print('___________________________')
print('Øvelse 7')
print('___________________________')
# Opret liste
l1 = list(range(1, 21))
# Manuel oprettelse
# # xs = [0,1,2,3]
# Gennemløb en liste
for x in l1:
    print(x ** 2)

print('___________________________')
print('Øvelse 10')
print('___________________________')
def funxs(xs):
    resultlist = []
    for x in xs:
        result = 2 * x ** 2 + 2
        resultlist.append(result)
    return resultlist
print(funxs([1, 2, 3, 4, 5]))

print('___________________________')
print('Øvelse 11')
print('___________________________')
def fx(lx, lp):
    f = 0
    resultlist = []
    for x in lx:
        for p in lp:
            f += p * x ** lp.index(p)
        resultlist.append(f)
    return resultlist

print(fx([1, 2, 3],[4, 5, 6]))

print('___________________________')
print('Øvelse 12')
print('___________________________')
xs = [1, 2, 3, 4, 5, 6]
ys = [1, 4, 9, 16, 25, 36]

plt.plot(xs,ys, 'b*')
plt.xlabel("x")
plt.ylabel("y=x^2")
plt.title("Plot of y=x^2")
plt.show()

print('___________________________')
print('Øvelse 13')
print('___________________________')
xs = [1, 2, 3, 4, 5, 6]
ys = [1, 4, 9, 16, 25, 36]

plt.plot(xs,ys, 'go-')
plt.xlabel("x")
plt.ylabel("y=x^2")
plt.title("Plot of y=x^2")
plt.show()

print('___________________________')
print('Øvelse 14')
print('___________________________')
f14 = 0
xListe = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yListe = []

for x in xListe:
    f14 += 2 * x**3 - 3 * x**2 + 5
    yListe.append(f14)

import matplotlib.pyplot as plt
plt.plot(xListe, yListe, 'go-')
plt.xlabel("x")
plt.ylabel("y=2x^3 - 3x^2 + 5")
plt.title("Plot of y=2x^3 - 3x^2 + 5")
plt.show()
'''
print('___________________________')
print('Øvelse 15')
print('___________________________')

def linspace(a, b, n):
    liste = []
    interval = (b - a) / (n-1)
    for i in range(0, n):
        liste.append(a + i * interval)
    return liste

print(linspace(1, 100, 7))
'''
print('___________________________')
print('Ekstraopgave 1')
print('___________________________')
def high_low(list1):
    high = list1[0]
    low = list1[0]
    highplacement = 0
    lowplacement = 0
    for elm in list1:
        if elm > high:
            high = elm
            highplacement = list1.index(elm) + 1
        if elm < low:
            low = elm
            lowplacement = list1.index(elm) + 1

    print('Det højeste tal er {} og det er tal nummer {} i listen, det laveste tal er {} og det er tal nummer {} i listen'.format(high, highplacement, low, lowplacement))

high_low([1,2,3])
print('___________________________')
print('Ekstraopgave 2')
print('___________________________')
'''

