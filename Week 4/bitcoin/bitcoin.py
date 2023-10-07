# Roger Hennessy
# 06-10-2023

import requests
import json
import sys

# Create main()
def main():
    # Call bitcoin_tracker()
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_tracker(response)

    except requests.RequestException:
        sys.exit()

def bitcoin_tracker(response):
    # TODO
    # Here we should add EUR + GBP to the program
    if len(sys.argv) > 2:
        '''
            Have sys.argv[2] be EUR/eur or GBP/gbp
            Have error check
            Pass currency to return_price()
            Even better would be to not use command line arguments.
            Make it a program, asking for user input to choose currency and amount.

        '''
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 1:
        sys.exit("Missing command-line argument")

    # TODO - Need to figure out how to accept a float value
    elif sys.argv[1].isdigit():
        return_price(response, int(sys.argv[1]))

    elif isfloat(sys.argv[1]):
        return_price(response, float(sys.argv[1]))

    elif not sys.argv[1].isdigit():
        sys.exit("Command-line argument is not a number")

def return_price(response, amount):
    # Here we will get the current BTC price in dollars
    btc_rate_json = response.json()

    #TODO
    # Have EUR and GBP rates, just use an if statement
    btc_rate = btc_rate_json["bpi"]["USD"]["rate_float"]

    amount = (amount * btc_rate)
    print(f"${amount:,}")

# Not sure how else to check if the argument is a float
def isfloat(arg):
    try:
        float(arg)
        return True

    except ValueError:
        return False

# Call  main()
if __name__ == "__main__":
    main()