def main():
    x = get_fraction("Fraction: ")

def get_fraction(prompt):
    while True:
        try:
            f = int(input(prompt))
            n,waste,d = f.split
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
