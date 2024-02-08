

str = input("Input: ")
vowels = ["a","e","i","o","u"]
flag = False
i=0
j=0
while i < len(str):
    j=0
    flag = False
    while j < len(vowels):
        if str[i].lower() == vowels[j]:
            flag = True
            break
        j+=1
    if flag==False:
        print(str[i],end="")
    i+=1


