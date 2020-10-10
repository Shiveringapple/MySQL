import csv
import codecs
import requests
import io
import json
# with codecs.open("2020-07-30.csv", "r", encoding="utf8") as f:
#     ret = list(csv.reader(f))
#     for item in ret:
#         print(item)

# r = requests.get("https://lod2.apc.gov.tw/API/v1/dump/datastore/A53000000A-000041-003")
# f = io.StringIO(r.text)
# ret = list(csv.reader(f))
# for item in ret:
#     print(item[1], item[2])

# r = requests.get("https://lod2.apc.gov.tw/API/v1/dump/datastore/A53000000A-000041-001")
# ret = json.loads(r.text)
# print(ret[0]["result"]["records"][0]["Name"])
# for item in ret[0]["result"]["records"]:
#     print(item["DateListed"], item["Region"], item["Name"])
# ret = json.loads(r.text)
# for item in ret[0]["result"]["records"]:
#     print(item["Name"], item["Ethnic"])

# for p in range(1, 4):
#     r = requests.get("https://udn.com/api/more?",
#                      params={
#                          "page":"p",
#                          "id":"",
#                          "channelId":"1",
#                          "cate_id":"0",
#                          "type":"breaknews",
#                          "totalRecNo":"6532"
#                      }
#                      )
# ret = json.loads(r.text)
# for item in ret["lists"]:
#     print(item["title"], item["view"])

from bs4 import BeautifulSoup
#
# fileName = 1
# r1 = requests.get("https://money.udn.com/rank/newest/1001/0/1")
# c1 = BeautifulSoup(r1.text, "html.parser")
# for item1 in c1.find_all("tr"):
#     data1 = item1.find_all("td")
#     if len(data1) > 0:
#         # print(data1[2].text, data1[0].text)
#         r2 = requests.get(data1[0].find("a").attrs["href"])
#         c2 = BeautifulSoup(r2.text, "html.parser")
#         with codecs.open("html/" + str(fileName) + ".txt", "w", "utf-8") as f:
#             f.write("新聞標題:" + data1[0].text + "\r\n")
#             f.write("新聞時間:" + data1[2].text + "\r\n")
#             f.write("新聞內容: \r\n" + c2.find("div", {"id":"article_body"}).text)
#         fileName += 1

# fileName = 1
# r1 = requests.get("https://newtalk.tw/news/summary/today")
# r1.encoding = "utf-8"
# c1 = BeautifulSoup(r1.text, "html.parser")
# for item1 in c1.find_all("div", {"class": "text"}):
#     with codecs.open("html2/" + str(fileName) + ".txt", "w", "utf-8") as f:
#         f.write("新聞日期:" + item1.find("div", {"class": "news_date"}).text.replace("發布", "") + "\r\n")
#         f.write("新聞標題:" + item1.find("div", {"class": "news_title"}).text.replace("", "").replace("\r\n", "") + "\r\n")
#         f.write("新聞簡介:" + item1.find("div", {"class": "news_text"}).text)
#     fileName += 1
fileName = 1
r1 = requests.get("https://newtalk.tw/news/summary/today")
r1.encoding = "utf-8"
c1 = BeautifulSoup(r1.text, "html.parser")
for item1 in c1.find_all("img", {"class": "fit"}):
    r2 = requests.get(item1.attrs["src"])
    with codecs.open("image/" + str(fileName) + ".jpg", "wb") as f:
        f.write(r2.content)
    fileName += 1
