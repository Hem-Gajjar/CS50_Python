def main():
    x = get_fraction()
    x = int(x)
    if(x==100):
        print("F")
    elif(x==0):
        print("E")
    else:
        print(f"{x}%")
def get_fraction():
    while True:
        try:
            f = input("Fraction: ")
            n = int(f[0])
            d = int(f[2])
            # print(n)
            # print(d)
            x = 
            # print(x)
            return (x)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
