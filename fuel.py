def main():
    x = get_fraction("Fraction: ")

def get_fraction(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
