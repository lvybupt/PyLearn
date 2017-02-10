'''
计数排序  python算法 page 86

'''

from collections import defaultdict

def counting_sort(A, key = lambda x:x):
    ### key 是一个自定义的函数表达式,可以定义计数排序的规则

    B,C = [],defaultdict(list)
    for x in A :
        C[key(x)].append(x)
    for k in range(min(C),max(C)+1):
        B.extend(C[k])
    return B

if __name__ == '__main__':
    a = [10,5,6,8,90,4,5,87,67,4]
    print(len(a))
    b=counting_sort(a)
    print(b)
