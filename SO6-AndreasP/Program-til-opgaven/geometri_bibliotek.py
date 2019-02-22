import math


class Point():
    '''
    Repræsenterer et punkt i rummet
    '''

    def __init__(self, x, y, ):
        '''
        Retunerer et punkt
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Laver formatet punkterne udskrives på.
        '''
        return "({}, {})".format(self.x, self.y)


class Vector2D():
    def __init__(self, x, y):
        '''
        Returnerer en vector.
        '''
        self.x = x
        self.y = y

    @classmethod
    def stedvektor(cls, p: Point):
        '''
        Retunerer en stedvektor til et punkt.
        '''
        return cls(p.x, p.y)

    @classmethod
    def forbindende_vektor(cls, x1, y1, x2, y2):
        '''
        Retunerer en forbindende vektor.                                                                
        '''
        return cls(x2 - x1, y2 - y1)

    def length(self):
        '''
        Retunerer længden af vektoren, hvor man har en vektor som input. Altså ikke længden mellem to punkter.
        '''
        l = math.sqrt(self.x**2 + self.y**2)

        return l

    def __str__(self):
        '''
        Laver formatet vektorer udskrives på.
        '''
        return "({}, {})".format(self.x, self.y)
