class Element:
    __slots__ = ('value', 'priority', 'link')

    def __init__(self, value = None, priority=None, link=None):
        self.value = value
        self.priority = priority
        self.link = link

class QueueNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class OurHeap:
    __slots__ = ('stuff','sz')

    def __init__(self):
        self.stuff = [None for _ in range(1000)]
        self.sz = 0

    def insert(self,value):
        self.stuff[self.sz] = value
        self.stuff[self.sz].data.link = self.sz
        spot = self.sz
        while spot>0 and self.stuff[self.sz].data.priority > self.stuff[self.par(spot)].data.priority:
            self.stuff[self.sz], self.stuff[self.par(spot)] = self.stuff[self.par(spot)], self.stuff[self.sz]
            spot = self.par(spot)
            self.stuff[self.sz].data.link = self.sz
            self.stuff[spot].data.link = spot
        self.sz += 1


    def par(self, ind):
        return (ind-1)//2

    def pop(self):
        popped_element = self.stuff[0]
        self.sz -= 1
        self.stuff[0] = self.stuff[self.sz]
        self.stuff[0].data.link = 0
        loc=0
        swapLoc = self.__smallest(loc)
        while swapLoc != loc:
            self.stuff[loc], self.stuff[swapLoc] =  self.stuff[swapLoc], self.stuff[loc]
            self.stuff[loc].data.link = loc
            self.stuff[swapLoc].data.link = swapLoc
            loc = swapLoc
            swapLoc = self.__smallest(loc)
        return popped_element

    def pop_after_dequeue(self,node):
        self.stuff[0],self.stuff[node.data.link] = self.stuff[node.data.link],self.stuff[0]
        self.pop()

    def __smallest(self,loc):

        ch1 = loc*2 + 1
        ch2 = loc*2 + 2
        if ch1 >= self.sz:
            return loc
        if ch2 >= self.sz:
            if self.stuff[loc].data.priority > self.stuff[ch1].data.priority:
                return loc
            else:
                return ch1

        if self.stuff[ch1].data.priority>self.stuff[ch2].data.priority:
            if self.stuff[loc].data.priority>self.stuff[ch1].data.priority:
                return loc
            else:
                return ch1
        else:
            if self.stuff[loc].data.priority>self.stuff[ch2].data.priority:
                return loc
            else:
                return ch2


class OurQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        newnode = QueueNode(value)
        leftnode = self.tail
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.right = newnode
            newnode.left = self.tail
        self.tail = newnode
        return self.tail


    def dequeue(self):
        saveme = self.head
        self.head = self.head.right
        return saveme

    def rearrange(self,node):
        if self.head == node:
            self.head = node.right
        else:
            left = node.left
            right = node.right
            if left is not None:
                left.right = right
            if right is not None:
                right.left = left


    def is_empty(self):
        return self.head is None

def main():
    filename = input('Please enter the filename: ')
    queue_order = OurQueue()
    heap_confusion = OurHeap()
    with open(filename) as data:
        for item in data:
            parts = item.strip().split(' ')
            if parts[1] not in ("ready"):
                h = Element()
                h.value = parts[0]
                h.priority = int(parts[1])
                h = queue_order.enqueue(h)
                heap_confusion.insert(h)
                print(h.data.value+" is looking for help")
            elif(parts[0] in ("Colleen")):
                if heap_confusion.sz>0:
                    popped_element = heap_confusion.pop()
                    queue_order.rearrange(popped_element)
                    print("Colleen is helping "+popped_element.data.value)
            elif (parts[0] in ("Oliver")):
                if queue_order.head is not None:
                    popped_element = queue_order.dequeue()
                    heap_confusion.pop_after_dequeue(popped_element)
                    print("Oliver is helping "+popped_element.data.value)
        print("Students left unhelped: ")
        for i in range(heap_confusion.sz):
            print(heap_confusion.stuff[i].data.value)


if __name__ == '__main__':
    main()
