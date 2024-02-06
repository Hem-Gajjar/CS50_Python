import sys
import requests

try:
    if(len(sys.argv())!=2):
        num = float(input(sys.argv()))
        
    elif(len(sys.argv())==1):
        print("Missing command-line argument")
except ValueError:
    print("Command-line argument is not a number")

