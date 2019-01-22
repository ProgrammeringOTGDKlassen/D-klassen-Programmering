import math

'''
Opgave 8
Tilføjer detaljerede docstrings
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
    Vectorklassen repræsenterer en vector i rummet

    Variable:
    ___
    x:
    y:
    z:

    Metoder:
    ___
    __init()__: Returnerer en vector.
    stedvektor: Retunerer en stedvektor til et punkt.
    forbindende_vektor: Retunerer en forbindende vektor.
    sumvektor: Retunerer summen af to vektorer.
    differens: Retunerer differensen af to vektorer.
    length: Retunerer længden af vektoren, hvor man har en vektor som input. Altså ikke længden mellem to punkter.
    cross_product: Retunerer krydsproduktet af to vektorer (en vektor).
    dot_product: Retunerer krydsproduktet af to vektorer (en vektor).
    __str()__: Laver formatet vektorer udskrives på.
    '''

    def __init__(self, x, y, z):
        '''
        Returnerer en vector.
        '''
        self.x = x
        self.y = y
        self.z = z

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
        return cls(x2 - x1, y2 - y1, z2 - z1)

    # statisk metode som gør at man kan skrive vector.classens navn (vector, da classen hedder "vector")
    @classmethod
    def sumvektor(cls, v1, v2):
        '''
        Retunerer summen af to vektorer.
        '''
        return cls(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    @classmethod
    def differens(cls, v1, v2):
        '''
        Retunerer differensen af to vektorer.
        '''
        return cls(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z)

    # Da det ikke er en @classmethod skal man kalde den som en normal funktion (v.length()) uden nogle parametre i parantesen, da der kun bliver refereret til self
    def length(self):
        '''
        Retunerer længden af vektoren, hvor man har en vektor som input. Altså ikke længden mellem to punkter.
        '''
        l = math.sqrt(self.x**2 + self.y**2 + self.z**2)

        # Formaterer længden af tallet til kun at have 2 decimaler efter kommaet
        l = "{:10.2f}".format(l)

        return l

    @classmethod
    def cross_product(cls, v1, v2):
        '''
        Retunerer krydsproduktet af to vektorer (en vektor).
        '''
        c = cls(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x -
                v1.x * v2.z, v1.x * v2.y - v1.y * v2.x)

        return c

    def dot_product(self, v2):
        '''
        Retunerer krydsproduktet af to vektorer (en vektor).
        '''
        dp = self.x * v2.x + self.y * v2.y + self.z * v2.z

        return dp

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

# Udkommenterer opgave 3
'''
# Definerer den forbindende vektor, v, mellem to punkter vha. funktionen forbindende_vektor() i klassen Vector()
v = Vector.forbindende_vektor(1, 2, 3, 4, 5, 6)
# Printer den forbindende vektor
print("Den forbindende vektor er {}.".format(v))
'''

# Definerer to vektorer, v1 & v1, vha. klassen Vector():
v1 = Vector(1, 2, 3)
v2 = Vector(40, 50, 60)

# Udkommenterer opgave 4
'''
# Definerer summen af de to vektorer vha. funktionen sumvektor() inden i klassen Vektor():
s = Vector.sumvektor(v1, v2)
# Printer summen af de to vektorer
print("Summen af vektorerne {} & {} er {}".format(v1, v2, s))
'''

# Udkommenterer opgave 5
'''
# Definerer differensen af de to vektorer vha. funktionen differens() inden i klassen Vektor():
d = Vector.differens(v1, v2)
# Printer differensen af de to vektorer
print("Differensen af vektorerne {} & {} er {}".format(v1, v2, d))
'''

# Udkommenterer opgave 6
'''
# Definerer længden af vektor 1 & 2 vha. funktionen length() fra klassen Vector():
l1 = v1.length()
l2 = v2.length()
# Printer længden af de to vektorer
print("Længden af vektor 1 er {}".format(l1))
print("Længden af vektor 2 er {}".format(l2))
'''

# Udkommenterer opgave 7
'''
# Definerer krydsproduktet af to vektorer vha. funktionen cross_product() i klassen Vector():
k = Vector.cross_product(v1, v2)
# Printer krydsproduktet
print("Krydsproduktet for vektorerne {} & {} er {}".format(v1, v2, k))

# Definerer prikproduktet af to vektorer vha. funktionen dot_product() i klassen Vector():
prik = v1.dot_product(v2)
# Printer prikproduktet
print("Prikproduktet for vektorerne {} & {} er {}".format(v1, v2, prik))
'''

# Udkommenterer dette, da det er forstyrrende, når vi kører det
'''
print(Point.__doc__)  # Printer docstringen lige efter class Point():
print(Point.__init__.__doc__) # Printer docstringen lige efter __init__(self, x, y, z): under class Point():
print(Vector.__doc__)
print(Vector.__init__.__doc__)
print(Vector.stedvektor.__doc__)
print(Vector.__str__.__doc__)
nemt = True
if nemt == True:
    print("fucking nemt mand")
'''
