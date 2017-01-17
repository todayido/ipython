# coding:utf8

def sumary(a, b):
    c = a + b
    return "%s + %s = %s" % (a, b, c)


a = [1, 2]
# 直接传递元组参数即可
print sumary(*a)
