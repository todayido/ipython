# coding:utf8
def person(name="name", age=0):
    print "name:%s age:%d" % (name, age)

p = {"name": "name_20", "age": 20}
p2 = {"name": "name_22", "age": 22}
# a = (21, "Micky")
a = ("name_21", 21)

person("Micky", 20)
# 元组传值一个*
person(*a)
# 字典传值两个*
person(**p2)

