import requests
import json
import sys
import os

preferred_currency = "usd"

def get_trending_coins_data(
    verbose=False
    ):
    '''
    Function does 2 api requests out of 50 per minute.
    '''
    response = requests.get("https://api.coingecko.com/api/v3/search/trending")
    trending_data = json.loads(response.text)

    print("Trending searches on coingecko today:")

    request_string = "https://api.coingecko.com/api/v3/simple/price?ids="
    for e in trending_data.get("coins"): # Getting price for each trending coin by creating the proper request string
        add = f"%2C"
        if "https://api.coingecko.com/api/v3/simple/price?ids=" == request_string: # First iteration
            add = ""
        request_string += add + e.get("item").get("id")

    request_string += f"&vs_currencies={preferred_currency}&include_market_cap=true&include_24hr_change=true"
    print(request_string)

    response = requests.get(request_string)
    price_for_trending_coins = json.loads(response.text)


    for e in trending_data.get("coins"):
        coin_id = e.get("item").get("id")
        name = e.get("item").get("name")
        symbol = e.get("item").get("symbol")
        score = e.get("item").get("score")

        try:
            price = price_for_trending_coins.get(coin_id).get(preferred_currency)
            marketcap = price_for_trending_coins.get(coin_id).get(f"{preferred_currency}_market_cap")
            percent_change = price_for_trending_coins.get(coin_id).get(f"{preferred_currency}_24h_change")
        except:
            price = -1
            marketcap = -1
            percent_change = -1

        print(f"Rank: {score + 1}. {name} {symbol}, Price: {price} {preferred_currency}. Marketcap: {marketcap} {preferred_currency}. 24 Hour change: {round(percent_change, 2)}%.")

get_trending_coins_data()