def main():
    x = get_fraction()
    x = ceil(x)
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
            if isinstance(n,float):
                continue
            if isinstance(n,float):
                continue
            return (int(n)/int(d))*100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass





main()
