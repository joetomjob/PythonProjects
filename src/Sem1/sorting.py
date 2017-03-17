def isThere(l,a):
    for x in l:
        if x ==a:
            return 1
    return -1

def WhereIs(l,a):
    index = 0
    for x in l:
        if x == a:
            return index
        index += 1
    return -1

def seachSorted(l,a,left,right):
    index = (left+right)//2
    if l[index]==a:
        return index
    elif a>l[index]:
        return(seachSorted(l, a, index+1, right))
    elif a<l[index]:
        return(seachSorted(l, a, left, index-1))

def binarySearch(l,a):
    return (seachSorted(l, a, 0, len(l)))

def selectionSort(l):
    for i in range(len(l)):
        smallindex = i
        for j in range(i+1,len(l)):
            if l[j]<l[smallindex]:
                smallindex=j
        l[i],l[smallindex] = l[smallindex],l[i]
    return l

def selectionSort(l):
    for i in range(len(l)):
        smallindex = i
        for j in range(i+1,len(l)):
            if l[j]<l[smallindex]:
                smallindex=j
        l[i],l[smallindex] = l[smallindex],l[i]
    return l


def main():
    l = [1,2,3,4,5,6,7,8,9,20]
    print(isThere(l,21))
    print(WhereIs(l, 20))
    print(binarySearch(l,20))
    lnew = [11,2,23,4,45,6,7,8,0,9,20]
    print(selectionSort(lnew))


if __name__ == '__main__':
    main()