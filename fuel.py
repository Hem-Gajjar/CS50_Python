def main():
    x = get_fraction()
    print(x)
def get_fraction():
    while True:
        try:
            f = input("Fraction: ")
            n = f[0]
            d = f[2]
            print(n)
            print(d)
            x = int(n)/int(d)
            # print(x)
            return (x*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
