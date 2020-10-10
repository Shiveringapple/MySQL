import pymysql
import prettytable
import colorama
import sys
import os

password = input("請輸入資料庫root密碼: ")
port = input("請輸入資料庫的port: ")

if port == "":
    port = "3306"
link = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = password,
    db ="python_ai",
    charset ="utf8",
    port = int(port)
)
cur = link.cursor()


# 顯示會員列表(OK)
def search():
    cur.execute("SELECT `member`.`id`, `name`, `birthday`, `address`,`tel` FROM `member` LEFT join `tel` ON `member`.`id` = `tel`.`member_id`")
    link.commit()

    table = prettytable.PrettyTable(["編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
    table.align["編號"] = "c"
    table.align["姓名"] = "l"
    table.align["生日"] = "l"
    table.align["地址"] = "l"
    table.align["電話"] = "l"


    data = cur.fetchall()
    for i in range(0, len(data)):
        item = data[i]
        if i == 0 or (i>0 and data[i][0] != data[i-1][0]):
            table.add_row([item[0], item[1], item[2], item[3], item[4]])
        else:
            table.add_row(["", "", "", "", item[4]])
    print(table)


# 新增會員(OK)
def insert():
    user_name = input("請輸入會員姓名: ")
    user_birth = input("請輸入會員生日: ")
    user_address = input("請輸入會員地址: ")
    param = {
        "a": user_name,
        "b": user_birth,
        "c": user_address
    }
    cur.execute("INSERT INTO `member`(`name`,`birthday`,`address`) VALUES (%(a)s, %(b)s, %(c)s)", param)
    link.commit()


# 刪除會員(OK)
def delete():
    search()
    user_delete = input("請輸入欲刪除會員編號: ")
    param = {
        "id": user_delete
    }
    cur.execute("DELETE FROM `member` WHERE `id`=%(id)s", param)
    link.commit()



# 修改(OK)
def modify():
    search()
    param = []
    id = input("請輸入欲修改會員編號: ")
    param.append(input("請輸入修改後的姓名: "))
    param.append(input("請輸入修改的生日: "))
    param.append(input("請輸入修改的地址: "))

    cur.execute("UPDATE member SET name = '%s', birthday = '%s', address = '%s' WHERE id = '%s'" % (param[0], param[1], param[2], id))
    link.commit()


# 新增會員電話(OK)
def insert_tel():
    search()
    user_tel_id = input("請輸入欲新增號碼的會員編號: ")
    user_tel = input("請輸入欲新增的電話號碼: ")
    param = {
        "id": user_tel_id,
        "t": user_tel,
    }
    cur.execute("INSERT INTO `tel`(`member_id`, `tel`) VALUES (%(id)s, %(t)s)", param)
    link.commit()

# 刪除會員電話
def delete_tel():
    search()
    user_delete_id = input("請輸入欲刪除號碼的會員編號: ")

    # 顯示選擇會員編號後的電話號碼表(同一個人的電話號碼可能輸入多次)
    param = {
        "d": user_delete_id
    }
    cur.execute("SELECT `id`, `tel` FROM `tel` WHERE `member_id` = %(d)s", param)
    link.commit()

    table = prettytable.PrettyTable(["編號","電話"], encoding="utf8")
    table.align["編號"] = "c"
    table.align["電話"] = "l"

    data = cur.fetchall()
    for item in data:
        table.add_row([item[0], item[1]])
    print(table)

    # 刪除電話編號
    user_delete = input("請輸入欲刪除的電話編號: ")
    param = {
        "n": user_delete
    }
    cur.execute("DELETE FROM `tel` WHERE `tel`.`id` = %(n)s", param)
    link.commit()

while True:
    user = input("(0) 離開選單\n"
                 "(1) 顯示會員列表\n"
                 "(2) 新增會員資料\n"
                 "(3) 更改會員資料\n"
                 "(4) 刪除會員資料\n"
                 "(5) 新增會員電話\n"
                 "(6) 刪除會員電話\n"
                 "指令: ")
    if user == "0":
        sys.exit()
    elif user == "1":
        search()
        continue
    elif user == "2":
        insert()
        continue
    elif user == "3":
        modify()
        continue
    elif user == "4":
        delete()
        continue
    elif user == "5":
        insert_tel()
        continue
    elif user == "6":
        delete_tel()
        continue
    else:
        print(input("錯誤的指令，請重新輸入: "))
        continue


link.close()
