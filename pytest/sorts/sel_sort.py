'''
循环版选择排序,python 算法书  page81

'''

def sel_sort(seq):
    i=len(seq)
    while i > 0:
        maxj = i-1
        for j in range(i-1):
            if seq[j] > seq[maxj]: maxj =j

        seq[i-1],seq[maxj] = seq[maxj],seq[i-1]
        i -= 1

if __name__ == '__main__':
    a = [10,5,6,8,90,4,5,87,67,4]
    print(len(a))
    sel_sort(a)
    print(a)
