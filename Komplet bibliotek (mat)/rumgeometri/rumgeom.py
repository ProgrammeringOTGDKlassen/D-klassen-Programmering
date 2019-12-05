import math
import numpy as np

class Point():
    def __init__(self, coords: list()):
        self.coords = coords


class Vector():
    def __init__(self, coords: list()):
        self.coords = coords

    @classmethod
    def connect(cls, x1, y1, z1, x2, y2, z2, t1 = 0, t2 = 0):
        '''
        Returns a new vector from two points.
        '''
        return cls(x2 - x1, y2 - y1, z2 - z1, t2 - t1)


    @classmethod
    def fromPoint(cls, p: Point):
        '''
        Returns a new vector from a point
        '''
        return cls(p.coords)


    def __add__(self, other):
        if len(other.coords) != len(self.coords):
            raise ValueError("Wrong fucking length, nøøb")
        v = Vector(list())
        for a, b in zip(self.coords, other.coords):
            v.coords.append(a+b)
        return v


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.coords)):
                self.coords[i] = self.coords[i] * other
            return self
        
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors are not the same fucking length, nøøb")
        d = 0
        for i in range(len(self.coords)):
            d += self.coords[i] * other.coords[i]
        return d


    def length(self) -> float: # TODO make more efficient
        l = 0
        for c in self.coords:
            l += math.sqrt(c**2)
        return l


    def __str__(self):
        s = ""
        for c in self.coords:
            s += "{}, ".format(c)
        s = s[:-2]
        return s


class Line():
    def __init__(self, p0, d):
        self.p0 = p0
        self.d = d

    '''
    Factory methods
    '''
    @classmethod
    def createNew(cls, x0, y0, z0, a, b, c):
        '''
        Creates a new Line from a point and a direction vector
        '''
        p0 = Vector(x0, y0, z0)
        d = Vector(a, b, c)
        return cls(p0, d)


    @classmethod
    def createTwoPoints(cls, x1, y1, z1, x2, y2, z2):
        '''
        Creaates a new Line from two points on the line
        '''
        d = Vector(x2 - x1, y2 - y1, z2 - z1)
        p0 = Vector(x1, y1, z1)
        return cls(p0, d)


    def point(self, t: (float, int) = 0) -> Point:
        '''
        Return a point on the line, from a given parameter
        '''
        if not isinstance(t, (float, int)):
            raise TypeError('Parameter is not a valid number')
        p = Vector.fromPoint(self.p0)
        s = scale(t, self.d)
        return add(p, s)


    def getXPoint(self, x):
        '''
        Returns a point on the line, with the given x-getZCoord
        '''
        #Find the correct parameter
        t = (x-self.p0.x) / self.d.x
        return self.point(t)


    def __str__(self):
        return "(x, y, z) = ({}, {}, {}) + t*({}, {}, {})".format(self.p0.x, self.p0.y, self.p0.z, self.d.x, self.d.y, self.d.z)

class Plane():
    '''
    The class describes a plane in space.

    It is created by a point and two direction vectors
    or by three points.

    Attributes
    ----------
    p0 : Vector(x, y, z), where (x, y, z) is a point on the Plane
    d1 : A direction vector for the plane.
    d2 : Another direction vector for the plane. Can not be parallel to d1

    Factory methods
    -------
    createNew(x0, y0, z0, a1, b1, c1, a2, b2, c2)
        Returns a plane through (x0, y0, z0) with
        the direction vectors (a1, b1, c1)^T and (a2, b2, c2)^T

    createThreePoints(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        Returns a plane through the three points
        (x1, y1, z1), (x2, y2, z2) and (x3, y3, z3)


    normal()
        Returns a normal vector to the plane.
        The normal will be a unit vector.
    '''


    def __init__(self, p0, d1, d2):
        self.p0 = p0
        self.d1 = d1
        self.d2 = d2

    '''
    Factory methods
    '''
    @classmethod
    def createNew(cls, x0, y0, z0, a1, b1, c1, a2, b2, c2):
        '''
        Creates a new Plane from a point and two direction vectors
        '''
        p0 = Point(x0, y0, z0)
        d1 = Vector(a1, b1, c1)
        d2 = Vector(a2, b2, c2)
        return cls(p0, d1, d2)


    @classmethod
    def createThreePoints(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        '''
        Creaates a new Line from two points on the line
        '''
        d = np.array([x2 - x1, y2 - y1, z2 - z1])
        p0 = np.array([x1, y1, z1])
        return cls(p0, d)


    def normal(self) -> Vector:
        '''
        Returns a normal unit vector to the plane
        by crossing the two direction vectors
        '''
        return normalize(cross(self.d1, self.d2))


    def isInPlane(self, p) -> bool:
        '''
        Returns True if the point is in the plane,
        and False otherwise.
        '''
        #Testing for zero is done with math.isclose, to avoid rounding/floating point errors.
        #Since we are testing near zero, abs_tol is set to 1e-09
        return math.isclose(math.fabs(dot(self.normal(), Vector.connect(p.x, p.y, p.z, self.p0.x, self.p0.y, self.p0.z))),0, rel_tol=1e-09, abs_tol=1e-09)


    def listZPoints(self, ts, ss):
        Z = []
        for t in ts:
            for s in ss:
                Z.append(self.point(t, s).z)
        return Z


    def getZCoord(self, x, y):
        '''
        Returnerer en z-koordinat i planen, givet x og y.
        '''
        n = self.normal()
        z = (-n.x*(x - self.p0.x) - n.y*(y - self.p0.y) + n.z*self.p0.z) / n.z
        return z


    def point(self, t: (float, int) = 0, s: (float, int) = 0) -> Vector:
        '''
        Returns a point on the plane, from two given parameters
        '''
        p = Vector.fromPoint(self.p0)
        s1 = scale(t, self.d1)
        s2 = scale(s, self.d2)
        return add(add(p, s1), s2)


    def __str__(self):
        return "(x, y, z) = ({}, {}, {}) + t*({}, {}, {}) + s*({}, {}, {})".format(self.p0.x, self.p0.y, self.p0.z, self.d1.x, self.d1.y, self.d1.z, self.d2.x, self.d2.y, self.d2.z)


def scale(s: (float, int), v: Vector) -> Vector:
    '''
    Returns a copy of v, scaled by s.
    '''
    coords = list()
    res = Vector(coords)
    for i in range(len(v.coords)):
        res.coords[i] *= s
    return res


def normalize(v: Vector) -> Vector: # Function is fucked TODO
    '''
    Returns a unit-vector in the direction v
    '''
    if v.length() > 0.000001:
        s = 1 / v.length()
        return scale(s,v)
    else:
        return Vector(list([0 for i in range(len(v.coords))]))


def cross(v1: Vector, v2: Vector) -> Vector: # Function is fucked TODO
    '''
    Returns the cross product of v1 and v2
    '''
    if len(v1.coords) != 3 or len(v2.coords) != 3:
        raise ValueError("Vectors have to be 3 fucking D, nøøb")
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vector(x, y, z)


def angle(v1: Vector, v2: Vector) -> float:
    '''
    Returns the angle in degrees between v1 and v2
    '''
    return math.degrees(math.acos((v1 * v2) / (v1.length() * v2.length())))


def distancePointPlane(p: Point, a: Plane) -> float:
    #The distance between the point and the plane is
    # the absolute value of the dot product between
    # the unit normal vector of the plane, and the projection
    # of a vector connecting the point to the plane, onto that unit
    # normal vectors
    return math.fabs((a.normal() * Vector.connect(p.x, p.y, p.z, a.p0.x, a.p0.y, a.p0.z)))


def intersect(l: Line, p: Plane) -> Point:
    '''
    Calculates the intersection between a Line and a Plane.
    Returns None if the two arguments are parallel.
    '''
    if math.isclose((l.d * p.normal()), 0):
        #If the line direction is perpendicular to the plane normal,
        # the line and plane must be parallel.
        return None
    else:
        #There exists a parameter t, which makes
        # p.isInPlane(l.point(t)) == 0
        #Let's find it.
        #Initial guess
        t1 = 1
        p1 = l.point(t1)
        d1 = distancePointPlane(p1, p)
        t2 = 2
        p2 = l.point(t2)
        d2 = distancePointPlane(p2, p)

        #Calculate line through the two points (t,d)
        a = (d2 - d1) / (t2 - t1)
        b = d1 - a * t1

        #Find the t-value where d is zero
        # 0 = at+b <=> t = -b/a
        t = -b / a
        print('parameter: {}'.format(t))
        return l.point(t)


class Matrix():
    '''
    The class describes a matrix in space.

    It is created by a list of vectors.
    All vectors have 4 elements. (4D)

    Attributes
    ----------
    vectors : list(Vector(x, y, z, t), Vector(x, y, z, t), Vector(x, y, z, t), Vector(x, y, z, t)), where (x, y, z, t) is a point on the Plane
    m : The length of the matrix. The amount of vectors in the list of vectors

    Magic methods
    -------
    __str__()
        Defines the string representation of a matrix.
        Rows and columns are printed in the right positions.
    
    __add__()
        Magic method for addition in python. Two matrices can be added with +.
        
    
    __mul__()
        Magic method for multiplication, so matrices can be multiplied with the standard * operator.
        
    

    Factory methods
    -------
    equal_size(other)
        returns true, if one the self matrix is of equal size as the other matrix.
    '''


    def __init__(self, vectors: list()): # List of vectors
        prev = None
        for v in vectors:
            if prev == None:
                continue
            if len(v.coords) != len(prev.coords):
                raise ValueError("Vectors have to be same length in Matrix")
            prev = v
        
        self.vectors = vectors
        
        self.m = len(self.vectors) # Antal rækker
        self.n = len(self.vectors[0].coords) # Antal kolonner

    def __str__(self):
        '''
        Defines the string representation of a matrix.
        Rows and columns are printed in the right positions.
        '''
        s = ""
        for v in self.vectors:
            s += str(v) + "\n"
        return s

    def __add__(self, other):
        '''
        Magic method for addition in python. Two matrices can be added with +.
        '''
        if not isinstance(other, Matrix) or not self.equal_size(other):
            raise ValueError("Can only add two Matrix objects with same dimensions")
        
        vectors = list()
        for i in range(self.m):
            v1 = self.vectors[i]
            v2 = other.vectors[i]
            vectors.insert(i, v1 + v2)
        return Matrix(vectors)


    def __mul__(self, other):
        '''
        Magic method for multiplication, so matrices can be multiplied with the standard * operator.
        '''
        if isinstance(other, Vector):
            # Matrix vector product
            v = Vector(list())
            for n in range(len(other.vectors)):
                v += scale(other.vectors[n][n], self.vectors[n])
            return v
        elif isinstance(other, Matrix):
            # Matrix matrix product
            if self.n != other.m:
                raise ValueError("Wrong fucking sizes, nøøb")

            selfVectors = self.vectors
            selfColVectors = self.transpose()
            otherVectors = other.vectors
            otherColVectors = other.transpose()
            vectors = list()
            for col in range(other.n):
                cordinator = []

                for row in range(self.m):
                    coord = 0

                    for k in range(other.m):
                        coord += selfVectors[row].coords[k] * otherColVectors.vectors[col].coords[k]
                    
                    cordinator.append(coord)
                
                v = Vector(cordinator)
                vectors.append(v)
            matrix = Matrix(vectors)
            matrix = matrix.transpose()
            return matrix
        elif isinstance(other, int) or isinstance(other, float): # Skalering af matrix
            for i in range(len(self.vectors)):
                self.vectors[i] *= other
        else:
            raise ValueError("Can only multiply Matrix with Matrix, Vector, Integer or Float")


    @classmethod
    def identity_matrix(cls, s: int):
        '''
        Arguments:
        s: (int) size of matrix

        Returns:
        (Matrix) identity matrix

        Static method for generating identity matrix containing zeroes and a diagonal of ones.
        '''
        if not isinstance(s, int):
            raise ValueError("Size can only be an Integer")

        vectors = list()
        for i in range(s):
            v = Vector([0 for i in range(s)])
            v.coords[i] = 1
            vectors.append(v)
        return Matrix(vectors)


    def transpose(self):
        '''
        Swaps 
        '''
        vectors = list()
        for col in range(self.n):
            vRes = Vector(list())
            for row in range(self.m):
                v = self.vectors[row]
                vRes.coords.insert(row,v.coords[col])
            vectors.append(vRes)
        m = Matrix(vectors)
        return Matrix(vectors)

    # <Row Operations>
    def row_swap(self, row1:int, row2:int):
        '''
        Swaps row 1 and row 2, and returns the resulting matrix
        '''
        if row1 >= self.m or row2 >= self.m:
            raise ValueError("Given rows are outside the bounds of the matrix")
        v1 = self.vectors[row1]
        v2 = self.vectors[row2]
        self.vectors[row1] = v2
        self.vectors[row2] = v1
        return self
    
    def row_scale(self, row, scalar):
        '''
        Scales a row
        '''
        if self.row > self.m:
            raise ValueError("Given row is outside the bounds of the matrix")
        self.vectors[row] *= scalar
        return self

    def scaled_row_addition(self, row1, row2, scalar):
        '''
        Scales row1 and adds it to row2, returns the resulting matrix
        '''
        if row1 >= self.m or row2 >= self.m:
            raise ValueError("Given rows are outside the bounds of the matrix")
        vScaled = self.vectors[row1] * scalar
        self.vectors[row2] = vScaled + self.vectors[row2]
        return self
    # </Row Operations>
    
    
    def append_column(self, vector):
        if len(vector.coords) != self.n:
            raise ValueError("Vector needs to match the height of the Matrix")

        for i in range(len(vector.coords)):
            self.vectors[i].coords.append(vector.coords[i])
        return self

    # https://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/
    def gauss(self):
        for i in range(0, self.m):
            # Search for maximum in this column
            maxEl = abs(self.vectors[i].coords[i])
            maxRow = i
            for k in range(i+1, self.m):
                if abs(self.vectors[k].coords[i]) > maxEl:
                    maxEl = abs(self.vectors[k].coords[i])
                    maxRow = k

            # Swap maximum row with current row (column by column)
            for k in range(i, self.m+1):
                tmp = self.vectors[maxRow].coords[k]
                self.vectors[maxRow].coords[k] = self.vectors[i].coords[k]
                self.vectors[i].coords[k] = tmp

            # Make all rows below this one 0 in current column
            for k in range(i+1, self.m):
                c = -self.vectors[k].coords[i]/self.vectors[i].coords[i]
                for j in range(i, self.m+1):
                    if i == j:
                        self.vectors[k].coords[j] = 0
                    else:
                        self.vectors[k].coords[j] += c * self.vectors[i].coords[j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(self.m)]
        for i in range(self.m-1, -1, -1):
            x[i] = self.vectors[i].coords[self.m]/self.vectors[i].coords[i]
            for k in range(i-1, -1, -1):
                self.vectors[k].coords[self.m] -= self.vectors[k].coords[i] * x[i]

        result = Matrix.identity_matrix(self.n-1).append_column(Vector(x))
        return result
    # </Row Operations>

    def equal_size(self, other):
        """
        Returns True if self and other have same dimensions
        """
        if not isinstance(other, Matrix):
            raise ValueError("Can only compare two matrices")
        return other.m == self.m and other.n == self.n

    # Til robotten
    def get_rotation_matrix(self, angleX, angleY, angleZ):
        v1 = Vector(math.cos(angleZ)*math.cos(angleY), math.sin(angleZ)*math.cos(angleY), -1*math.sin(angleY))
        v2 = Vector(math.cos(angleZ)*math.sin(angleY)*math.sin(angleX)-math.sin(angleZ)*math.cos(angleX), math.sin(angleZ)*math.sin(angleY)*math.sin(angleX)+math.cos(angleZ)*math.cos(angleX), math.cos(angleY)*math.sin(angleX))
        v3 = Vector(math.cos(angleZ)*math.sin(angleY)*math.cos(angleX)+math.sin(angleZ)*math.sin(angleX), math.sin(angleZ)*math.sin(angleY)*math.cos(angleX)-math.cos(angleZ)*math.sin(angleX), math.cos(angleY)*math.cos(angleX))

        return Matrix([v1, v2, v3])
