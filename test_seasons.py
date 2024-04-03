from seasons import check_dob
from seasons import convert_to_words

def main():
    test_check_dob()
    test_convert_to_words()

def test_check_dob():
    assert check_dob("2004-09-10") == ("2004","09","10")
    assert check_dob("2004-9-9") == None
    assert check_dob("September 10, 2004") == None

def test_convert_to_words():
    convert_to_words("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    convert_to_words("1999-12-31") == "One thousand, four hundred forty minutes"
    convert_to_words("1970-01-01") == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"

if __name__ == "__main__":
    main()
