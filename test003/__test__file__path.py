# coding:utf8
import os


def __print__ath(path):
    for __file_name in os.listdir(path):
        # __file_path = os.getcwd() + "\\" + __file_name
        __file_path = os.path.join(path, __file_name)

        if os.path.isdir(__file_path) == True:
            __print__ath(__file_path)
        print __file_path


# __print__ath("../test003")

for path, d, name in os.walk("../test003"):
    print path, name
