vegies = {


}

def count_item(x):
    i=0
    count=1
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
        if count == 1 :
            vegies[x] = 1
        else:
            vegies.update({x:count})
    except EOFError:
        break

names = list(vegies.keys())
names.sort()

sorted_vegies = {i :vegies[i] for i in names}

print(sorted_vegies)

z=0
for z in sorted_vegies:
    print(f)

