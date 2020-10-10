import csv
import codecs
import requests
import io
import json
import prettytable
import colorama

# https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ASUS&page=1&sort=sale/dc

keyword = input("請輸入欲查詢的關鍵字:")

def user_research(keyword, page):
    r = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results?",
                     params={
                         "q": keyword,
                         "page": page,
                         "sort": "sale/dc"
                     }
                     )
    ret = json.loads(r.text)
    table = prettytable.PrettyTable(["名稱", "價格"], encoding="utf8")
    table.align["名稱"] = "l"
    table.align["價格"] = "c"
    for item in ret["prods"]:
        table.add_row([item["name"], item["price"]])
    print(table)
user_research(keyword, "1")
page = input("前往頁碼:")
# 每次輸入頁碼時，執行user_research(keyword, page)
while True:
    user_research(keyword, page)
    page = input("前往頁碼:")





