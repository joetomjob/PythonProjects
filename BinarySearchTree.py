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
            self.insert_from(self.root,value)

    def insert_from(self,node,value):
        if value < node.data:
            if node.left is None:
                node.left = BTNode(value)
            else:
                self.insert_from(node.left,value)
        else:
            if node.right is None:
                node.right = BTNode(value)
            else:
                self.insert_from(node.right, value)

    def height(self):
        return self.ht(self.root)

    def ht(self,node):
        if node is None:
            return 0
        else:
            leftht = self.ht(node.left)
            rightht = self.ht(node.right)
            height = max(leftht,rightht)+1
            return height


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

