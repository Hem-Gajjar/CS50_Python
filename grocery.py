vegies = {


}

def count_item(x):
    i=0
    count=0
    while i < len(vegies):
        if list(vegies[i]) == x :
            count=count+1
        i = i+1
    return count


while True:
    try:
        x = input()
        count = count_item(x)
        vegies.update({x:count})
    except EOFError:
        break
print(vegies)


