import requests
import json
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..')) # <- Adds parent folders modules to PATH

import stringFormatting as sf

preferred_currency = "usd"

watchList = [ # Names of cryptocurrencies to watch
    "Ethereum",
    "Bitcoin",
]

def formatToNiceformat(string):
    op = string.split(":")
    name = str(op[0]).capitalize()
    price = str(op[2])
    currency = str(op[1]).upper()
    return name, price, currency

def getStatusCode():
    response = requests.get("https://api.coingecko.com/api/v3/ping")
    return str(response.status_code)

def getCoinList():
    responseCode = getStatusCode()
    if responseCode == "200":
        response = requests.get("https://api.coingecko.com/api/v3/coins/list")
        heisann = str(response.text).split("{")
        filteredList = []
        for index, string in enumerate(heisann):
            if index == 0:
                continue
            filteredList.append(string.split("}")[0].split(","))
        return filteredList
    else:
        print("Bad status. Error code: " + responseCode)
        return []

def getInfoFromCoin(name, coinlist):
    '''
    name must be identical name of crypto coin
    '''
    for x in range(len(coinlist)):
        for y in range(len(coinlist[x])):
            if "name" in coinlist[x][y]:
                coinname = coinlist[x][y].split(":")[1].replace('"', "")
                if name == coinname:
                    id = coinlist[x][0].split(":")[1].replace('"', "")
                    symbol = coinlist[x][1].split(":")[1].replace('"', "")
                    name = coinlist[x][2].split(":")[1].replace('"', "")
                    return tuple((id, symbol, name)) # id symbol name
    return None

def getPriceForCoin(ids, currency):
    '''
    Id of coins, comma-separated if querying more than 1 coin. Pass ids as string. As: ids="ethereum,bitcoin,xno"
    Currency of coins, comma-separated if querying more than 1 vs_currency. Pass ids as string. As: currency="usd, nok"
    '''
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + ids + "&vs_currencies=" + currency)

    return response.text

def main():
    filterOut = ["{", "}", '"']

    eth = getPriceForCoin(getInfoFromCoin("Ethereum", getCoinList())[0], "usd")
    btc = getPriceForCoin(getInfoFromCoin("Bitcoin", getCoinList())[0], "usd")

    eth = sf.excludeCharsFromString(eth, filterOut)
    btc = sf.excludeCharsFromString(btc, filterOut)

    eth = formatToNiceformat(eth)
    btc = formatToNiceformat(btc)

    print(eth, btc)

def print_trending_coins_data(
    verbose=False
    ):
    '''
    Function does 2 api requests out of 50 per minute.
    '''
    response = requests.get("https://api.coingecko.com/api/v3/search/trending")
    trending_data = json.loads(response.text)

    #print("Trending searches on coingecko today:")

    request_string = "https://api.coingecko.com/api/v3/simple/price?ids="
    for e in trending_data.get("coins"): # Getting price for each trending coin by creating the proper request string
        add = f"%2C"
        if "https://api.coingecko.com/api/v3/simple/price?ids=" == request_string: # First iteration
            add = ""
        request_string += add + e.get("item").get("id")

    request_string += f"&vs_currencies={preferred_currency}&include_market_cap=true&include_24hr_change=true"
    #print(request_string)

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

        print(f"Rank: {score + 1}. {name} {symbol}, Price: {price} {preferred_currency}. Marketcap: {round(marketcap, 2)} {preferred_currency}. 24 Hour change: {round(percent_change, 2)}%.")