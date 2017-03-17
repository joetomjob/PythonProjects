class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class OurList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, value):
        newnode = ListNode(value, None)
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode
        self.tail = newnode

    def add_first(self, value):
        newnode = ListNode(value, None)
        newnode.next = self.head
        self.head = newnode
        if self.tail is None:
            self.tail = self.head

    def remove_first(self):
        saveme = self.head
        self.head = self.head.next
        return saveme.data

    def insert(self, ind, value):
        finger = self.head
        for _ in range(ind):
            finger = finger.next
        newnode = ListNode(value, finger.next)
        finger.next = newnode

    def start(self):
        return self.head

    def value_of(self, finger):
        return finger.data

    def next(self, finger):
        return finger.next

    def is_empty(self):
        return self.head is None


def main():
    t = OurList()
    t.add_last(12)
    t.add_last(13)
    t.add_last(14)
    t.add_last(15)
    t.add_first(16)

    node = ListNode(13, None)
    t.insert(2, 18)

    print(t.next(node))

    # while not t.is_empty():
    #     print(t.remove_first())


if __name__ == '__main__':
    main()
