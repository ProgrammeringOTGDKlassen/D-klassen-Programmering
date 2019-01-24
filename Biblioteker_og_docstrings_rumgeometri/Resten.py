import math


class Angle():
    pass


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

    def __str__(self):
        '''
        Laver formatet punkterne udskrives på.
        '''
        return "({}, {}, {})".format(self.x, self.y, self.z)


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

        return float(l)

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
            tæller *= -1
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


class PlaneWithEquation():
    def __init__(self, a, b, c, d):
        '''
        Retunerer en plan med planens ligning.   
        '''
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @classmethod
    def create_plane_equation(cls, x0, y0, z0, a1, b1, c1, a2, b2, c2):
        p0 = Point(x0, y0, z0)
        r1 = Vector(a1, b1, c1)
        r2 = Vector(a2, b2, c2)

        plane = Plane(p0, r1, r2)

        n = plane.normal()

        a = n.x
        b = n.y
        c = n.z
        d = (n.x*(-plane.p0.x) + n.y*(-plane.p0.y) + n.z*(-plane.p0.z))

        return cls(a, b, c, d)

    @classmethod
    def plane_equation(cls, pl):
        n = pl.normal()

        a = n.x
        b = n.y
        c = n.z
        d = (n.x*(-pl.p0.x) + n.y*(-pl.p0.y) + n.z*(-pl.p0.z))

        return cls(a, b, c, d)

    def __str__(self):
        return "{} * x + {} * y + {} * z + {} = 0".format(self.a, self.b, self.c, self.d)


class Plane():
    '''
    Klassen beskriver en plan i rummet. 

    Planen laves ud fra et punkt og to retningsvektorer eller ud fra tre punkter. 

    Attributes
    ---------
    p0 : Vector(x,y,z), hvor (x,y,z) er et punkt i planen. 
    r1 : En retningsvektor for planen. 
    r2 : En anden retningsvektor for planen. Må ikke være parallel med r1.
    '''

    def __init__(self, p0, r1, r2):
        '''
        Retunerer en plan.   
        '''
        self.p0 = p0
        self.r1 = r1
        self.r2 = r2

    '''
    Factory methods
    '''

    @classmethod
    def create_plane(cls, x0, y0, z0, a1, b1, c1, a2, b2, c2):
        '''
        Laver en plan ud fra 9 tal.
        '''
        p0 = Point(x0, y0, z0)
        r1 = Vector(a1, b1, c1)
        r2 = Vector(a2, b2, c2)

        return cls(p0, r1, r2)

    @classmethod
    def parameter_plane_three_points(cls, p1, p2, p3):
        '''

        Laver en plan ud fra tre punkter                    
        '''

        # Vi tager den forbindende vektor mellem de to punkter
        r1 = Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
        r2 = Vector(p3.x - p1.x, p3.y - p1.y, p3.z - p1.z)
        p0 = Vector(p1.x, p1.y, p1.z)

        return Plane(p0, r1, r2)

    def normal(self) -> Vector:
        '''
        Retunerer en vector
        '''
        return Vector.cross_product(self.r1, self.r2)

    @classmethod
    def angle_planes(cls, pl1, pl2) -> Angle:
        '''
        Finder vinklen mellem to planer.
        '''
        n1 = pl1.normal()
        n2 = pl2.normal()

        tæller = n1.dot_product(n2)
        nævner = float(n1.length()) * float(n2.length())

        cosw = tæller / nævner

        w = math.degrees(math.acos(cosw))

        if w >= 90:
            w = 180 - w
        else:
            pass

        return w

    def point_in_plane(self, t, s):
        '''
        Retunerer et punkt i planen efter s og t værdierne suppleret
        '''
        v1 = Vector(self.r1.x * t, self.r1.y * t, self.r1.z * t)
        v2 = Vector(self.r2.x * t, self.r2.y * t, self.r2.z * t)

        point = Point(self.p0.x + v1.x + v2.x, self.p0.y +
                      v1.y + v2.y, self.p0.z + v1.z + v2.z)

        return point

    @classmethod
    def intersection_line_plane(cls, pl, l):
        '''
        Retunerer punktet for skæringen mellem en linje og en plan
        '''
        plEQ = pl.plane_equation()

        tæller = - plEQ.a * l.p0.x - plEQ.b * l.p0.y - plEQ.c * l.p0.z - plEQ.d
        nævner = plEQ.a * l.r.x + plEQ.b * l.r.y + plEQ.c * l.r.z

        t = tæller / nævner

        return Point(l.p0.x + t * l.r.x, l.p0.y + t * l.r.y, l.p0.z + t * l.r.z)

    def plane_equation(self):
        '''
        Retunerer planensligning med funktionalitet: man kan tage a, b, c og d ud fra planen ved f.eks. at sige plan.a eller plan.b
        '''
        return PlaneWithEquation.plane_equation(self)

    @classmethod
    def proj_point_plane(cls, pl, p):
        n = pl.normal()
        line = Line(p, n)

        proj = Plane.intersection_line_plane(pl, line)

        return proj

    @classmethod
    def proj_line_plane(cls, pl, l):
        '''
        Retunerer en projektion af en linje i en plan
        '''
        op = Plane.intersection_line_plane(pl, l)
        n = pl.normal()
        rl = l.r
        projvv = Vector.proj_vek(n, rl)
        projLP = Vector(rl.x - projvv.x, rl.y - projvv.y, rl.z - projvv.z)
        final = Line(op, projLP)

        return final

    def __str__(self):
        '''
        Laver formatet for en parameterfremstilling for en plan i rummet.       
        '''
        return "(x, y, z) = {} + t * {} + s * {}".format(self.p0, self.r1, self.r2)


'''
pl = Plane.create_plane(1, 2, 3, 4, 5, 6, 7, 8, 9)

p = Point(1, 2, 3)

print(Plane.proj_point_plane(pl, p))
'''
