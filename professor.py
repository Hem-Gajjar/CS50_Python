import random

def main():
    level = get_level()
    i=0
    incorrect_count = 0
    correct_count = 0
    while(i<10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_ans = x+y
        while(incorrect_count<=3):
            try:
                z = int(input(f"{x} + {y} ="))
                if(z == correct_ans):
                    i = i+1
                    correct_count += 1
                    incorrect_count =0
                    break
                else:
                    incorrect_count += 1
                    print("EEE")
                    if(incorrect_count == 3):
                        print(f"{x} + {y} = {correct_ans}")
                        i+=1
                        incorrect_count = 0
                        break
            except ValueError:
                pass

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

def generate_integer(level):

    if(level==1):
        low = 0
        high = 9
    elif(level==2):
        low = 10
        high = 99
    else:
        low=100
        high=999

    while True:

        x = random.randint(low,high)
        if(x >= 0):
            return x
        else:
            pass

if __name__ == "__main__":
    main()
