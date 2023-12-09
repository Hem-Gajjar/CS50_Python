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



            
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
