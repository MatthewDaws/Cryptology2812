import ma2812.euclid
import math, random

def test_gcd():
    assert( ma2812.euclid.gcd(5, 7) == 1 )
    assert( ma2812.euclid.gcd(5, -7) == 1 )
    assert( ma2812.euclid.gcd(10, 14) == 2 )
    assert( ma2812.euclid.gcd(-10, 14) == 2 )

def test_extended_gcd_57():
    d, s, t = ma2812.euclid.extgcd(5, 7)
    assert( d == 1 )
    assert( 5*s + 7*t == 1 )

def test_extended_gcd_57neg():
    d, s, t = ma2812.euclid.extgcd(-5, 7)
    assert( d == 1 )
    assert( (-5)*s + 7*t == 1 )

    d, s, t = ma2812.euclid.extgcd(5, -7)
    assert( d == 1 )
    assert( 5*s + (-7)*t == 1 )

    d, s, t = ma2812.euclid.extgcd(-5, -7)
    assert( d == 1 )
    assert( (-5)*s + (-7)*t == 1 )

def test_extended_gcd_large():
    a, b = 45327645376, 2453768324576
    d, s, t = ma2812.euclid.extgcd(a, b)
    assert( math.gcd(a, b) == d )
    assert( a*s + b*t == d )

def test_extended_gcd_random():
    for _ in range(1000):
        a = random.randrange(-100000, 100000)
        b = random.randrange(-100000, 100000)
        d, s, t = ma2812.euclid.extgcd(a, b)
        assert( math.gcd(a, b) == d )
        assert( a*s + b*t == d )
