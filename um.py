import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    mystring = re.findall("\b\W*um\W",s)
    return len(mystring)


if __name__ == "__main__":
    main()
