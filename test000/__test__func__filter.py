# coding:utf8
# 能被2整除的数


def build__in__func(x):
    if x % 2 == 0:
        return True
    else:
        return False

print build__in__func(5)
l = range(10)
a = filter(build__in__func, l)
print a