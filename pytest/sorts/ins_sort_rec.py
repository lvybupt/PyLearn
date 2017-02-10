'''
插入排序 递归办  python 算法 page 80

'''

def ins_sort_rec(seq,i):
    if i == 0: return
    print(i)
    ins_sort_rec(seq,i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1],seq[j] = seq[j],seq[j-1]
        j -= 1


if __name__ == '__main__':
    a = [10,5,6,8,90,4,5,87,67,4]
    print(len(a))
    ins_sort_rec(a,len(a)-1)
    print(a)