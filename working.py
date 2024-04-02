import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrect = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if isCorrect:
        pieces = isCorrect.groups()
        if int(pieces[1])>12 or int(pieces[5])>12:
            raise ValueError
        return pieces
    else:
        raise ValueError

def new_format(hour,minute,am_pm)
if __name__ == "__main__":
    main()
