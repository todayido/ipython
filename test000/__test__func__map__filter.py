# coding:utf8

name = ['tom', 'jerry', 'micky']
age = [20, 30, 40]
tel = [111,222]
a = zip(name, age)
# [('tom', 20), ('jerry', 30), ('micky', 40)]
print a

# [('tom', 20, 111), ('jerry', 30, 222)]
print zip(name, age, tel)

# [('tom', 20, 111), ('jerry', 30, 222), ('micky', 40, None)]
print map(None, name, age, tel)

def f(x, y):
    return x * y


a = [2, 3, 4]
b = [5, 6, 7]
# [(2, 5), (3, 6), (4, 7)]
print map(None, a, b)
# [10, 18, 28]
print map(f, a, b)