"""
utils
~~~~~

Various useful routinues, including large integer powers.
"""

def powmodn(x, k, n):
    """Computes `(x**k)%n` quickly."""
    x0, k0, n, y = int(x), int(k), int(n), 1
    if k0 < 0:
        raise ValueError("Cannot compute negative powers.")
    while k0 > 0:
        if k0 % 2 == 0:
            k0 = k0 // 2
            x0 = (x0*x0) % n
        else:
            k0 -= 1
            y = (y*x0) % n
    return y
