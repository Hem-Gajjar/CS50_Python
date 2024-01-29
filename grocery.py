vegies = {}
while True:
    try:
        x = input()
        
        vegies.update({x:0})
    except EOFError:
        break
print(vegies)


