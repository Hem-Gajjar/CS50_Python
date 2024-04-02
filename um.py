import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    mystring = re.findall(r"(\b\W*um\W*)",s,re.IGNORECASE)
    return len(mystring)


if __name__ == "__main__":
    main()
