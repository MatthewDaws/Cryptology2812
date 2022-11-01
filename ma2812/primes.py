"""
primes
~~~~~~

Primality testing and factorisation.
"""

from .utils import powmodn
import random as _random

def _factor_step_one(n):
    """Extract -1 and 2 factors, returns (partial_factors_list, current_n)"""
    n = int(n)
    factors = []
    if n < 0:
        factors.append(-1)
        n = -n
    while n%2 == 0 and n > 1:
        factors.append(2)
        n = n // 2
    return factors, n

def brute_factor(n):
    """Brute force factorisation
    
    n: The number to factorise

    Returns: List of factors
    """
    factors, n = _factor_step_one(n)
    p = 3
    while n > 1 and p*p <= n:
        if n%p == 0:
            factors.append(p)
            n = n // p
        else:
            p+=2
    if n>1:
        factors.append(n)
    return factors

class MillerRabin:
    def __init__(self, n):
        self._n = int(n)
        if self._n % 2 == 0:
            raise ValueError("Value is even!")
        self._d = self._n - 1
        self._s = 0
        while self._d % 2 == 0:
            self._d = self._d // 2
            self._s += 1

    @property
    def s(self):
        return self._s

    @property
    def d(self):
        return self._d

    def run_test(self, b):
        """Perform a test with a fixed value of 'b'.
        
        Returns: True if probably prime; False if definitely not prime."""
        self._carray = []
        self._carray.append( powmodn(b, self._d, self._n) )
        if self._carray[0] == 1 or self._carray[0] == self._n-1:
            return True
        index = 1
        while index < self._s:
            self._carray.append( (self._carray[index-1]**2) % self._n )
            if self._carray[index] == self._n-1:
                return True
            if self._carray[index] == 1:
                return False
            index += 1
        return False

    @property
    def last_c_array(self):
        return self._carray

    def run_random_tests(self, loops):
        for _ in range(loops):
            b = _random.randrange(1, self._n)
            result = self.run_test(b)
            if not result:
                return False
        return True


def is_prime(n):
    """Checks if `n` is prime.
    
    Uses small trial division, and then 10 loops of Miller-Rabin."""
    n = int(n)
    if n<0:
        n = -n
    if n == 0 or n==1:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    p = 3
    while p<300 and p*p<=n:
        if n%p == 0:
            return False
        p += 2
    mr = MillerRabin(n)
    return mr.run_random_tests(10)

def factorise(n):
    """Attempts to intelligently factorise `n`."""
    factors, n = _factor_step_one(n)
    p, target_p = 3, 10000
    while n > 1:
        n_sqrt = int(n**0.5)
        while p < target_p and p <= n_sqrt:
            if n%p == 0:
                factors.append(p)
                n = n//p
                n_sqrt = int(n**0.5)
            else:
                p += 2
        if MillerRabin(n).run_random_tests(10):
            factors.append(n)
            return factors
        target_p += target_p
    return factors
