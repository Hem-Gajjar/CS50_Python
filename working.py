import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s):
        get_groups = re.search(r"(([0-9].*)((:[0-9])*) ([A-Z]+) to ([0-9].*)((:[0-9])*) ([A-Z]+))",s)
        our_groups = get_groups.groups()
        print(our_groups)
        final_start_hour,final_start_min,final_end_hour,final_end_min
        try:
            start = our_groups[1]
            if re.search("([0-9]:[0-9]*)",start):
                start_hour,start_min = start.split(":")
                start_zone = our_groups[4]
                if(start_zone=="AM"):
                    final_start_hour = 0 + int(start_hour)
                    final_start_min = start_min
                    

            end = our_groups[5]
            if re.search("([0-9]:[0-9]*)",end):
                end_hour,end_min = end.split(":")
            end_zone = our_groups[8]
        except:
            pass



if __name__ == "__main__":
    main()
