import sys
import csv
count = len(sys.argv)

if count<3:
    print("Too few command-line arguments")
elif count>3:
    print("Too many command-line arguments")

file1 = sys.argv[1]
file2 = sys.argv[2]

students = []

try:
    with open(file1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"first":row["name"],"house":row["house"]})

    for student in students:
        print(f"{student['name']},{student['house']}")

except FileNotFoundError:
    sys.exit("Could not read",file1)


try:
    with open(file2,"a") as file:
        writer= csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first":first})
except FileNotFoundError:
    sys.exit("Could not read",file2)
