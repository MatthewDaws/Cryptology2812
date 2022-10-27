import pytest
 
import ma2812.utils

def test_powmodn_ones():
    assert( ma2812.utils.powmodn(1,5,7) == 1 )
    assert( ma2812.utils.powmodn(1,5,9) == 1 )
    assert( ma2812.utils.powmodn(1,131234,121) == 1 )

def test_powmodn():
    assert( ma2812.utils.powmodn(3,2,11) == 9 )
    assert( ma2812.utils.powmodn(3,2,5) == 4 )

def test_powmodn_corners():
    with pytest.raises(ValueError):
        ma2812.utils.powmodn(2, -3, 7)

    assert( ma2812.utils.powmodn(2, 0, 7) == 1 )