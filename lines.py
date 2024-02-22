import sys

count = len(sys.argv)
file_name = sys.argv[1]
name,ext = file_name.split(".")


if count < 2:
    sys.exit("Too few command-line arguments")
elif count > 2:
    sys.exit("Too many command-line arguments")
elif ext != py:
    sys.exit("Not a Python file")


try:
    with open(file_name,"r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
