import re

s = "abc"
print re.findall(s, "aabcaaaaaaaaaa")

st = "top tip tap twp tep"

print re.findall("top", st)

res = r"t[^io]p"

print re.findall(res, st)
