import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("([0-9].*(:[0-9])* [A-Z]+ to [0-9].*(:[0-9])* [A-Z]+)",s):
        get_groups = s.groups()
        print(get_groups)


if __name__ == "__main__":
    main()
