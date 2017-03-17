def search_sorted(a,item,min,max):

    while min<max:
        m = int(min+max/2)
        if item==a[m]:
            return m
        elif item > a[m]:
            return(search_sorted(a,item,m+1,max))
        else:
            return (search_sorted(a, item, 0, m-1))

def binarysearch(a,item):
    print(search_sorted(a,item,0,len(a)))

def main():
    a = [1,2,3,4,5,6,7,8]
    binarysearch(a,50)

if __name__ == '__main__':
    main()