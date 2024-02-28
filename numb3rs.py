import re
import sys

def main():
    ip = input("IPv4 Address:")
    validate(ip)

def validate(ip):
    flag = False
    if re.search(r"^[0-255]+\.[0-255]+\.[0-255]+\.[0-255]$",ip):
        print("Valid")
    else:
        print("Invalid")



if __name__ == "__main__":
    main()
