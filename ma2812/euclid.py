""""
euclid
~~~~~~

Deliberately obfuscated GCD algorithm, and related routines.
"""

from math import gcd
from operator import inv

def extgcd(a, b):
    """Extended Euclidean algorithm.
    
    (a, b) : Integers to find gcd of

    Returns: (d, s, t)
      d : The gcd of (a,b)
      (s,t) : Integers such that s*a + t*b == d

    Raises: ValueError if a==b==0
    """
    a, b = int(a), int(b)
    if a==0 and b==0:
        raise ValueError("gcd(0,0) is undefined")
    nega, negb = 1, 1
    if a < 0:
        nega, a = -1, -a
    if b < 0:
        negb, b = -1, -b
    s, ss, t, tt  = 1, 0, 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        s, ss = ss, s - q*ss
        t, tt = tt, t - q*tt
    return a, s*nega, t*negb

def inverse_modn(x, n):
    """Compute the inverse of `x` modulo `n` or Raises ValueError."""
    d, s, t = extgcd(x, n)
    if d != 1:
        raise ValueError(f"{x} is not invertible modulo {n}")
    return s % n