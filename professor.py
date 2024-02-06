import random

def main():
    level = get_level()
    i=0
    while(i<10):
        

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if(x >= 1 and x <= 3 ):
                return(x)
            else:
                pass
        except ValueError:
            pass

def generate_integer():
    while True:
        x = random.randint()
        if(x >= 0):
            return x
        else:
            pass

if __name__ == "__main__":
    main()
