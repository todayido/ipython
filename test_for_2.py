import time

d = {1: 1111, 2: 2222, 3: 3333, 5: 5555}
for x in range(1, 6):
    print x
    time.sleep(1)
    if x == 3:
        ## ending is not printed
        break
else:
    print "ending..."
