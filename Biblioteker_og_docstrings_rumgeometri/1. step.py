import math

'''
Opgave 1
Undersøger hvilken print-linje der printer hvilken docstring
Laver docstrings til Vector() og printer dem
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


# Printer docstringen lige efter class Point():
print(Point.__doc__)
# Printer docstringen lige efter __init__(self, x, y, z): under class Point():
print(Point.__init__.__doc__)
# Printer docstringen lige efter class Vector():
print(Vector.__doc__)
# Printer docstringen lige efter __init__(self, x, y, z): under class Vector():
print(Vector.__init__.__doc__)

nemt = True
if nemt == True:
    print("fucking nemt mand")
