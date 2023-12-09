def main():
    x = get_fraction("Fraction: ")
    print(f"{x}%")
def get_fraction(prompt):
    while True:
        try:
            return (int(input(prompt))*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
