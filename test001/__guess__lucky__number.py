lucky_number = 20
input_number = -1
count = 3
while input_number!=lucky_number and count != 0:
    input_number = int(input("Input ur number:"))
    if input_number > lucky_number:
        print "big"
    elif input_number<lucky_number:
        print "small"
    # 超过次数退出程序
    count = count - 1

if count == 0:
    print("try too times ...")
else:
    print ("Bingo")