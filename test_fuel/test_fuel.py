
try:
    from test_fuel.fuel import convert , gauge
except:
    from fuel import convert , gauge

# def main():
    # test_correct_input()

def test_correct_input():
    assert convert('1/4') == 25
    assert convert('1/4') == 25

# if __name__ == "__main__":
#     main()
