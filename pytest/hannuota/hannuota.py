'''
解决汉诺塔问题:请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

'''

def hannuota(n,a,b,c):
    if n == 1:
        print(a,"==>",c)
        return
    else:
        hannuota(n-1,a,c,b)
        print(a,"==>",c)
        hannuota(n-1,b,a,c)

def main():
    hannuota(3,'A','B','C')

if __name__ == '__main__':
    main()