"""
matrices
~~~~~~~~

Basic matrix support: 2x2 matrices modulo a number
"""

from .euclid import gcd, inverse_modn

class Vector():
    def __init__(self, n, value=[0,0]):
        self._n = int(n)
        try:
            self._val = [None, None]
            for i in range(2):
                self._val[i] = int(value[i]) % n
        except:
            raise ValueError("Initial value does not appear to be a 2x2 matrix")

    @property
    def modulus(self):
        return self._n

    def entry(self, i):
        return self._val[i]

    def __eq__(self, other):
        if self.modulus != other.modulus:
            return False
        return all( self.entry(i) == other.entry(i) for i in range(2) )

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError()
        if self.modulus != other.modulus:
            raise ValueError("Cannot add vectors of different modulus.")

        entries = [None,None]
        for i in range(2):
                entries[i] = self.entry(i) + other.entry(i)
        return Vector(self._n, entries)

    def __rmul__(self, other):
        try:
            mult = int(other)
        except:
            raise TypeError("Can only multiply by an integer")
        entries = [None,None]
        for i in range(2):
                entries[i] = mult * self.entry(i)
        return Vector(self._n, entries)

    def __str__(self):
        return f"[{self._val[0]}, {self._val[1]}]"

    def __repr__(self):
        return f"Vector({str(self)})"


class Matrix():
    def __init__(self, n, value=[[0,0],[0,0]]):
        self._n = int(n)
        try:
            self._val = [[0,0], [0,0]]
            for i in range(2):
                for j in range(2):
                    self._val[i][j] = int(value[i][j]) % n
        except:
            raise ValueError("Initial value does not appear to be a 2x2 matrix")
    
    @property
    def modulus(self):
        return self._n

    def entry(self, i, j):
        return self._val[i][j]

    def is_identity(self):
        return (self.entry(0,0) == 1 and self.entry(0,1) == 0 and
            self.entry(1,0) == 0 and self.entry(1,1) == 1)

    @property
    def determinant(self):
        d = (self.entry(0,0) * self.entry(1,1)) - (self.entry(1,0) * self.entry(0,1))
        return d % self._n

    def is_invertible(self):
        return gcd(self._n, self.determinant) == 1

    def inverse(self):
        mult = inverse_modn(self.determinant, self._n)
        a = mult * self.entry(1,1)
        b = -mult * self.entry(0,1)
        c = -mult * self.entry(1,0)
        d = mult * self.entry(0,0)
        return Matrix(self._n, [[a,b], [c,d]])

    def __eq__(self, other):
        if self.modulus != other.modulus:
            return False
        return all( self.entry(i,j) == other.entry(i,j) for i in range(2) for j in range(2) )

    def __mul__(self, other):
        if type(other) == Vector:
            if self.modulus != other.modulus:
                raise ValueError("Cannot multiply matrices of different modulus.")
            entries = [None,None]
            for i in range(2):
                entries[i] = self.entry(i,0)*other.entry(0) + self.entry(i,1)*other.entry(1)
            return Vector(self._n, entries)

        if type(self) != type(other):
            raise TypeError()
        if self.modulus != other.modulus:
            raise ValueError("Cannot multiply matrices of different modulus.")

        entries = [[None,None], [None,None]]
        for i in range(2):
            for j in range(2):
                entries[i][j] = self.entry(i,0)*other.entry(0,j) + self.entry(i,1)*other.entry(1,j)
        return Matrix(self._n, entries)

    def __rmul__(self, other):
        try:
            mult = int(other)
        except:
            raise TypeError("Can only multiply by an integer")
        entries = [[None,None], [None,None]]
        for i in range(2):
            for j in range(2):
                entries[i][j] = mult * self.entry(i,j)
        return Matrix(self._n, entries)
        
    def __str__(self):
        return "[[{}, {}], [{}, {}]]".format(self.entry(0,0), self.entry(0,1),
            self.entry(1,0), self.entry(1,1))

    def __repr__(self):
        return "Matrix({})".format(str(self))
