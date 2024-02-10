try:
    from test_bank.bank import value
except:
    from bank import value

# def main():
    # test_hello()
    # test_hii()
    # test_namaste()


def test_hello():
    assert value("hello") == 0
def test_HELLO():
    assert value("HELLO") == 0


def test_hii():
    assert value("hii") == 20

def test_HII():
    assert value("HII") == 20


def test_NAMASTE():
    assert value("namaste") == 100
def test_namaste():
    assert value("NAMASTE") == 100


# if __name__ == "__main__":
#     main()
