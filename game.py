import random
while True:
    try:
        level = int(input("Level: "))
        if(is_neg(level)):
            continue
        else:
            rand = random.randint(1,level)
            guess = int(input("Guess: "))
            if(rand == guess):
                print("Just right!")
    except:
        break


def is_neg(x):
    print("called")
    if (x<0):
        return True
    else:
        return False
