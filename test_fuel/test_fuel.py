import pytest
try:
    from test_fuel.fuel import convert , gauge

except:
    from fuel import convert , gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('x/y')

def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"

