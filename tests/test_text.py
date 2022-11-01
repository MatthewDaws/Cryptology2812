import pytest
import ma2812.text

def test_to_code():
    assert( ma2812.text.letter_to_code("a") == 0 )
    assert( ma2812.text.letter_to_code("c") == 2 )
    assert( ma2812.text.letter_to_code("z") == 25 )
    assert( ma2812.text.letter_to_code("bcd") == 1 )

def test_to_code_out_of_range():
    with pytest.raises(ValueError):
        ma2812.text.letter_to_code(" ")
    with pytest.raises(ValueError):
        ma2812.text.letter_to_code("A")
    with pytest.raises(ValueError):
        ma2812.text.letter_to_code(5)

def test_to_letter():
    assert( ma2812.text.code_to_letter(0) == "a" )
    assert( ma2812.text.code_to_letter(1) == "b" )
    assert( ma2812.text.code_to_letter(25) == "z" )

def test_to_letter_out_of_range():
    with pytest.raises(ValueError):
        ma2812.text.code_to_letter(-1)
    with pytest.raises(ValueError):
        ma2812.text.code_to_letter(26)
