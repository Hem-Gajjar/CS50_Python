from twttr import check

def test_twttr():
    assert check("twitter") == "twttr"
    assert check("hem") == "hm"
