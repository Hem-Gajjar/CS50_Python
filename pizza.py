import sys

count = len(sys.argv)
file_name = sys.argv[1]
name,ext =  file_name.split(".")

print(name,ext)
