'''
朴素版明星问题  python 算法书 87 页

'''

def naive_celeb(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if i == j : continue
            if G[i][j] : break
            if not G[j][i] : break
        else:  ###else 对应 for ,而不是对应  if。 break 未执行,就else
            return  i
    return n

if __name__ == '__main__':
    from random import  randrange
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    print(c)
    for i in range(n):
        G[i][c] = True
        G[c][i] = False
    print(naive_celeb(G))