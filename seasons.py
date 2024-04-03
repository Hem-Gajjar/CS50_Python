from datetime import date
import sys

def main():
    try:
        year,month,day = input("Date of Birth").split("-")
    except ValueError:
        sys.exit("Invalid Date")

...


if __name__ == "__main__":
    main()
