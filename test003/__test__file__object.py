# coding:utf8

fo = open("test.txt", "a+")
# content = fo.read()
# print content

# for i in open("test.txt"):
#     print i

# print fo.readline()
# # 将指针移动到开头，继续读取
# fo.seek(0, 0)
# print fo.readline()

l = ["one\n", "two\n", "three\n"]
fo.writelines(l)
fo.close()



