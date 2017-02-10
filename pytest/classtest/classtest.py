'''
class 测试

'''

class Tree:
    def __init__(self,kids,next=None):
        self.kids = self.val=kids
        self.next = next

def main():
    t = Tree(Tree("a",Tree("b",Tree("c",Tree("d")))))
    print(t.kids.next.next.val)

if __name__ == '__main__':
    main()