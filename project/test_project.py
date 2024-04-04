from project import select_by_year
from project import select_by_genre
from project import select_by_actor

def test_select_by_year():
    assert select_by_year("1971") == True
    assert select_by_year("1972") == False


def test_select_by_genre():
    assert select_by_genre("Drama") == True
    assert select_by_genre("Nothing") == False


def test_select_by_actor():
    assert select_by_actor("Upendra Trivedi") == True
    assert select_by_actor("Arvind Trivedi") == True

