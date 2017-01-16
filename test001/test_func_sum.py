# coding:utf8

def sumary(a, b):
    c = a + b
    print "求和：", a, " + ", b, " = ", c


def sumary2(a, b):
    c = a + b
    return "%s + %s = %s" % (a, b, c)


sumary(2, 2)
print sumary2(2, 2)
