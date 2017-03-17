import random
class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = BTNode(value)
        else:
            self.insert_from(self.root,value)

    def insert_from(self,node,value):
        if value > node.data:
            if node.right is None:
                node.right = BTNode(value)
            else:
                self.insert_from(node.right, value)
        else:
            if node.left is None:
                node.left = BTNode(value)
            else:
                self.insert_from(node.left, value)

    def traverse(self):
        self.traverse_from(self.root)

    def traverse_from(self,node):
        if node is None:
            return
        else:
            #print(node.data, end=' ')
            self.traverse_from(node.left)
            print(node.data, end=' ')
            self.traverse_from(node.right)

    def height(self):
        return self.ht(self.root)

    def ht(self,node):
        if node is None:
            return 0
        else:
            return max(self.ht(node.left),self.ht(node.right))+1


def main():
    t = BinaryTree()
    t.insert(8)
    t.insert(6)
    t.insert(4)
    t.insert(3)
    t.insert(9)
    t.insert(11)
    t.insert(12)

    # l = [random.randint(1,100) for _ in range(  10)]
    # print(l)
    # for item in l:
    #     t.insert(item)


    t.traverse()
    print()
    print(t.height())


if __name__ == '__main__':
    main()

