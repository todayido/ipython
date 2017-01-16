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


def operator(x, o, y):
    if o == "+":
        return add(x, y)
    elif o == "-":
        return minus(x, y)
    elif o == "*":
        return multi(x, y)
    else:
        return divide(x, y)


print operator(2, "/", 1)
