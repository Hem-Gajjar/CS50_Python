vegies = {}
while True:
    try:
        x = input()
        vegies.update(x)
    except EOFError:
        break
print(vegies)


