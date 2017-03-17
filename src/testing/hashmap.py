from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

class Delobj: pass

DELETED = Entry(Delobj(), None)

class Hashmap:
    def __init__(self):
        self.table = [None] * 3
        self.entries = 0

    def __contains__(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        return self.table[index] is not None

    def put(self, key, value):
        self.entries += 1
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index] != DELETED:
            index += 1
            if index == len(self.table):
                index = 0
        self.table[index] = Entry(key, value)
        if self.entries / len(self.table) > 0.7:
            self.entries = 0
            oldtable = self.table
            self.table = [None] * (2 * len(self.table))
            for entry in oldtable:
                if entry is not None:
                    self.put(entry.key, entry.value)

    def get(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            return None
        return self.table[index].value

    def remove(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED
            #check if : self.entries -=1 is to be added

    def hash_func(self, key):
        return len(key)

    def printMap(self):
        for i in range(len(self.table)):
            print(str(i) + ": " + str(self.table[i]))


def testmap():
    map = Hashmap()
    map.put('apple', 1)
    map.put('banana', 2)
    map.put('orange', 15)
    map.printMap()
    print('apple?', 'apple' in map)
    print('grape?', 'grape' in map)
    print('orange = ', map.get('orange'))

    print('--------- adding one more to force table resize ')
    map.put('grape', 7)
    map.printMap()

    print('--------- testing remove')
    map.remove('apple')
    map.printMap()
    print(map.get('grape'))

    print('--------- testing add to a DELETED location')
    map.put('peach', 16)
    map.printMap()
    print(map.get('grape'))


if __name__ == '__main__':
    testmap()
