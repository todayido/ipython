# coding:utf8
from __future__ import division


def add(x, y):
    return x+y


def minus(x, y):
    return x-y


def multi(x, y):
    return x*y


def divide(x, y):
    return x/y

operator = {"+": add, "-": minus, "*": multi, "/": divide}


# print operator["+"](3, 2)
def f(x, o, y):
    return operator.get(o)(x, y)


print f(2, "-", 2)

