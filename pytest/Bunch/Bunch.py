'''
class Bunch python算法书34页,适用于表示树

'''

class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch,self).__init__(*args,**kwds)
        self.__dict__ = self

def main():
    T = Bunch
    t = T(left=T(left="a",right="b"),right=T(left="c"))
    print(t.left)

if __name__ == '__main__':
    main()

