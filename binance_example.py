#!/usr/bin/env python

import binance
from pprint import pprint
from password_storage import get_credentials


def binance_summary():

    # instead of having the API in the script..not a perfect solution
    sign_key, sign_SECRET = get_credentials('binance_api')

    api_info = {
        'sign_key': sign_key,
        'sign_SECRET': sign_SECRET,
        'sign_id': 'anyone',
        'coin_symbol': 'ZEC',
    }

    binance.set(api_info['sign_key'], api_info['sign_SECRET'])
    relation = {'ZEC': 'ZECBTC',
                'BTC': 'BTCUSDT'}

    prices = binance.prices()
    balances = binance.balances()

    btc_price = float(prices['BTCUSDT'])
    # print ("The current Bitcoin price is $ {0:.2f}").format(btc_price)
    print

    # print float(prices['ZECBTC'])

    # cycle thru all coins balances
    for key in balances.keys():

        # if balance is greater than 0, display balance info
        if float(balances[key]['free']) > 0:

            # determine 'free' balance
            balance_coin = float(balances[key]['free'])

            # handle BTC different because other coins are based on BTC
            if key == 'BTC':

                # determine the coins current price
                coin_price = float(prices[relation[key]])

                # calculate the coin balance in USD
                balance_usd = balance_coin * float(prices[relation[key]])

                # display information to screen
                template = ("The {0} price is currently $ {1:.2f}")
                print template.format(key, coin_price)

            else:

                # calculate the price of the coin in USD not BTC
                coin_price = float(prices[relation[key]]) * btc_price

                # calculate the coin balance in USD
                balance_usd = (float(prices[relation[key]])
                               * balance_coin * btc_price)

                # display information to screen
                template = ("The {0} price is currently $ {1:.2f}")
                print template.format(key, coin_price)

            print ("\n\tYour {0} balance is {1}").format(key, balance_coin)
            print ("\tYour {0} balance is worth $ {1:.2f}".format(key,
                                                                  balance_usd))
            print


def main():

    binance_summary()


if __name__ == "__main__":

    main()
