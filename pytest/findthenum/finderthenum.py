'''
python 算法  习题3-4

'''

def ftm1(num,q):
    upnum=1
    while upnum <= num:
        upnum = upnum * (2**q)
    for i in range(upnum):
        if num == i:
            return i

def ftm2(num,q):
    upnum = 1
    while upnum <= num:
        upnum = upnum * (2 ** q)
    ##i = upnum
    downnum = 0
    while True:
        if (upnum + downnum) > num * 2:
            upnum = (upnum + downnum)//2
        elif(upnum + downnum) < num * 2:
            downnum = (upnum + downnum)//2
        else:
            return (upnum + downnum)//2

if __name__ == '__main__':
    from  random import randrange
    n = 10 ** 8
    num = randrange(n)

    print("ftp1",ftm1(num,10))
    print("ftp2",ftm2(num,10))
    print(num)
