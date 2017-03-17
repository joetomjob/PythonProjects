class Ourheap:
    def __init__(self):
        self.stuff = [None] * 100
        self.sz = 0

    def insert(self, value):
        self.stuff[self.sz] = value
        spot = self.sz

        while spot > 0 and self.stuff[spot] < self.stuff[self.par(spot)]:
            self.stuff[spot], self.stuff[self.par(spot)] = self.stuff[self.par(spot)], self.stuff[spot]
            spot = self.par(spot)
        self.sz += 1

    def remove(self):
        ref = self.stuff[0]
        self.sz -= 1
        self.stuff[0] = self.stuff[self.sz - 1]
        loc = 0
        swaploc = self.smallest(loc)
        while loc != swaploc:
            self.stuff[loc], self.stuff[swaploc] = self.stuff[swaploc], self.stuff[loc]
            loc = swaploc
            swaploc = self.smallest(loc)
        return ref

    def smallest(self, ind):
        lf = 2 * ind + 1
        rt = 2 + ind + 2

        if lf > self.sz:
            return ind

        if rt > self.sz:
            if self.stuff[ind] < self.stuff[lf]:
                return ind
            else:
                return lf

        if self.stuff[lf] < self.stuff[rt]:
            if self.stuff[lf] < self.stuff[ind]:
                return lf
            else:
                return ind
        else:
            if self.stuff[rt] < self.stuff[ind]:
                return rt
            else:
                return ind


    def par(self, ind):
        return ind // 2;


def main():
    h = Ourheap()
    h.insert(5)
    h.insert(2)
    h.insert(3)
    h.insert(9)
    h.insert(1)
    h.insert(7)
    h.insert(4)
    print(h.stuff[:h.sz])

    print(h.remove())
    print(h.stuff[:h.sz])



if __name__ == '__main__':
    main()
