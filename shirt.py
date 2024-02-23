import sys

count = len(sys.argv)

if count < 3:
    sys.exit("Too few command-line arguments")
elif count > 3:
    sys.exit("Too many command-line arguments")

filename1 = sys.argv[1]
# print(filename1)
filename2 = sys.argv[2]
# print(filename2)
try:
    name1,ext1 = filename1.split(".")
    name2,ext2 = filename2.split(".")
except:
    sys.exit("Invalid input")

ext1 = ext1.lower()
ext2 = ext2.lower()
# print(ext1)
# print(ext2)


if ext1 == "jpg" or ext1 == "jpeg" or ext1 == "png" or ext2 == "jpg" or ext2 == "jpeg" or ext2 == "png":
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    # else:

else:
    sys.exit("Invalid input")

