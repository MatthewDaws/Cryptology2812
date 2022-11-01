import pytest

import ma2812.primes

def test_brute_factor():
    f = ma2812.primes.brute_factor(5)
    assert( f == [5] )

    f = ma2812.primes.brute_factor(1)
    assert( f == [] )

    f = ma2812.primes.brute_factor(-1)
    assert( f == [-1] )

    f = ma2812.primes.brute_factor(-5)
    assert( f == [-1, 5] )

    f = ma2812.primes.brute_factor(2)
    assert( f == [2] )

    f = ma2812.primes.brute_factor(2*2*2)
    assert( f == [2,2,2] )

    f = ma2812.primes.brute_factor(2*3*5*5)
    assert( f == [2,3,5,5] )

    f = ma2812.primes.brute_factor(2*2*3*5*5)
    assert( f == [2,2,3,5,5] )

    f = ma2812.primes.brute_factor(2*2*3*3*3*5)
    assert( f == [2,2,3,3,3,5] )

    f = ma2812.primes.brute_factor(97)
    assert( f == [97] )

    f = ma2812.primes.brute_factor(97*89)
    assert( f == [89,97] )

def test_MillerRabin_sd():
    mr = ma2812.primes.MillerRabin(15)
    assert(mr.d == 7)
    assert(mr.s == 1)

    mr = ma2812.primes.MillerRabin(265)
    assert(mr.d == 33)
    assert(mr.s == 3)

def test_MillerRabin_testing():
    mr = ma2812.primes.MillerRabin(561)

    assert( not mr.run_test(2) )
    assert( mr.last_c_array == [263, 166, 67, 1] )

    assert( not mr.run_test(3) )
    assert( mr.last_c_array == [78, 474, 276, 441] )

    assert( not mr.run_test(4) )
    assert( mr.last_c_array == [166, 67, 1] )

    assert( not mr.run_random_tests(10) )

def test_is_prime():
    assert( ma2812.primes.is_prime(2) )
    assert( ma2812.primes.is_prime(3) )
    assert( ma2812.primes.is_prime(5) )
    assert( ma2812.primes.is_prime(7) )

    assert( not ma2812.primes.is_prime(1) )
    assert( not ma2812.primes.is_prime(4) )
    assert( not ma2812.primes.is_prime(9) )
    assert( not ma2812.primes.is_prime(15) )

    assert( ma2812.primes.is_prime(101749) )

    assert( not ma2812.primes.is_prime(227 * 233) )

def test_factorise_small():
    assert( ma2812.primes.factorise(1) == [] )
    assert( ma2812.primes.factorise(-1) == [-1] )
    assert( ma2812.primes.factorise(2) == [2] )
    assert( ma2812.primes.factorise(8) == [2,2,2] )
    assert( ma2812.primes.factorise(-4) == [-1,2,2] )
    assert( ma2812.primes.factorise(2*3*5*5) == [2,3,5,5] )
    assert( ma2812.primes.factorise(2*2*3*5*5) == [2,2,3,5,5] )
    assert( ma2812.primes.factorise(2*2*3*3*3*5) == [2,2,3,3,3,5] )
    assert( ma2812.primes.factorise(97) == [97] )
    assert( ma2812.primes.factorise(97*89) == [89,97] )

def test_factorise_large():
    assert( ma2812.primes.factorise(15601) == [15601] )
    assert( ma2812.primes.factorise(15601*15773) == [15601, 15773] )
    assert( ma2812.primes.factorise(35933 * 36497) == [35933, 36497] )