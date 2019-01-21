import math


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
    vec2_vinkel: Retunerer vinklen mellem to vektorer.
    proj_vec: Retunerer projektionen af en vektor på en anden vektor.
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

    def vec2_vinkel(self, v2):
        '''
        Retunerer vinklen mellem to vektorer.
        '''

        v = (self.x * v2.x + self.y * v2.y + self.z * v2.z) / (math.sqrt((self.x) **
                                                                         2 + (self.y)**2 + (self.z)**2) * math.sqrt((v2.x)**2 + (v2.y)**2 + (v2.z)**2))

        v = math.degrees(math.acos(v))

        return v

    @classmethod
    def proj_vek(cls, v1, v2):
        '''
        Retunerer projektionen af en vektor på en anden vektor.
        '''

        skalar = (v1.x * v2.x + v1.y * v2.y + v1.z * v2.z) / \
            (math.sqrt((v2.x)**2 + (v2.y)**2 + (v2.z)**2))
        proj = cls(skalar * v2.x, skalar * v2.y, skalar * v2.z)

        return proj

    def __str__(self):
        '''
        Laver formatet vektorer udskrives på.
        '''
        return "({}, {}, {})".format(self.x, self.y, self.z)

    @classmethod
    def prik(cls, x1, y1, z1, x2, y2, z2) -> float:
        '''
        Returnerer prikproduktet af to vektorer
        '''
        return x1*x2+y1*y2+z1*z2

    @classmethod
    def scale(cls, v1, s):
        return cls(v1.x * s, v1.y * s, v1.z * s)


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
v2 = Vector(1, 2, 3)

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

# Udkommenterer opgave 9
'''
# Definerer vinklen mellem to vektorer vha. funktionen vec2_vinkel() i klassen Vector():
vin = v1.vec2_vinkel(v2)
# Printer vinklen
print("Vinklen mellem {} & {} er {}".format(v1, v2, vin))

# Definerer projektionen af v1 på v2 vha. fuktionen proj_vec() i klassen Vector():
proj = Vector.proj_vek(v1, v2)
# Printer projektionen
print("Projektionen af {} på {} er {}".format(v1, v2, proj))
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

# Herfra kommer opgaverne 10-18 om linjer:

'''
Opgave 16
     Tilføj en funktion til at baregne afstanden mellem to linjer.
     Tilføj docstrings.
     Print docstringen for afstanden.       
'''


class Line():
    '''
    Line klassen ræpresentere en linje i rummet
    '''

    def __init__(self, p0, r):

        self.p0 = p0
        self.r = r

    @classmethod
    def create(cls, p0, r):
        '''
        Laver en linje udfra et punkt og en retningsvektor
        '''
        p0 = Vector(p0.x, p0.y, p0.z)
        r = Vector(r.x, r.y, r.z)
        return Line(p0, r)

    @classmethod
    def parameter_line_two_points(cls, x1, y1, z1, x2, y2, z2):
        '''
        Laver en linje ud fra to punkter                    
        '''

        # Vi tager den forbindende vektor mellem de to punkter
        r = Vector(x2 - x1, y2 - y1, z2 - z1)
        p0 = Vector(x1, y1, z1)
        return Line(p0, r)

    def point(self, t: (float, int) = 0) -> Vector:
        '''
        Laver en stedvektor til et punkt, så skalerer den en anden vektor med en konstant og lægger den sammen med stedvektoren.
        '''
        p = Vector.stedvektor(self.p0)
        s = Vector.scale(self.r, t)
        return Vector.sumvektor(p, s)

    def line2_vinkel(self, l2):
        '''
        Beregner vinklen mellem to linjer
        '''
        r1 = self.r
        r2 = l2.r
        v = r1.vec2_vinkel(r2)
        return v

    def len_point_to_line(self, p):
        '''
        Beregner længden mellem et punkt og en linje
        '''
        p0p = Vector.forbindende_vektor(
            self.p0.x, self.p0.y, self.p0.z, p.x, p.y, p.z)
        tællerVector = Vector.cross_product(p0p, self.r)
        tæller = tællerVector.length()

        dist = float(tæller) / float(self.r.length())

        return dist

    def len_line_to_line(self, l):
        '''
        Beregner længden mellem en linje og en anden linje
        '''
        n = Vector.cross_product(self.r, l.r)
        p1p2 = Vector.forbindende_vektor(
            self.p0.x, self.p0.y, self.p0.z, l.p0.x, l.p0.y, l.p0.z)
        tæller = float(n.dot_product(p1p2))
        if tæller < 0:
            tæller *= -tæller
        dist = tæller / float(n.length())

        return dist

    def __str__(self):
        '''
        Laver parameterfremstillingn for en linje udfra p0 og en retningsvektor
        '''
        return "(x, y, z) = {} + t * {}".format(self.p0, self.r)


# Udkommentrere opgave 10
'''
print(Line.__doc__)
print(Line.__init__.__doc__)
print(Line.create.__doc__)
'''

# Udkommenterer opgave 11
'''
p0 = Vector(69, 420, 720)
r = Vector(7, 8, 9)
l = Line.create(p0, r)
print(Line.__str__.__doc__)
print("Linjen gennem punktet {} med retningsvektor {} er {}".format(p0, r, l))
'''

# Udkommenterer opgave 12
'''
m = Line.parameter_line_two_points(37, 74, 93, 102, 70, 30)
print("Printer en linjes parameterfremstilling {}".format(m))
'''
# Udkommenterer opgave 13
'''
l = Line(Point(0,0,0),Vector(1,2,3))
print(l.point(2.3))
'''


# Udkommenterer opgave 14
'''
m1 = Line.parameter_line_two_points(37, 74, 93, 102, 70, 30)
m2 = Line.parameter_line_two_points(1, 2, 3, 4, 5, 6)
vinkel = m1.line2_vinkel(m2)
print(vinkel)
'''

# Udkommenterer opgave 15
'''
p0 = Vector(69, 420, 720)
l = Line(Point(0, 0, 0), Vector(1, 2, 3))
længde = l.len_point_to_line(p0)
print(længde)
'''

l1 = Line(Point(0, 0, 0), Vector(1, 2, 3))
l2 = Line.parameter_line_two_points(37, 74, 93, 102, 70, 30)
længde = l1.len_line_to_line(l2)
print(længde)
