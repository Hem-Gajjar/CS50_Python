from seasons import check_dob
from seasons import convert_to_words

def main():
    test_check_dob()
    convert_to_words()

def test_check_dob():
    assert check_dob("1998-07-03") == ("1998","07","03")
    assert check_dob("1998-7-3") == None
    assert check_dob("July 3, 1998") == None



if __name__ == "__main__":
    main()
