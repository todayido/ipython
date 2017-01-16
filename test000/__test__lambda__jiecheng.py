# coding:utf8
# reduce内置计算阶乘


def func(x):
    if x > 0:
        print x
        x * func(x-1)


# 简单的reduce计算函数实现阶乘

a = range(1,6)
def f(x, y):
    return x*y

print reduce(f, a)
print reduce(lambda x, y: x*y, a)

