import random
def is_neg(x):
    if (x<0):
        return True
    else:
        return False


while True:
    try:
        level = input("Level: ")
        if(is_neg(level) and isnumeric(level)==0):
            continue
        else:
            level = int(level)
            rand = random.randint(1,level)
            while True:
                guess = int(input("Guess: "))
                if(rand == guess):
                    print("Just right!")
                    break
                elif(rand<guess):
                    print("Too large!")
                    continue
                elif(rand>guess):
                    print("Too small!")
                    continue
            break
    except:
        print("ooo")
        break



