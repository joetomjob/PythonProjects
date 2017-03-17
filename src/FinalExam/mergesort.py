
def mergesort(list):
    if len(list) ==1:
        return list
    else:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    l_ind = 0
    r_ind = 0

    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] < right[r_ind]:
            result.append(left[l_ind])
            l_ind += 1
        else:
            result.append(right[r_ind])
            r_ind += 1

    if l_ind < len(left):
        result.extend(left[l_ind:])

    if r_ind < len(right):
        result.extend(right[r_ind:])

    return result


def main():
    l = [1, 99, 3, 76, 100, 2, 4, 5, 65]
    print(mergesort(l))


if __name__ == '__main__':
    main()
