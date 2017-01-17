import re

count = 0
fo = open("test.txt")
for s in fo.readlines():
    line = re.findall("hello", s)
    if len(line) > 0:
        count += len(line)

print "Search %d hello..." % count
fo.close()
