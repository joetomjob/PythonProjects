try:
    with open('data.txt') as data:
        print(data.readline())
except FileNotFoundError:
    print('This  is not the file')


