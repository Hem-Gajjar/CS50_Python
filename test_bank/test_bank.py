from test_bank.bank import value

def main():
    test_hello()
    test_hii()
    test_namaste()


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_hii():
    assert value("hii") == 20

def test_namaste():
    assert value("namaste") == 100

if __name__ == "__main__":
    main()
