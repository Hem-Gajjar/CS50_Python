str = input("camelCase: ")
i=0
while i < len(str):

    if (str[i].isupper()):
        print("_",end="")
    str[i] = str[i].lower()
    print(str[i],end="")
    i+=1
print()
