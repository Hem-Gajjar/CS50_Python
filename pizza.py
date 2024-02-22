import sys
import csv
from tabulate import tabulate

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

        for row in reader:
            table.append([row[0],row[1],row[2]])

        table.pop(0)
    print(tabulate(table,headers=["Sicilian Pizza","Small","Large"],tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
