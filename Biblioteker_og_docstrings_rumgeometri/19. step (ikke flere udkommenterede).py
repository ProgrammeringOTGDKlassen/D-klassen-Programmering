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


class Line():
    '''
    Line klassen ræpresentere en linje i rummet

    Variable:
    ___
    p0:
    r:

    Metoder:
    ___
    __init()__: Returnerer en linje.
    create: Laver en linje udfra et punkt og en retningsvektor
    parameter_line_two_points: Laver en linje ud fra to punkter 
    point: Laver en stedvektor til et punkt, så skalerer den en anden vektor med en konstant og lægger den sammen med stedvektoren.
    line2_vinkel: Beregner vinklen mellem to linjer
    len_point_to_line: Beregner længden mellem et punkt og en linje
    len_line_to_line: Beregner længden mellem en linje og en anden linje
    proj_point_on_line: Beregner projektionen af et punkt på en linje
    __str()__: Laver parameterfremstillingn for en linje udfra p0 og en retningsvektor
    '''

    def __init__(self, p0, r):
        '''
        Returnerer en linje.
        '''
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

    def proj_point_on_line(self, p):
        '''
        Beregner projektionen af et punkt på en linje
        '''
        p0p = Vector.forbindende_vektor(
            p.x, p.y, p.z, self.p0.x, self.p0.y, self.p0.z)
        tæller = float(p0p.dot_product(self.r))
        skalar = tæller / float(self.r.length())**2
        proj = Vector(skalar * self.r.x, skalar * self.r.y, skalar * self.r.z)

        return proj

    def __str__(self):
        '''
        Laver parameterfremstillingn for en linje udfra p0 og en retningsvektor
        '''
        return "(x, y, z) = {} + t * {}".format(self.p0, self.r)


'''
Opgave 19
    *Beskrivelse*
'''
