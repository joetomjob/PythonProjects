from collections import namedtuple

StackNode = namedtuple('StackNode',('data','next'))

class OurStack():
    def __init__(self):
        self.top = None

    def insert(self,value):
        node = StackNode(value,self.top)
        self.top = node

    def pop(self):
        saveme = self.top
        self.top = self.top.next
        return saveme.data

    def is_empty(self):
        return self.top is not None


