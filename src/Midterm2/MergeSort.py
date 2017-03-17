
def mergeSort(list):
    if len(list) == 1:
        return list
    else:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left,right)

def merge(left,right):
    result = []
    left_index = 0
    right_index = 0
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left_index<len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


def main():
    list = [89,3,7,1,9,2,887,54]
    print(mergeSort(list))


if __name__ == '__main__':
    main()
