def SelectionSort(list):
    for i in range(len(list)):
        smallest = i
        for j in range(i+1,len(list)):
            if list[j]<list[smallest]:
                smallest = j
        list[i],list[smallest] =list[smallest],list[i]

    return list



def main():
    list = [5,9,1,3,99,3,76,2]
    print(SelectionSort(list))

if __name__ == '__main__':
    main()
