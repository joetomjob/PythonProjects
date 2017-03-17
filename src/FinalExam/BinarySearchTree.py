class BTNode:

    __slots__ = ('data','left','right')

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class OurTree:
    __slots__ = ('root')

    def __init__(self):
        self.root = None

    def traverse(self):
        self.traversefromlefttoright(self.root)

    def traversefromlefttoright(self,node):
        if node is None:
            return
        else:
            self.traversefromlefttoright(node.left)
            print(node.data, end=' ')
            self.traversefromlefttoright(node.right)

    def insert(self,value):
        if self.root is None:
            self.root = BTNode(value)
        else:
            self.insertfrom(self.root,value)

    def insertfrom(self,node,value):
        if value<node.data:
            if node.left is None:
                node.left = BTNode(value)
            else:
                self.insertfrom(node.left, value)
        else:
            if node.right is None:
                node.right = BTNode(value)
            else:
                self.insertfrom(node.right,value)

    def height(self):
        return self.ht(self.root)

    def ht(self,node):
        if node is None:
            return 0
        else:
            lh = self.ht(node.left)
            rh = self.ht(node.right)
            return max(lh,rh)+1

def main():
    t = OurTree()
    t.insert(5)
    t.insert(2)
    t.insert(1)
    t.insert(8)
    t.insert(9)
    t.insert(3)
    t.traverse()
    print()
    print(t.height())

if __name__ == '__main__':
    main()

