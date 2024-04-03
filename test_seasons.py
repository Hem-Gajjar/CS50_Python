from seasons import minutes_lived


def main():
    test_1()
    test_2()

def test_1():
    assert minutes_lived(2003,5,17) == "Ten million, nine hundred eighty-four thousand, three hundred twenty minutes"
    assert minutes_lived(2000,2,1) == "Twelve million, seven hundred thirteen thousand, seven hundred sixty minutes"
    # assert minutes_lived(1999,01,01) == "Five hundred twenty-five thousand, six hundred minutes"

def test_2():
    assert minutes_lived(23,1,2000) == "Invalid Date"
if __name__ == "__main__":
    main()
