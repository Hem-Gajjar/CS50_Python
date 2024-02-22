import sys
import csv
import tabulate

table= []

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
        reader = csv.reader(file)
        for pizza,small,large in reader:
            table.append()
            # print(tabulate(row,"Sicilian Pizza","Small","Large",tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
