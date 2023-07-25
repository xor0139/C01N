"""Special for Ilnur Stybayev"""
import json
from sys import argv
from os import listdir
#---------Add and cute url function----------------
def url(url: str, urls: list):
    if "?" in url:
        if url[:url.find("?")] not in urls:
            urls.append(url[:url.find("?")]) 
    else:
        if url not in urls:
            urls.append(url)            
#---------Array for urls---------------------------
urls = []
#---------Load wallets list file-------------------
with open(argv[3], "r", encoding="UTF-8") as file_wallets:
    wallets = file_wallets.read().split("\n")
#---------Load folder for dumps--------------------
dumps = listdir(argv[1])
#---------Load dump--------------------------------
for dump in dumps:
    with open(f"{argv[1]}\\{dump}", "r", encoding="UTF-8") as dump_file:
        data = json.load(dump_file)
# --------all--------------------------------------  
        for i in data["log"]["entries"]:
# --------binance, huoby, Kucoin, etc--------------             
            try:
                for j in i["request"]["queryString"]:
                    for wallet in wallets:
                        if j["value"] == wallet:
                            url(i["request"]["url"], urls)
            except:
                continue                    
#---------bitfinex---------------------------------                            
            try:
                for wallet in wallets:
                    if wallet in i["response"]["content"]["text"]:
                        url(i["request"]["url"], urls)    
            except:
                continue                
#---------bittrex----------------------------------                     
            try:
                for dic in i["request"]["postData"]["params"]:
                    for wallet in wallets:
                        if dic["value"] == wallet:
                            url(i["request"]["url"], urls)
            except:
                continue                                   
#---------Save urls to file------------------------
with open(argv[2], "a", encoding="UTF-8") as result_file:
    unique_url = list(set(urls))
    unique_url.sort()
    for url in unique_url:
        result_file.write(f"{url}\n")
#---------The End----------------------------------
print("Finish yopta =)")

#---------xor0139----------------------------------