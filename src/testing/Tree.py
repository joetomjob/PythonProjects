
class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class OurTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        self.traverselefttoright(self.root)

    def traverselefttoright(self,Node):
        if Node is None:
            return
        else:
            self.traverselefttoright(Node.left)
            self.traverselefttoright(Node.right)
            print(Node.data, end=' ')

def main():
    a= BTNode('2')
    b= BTNode('1')
    c = BTNode('+')
    c.left =b
    c.right =a
    three = BTNode('3')
    two = BTNode('2')
    minus = BTNode('-')
    minus.left = three
    minus.right = two
    root = BTNode('*')
    root.left = c
    root.right = minus
    t = OurTree()
    t.root = root
    t.traverse()



if __name__ == '__main__':
    main()