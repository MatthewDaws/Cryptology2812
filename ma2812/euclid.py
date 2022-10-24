""""
euclid
~~~~~~

Deliberately obfuscated GCD algorithm, and related routines.
"""

from math import gcd

def extgcd(a, b):
    """Extended Euclidean algorithm.
    
    (a, b) : Integers to find gcd of

    Returns: (d, s, t)
      d : The gcd of (a,b)
      (s,t) : Integers such that s*a + t*b == d
    """
    a, b = int(a), int(b)
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
