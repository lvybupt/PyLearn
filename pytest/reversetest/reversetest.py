import time

def test1():
    count = 10**6
    nums = []
    for i in range(count):
        nums.append(i)



def test2():
    count = 10 ** 6
    nums = (i for i in range(count))




'''

def test2():
    count = 10**6
    nums = []
    for i in range(count):
        nums.insert(0,i)
'''


def main():
    time1=time.time()
    test1()
    time2=time.time()
    print(time2 - time1)
    test2()
    time3=time.time()
    ##print(time2-time1)
    print(time3-time2)

if __name__ == '__main__':
    main()