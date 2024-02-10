try:
    from test_bank.bank import value
except:
    from bank import value

# def main():
    # test_hello()
    # test_hii()
    # test_namaste()


def test_hello():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"


def test_hii():
    assert value("hii") == "$20"
    assert value("HII") == "$20"


def test_namaste():
    assert value("namaste") == "$100"
    assert value("NAMASTE") == "$100"


# if __name__ == "__main__":
#     main()
