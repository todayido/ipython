# coding:utf8

__file__name = "aa.txt"
try:
    fo = open(__file__name)
except IOError, msg:
    print msg
    pass
except NameError, msg:
    print msg
    pass
finally:
    print "OK"
    fo.close()
