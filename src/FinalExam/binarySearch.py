def binarySearch(list,item,l,r):
    if l<=r:
        index = (l+r)//2
        if list[index] == item:
                return index
        elif list[index] < item:
            return binarySearch(list,item,index+1,r)
        else:
            return binarySearch(list, item, l, index-1)

def searchsorted(list,item):
    return binarySearch(list,item,0,len(list)-1)


def main():
    list = [1,2,3,4,5,6,7,8,9]
    print(searchsorted(list,1))

if __name__ == '__main__':
    main()