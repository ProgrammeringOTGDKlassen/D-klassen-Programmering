import math


class Point():
    '''
    Represents a point in space
    '''

    def __init__(self, x, y):
        '''
        Returns a point
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Creates the format for the points
        '''
        return "({}, {})".format(self.x, self.y)


class Vector2D():
    def __init__(self, x, y):
        '''
        Returns a vector
        '''
        self.x = x
        self.y = y

    @classmethod
    def stedvektor(cls, p: Point):
        '''
        Returns a Position (vector) for a point
        '''
        return cls(p.x, p.y)

    @classmethod
    def forbindende_vektor(cls, x1, y1, x2, y2):
        '''
        Returns a connecting vector                                                                
        '''
        return cls(x2 - x1, y2 - y1)

    def length(self):
        '''
        Returns the length of a vector
        '''
        l = math.sqrt(self.x**2 + self.y**2)

        return l

    def __str__(self):
        '''
        Creates the format for the vectors
        '''
        return "({}, {})".format(self.x, self.y)
