def merge(left,right):

    a = []
    k=0
    i=0
    j=0
    if(i<len(left) & j<len(right)):
        if left[i]<right[j]:
            a[k]= a[i]
            i += 1
        else:
            a[k]= a[j]
            j += 1
        k += 1
    if i<len(left):
        a[k] = a[i]
        i += 1
        k += 1
    if j<len(right):
        a[k] = a[j]
        j += 1
        k += 1
    return a


def merge_sort(a,l,r):
    if(l<r):
        m = int((l+r)/2)

        merge_sort(a,l,m)
        merge_sort(a,m+1,r)

        a = merge(left,right)
        return a


def main():
    a = [9,8,7,6,5,4,3]
    print(merge_sort(a,0,len(a)))


if __name__ == '__main__':
    main()