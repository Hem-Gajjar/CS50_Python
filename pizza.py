import sys
import csv

count = len(sys.argv)
file_name = sys.argv[1]
name,ext =  file_name.split(".")

if count < 2:
    sys.exit("Too few command-line arguments")
elif count > 2:
    sys.exit("Too many command-line arguments")
elif ext != "csv":
    sys.exit("Not a CSV file")

try:
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print({"Sicilian Pizza":row["Sicilian Pizza"],row["Small"],row["Large"]})

except FileNotFoundError:
    sys.exit("File does not exist")
