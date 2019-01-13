import math

'''
Opgave 2 
Tilføjer en funktion til vektorklassen
Printer docstringsne
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

    def __str__(self):
        '''
        Laver formatet vektorer udskrives på.
        '''
        return "({}, {}, {})".format(self.x, self.y, self.z)


# Definerer et punkt, p1, vha. klassen Punkt():
p1 = Point(1, 2, 3)
# Definerer en stedvektor, p, vha. funktionen stedvektor() i klassen Vektor():
p = Vector.stedvektor(p1)
# Printer stedvektoren
print("Stedvektoren er {}.".format(p))

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
