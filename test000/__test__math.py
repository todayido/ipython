#coding:utf8

print "求长度：", len([1, 2, 3])
# 查看帮助
# print "====\n", help(divmod)
print "取商和余数：", divmod(10,3)
print "求平方：", pow(2,4)
print "求最小值", min(2,4,5,6,1,1)

a = 100
b = []
print "是否可被调用：", callable(a)
print "是否是整数:", isinstance(a, int)
print "是否是元组:", isinstance(b, list)

print range(10)
# 0...9
print xrange(10)[9]
print xrange(10)[10]