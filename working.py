import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    is isCorrect = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if isCorrect:
        pieces = isCorrectFormat.groups()
        return pieces
    else:
        raise ValueError


if __name__ == "__main__":
    main()
