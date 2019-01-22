import math

'''
Opgave 6
Tilføjer en funktion til længden af en vektorer
Tilføjer docstrings dertil
Begræns længden af et tal med to tal efter kommaet
Printer docstrings for længden af en vektor
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
        Tager summen af to vektorer.
        '''
        return cls(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    @classmethod
    def differens(cls, v1, v2):
        '''
        Tager differensen af to vektorer.
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
# Definerer summen af de to vektorer vha funktionen sumvektor() inden i klassen Vektor():
s = Vector.sumvektor(v1, v2)
# Printer summen af de to vektorer
print("Summen af vektorerne {} & {} er {}".format(v1, v2, s))
'''

# Udkommenterer opgave 5
'''
# Definerer differensen af de to vektorer vha funktionen differens() inden i klassen Vektor():
d = Vector.differens(v1, v2)
# Printer differensen af de to vektorer
print("Differensen af vektorerne {} & {} er {}".format(v1, v2, d))
'''

# Definerer længden af vektor 1 & 2 vha. funktionen length() fra klassen Vector():
l1 = v1.length()
l2 = v2.length()
# Printer længden af de to vektorer
print("Længden af vektor 1 er {}".format(l1))
print("Længden af vektor 2 er {}".format(l2))

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
