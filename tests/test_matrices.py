from typing import Type
import pytest

import ma2812.matrices

def test_Vector_construct():
    m = ma2812.matrices.Vector(5)
    assert( m.modulus == 5 )
    assert( m.entry(0) == 0 and m.entry(1) == 0 )

    m = ma2812.matrices.Vector(5, [-2, 7])
    assert( m.entry(0) == 3 and m.entry(1) == 2 )

    with pytest.raises(ValueError):
        ma2812.matrices.Vector(5, None)

    assert( str(m) == "[3, 2]" )
    assert( m.__repr__() == "Vector([3, 2])" )

def test_Vector_equality():
    v1 = ma2812.matrices.Vector(5)

    v2 = ma2812.matrices.Vector(5, [0,0])
    assert( v1==v2 )

    v2 = ma2812.matrices.Vector(5, [1,2])
    assert( v1!=v2 )

def test_Vector_scalar_mult():
    v = ma2812.matrices.Vector(5, [-2, 7])
    vv = 3 * v
    ve = ma2812.matrices.Vector(5, [4, 1])
    assert( vv == ve )

def test_Vector_add():
    v = ma2812.matrices.Vector(7, [1, 3])
    v1 = ma2812.matrices.Vector(7, [4, 3])
    assert( v+v1 == ma2812.matrices.Vector(7, [5, 6]) )

def test_Vector_access():
    v = ma2812.matrices.Vector(7, [1, 3])
    assert( v[0] == 1 )
    assert( v[1] == 3 )

    with pytest.raises(IndexError):
        v[2]
    with pytest.raises(IndexError):
        v[-1]

def test_Vector_set():
    v = ma2812.matrices.Vector(7, [1, 3])
    v[0] = 5
    assert( v[0] == 5 )

def test_Vector_to_list():
    v = ma2812.matrices.Vector(7, [1, 3])
    assert( list(v) == [1,3] )

def test_Matrix_construct():
    m = ma2812.matrices.Matrix(5)
    assert( m.modulus == 5 )
    
    assert( m.entry(0,0) == 0 )
    assert( m.entry(0,1) == 0 )
    assert( m.entry(1,0) == 0 )
    assert( m.entry(1,1) == 0 )

    assert( not m.is_identity() )

    m = ma2812.matrices.Matrix(7, [[1,0], [0,1]])
    assert( m.modulus == 7 )
    
    assert( m.entry(0,0) == 1 )
    assert( m.entry(0,1) == 0 )
    assert( m.entry(1,0) == 0 )
    assert( m.entry(1,1) == 1 )

    assert( m.is_identity() )

    with pytest.raises(ValueError):
        ma2812.matrices.Matrix(5, None)
    with pytest.raises(ValueError):
        ma2812.matrices.Matrix(5, [1,2])

@pytest.fixture
def m():
    return ma2812.matrices.Matrix(7, [[1,3], [4,2]])

def test_Matrix_repr(m):
    assert( str(m) == "[[1, 3], [4, 2]]")
    assert( m.__repr__() == "Matrix([[1, 3], [4, 2]])" )

def test_Matrix_Inverses(m):
    m1 = ma2812.matrices.Matrix(5)
    assert( m1.determinant == 0 )
    assert( not m1.is_invertible() )

    assert( m.determinant == ((2-12)%7) )
    assert( m.is_invertible() )
    mi = m.inverse()
    assert( mi.entry(0,0) == 4 )
    assert( mi.entry(0,1) == 1 )
    assert( mi.entry(1,0) == 6 )
    assert( mi.entry(1,1) == 2 )

def test_Matrix_access(m):
    assert( m.entry(0,0) == 1 )
    assert( m.entry(1,0) == 4 )
    with pytest.raises(IndexError):
        m.entry(-1, 0)
    with pytest.raises(IndexError):
        m.entry(0, 2)

def test_Matrix_Equality(m):
    mi = m.inverse()

    emi = ma2812.matrices.Matrix(7, [[4,1], [6,2]])
    assert( mi == emi )
    
    assert( mi != m )

    emi = ma2812.matrices.Matrix(5, [[4,1], [6,2]])
    assert( mi != emi )

def test_Matrix_mult(m):
    mi = m.inverse()

    x = m*mi
    assert( x.is_identity() )
    x = mi*m
    assert( x.is_identity() )

    mm = ma2812.matrices.Matrix(7, [[2,6], [4,5]])
    x = m*mm
    ex = ma2812.matrices.Matrix(7, [[0,0], [2,6]])
    assert( x == ex )

def test_Matrix_mult_cannot(m):
    m1 = ma2812.matrices.Matrix(4, [[1,3], [4,2]])
    with pytest.raises(ValueError):
        m * m1

    with pytest.raises(TypeError):
        m * 5

def test_Matrix_mult_scalar(m):
    x = 5*m
    ex = ma2812.matrices.Matrix(7, [[5, 15], [20,10]])
    assert( x == ex )

def test_Matrix_Vector_mult(m):
    v = ma2812.matrices.Vector(7, [-2, 7])
    assert( m*v == ma2812.matrices.Vector(7, [5,6]) )

    v = ma2812.matrices.Vector(5, [-2, 7])
    with pytest.raises(ValueError):
        m*v
