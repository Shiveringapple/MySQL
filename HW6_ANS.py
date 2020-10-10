import requests
import prettytable
import os
from bs4 import BeautifulSoup

r1 = requests.get("https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
            params={
                "ID": "Sat Aug 01 2020 09:46:08 GMT 0800 (台北標準時間)"
            }
                  )
c1 = BeautifulSoup(r1.text, "html.parser")
table = prettytable.PrettyTable(["地區", "氣溫"], encoding = "utf-8")
for item1 in c1.find_all("tr"):
    table.add_row([item1.find("th").text, item1.find("span").text])
print(table)