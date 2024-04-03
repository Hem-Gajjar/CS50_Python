from datetime import timedelta
import inflect
import sys

def main():
    print(convert(input("Date of Birth: ")))


def convert(x):
    q = inflect.engine()
    try:
        years, months, days = x.split("-")
        years = int(years)
        months = int(months)
        days = int(days)
        dob = date(years, months, days)
        today = date.today()
        difference = today - dob
        min = round(difference.total_seconds()/60)
        words = q.number_to_words(min, andword="").capitalize() + " minutes"
        return words
    except ValueError:
        sys.exit("Date must be inputted in YYYY-MM-DD format.")



if __name__ == "__main__":
    main()
