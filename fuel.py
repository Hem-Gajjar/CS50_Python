def main():
    x = get_fraction()
    x = int(x)
    if(x==100):
        print("F")
    elif(x==0):
        print("E")
    else:
        print(f"{x}%",end="")

def get_fraction():
    while True:
        try:
            f = input("Fraction: ")
            array = (f.partition("/"))
            n = array[0]
            d = array[2]
            # print(n)
            # print(d)
            if is_float(n):
                continue
            if is_float(d):
                continue
            return int(n)/int(d)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def is_float(x):

    if x.replace(".","").isnumeric():
        return True
    else:
        return False


main()
