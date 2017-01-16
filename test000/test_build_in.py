# coding:utf8
# 首字母大写
print str.capitalize("hello")
print str.capitalize("hello world")

# 替换
print str.replace("good", "oo" , "e")
# 替换一次
print str.replace("good", "o" , "e", 1)

ip = "192.168.1.1"
# ['192', '168', '1', '1']
print str.split(ip, ".")
