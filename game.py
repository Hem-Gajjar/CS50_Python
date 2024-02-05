while True:
    try:
        level = int(input("Level: "))
        if(level < 0):
            continue
        else:
            break
    except:
        break
