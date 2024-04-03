from datetime import date
import sys

def main():
    try:
        year,month,day = input("Date of Birth").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    minutes_lived(year,month,day)

def minutes_lived(year,month,day):
    try:
        dt = date(int(year),int(month),int(day))
    except ValueError:
        return "Invalid Data"

    tday = date.today()
    diff = tday - dt
    minutes = int(diff.total_seconds()/60)
    
if __name__ == "__main__":
    main()
