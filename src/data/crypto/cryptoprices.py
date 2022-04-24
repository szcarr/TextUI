import requests
import json
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..')) # <- Adds parent folders modules to PATH

import stringFormatting as sf

#response = requests.get("https://api.coingecko.com/api/v3/ping")

#print(response.status_code)
#print(response.headers['content-type'])
#print(response.encoding)
#print(response.text)

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

main()