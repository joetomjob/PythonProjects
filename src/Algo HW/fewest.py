import random

def compute(ilist,cValue,digitCounter):

    lTotal=0
    gTotal = 0
    eTotal = 0
    lesser = []
    equality = []
    greater = []
    pivot = random.choice(ilist)

    for counter in ilist:
        if counter<pivot:
            lesser.append(counter)
            lTotal+=counter
        elif counter == pivot:
            equality.append(counter)
            eTotal+=counter
        elif counter>pivot:
            greater.append(counter)
            gTotal+=counter

    if gTotal>cValue:
        return compute(greater,cValue,digitCounter)
    elif gTotal<=cValue:
        cValue=cValue-gTotal
        digitCounter+=len(greater)

        temp=0
        counter=0
        while(counter<len(equality)):
            temp+=equality[counter]
            if(temp>cValue):
                digitCounter+=1
                return digitCounter;
            else:
                counter+=1;
                digitCounter+=1;

        cValue = cValue-eTotal;
        return compute(lesser,cValue,digitCounter)

    return digitCounter;







def main():
    n = input().strip()
    cValue = int(input().strip())
    inputList = list(map(int,input().strip().split(" ")))
    print(compute(inputList,cValue,0))



if __name__=='__main__':
    main()