import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s):
        get_groups = re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s)
        our_groups = get_groups.groups()
        print(our_groups)
        start = our_groups[1]
        start_zone = our_groups[4]
        end = our_groups[5]
        end_zone = our_groups[8]
        print(start)
        print(start_zone)
        print(end)
        print(end_zone)
        

if __name__ == "__main__":
    main()
