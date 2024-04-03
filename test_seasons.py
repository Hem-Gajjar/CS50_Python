from seasons import convert
def main():
    test_date()

def test_date():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"

if __name__ == "__main__":
    main()
