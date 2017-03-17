class ListNode:

    def __init__(self,data,next):
        self.data = data
        self.next = next

class OurList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self,item):
        newNode = ListNode(item,None)
        if self.tail is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def remove_first(self):
        if self.head is None:
            self.tail = None
        saveme = self.head
        self.head = self.head.next
        return saveme

    def is_empty(self):
        return self.head is None

    def add_first(self,item):
        newnode = ListNode(item,self.head)
        if self.tail is None:
            self.tail = newnode
        self.head = newnode

    def insert(self, item, ind):
        finger = self.head
        for _ in range(ind):
            finger = finger.next
        newnode = ListNode(item,finger.next)
        finger.next = newnode

    def start(self):
        return self.head

    def value_of(self,finger):
        return finger.data

    def next(self,finger):
        return finger.next

    def insert_after(self,finger,item):
        newnode = ListNode(item,finger.next)
        finger.next = newnode

    def __str__(self):
        r =''
        finger = self.head
        while finger is not None:
            r = r+str(finger.data)
            finger = finger.next
        return r

    def copy(self):
        r = OurList()
        finger = self.head
        if self.head is not None:
            while finger is not None:
                r.add_last(finger.data)
                finger = finger.next
        return r

    def join(self, other):
        if self.tail is None:
            self.head = other.head
        else:
            self.tail.next = other.head
        self.tail = other.tail

    def splice(self, ind, other):
        finger = self.head
        for _ in range(ind):
            finger = finger.next
        x = finger.next
        finger.next = other.head
        other.tail.next = x

    def snip(self, i1, i2):
        if self.head is not None:
            finger = self.head
            for _ in range(i1-1):
                finger = finger.next
            x = finger
            for _ in range(i2-i1):
                finger = finger.next
            x.next = finger.next


def main():
    t = OurList()
    t.add_last(2)
    t.add_last(3)
    t.add_last(4)

    t.insert(78,0)

    t.insert_after(t.start().next.next,99)

    node = ListNode(78,None)


    #while not t.is_empty():
        #print(t.remove_first().data)
    print()

    print(t.value_of(node))
    print(t.next(node))

    t.insert_after(node, 98)

    print()
    print(t.__str__())
    print()

    x = OurList()
    x = t.copy()

    t.join(x)

    t.splice(1,x)

    #t.snip(2,4)
    #while not x.is_empty():
        #print(x.remove_first().data)

    while not t.is_empty():
        print(t.remove_first().data)

if __name__ == '__main__':
    main()



