def main():
    convert()

def gauge(x):
    x = round(x)
    if(x==100 or x==99):
        print("F")
    elif(x==0 or x==1):
        print("E")
    else:
        print(f"{x}%",end="")

def convert():
    while True:
        try:
            f = input("Fraction: ")
            array = (f.partition("/"))
            n = array[0]
            d = array[2]
            if(int(n)<=int(d)):
                if isinstance(n,float):
                    continue
                if isinstance(n,float):
                    continue
                gauge((int(n)/int(d))*100)
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass




if __name__ == "__main__":
    main()
