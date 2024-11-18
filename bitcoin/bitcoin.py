import requests
import sys

def get_btc_value():
    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        return float(res["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        sys.exit("Request problem")

def main():
    nb_to_buy = 0
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        nb_to_buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        btc_value = get_btc_value()
        price = btc_value * nb_to_buy
        print(f"${price:,.4f}")

main()
