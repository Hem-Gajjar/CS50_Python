import sys
import requests

try:
    if(len(sys.argv)!=2):
        num = float(input(sys.argv()))
        response = requests.get("https://api.coindesk.com/get")
        print(json.dumps(response.json(),indent=2))
    elif(len(sys.argv)==1):
        print("Missing command-line argument")
except ValueError:
    print("Command-line argument is not a number")

