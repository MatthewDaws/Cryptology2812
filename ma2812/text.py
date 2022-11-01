"""
text
~~~~

Very simple code to convert to/from the "basic alpha numeric code".
"""

def letter_to_code(x):
    """Converts (the first letter of) `x` using the basic alpha numeric code."""
    s = str(x)[0]
    n = ord(s) - ord("a")
    if n < 0 or n > 25:
        raise ValueError("{} -> '{}' is not a lower-case letter".format(x, s))
    return n

def code_to_letter(n):
    """Converts the number `n` to a character, using the basic alpha numeric code."""
    n = int(n)
    if n < 0 or n > 25:
        raise ValueError("{} is not in the range 0--25".format(n))
    return chr(n + ord("a"))
