import random
def is_neg(x):
    if (x<0):
        return True
    else:
        return False


while True:
    try:
        level = input("Level: ")
        if(level.isnumeric()):
            level = int(level)
            rand = random.randint(1,level)
            while True:
                guess = input("Guess: ")
                if(guess.isalpha() or guess.isalnum()):
                    continue
                guess = int(guess)
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

        else:
            continue

    except:
        print("ooo")
        break



