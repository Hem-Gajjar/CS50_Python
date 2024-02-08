input_str = input("Input: ")
vowels = ["a","e","i","o","u"]

def check(str):
    xyz = ""
    str = str.lower()
    for i in str:
        for x in vowels:
            if(i==x):
                break
            if(i!=x)
                xyz+=i
                # break

    return xyz

print(check(input_str))
