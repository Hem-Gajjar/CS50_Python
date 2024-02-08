from twttr import shorten


def main():
    test_normal()
    # test_capital()
    # test_number()
    # test_pun()

def test_normal():
    assert shorten("twitter") == "twttr"
    assert shorten("hem") == "hm"

def test_capital():
    assert shorten("hEm") == "hm"

def test_number():
    assert shorten("h3m") == "h3m"

# def test_pun():
#     assert shorten("h,m") == "hm"


if __name__=="__main__":
    main()
