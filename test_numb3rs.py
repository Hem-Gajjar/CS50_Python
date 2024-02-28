try:
    from numb3rs import validate
except:
    from numb3rs import validate

def test_one():
    assert validate("2.2.2.2")
    assert validate("0.0.0.0")

def test_two():
    assert validate("22.22.22.22")

def test_three():
    assert validate("222.222.222.222")
    assert validate("223.224.225.226")
    assert validate("553.224.225.226")

def test_four():
    assert validate("2222.2222.2222.2222")
