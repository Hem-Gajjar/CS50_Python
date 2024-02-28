import re
import sys

def main():
    ip = input("IPv4 Address:")
    validate(ip)

def validate(ip):

    if re.search(r"^(([0-2].+[0-5].+[0-5])|([0-9]+[0-9])|([0-9]))+\.(([0-2][0-5][0-5])|([0-9][0-9])|([0-9]))+\.(([0-2][0-5][0-5])|([0-9][0-9])|([0-9]))+\.(([0-2][0-5][0-5])|([0-9][0-9])|([0-9]))$",ip):
        print("True")
    else:
        print("False")



if __name__ == "__main__":
    main()
