from twttr import shorten

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("hem") == "hm"
    assert shorten("hEm") == "hm"
    assert shorten("h3m") == "hm"
