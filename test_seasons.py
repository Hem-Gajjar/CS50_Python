from seasons import check_dob

def main():
    test_check_dob()

def test_check_dob():
    assert check_dob("2004-09-10") == ("2004","09","10")
    assert check_dob("2004-9-9") == None
    assert check_dob("September 10, 2004") == None

if __name__ == "__main__":
    main()
