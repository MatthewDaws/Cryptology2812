from multiprocessing.sharedctypes import Value
import pytest
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

def test_extended_gcd_zero():
    d, s, t = ma2812.euclid.extgcd(7, 0)
    assert( d==7 )
    assert( 7*s == 7 )

    d, s, t = ma2812.euclid.extgcd(0, 1)
    assert( d==1 )
    assert( t == 1 )

    with pytest.raises(ValueError):
        ma2812.euclid.extgcd(0, 0)

def random_pairs_not_zero(count, low, high):
    for _ in range(count):
        a = random.randrange(low, high)
        b = random.randrange(low, high)
        if a==0 and b==0:
            continue
        yield a, b

def test_extended_gcd_random():
    for a, b in random_pairs_not_zero(1000, -100000, 100000):
        d, s, t = ma2812.euclid.extgcd(a, b)
        assert( math.gcd(a, b) == d )
        assert( a*s + b*t == d )

def test_inverse_modn():
    y = ma2812.euclid.inverse_modn(5, 17)
    assert( y>=0 and y<17 and (5*y)%17 == 1 )

    for x, n in random_pairs_not_zero(1000, 1, 100000):
        if math.gcd(x, n) != 1:
            with pytest.raises(ValueError):
                ma2812.euclid.inverse_modn(x, n)
            continue
        y = ma2812.euclid.inverse_modn(x, n)
        assert( y>=0 and y<n and (x*y) % n == 1 )

def test_inverse_modn_notcoprime():
    with pytest.raises(ValueError):
        ma2812.euclid.inverse_modn(5, 15)

