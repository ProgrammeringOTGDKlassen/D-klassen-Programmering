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
    def connecting_vector(cls, x1, y1, x2, y2):
        return cls(x2 - x1, y2 - y1)
    
    @classmethod
    def sumvektor(cls, v1, v2):
        '''
        Retunerer summen af to vektorer.
        '''
        return cls(v1.x + v2.x, v1.y + v2.y)
    
    def __str__(self):
        '''
        Laver formatet vektorer udskrives på.
        '''
        return "({}, {})".format(self.x, self.y)
