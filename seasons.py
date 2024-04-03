from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    birth_date = input("Date of birth: ")
    try:
        year,month,day = check_dob(birth_date)
    except:
        sys.exit("Invalid Date")
    convert_to_words()


def convert_to_words():
    date_of_birth = date(int(year),int(month),int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24*60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + " minutes")

def check_dob(dob):
    if re.search(r"^[0-9]{1,4}-[0-9]{2}-[0-9]{2}$",dob):
        year,month,day = dob.split("-")
        return year,month,day

if __name__ == "__main__":
    main()
