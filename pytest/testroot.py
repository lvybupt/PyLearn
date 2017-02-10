
'''
s = ""
a = ["a","b","c","d"]
t = s.join(a)
print(t)
string.producer()


print(sum(0.1 for i in range(10)) == 1.0)


def S(seq,i = 0):
    if i == len(seq) :return 0
    return S(seq,i+1) +seq[i]

print(S(range(1,101)))



dd = float("inf")
print(dd)

from random import  randrange
seq = [randrange(10*10) for i in range(100)]
for x in seq:
    for y in seq:
        if x == y : continue
        d =abs(x-y)
        if d < dd :
            xx,yy,dd = x,y,d

print(xx,yy)

'''

offsets = (0,-1),(90,0)
for i,j in offsets:
    for m,n in offsets:
        print(m,i)
        print(n,j)

'''
'''
