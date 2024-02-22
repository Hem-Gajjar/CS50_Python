import sys

count = len(sys.argv)
file_name = sys.argv[1]
name,ext = file_name.split(".")


if count < 2:
    sys.exit("Too few command-line arguments")
elif count > 2:
    sys.exit("Too many command-line arguments")
elif ext != "py":
    sys.exit("Not a Python file")

def count_loc():
    try:
        with open(file_name,"r") as file:
            loc = 0
            for line in file:
                if line.lstrip().startswith("#"):
                    pass
                elif line.lstrip() == "":
                    pass
                elif line.lstrip().startswith('"""')or line.lstrip().startswith("'''"):
                    loc += 1
                else:
                    loc += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return loc
print(count_loc())
