def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        left, right = a[:len(a) // 2], a[len(a) // 2:]
        return merge(merge_sort(left), merge_sort(right))


def main():
    a = [1, 6, 3, 5, 4]
    print(merge_sort(a))


if __name__ == "__main__":
    main()
