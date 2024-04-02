import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"(([0-9].*)((:[0-9])*) [A-Z]+ to ([0-9].*)((:[0-9])*) [A-Z]+)",s):
        get_groups = re.search(r"(([0-9].*)((:[0-9])*) [A-Z]+ to ([0-9].*)((:[0-9])*) [A-Z]+)",s)
        our_groups = get_groups.groups()
        start = our_groups[2]
        end = our_groups[5]
        print(start)
        print(end)


if __name__ == "__main__":
    main()
