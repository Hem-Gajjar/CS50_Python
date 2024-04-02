from um import count

def main():
    test_ulcase()
    test_uminword()
    test_umalone()

def test_ulcase():
    assert count("Um, Thanks for the album")==1
    assert count("Um, thanks, um...")==2

def test_uminword():
    assert count("yummi") == 0
def test_umalone():
    assert count("Hello um world") == 1
    assert count("um?") == 1
if __name__ == "__main__":
    main()
