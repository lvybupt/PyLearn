'''
寻找最大排序问题  非递归  python算法 page 85

'''

def max_perm(M):
    M_len = len(M)
    A = set(range(M_len))
    A_Count = [0]*M_len
    for i in M:
        A_Count[i] += 1
    Q = [i for i in A if A_Count[i] == 0]
    while Q:
        i = Q.pop()
        A_Count[M[i]] -= 1
        A.remove(i)
        if A_Count[M[i]] == 0:
            Q.append(M[i])
    return A

if __name__ == '__main__':
    M = [2,2,0,5,3,5,7,4]
    print(max_perm(M))
