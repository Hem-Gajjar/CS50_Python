vegies = {


}

def count_item(x):
    i=0
    count=0
    a = list(vegies)
    while i < len(vegies):
        if a[i] == x :
            count=count+1
        i = i+1
    return count


while True:
    try:
        x = input()
        count = count_item(x)
        if count == 0 :
            vegies[x] = 0
        else:
            vegies.update({x:count})
    except EOFError:
        break
print(vegies)


