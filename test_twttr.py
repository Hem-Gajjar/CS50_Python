from twttr import shorten()

# def test_normal():
#     assert shorten("twitter") == "twttr"
#     assert shorten("hem") == "hm"

def test_capital():
    assert shorten("hEm") == "hm"

def test_number():
    assert shorten("h3m") == "hm"

def test_pun():
    assert shorten("h,m") == "hm"
