from datetime import date
import sys
import re


def main():
    birth_date = input("Date of birth: ")
    try:
        year,month,day = check_dob(birth_date)
        print(year,month,day)
    except:
        sys.exit("Invalid Date")

def check_dob(dob):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",dob):
        year,month,day = dob.split("-")
        return year,month,day

if __name__ == "__main__":
    main()
