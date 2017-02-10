#-*- coding: UTF-8 -*-

import os
import fnmatch

import time

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

def main():
    time1 = time.time()

    for filename in iterfindfiles("/Volumes/程序音乐图书", "*杂货店*.*"):
        print(filename)

    time2 = time.time()
    print(time2-time1)

    print("end")

if __name__=='__main__':
    main()