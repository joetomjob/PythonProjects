class QueueNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class OurQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        newnode = QueueNode(value,None)
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode
        self.tail = newnode

    def dequeue(self):
        saveme = self.head
        self.head = self.head.next
        return saveme.data

    def is_empty(self):
        return self.head is None


def main():
    t = OurQueue()
    t.enqueue(2)
    t.enqueue(6)
    t.enqueue(8)
    t.enqueue(9)

    while not t.is_empty():
        print(t.dequeue())

if __name__ == '__main__':
    main()

