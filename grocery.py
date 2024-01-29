vegies = {
    "name":""
}
while True:
    try:
        x = input()
        vegies.update({"name":x})
    except EOFError:
        break
print(vegies)


