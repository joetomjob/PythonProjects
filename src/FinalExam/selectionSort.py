def selectionsort(_list):
    for x in range(len(_list)):
        small = x
        for y in range(x+1,len(_list)):
            if _list[small]>_list[y]:
                small = y
        _list[x],_list[small] = _list[small],_list[x]
    return _list


def main():
    _list = [599,7,1,300,9,10,599,31,89,5]
    print(selectionsort(_list))

if __name__ == '__main__':
    main()