import pytest
try:
    from test_fuel.fuel import convert
    from test_fuel.fuel import gauge
except:
    from fuel import convert
    from fuel import gauge

def test_prompt():
    with pytest.raises(TypeError):
        assert convert(3/4) == "75%"


