try:
    from numb3rs import validate
except:
    from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.1.1")== False
    assert validate(r"1.1")== False
    assert validate(r"1")== False


def test_range():
    assert validate(r"255.255.255.255")==True
    assert validate(r"0.0.0.0")==True
    assert validate(r"500.2.2.2")==False
    assert validate(r"2.500.2.2")==False
    assert validate(r"2.2.500.2")==False
    assert validate(r"2.2.2.500")==False


if __name__ == "__main__":
    main()
