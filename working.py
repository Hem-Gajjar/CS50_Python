import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s):
        get_groups = re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s)
        our_groups = get_groups.groups()
        print(our_groups)
        try:
            start = our_groups[1]
            if re.search("([0-9]:[0-9]*)",start):
                start_hour,start_min = start.split(":")
            start_zone = our_groups[4]
            end = our_groups[5]
            if re.search("([0-9]:[0-9]*)",end):
                end_hour,end_min = end.split(":")
            end_zone = our_groups[8]
        except:
            pass
        print(start)
        print(start_hour)
        print(start_min)
        print(start_zone)
        print(end)
        print(end_hour)
        print(end_min)
        print(end_zone)
        final_time=""


if __name__ == "__main__":
    main()
