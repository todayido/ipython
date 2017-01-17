# coding:utf8
# 注意连接数据库版本：3.6
import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='root',
                             db='mysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
cursor.execute("select * from user")
result = cursor.fetchall()

for c in result:
    print(c["Host"])
# print(result)
