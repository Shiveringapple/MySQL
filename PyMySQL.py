import pymysql
import prettytable
import colorama

# table = prettytable.PrettyTable(["ID", "Title"], encoding="utf-8")
# table.align["ID"] = "r"
# table.align["Title"]= "l"
#
# table.add_row(["1", "aaa"])
# table.add_row(["2", "bbb"])
# table.add_row(["3", "ccc"])
# print(table)

link = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="python",
    charset="utf8"
)
cur = link.cursor()

# 新增
# param ={
#     "a":"標題",
#     "b":"來源",
#     "c":"2020-07-23",
#     "d":"說明"
# }
# cur.execute("INSERT INTO `news`(`Title`,`Source`,`Create_time`,`Description`) VALUES(%(a)s,%(b)s,%(c)s,%(d)s)", param)
# link.commit()
#
# print("ID:", cur.lastrowid)

# 刪除
# param = {
#     "Id":"17",
# }
# cur.execute("DELETE FROM `news` WHERE `Id`=%(Id)s", param)
# link.commit()


# 搜尋
param = {
    "Id": "20",
}
cur.execute("SELECT * FROM `news` WHERE `Id`<%(Id)s", param)
# data = cur.fetchall()
# for item in data:
#     print(item[0], item[1])

# param = {
#     "Id":"17",
# }
# cur.execute("SELECT * FROM `news` WHERE `Id`<%(Id)s", param)
# data = cur.fetchone()
# print(data[0], data[1])
#
# data = cur.fetchone()
# print(data[0], data[1])
#
# data = cur.fetchone()
# print(data[0], data[1])
#
# data = cur.fetchall()
# for item in data:
#     print(item[0], item[1])
#
# print("總共資料數量:", cur.rowcount)

colorama.init(True)

table = prettytable.PrettyTable(["ID", "Title"], encoding="utf8")
table.align["ID"] = "r"
table.align["Title"] = "l"

data = cur.fetchall()
for item in data:
    # print(item[0], item[1])
    table.add_row([item[0], colorama.Back.BLUE + item[1] + colorama.Back.RESET])
print(table)

print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "總共資料數量:", cur.rowcount)






link.close()
