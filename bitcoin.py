import sys
import requests
import json
try:
    if(len(sys.argv)==2):
        # num = float(input(sys.argv[1]))
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = response.json()
        for i in o["bpi"]:
            for j in i[0]:
                print(j[2])

    elif(len(sys.argv)==1):
        print("Missing command-line argument")
        sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

