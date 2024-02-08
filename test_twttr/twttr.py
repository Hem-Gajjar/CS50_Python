
vowels = ["a","e","i","o","u","A","E","I","O","U",","]

def main():
    input_str = input("Input: ")
    print(shorten(input_str))


def shorten(str):
    xyz = ""
    for i in str:
        flag = False
        for x in vowels:
            if(i==x ): # vowel  or i.isnumeric()
                flag = True
                break
        if flag == False:
            xyz+=i

    return xyz

if __name__=="__main__":
    main()
