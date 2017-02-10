#-*- coding: UTF-8 -*-
'''
搜索某个文件路径下,包含所有子文件夹内文件名包含特定字符串的程序
'''

import os
import fnmatch

####测试
import time

def searchfile(curdir,sfitem):
    sfresult = []
    files = os.listdir(curdir)
    for name in files:
        fullname = os.path.join(curdir,name)
        if os.path.isdir(fullname):
            sfresult.extend(searchfile(fullname,sfitem))
        else:
            if sfitem in name :
                sfresult.append(fullname)

    return sfresult
'''
for filename in searchfile("/Volumes/程序音乐图书", "白夜行"):
    print (filename)
'''
def main():
    time1 = time.time()

    for filename in searchfile("/Volumes/程序音乐图书", "悟空"):
        print (filename)

    time2 = time.time()

    print(time2-time1)

if __name__=='__main__':
    main()