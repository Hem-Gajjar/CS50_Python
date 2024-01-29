vegies = {
    "name":"",
    "count":0
}
while True:
    try:
        x = input()
        vegies.update("name:")
    except EOFError:
        break
print(vegies)


