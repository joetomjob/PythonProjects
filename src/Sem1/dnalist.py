class ListNode:
    def __init__(self, data, next):
        self.item = data
        self.next = next


class DNAList:
    def __init__(self, gene=''):
        self.head = None
        self.tail = None

        if gene is not None:
            for i in range(len(gene)):
                if gene[i] in ['A', 'C', 'G', 'T']:
                    newnode = ListNode(gene[i], None)
                    if self.tail is None:
                        self.head = newnode
                    else:
                        self.tail.next = newnode
                    self.tail = newnode

    def append(self, item):
        if item in  ['A','C','G','T']:
            newnode = ListNode(item, None)
            if self.tail is None:
                self.head = newnode
            else:
                self.tail.next = newnode
            self.tail = newnode
        else:
            print("A,C,G and T are only accepted by DNA")


    def join(self, other):
        if self.tail is None:
            self.head = other.head
        else:
            self.tail.next = other.head
        self.tail = other.tail

    def splice(self, ind, other):
        if type(ind)==int:
            if ind >= 0:
                finger = self.head
                for _ in range(ind):
                    if finger is not None:
                        finger = finger.next
                if finger is None:
                    if finger == self.head:
                        self.head = other.head
                        self.tail = other.tail
                    else:
                        print("Index is out of bounds")
                else:
                    x = finger.next
                    if other.head is not None:
                        finger.next = other.head
                        other.tail.next = x
            else:
                print("please enter a value greater than 0")
        else:
            print("please enter an integer value as index")

    def snip(self, i1, i2):
        if self.head is not None:
            finger = self.head
            for _ in range(i1 - 1):
                finger = finger.next
            x = finger
            for _ in range(i2 - i1):
                finger = finger.next
            x.next = finger.next

    def replace(self, repstr, other):
        if self.head is not None:
            trav = self.head
            temp = self.head
            start = self.head
            end = self.head
            while trav != None:
                if trav.item == repstr[0]:
                    r = ''
                    for i in range(len(repstr)):
                        if temp.item == repstr[i]:
                            r = r + temp.item
                            end = temp
                            temp = temp.next
                    if r == repstr:
                        if other.head is not None:
                            if trav == self.head:
                                self.head = other.head
                            else:
                                start.next = other.head
                            other.tail.next = end.next
                        else:
                            if trav == self.head:
                                self.head = end.next
                            else:
                                start.next = end.next

                        return
                start = trav
                trav = trav.next
                temp = trav

    def copy(self):
        r = DNAList()
        finger = self.head
        if self.head is not None:
            while finger is not None:
                r.append(finger.item)
                finger = finger.next
        return r

    def __str__(self):
        r = ''
        finger = self.head
        while finger is not None:
            r += str(finger.item)
            finger = finger.next
        return r



