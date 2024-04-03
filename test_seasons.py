from seasons import convert
import pytest

def test_seasons():
    assert convert("2022-09-10") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-09-10") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit):
        convert("sdfs-sd-sd")
    with pytest.raises(SystemExit):
        convert("20220910")
    with pytest.raises(SystemExit):
        convert("cat")
