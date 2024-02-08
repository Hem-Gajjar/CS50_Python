input_str = input("Input: ")
vowels = ["a","e","i","o","u"]

def check(str):
    xyz = ""
    str = str.lower()
    for i in str:
        flag = False
        for x in vowels:
            if(i==x): # vowel
                flag = True
                break
        if flag == False:
            xyz+=i

    return xyz

print(check(input_str))

