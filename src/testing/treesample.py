class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class OurTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        self.traverse_from(self.root)

    def traverse_from(self,node):
        if node is None:
            return
        else:
            self.traverse_from(node.left)
            self.traverse_from(node.right)
            print(node.data, end=' ')

def main():
    one = BTNode("1")
    two = BTNode("2")
    plus = BTNode("+")
    plus.left = one
    plus.right = two
    minus = BTNode("-")
    a = BTNode("3")
    b = BTNode("2")
    minus.left = a
    minus.right = b
    mul = BTNode("*")
    mul.left = plus
    mul.right = minus
    root = OurTree()
    root.root = mul
    root.traverse()

if __name__ == '__main__':
    main()