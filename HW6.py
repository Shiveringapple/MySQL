import csv
import codecs
import requests
import io
import json
import prettytable

from bs4 import BeautifulSoup
r1 = requests.get("https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Thu%20Jul%2030%202020%2017:14:01%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)")
r1.encoding = "utf-8"
c1 = BeautifulSoup(r1.text, "html.parser")
table = prettytable.PrettyTable(["地區", "氣溫"], encoding="utf8")
for item1 in c1.find_all("tr"):
    data1 = item1.find_all("td")
    data2 = item1.find_all("th")
    data3 = item1.find_all("span")
    # print(data2[0].text, data3[0].text)

    table.align["地區"] = "c"
    table.align["氣溫"] = "c"
    table.add_row([data2[0].text, data3[0].text])
print(table)

