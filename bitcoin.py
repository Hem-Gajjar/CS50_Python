import sys
import requests
import json

try:
    if len(sys.argv) == 2:
        num = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = float(o["bpi"]["USD"]["rate_float"])
        amount = rate * num
        print(f"${amount:,.4f}")
    elif len(sys.argv) == 1:

        sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Command-line argument is not a number")
