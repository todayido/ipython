import re

s = "abc"
print re.findall(s, "aabcaaaaaaaaaa")

st = "top tip tap twp tep"

print re.findall("top", st)

res = r"t[^io]p"

print re.findall(res, st)

st = "hello a hello b"
print re.findall("^hello", st)
print "====", re.findall("hello$", st)

res = "t[abc$]"

res = r"x[a-zA-Z0-9]{3}y"
print "====", re.findall(res, "x123y")