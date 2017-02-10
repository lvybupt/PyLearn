'''
归并排序  python算法书 page 68

'''

def mergesort(seq):
    mid = len(seq)//2
    lft,rgt = seq[:mid],seq[mid:]
    if len(lft) > 1 : lft = mergesort(lft)
    if len(rgt) > 1 : rgt = mergesort(rgt)
    res = []
    while lft and rgt :
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt ) + res

if __name__ == '__main__':
    seq = [10, 2, 4, 98, 23, 87, 2]
    seq = mergesort(seq)
    print(seq)