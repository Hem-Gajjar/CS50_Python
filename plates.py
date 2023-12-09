def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0

    length = len(s)
    if length < 2 or length > 6:
        return False
    # else:
    #     if s[0].isnumeric() or s[1].isnumeric():
    #         return False
    #     else:
    #         while s[i].isalpha():
    #             i+=1
    #         i+=1
    #         while s[i].isnumeric():
    #             i+=1
    #         if(i >= len(s)):
    #             return False


main()
