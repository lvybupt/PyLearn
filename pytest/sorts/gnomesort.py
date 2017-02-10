'''
侏儒排序法,python算法书68页

'''

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i ==0 or seq[i-1] <= seq [i]:
            i +=1
        else:
            seq[i],seq[i-1] = seq[i-1],seq[i]
            i -=1

if __name__ == '__main__':
    seq = [10,2,4,98,23,87,2]
    gnomesort(seq)
    print(seq)