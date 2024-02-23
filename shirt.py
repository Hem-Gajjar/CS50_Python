import sys

count = len(sys.argv)

if count < 2:
    sys.exit("Too few command-line arguments")
elif count > 2:
    sys.exit("Too many command-line arguments")
elif count == 2:
    
