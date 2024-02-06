import sys
import requests
import json
try:
    if(len(sys.argv)==2):
        print(sys.argv[1])

        num = sys.argv[1]

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = response.json()
        rate = float(o["bpi"]["USD"]["rate"])
        print(rate*num)
    elif(len(sys.argv)==1):
        print("Missing command-line argument")
        sys.exit()

except ValueError:
    print("Command-line argument is not a number")

    sys.exit()

