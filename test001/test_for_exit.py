s = "hello"
d = {1: 1111, 2: 2222, 4: 3333, 5: 4444}
for x in range(1, 10):
    if x == 2:
        pass
    if x == 5:
        print "hello 22222222"
        continue
    if x == 3:
        break
else:
    print "Ending..."

for x in range(1, 10):
    print "--------> ", x