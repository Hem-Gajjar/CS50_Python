import sys
import requests
import json
try:
    if(len(sys.argv)==2):

        print("1")
        num = float(sys.argv[1])
        print("2")
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print("3")
        o = response.json()
        print("4")
        rate = (o["bpi"]["USD"]["rate"])

        print(rate)
        print(rate*num)
        print("6")
    elif(len(sys.argv)==1):
        print("Missing command-line argument")
        sys.exit()

except ValueError:
    print("Command-line argument is not a number")

    sys.exit()

