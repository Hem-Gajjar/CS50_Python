str = input("Input: ")
vowels = ["a","e","i","o","u"]
flag = False
i=0
j=0
while i < len(str):
    j=0
    flag = False


    while j < len(vowels):
        # print(str[i],vowels[j],sep="-")
        if str[i].lower() == vowels[j]:
            print("",end="")
            break
        else:
            print(str[i],end="")
            break
        j+=1
    i+=1

