import sys

count = len(sys.argv)
file_name = sys.argv[1]
name,ext =  file_name.split(".")

if count < 2:
    sys.exit("Too few command-line arguments")
elif 
