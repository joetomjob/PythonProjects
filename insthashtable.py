import re
import hashmap
import math


def fileReadandCompute(filename1, loadfactor):
    x = [hash_func, hash_func_2, hash_func_3]
    for m in range(3):
        h1 = hashmap.Hashmap(x[m], loadfactor)
        with open(filename1, encoding='utf8') as data:
            for t in data:
                t = t.replace('\n', '')
                parts = re.split('\W+', t)
                if '' in parts:
                    parts.remove('')

                for item in parts:
                    h1.put(item.lower())
        r = 0;
        k = ''
        for i in h1.table:
            if i is not None:
                if i.value > r:
                    r = i.value
                    k = i.key
        print("The output for " +str(m+1)+" th hash function is :")
        print("The most ocuring words is : "+ str(k))
        print("The number of times word " + str(k) + " occurs is : " + str(r))
        print("The number of probes is " + str(h1.probes))
        print("The number of collisions is " + str(h1.collisions))
        print()


def testfirstfile(loadfactor, filename):
    fileReadandCompute(filename, loadfactor)


def hash_func(key):
    return hash(key)


def hash_func_2(key):
    h = 0
    mult = 1
    for ch in key:
        h += ord(ch) * mult
        mult *= 131
    return h


def hash_func_3(key):
    h = 0
    k = 1
    for ch in key:
        h += int(math.pow(ord(ch), k))
        k += 1
    return h


def main():
    # filename1 = "Autobiography.txt"
    # filename2 = "Meditations.txt"
    loadfactor = input("Please enter the load factor: ")
    filename = input("Enter filename: ")
    testfirstfile(loadfactor, filename)



if __name__ == '__main__':
    main()
