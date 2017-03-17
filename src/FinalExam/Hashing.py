from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))


class DelObj: pass


DELETED = Entry(DelObj(), None)


class hashmap:
    def __init__(self):
        self.table = [None] * 15
        self.entries = 0

    def remove(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED
            self.entries -= 1

    def put(self, key, value):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index] != DELETED:
            index += 1
            if index == len(self.table):
                index = 0
        self.table[index] = Entry(key, value)
        self.entries += 1
        if self.entries / len(self.table) > .7:
            oldtable = self.table
            self.table = [None] * (2 * len(self.table))
            for item in oldtable:
                if item is not None:
                    self.put(item.key, item.value)

    def __contains__(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        return self.table[index] is not None

    def get(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        return None

    def hash_func(self, key):
        return len(key)

    def printMap(self):
        for item in self.table:
            print(item)


def main():
    h = hashmap()
    h.put("a", 1)
    h.put("b", 2)
    h.put("c", 3)
    h.put("d", 4)
    h.put("e", 5)
    h.put("f", 6)
    h.put("g", 7)
    h.put("h", 8)
    print(h.__contains__('h'))
    print(h.get("g"))
    h.remove("g")
    print(h.get("g"))
    h.printMap()


if __name__ == '__main__':
    main()
