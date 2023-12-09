str = input("Input: ")
vowels = ["a","e","i","o","u"]
flag = False
i=0
j=0
while i < len(str):
    j=0
    Flag = False
    while j < len(vowels):
        if str[i].lower == vowels[j]:
            print("")
        else:
            Flag = True
            break
        j+=1
    if Flag:
        print(str[i],end="")
    i+=1

