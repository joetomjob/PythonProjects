def merge(left,right):
    final = []
    li = 0
    ri = 0
    while(li<len(left) and ri<len(right)):
        if left[li]<right[ri]:
            final.append(left[li])
            li += 1
        else:
            final.append(right[ri])
            ri += 1
    if li<len(left):
        final.extend(left[li:])
    if ri<len(right):
        final.extend(right[ri:])

    return final


def mergesort(list):
    if len(list) == 1:
        return list
    else:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return merge(left,right)


def binarysearch(l,i):
    return bins(l,i,0,len(l)-1)


def bins(l,i,le,ri):
    while le <= ri:
        mid = (le+ri)//2
        if i == l[mid]:
            return mid
        if i<l[mid]:
            return bins(l,i,le,mid-1)
        else:
            return bins(l,i,mid+1,ri)

class Ourheap:
    __slots__('stuff','sz')

    def __init__(self):
        self.stuff = [None for _ in range(100)]
        self.sz = 0

    def insert(self,value):
        self.stuff[self.sz] = value
        spot = self.sz
        while spot>0 and self.stuff[self.sz] < self.stuff[self.par(spot)]:
            self.stuff[self.sz],self.stuff[self.par(spot)] = self.stuff[self.par(spot)],self.stuff[self.sz]
            spot = self.par(spot)
        self.sz += 1

    def par(self,ind):
        return (ind-1)//2


l = [56,1,385,5,3,9]
print(mergesort(l))
print(binarysearch(mergesort(l),385))

