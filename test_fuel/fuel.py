def main():
    x = convert('1/4')
    print(x)
    gauge(x)

def gauge(x):
    # x = round(x)
    if(x>=99):
        print("F")
    elif(x<=1):
        print("E")
    else:
        print(f"{x}%")

def convert(f):
    while True:
        try:
            array = (f.partition("/"))
            n = array[0]
            d = array[2]
            if(int(n)<=int(d)):
                if isinstance(n,float):
                    f = input("Fraction: ")
                    continue
                if isinstance(n,float):
                    f = input("Fraction: ")
                    continue
                return(round((int(n)/int(d))*100))

        except ValueError:
            pass
        except ZeroDivisionError:
            pass




if __name__ == "__main__":
    main()
