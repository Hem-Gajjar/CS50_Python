def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    flag = True
    length = len(s)
    if length < 2 or length > 6:
        flag = False
    else:
        flag = True
    if s[0].isnumeric() or s[1].isnumeric():
        flag =  False
    else:
        
        while s[i].isalpha():
            i+=1
        i+=1
        while s[i].isnumeric():
            i+=1
        if(i >= len(s)):
            flag = False
        else:
            flag = True
    return flag
main()
