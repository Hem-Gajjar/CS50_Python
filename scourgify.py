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
    with open(file1) as one:
        reader = csv.DictReader(one)
        for row in reader:
            students.append({"first":row["name"],"house":row["house"]})


except FileNotFoundError:
    sys.exit("Could not read",file1)


try:
    with open(file2,"a") as two:
        for student in students:
            writer= csv.DictWriter(two,fieldnames=["first","last","house"])
            first,last = student['first'].split(",")
            house = student['house']
            writer.writerow({"first":first,"last":last,"house":house})

except FileNotFoundError:
    sys.exit("Could not read",file2)

