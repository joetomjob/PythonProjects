import re
import math
from copy import deepcopy
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))


# class Entry:
#     def __init__(self, key, value = 1):
#         self.key = key
#         self.value = value

class Delobj: pass


DELETED = Entry(Delobj(), None)
MAXVALUE = 100000


class Hashmap:
    def __init__(self, hash_func, loadfactor):
        self.table = [None] * MAXVALUE
        self.entries = 0
        self.collisions = 0
        self.probes = 0
        self.hash_func = hash_func
        self.loadfactor = float(loadfactor)

    def __contains__(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == len(self.table):
                index = 0
        self.probes += 1
        return self.table[index] is not None

    def put(self, key, value=1):
        index = self.hash_func(key) % len(self.table)
        check_index = deepcopy(index)
        while self.table[index] is not None and self.table[index] != DELETED and self.table[index].key != key:
            self.probes += 1
            if index == check_index:
                self.collisions += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None and self.table[index] != DELETED:
            if self.table[index].key == key:
                self.probes += 1
                self.table[index] = Entry(key, self.table[index].value + 1)
                # self.table[index].value = self.table[index].value+1
        else:
            self.entries += 1
            self.probes += 1
            self.table[index] = Entry(key, value)
        if self.entries / len(self.table) > self.loadfactor:
            self.entries = 0
            oldtable = self.table
            self.table = [None] * (2 * len(self.table))
            for entry in oldtable:
                if entry is not None:
                    self.put(entry.key, entry.value)

    def get(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.probes += 1
            return None
        self.probes += 1
        return self.table[index].value

    def remove(self, key):
        index = self.hash_func(key) % len(self.table)
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.probes += 1
            self.table[index] = DELETED


    def printMap(self):
        for i in range(len(self.table)):
            print(str(i) + ": " + str(self.table[i]))
