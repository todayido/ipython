# coding:utf8
# lambda 快速定义单行的最小函数，从List借鉴而来
# 其lambda 是返回了一个函数对象


def func(x, y):
    return x * y


print func(2, 3)

g = lambda x,y:x*y
print g(6, 2)*2