# 爬蟲

import requests
import json

url = "http://teaching.bo-yuan.net/test/requests/"

r = requests.get(url)
r.encoding = "utf-8"
print(r.text)

param = {"action": "value"}
r = requests.get(url, params=param)
r.encoding = "utf-8"
print(r.text)

r = requests.delete(url, params=param)
r.encoding = "utf-8"
print(r.text)

data = {"id": "value"}
r = requests.delete(url, params=param, data=data)
r.encoding = "utf-8"
print(r.text)


data = {"id": "value"}
r = requests.put(url, params=param, data=data)
r.encoding = "utf-8"
print(r.text)

data = {"id": "value"}
r = requests.patch(url, params=param, data=data)
r.encoding = "utf-8"
print(r.text)

data = {"id": "value", "name": "value"}
r = requests.patch(url, params=param, data=data)
r.encoding = "utf-8"
print(r.text)

data = {"id": "value", "name": "value", "address": "value"}
r = requests.post(url, params=param, data=data)
r.encoding = "utf-8"
print(r.text)

# x = ["a", "b", "c", "d", "0", "1", "2", "3", "4", "5"]
# y = []
# def pwdList(v, n):
#     global x, y
#     for i in x:
#         if n > 1:
#             pwdList(v+i, n-1)
#         print(v+i)
#         y.append(v+i)
# pwdList("", 2)
#
#
# for pwd in y:
#     r1 = requests.post(
#         "http://teaching.bo-yuan.net/",
#         params={
#             "uid":"5f1b84a522c97"
#         },
#         headers={
#             "Cookie":"PHPSESSID=25h5rk5udhei6tdiu2rhqik942",
#         },
#         data={
#             "ex[class]":"5f17dc98b0dfd",
#             "ex[username]":"99測試",
#             "ex[password]":pwd
#         }
#     )
#     r2 = requests.get(
#         "http://teaching.bo-yuan.net/",
#         headers={
#             "Cookie":"PHPSESSID=25h5rk5udhei6tdiu2rhqik942",
#         }
#     )
#     r2.encoding="utf-8"
#     if "5f1b84a522c97" not in r2.text:
#         print("登入成功! 密碼是:", pwd)
#         break