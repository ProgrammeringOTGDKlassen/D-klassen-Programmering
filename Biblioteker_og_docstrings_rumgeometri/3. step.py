import math

'''
Opgave 3
Tilføjer en funktion til en forbindende vektor
Tlføjer docstrings dertil
Printer docstrings for vektoren
'''


class Point():
    '''
    Repræsenterer et punkt i rummet
    '''

    def __init__(self, x, y, z):
        '''
        Retunerer et punkt
        '''
        self.x = x
        self.y = y
        self.z = z


class Vector():
    '''
    Repræsenterer en vector i rummet
    '''

    def __init__(self, x, y, z):
        '''
        Returnerer en vector
        '''
        self.x = x
        self.y = y
        self.z = z

    # statisk metode som gør at man kan skrive vector.metodens navn (vector, da classen hedder "vector")
    @classmethod
    def stedvektor(cls, p: Point):
        '''
        Retunerer en stedvektor til et punkt.
        '''
        return cls(p.x, p.y, p.z)

    @classmethod
    def forbindende_vektor(cls, x1, y1, z1, x2, y2, z2):
        '''
        Retunerer en forbindende vektor.
        '''
        return cls(x2-x1, y2-y1, z2-z1)

    def __str__(self):
        '''
        Laver formatet vektorer udskrives på.
        '''
        return "({}, {}, {})".format(self.x, self.y, self.z)


# Udkommenterer opgave 2
'''
# Definerer et punkt, p1, vha. klassen Punkt():
p1 = Point(1, 2, 3)
# Definerer en stedvektor, p, vha. funktionen stedvektor() i klassen Vektor():
p = Vector.stedvektor(p1)
# Printer stedvektoren
print("Stedvektoren er {}.".format(p))
'''

# Definerer den forbindende vektor, v, mellem to punkter vha. funktionen forbindende_vektor() i klassen Vector()
v = Vector.forbindende_vektor(1, 2, 3, 4, 5, 6)
# Printer den forbindende vektor
print("Den forbindende vektor er {}.".format(v))


# Udkommenterer dette, da det er forstyrrende, når vi kører det
'''
# Printer docstringen lige efter class Point():
print(Point.__doc__)
# Printer docstringen lige efter __init__(self, x, y, z): under class Point():
print(Point.__init__.__doc__)
# Printer docstringen lige efter class Vector():
print(Vector.__doc__)
# Printer docstringen lige efter __init__(self, x, y, z): under class Vector():
print(Vector.__init__.__doc__)
# Printer docstringen inden i funktionen stedvektor():
print(Vector.stedvektor.__doc__)
# Printer docstringen inden i formateringsfunktionen (___str___():)
print(Vector.__str__.__doc__)
'''
