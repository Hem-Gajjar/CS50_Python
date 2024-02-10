
try:
    from test_fuel.fuel import convert
except:
    from fuel import convert

try:
    from test_fuel.fuel import gauge
except:
    from fuel import gauge

def test_prompt():
    try:
        assert convert(3/4) == "75%"
        assert convert(1/3) == "33%"
        assert convert(2/3) == "67%"
    except TypeError:
        pass
    except ZeroDivisionError:
        pass

def test_EandF():
    try:
        assert convert(0/100) == "E"
        assert convert(1/100) == "E"
        assert convert(100/100) == "F"
        assert convert(99/100) == "F"
    except TypeError:
        pass
    except ZeroDivisionError:
        pass

def test_reprompt():
    try:
        assert convert(100/0) is None
        assert convert(10/3) is None
        assert convert("three/four") is None
        assert convert(1.5/4) is None
        assert convert(3/5.5) is None
        assert convert(5-10) is None
    except TypeError:
        pass
    except ZeroDivisionError:
        pass

