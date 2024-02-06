import sys
import requests
import json
try:
    if(len(sys.argv)==2):
        # num = float(input(sys.argv[1]))
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(response.json())
        print(json.dumps(response.json(),indent=2))
        # print(response)
    elif(len(sys.argv)==1):
        print("Missing command-line argument")
        sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

