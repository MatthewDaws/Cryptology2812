"""
Python routines to support teaching of MA2812 Cryptology.
"""

# Is this ideal to have this hard-coded both here and in the "pyproject.toml" file?
__version__ = "0.1.0"

from .euclid import gcd, extgcd, inverse_modn
