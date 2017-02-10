'''
插入排序,循环版  python 算法书 page 80

'''

def ins_sort(seq):
    seq_len=len(seq)
    for i in range(seq_len):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            seq[j-1],seq[j] = seq[j],seq[j-1]
            j -= 1


if __name__ == '__main__':
    a = [10,5,6,8,90,4,5,87,67,4]
    print(len(a))
    ins_sort(a)
    print(a)