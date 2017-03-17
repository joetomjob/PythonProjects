from collections import namedtuple

StackNode = namedtuple('StackNode',('data','next'))

class OurStack:
    def __init__(self):
        self.top = None

    def insert(self,value):
        newnode = StackNode(value,self.top)
        self.top = newnode

    def pop(self):
        saveme = self.top
        self.top = self.top.next
        return saveme.data

    def display(self):
        self.displayallvalues(self.top)

    def displayallvalues(self,top):
        while top is not None:
            print(top.data)
            top = top.next

    def is_empty(self):
        return self.top is None

def main():
    s = OurStack()
    s.insert(1)
    s.insert(5)
    s.insert(9)
    #s.pop()
    s.display()

    while not s.is_empty():
        print(s.pop(),end=' ')



if __name__ == '__main__':
    main()
