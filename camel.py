str = input("camelCase: ")
i=0
while i < len(str):

    if (str[i].isupper()):
        print("_",end="")
    print(str[i],end="")
    i+=1
print()
