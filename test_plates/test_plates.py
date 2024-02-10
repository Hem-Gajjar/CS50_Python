try:
    from test_plates.plates import is_valid
except:
    from plates import is_valid

def test_first_two_letters():
    assert is_valid("50CS") == False
    assert is_valid("CS50") == True

def test_no_of_char():
    assert is_valid("50ABCDEFGHI") == False
    assert is_valid("H") == False
    assert is_valid("HG10") == True

def test_number_in_middle():
    assert is_valid("H50CS") == False

def test_no_at_last():
    assert is_valid("CS50") == True

def test_first_no_zero():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("CS.50") == False


