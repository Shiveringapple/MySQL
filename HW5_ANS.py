import requests
import json
import prettytable
import os

os.system("cls")
keyword = input("關鍵字:")
page = 1

while True:
    os.system("cls")
    r1 = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results",
                      params= {"q": keyword,
                               "page": page,
                               "sort": "sale/dc"})
    r1.encoding = "utf-8"
    ret = json.loads(r1.text)

    table = prettytable.PrettyTable(["商品名稱", "價格"], encoding="utf-8")
    table.align["商品名稱"] = "l"
    table.align["價格"] = "l"
    for item in ret["prods"]:
        table.add_row([item["name"], item["price"]])
    print(table)

    page = input("前往頁碼:")