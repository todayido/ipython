s = "hello"
d = {1:1111,2:2222,4:3333,5:4444}
# for n in range(len(s)):
#     print "======", s[n]
#
# for x in range(s):
#     if x >= 2:
#         print x

for x in d:
    print d[x]
    # print x

print d.items()

# 遍历集合：KEY,VALUE
for k,v in d.items():
    print k
    print v
