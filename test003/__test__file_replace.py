# coding:utf*
import re

# 拷贝文件内容，并替换
__from__file = open("test.txt")
__to__file = open("test2.txt", "a+")

for s in __from__file.readlines():
    ss = s.replace("hello", "world")
    __to__file.writelines(ss)

__from__file.close()
__to__file.close()