"""
Python routines to support teaching of MA2812 Cryptology.
"""

# Is this ideal to have this hard-coded both here and in the "pyproject.toml" file?
__version__ = "0.1.0"

from .euclid import gcd, extgcd, inverse_modn
from .primes import brute_factor, factorise, is_prime
from .text import letter_to_code, code_to_letter
from .matrices import Vector, Matrix
from .utils import powmodn
