# coding:utf8
# 默认值的话从右向左定义默认参数 def a(a=1, b)是错误的，如果想用请使用 def a(b ,a=1)


def a(x="圣代", y="草莓"):
    print "here is a ", x, "flavor: ", y
sssssssssss

# = raw_input("请输入你要什么(圣代，甜筒)：")
# b = raw_input("请输入你要什么口味的：")

# 所有参数都传递
a()
# 默认第一个参数
a("甜筒")
# 只传递第二个参数
a(y="苹果")
