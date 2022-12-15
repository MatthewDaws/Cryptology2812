"""
utils
~~~~~

Various useful routinues, including large integer powers.
"""

def powmodn(x, k, n):
    """Computes `(x**k)%n` quickly.  The builtin `pow` command can also do this, of course..."""
    x0, k0, n, y = int(x), int(k), int(n), 1
    if k0 < 0:
        raise ValueError("Cannot compute negative powers.")
    while k0 > 0:
        if k0 & 1 == 0:
            k0 >>= 1
            x0 = (x0*x0) % n
        else:
            k0 -= 1
            y = (y*x0) % n
    return y
