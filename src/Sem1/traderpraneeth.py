
from collections import namedtuple

def buy1(name,quant,price,vd):
    if name in vd:
        cost = vd[price]
    return cost * int(quant)

def buy2(name1,quant1,price1,ht):

    if name1 in ht:
        cost = ht[price1]
    return cost * int(quant1)

def main():
    '''f = input('Enter the ValleyDale filename(with .txt): ')
    g = input('Enter the Hilltown filename(with .txt): ')
    tup = (line.split() for line in open(f))
    vd = [(name, int(quant), int(price))for name, quant, price in tup]
    print(vd)

    tup2 = (line.split() for line in open(g))
    ht = [(name1, int(quant1), int(price1)) for name1, quant1, price1 in tup2]
    print(ht)'''
    '''data = Donkeys 10 5
    Swords 2 6
    Cookpots 12 3'''

    yourdata = dict()
    f = input('Enter the ValleyDale filename(with .txt): ')
    with open(f) as data:
     lines = data.readline('/n')
     for l in lines:
        fields = l.split(' ')
        price = int(fields.pop(2))
        quantity = int(fields.pop(1))
        item = fields.pop(0).strip()
        value = {'quantity': quantity, 'price': price}
        key = ''.join(f.strip() for f in item)
        if key not in yourdata:
            yourdata[key] = [value]
        else:
            yourdata[key].append(value)

     #print(yourdata)

    yourdata1 = dict()
    g = input('Enter the HillTown filename(with .txt): ')
    with open(g) as data:
     lines = data.readline('/n')
     for l in lines:
        fields = l.split(' ')
        price = int(fields.pop(2))
        quantity = int(fields.pop(1))
        item = fields.pop(0).strip()
        value = {'quantity': quantity, 'price': price}
        key = ''.join(f.strip() for f in item)
        if key not in yourdata:
            yourdata1[key] = [value]
        else:
            yourdata1[key].append(value)

     print(yourdata1)



main()