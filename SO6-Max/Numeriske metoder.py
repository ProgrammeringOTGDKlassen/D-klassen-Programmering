import math
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
print(funxs([1, 2, 3, 4]))