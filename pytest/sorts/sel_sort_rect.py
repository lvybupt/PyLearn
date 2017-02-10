'''
选择排序 递归版 python 算法书 page 81

'''


def sel_sort_rect(seq,i):
    if i == 0: return
    maxj = i
    for j in range(i):
        if seq[j] > seq [maxj]:
            maxj = j

    seq[maxj],seq[i] = seq[i],seq[maxj]
    sel_sort_rect(seq,i-1)

if __name__ == '__main__':
    a = [10,5,6,8,90,4,5,87,67,4]
    print(len(a))
    sel_sort_rect(a,len(a)-1)
    print(a)