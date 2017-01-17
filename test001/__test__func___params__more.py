# coding:utf8
def func(x, *args):
    print x, args

a = [1, 2, 3]

func(1)
func(1,2)
func(1,2,3)
print "========================="
def func2(x, *agrs, **kwargs):
    print x
    print agrs
    print kwargs

# 注意不能出现与参数相同的字典数据
# func2(1, 2, 3, x = 10, y=20, z=30)
func2(1, 2, 3, y=20, z=30)

