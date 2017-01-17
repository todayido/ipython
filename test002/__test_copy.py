# coding:utf8
import copy

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a
print id(a), a
a.append(10)
c = copy.copy(a)

a[3] = 0
# 浅拷贝a=c 包括地址
print id(b), b
print id(c), c

# 深拷贝，完全拷贝
d = copy.deepcopy(a)
