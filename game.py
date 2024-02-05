import random
while True:
    try:
        level = int(input("Level: "))
        if(level < 0):
            continue
        else:
            random.randint(1,level)

    except:
        break


def is_negetive
