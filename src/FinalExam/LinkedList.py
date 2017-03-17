class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class OurList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        node = ListNode(item, None)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def add_first(self, item):
        node = ListNode(item, None)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def remove_first(self):
        save_me = self.head
        self.head = self.head.next
        return save_me.data

    def insert(self, ind, value):
        finger = self.head
        for i in range(ind):
            finger = finger.next
        node = ListNode(value, finger.next)
        finger.next = node
