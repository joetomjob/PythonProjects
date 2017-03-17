from collections import namedtuple
#QueueNode = namedtuple('QueueNode',('data','next'))


class QueueNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,item):
        newnode = QueueNode(item, None)

        if self.tail is None:
            self.head = newnode        #For the first time head is set to new node. 2nd time, next of head should point to next node. Here 1st time head and tail are same. so in next line we have written self.tail.next = newnode. Therefore after 1st time the next of head is also set to next node
        else:
            self.tail.next = newnode
        self.tail = newnode

    def dequeue(self):
        if self.head is None:
            self.tail = None
        saveme = self.head
        self.head = self.head.next
        return saveme.data

    def is_empty(self):
        return self.head is None

def main():
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    while not q.is_empty():
        print(q.dequeue())

if __name__ == '__main__':
    main()
