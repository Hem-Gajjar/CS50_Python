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
            if(is_neg(level)):
                continue
            rand = random.randint(1,level)
            while True:
                guess = input("Guess: ")
                if(guess.isnumeric()):
                    guess = int(guess)
                    if(guess >level):
                        # print("Too large!")
                        continue
                    else:
                        if(rand == guess):
                            print("Just right!")
                            break
                        elif(rand<guess):
                            print("Too large!")
                            continue
                        elif(rand>guess):
                            print("Too small!")
                            continue
                else:
                    continue
            break

        else:
            continue

    except Exception as ex:
        # print(f"Exception Occured:{ex}")
        break



