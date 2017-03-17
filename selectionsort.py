def selection_sort(l):
    for i in range(len(l)):
        small_index = i
        for j in range(i + 1, len(l)):
            if l[j][1] > l[small_index][1]:
                small_index = j
        l[i], l[small_index] = l[small_index], l[i]
    return l

