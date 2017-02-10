'''
寻找最大排序问题 递归算法 python算法书 page 84

'''

def naive_max_perm(M,A = None):
    if A == None : A = set(range(len(M)))
    C = set(M[i] for i in A)
    B = A - C
    if B :
        A = C  ####原程序此处不一样
        return naive_max_perm(M,A)
    return A

if __name__ == '__main__':
    M = [2,2,0,5,3,5,7,4]
    print(naive_max_perm(M))