import pytest
try:
    from test_fuel.fuel import convert , gauge
except:
    from fuel import convert , gauge

# def main():
    # test_correct_input()
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"


# if __name__ == "__main__":
#     main()
