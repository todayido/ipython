count = 0
while (count < 8):
    print "The number is:", count
    count += 1
x = "a"
while x != "q":
    print "hello"
    x = raw_input("Please input something:(q for quit)")
    if not x:
        break
else:
    print "ending..."