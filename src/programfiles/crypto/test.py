import requests
import json
import sys
import os


response = requests.get("https://api.coingecko.com/api/v3/search/trending")
#print(response.text)
dump = json.loads(response.text)
#print(type(dump))
#name = dump.get("item").get("name")
#print(name)
#print(dump.get("coins"))

print("Trending searches on coingecko today:")
for e in dump.get("coins"):
    name = e.get("item").get("name")
    symbol = e.get("item").get("symbol")
    print(f"({symbol}) {name}")
#print(dump.get("coins")[0].get("item").get("name"))
#print(dump.get("coins")[5].get("item").get("name"))
#for k in dump.get("coins")[0].get("item").get("name"):
#    print(k)
    #print(something.get(k))