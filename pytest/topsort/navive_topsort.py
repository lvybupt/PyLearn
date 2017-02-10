'''
python 算法书 朴素的拓扑排序 page 90

'''

def navie_topsort(G, S=None ):
    if S == None: S = set(G)
    if len(S) == 1 : return list(S)
    v = S.pop()
    seq = navie_topsort(G,S)
    min_i = 0
    for i,u in enumerate(seq):
        if v in G[u]: min_i =i+1
    seq.insert(min_i,v)
    return seq

if __name__ == '__main__':
    print(1)