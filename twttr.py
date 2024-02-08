
input_str = input("Input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U",","]


def shorten(str):
    xyz = ""

    for i in str:
        flag = False
        for x in vowels:
            if(i==x or i.isnumeric()): # vowel
                flag = True
                break
        if flag == False:
            xyz+=i

    return xyz

print(shorten(input_str))

