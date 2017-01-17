# coding:utf8

# 打开文件
# fo = open("test.txt", "w+")
# fo = open("test.txt", "r+")
fo = open("test.txt", "a+")
# 读取文件内容
fo.write("123")
# 提交更新
fo.flush()
content = fo.read()
# 关闭文件
fo.close()

print content
