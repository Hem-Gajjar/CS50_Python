from bank import value

def main():
    test_hello()
    test_hii()
    test_namaste()


def test_hello():
    assert value("Hello") == "$0"
    print("done")

def test_hii():
    assert value("hii") == "$20"
    print("done")

def test_namaste():
    assert value("namaste koi kaam") == "$100"
    print("done")

if __name__ == "__main__":
    main()
