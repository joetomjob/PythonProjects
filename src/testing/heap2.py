class heap:
    __slots__ = ('stuff', 'sz')

    def __init__(self):
        self.stuff = [None for _ in range(1000)]
        self.sz = 0

    def insert(self, value):
        self.stuff[self.sz] = value
        spot = self.sz
        while spot > 0 and self.stuff[spot] > self.stuff[self.par(spot)]:
            self.stuff[spot], self.stuff[self.par(spot)] = self.stuff[self.par(spot)], self.stuff[spot]
            spot = self.par(spot)
        self.sz += 1

    def par(self, ind):
        return (ind - 1) // 2

    def remove(self):
        removedelt = self.stuff[0]
        self.sz -= 1
        self.stuff[0] = self.stuff[self.sz]

        loc = 0
        swaploc = self.smallest(loc)

        while loc != swaploc:
            self.stuff[loc],self.stuff[swaploc] = self.stuff[swaploc],self.stuff[loc]
            loc = swaploc
            swaploc = self.smallest(loc)
        return removedelt

    def smallest(self, ind):
        lf = 2 * ind + 1
        rt = 2 * ind + 2

        if lf>self.sz:
            return ind

        if rt>self.sz:
            if self.stuff[ind] < self.stuff[lf]:
                return lf
            else:
                return ind
        if self.stuff[lf] < self.stuff[rt]:
            if self.stuff[ind] < self.stuff[rt]:
                return rt
            else:
                return ind
        else:
            if self.stuff[ind] < self.stuff[lf]:
                return lf
            else:
                return ind


def main():
    h = heap()
    h.insert(5)
    h.insert(2)
    h.insert(3)
    h.insert(9)
    h.insert(1)
    h.insert(7)
    h.insert(4)
    print(h.stuff[:h.sz])

    while h.sz >0:
        print(h.remove(),end=' ')

main()
