class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class OurTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        self.traversefromlefttoright(self.root)

    def traversefromlefttoright(self,node):
        if node is None:
            return
        else:
            # print(node.data, end=' ')
            self.traversefromlefttoright(node.left)
            # print(node.data, end=' ')
            self.traversefromlefttoright(node.right)
            print(node.data, end=' ')


def main():
    one = BTNode("1")
    two = BTNode("2")
    plus = BTNode("+")
    plus.left = one
    plus.right = two
    a = BTNode("3")
    b = BTNode("2")
    minus = BTNode("-")
    minus.left = a
    minus.right = b
    mul = BTNode("*")
    mul.left = plus
    mul.right = minus

    t = OurTree()
    t.root = mul
    t.traverse()




if __name__ == '__main__':
    main()
