from um import count

def main():
    test_ulcase()
    test_uminword()
    test_umalone()

def test_ulcase():
    assert count("Um, Thanks for the album")==1
    assert count("Um, thanks, um...")==2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?")==3
def test_uminword():
    assert count("yummy") == 0
def test_umalone():
    assert count("Hello um world") == 1
    assert count("um?") == 1
if __name__ == "__main__":
    main()
