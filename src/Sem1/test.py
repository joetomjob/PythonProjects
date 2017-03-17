import math

#print(" ".join(['hi','this','is','joe']))

#print([c for c in "".join(['hi','this','is','joe'])])

#print(list(set([x[i] for x in ['joe','tom','job'] for i in range(0,3,2)])))

#for i in range(5):
    #print(i)
x=9
y=3

#if (x>4) & (y<2):
#    print(y)
#elif x<5:
#    print(x)
#else:
#    print(5)

#while(x>1):
#    print (2)
#    x=x-1

#for i in [1,4,6,7]:
#    print(i)



def rotate(x):
    m =""
    m=x[len(x)-1:]+x[:len(x)-1]
    print(m)

def rotateMul(x,y):

    r = int(abs(y))%len(x)
    m =""
    m=x[len(x)-r:]+x[:len(x)-r]
    print(m)

def reverse(x):
    m =""
    for i in range(len(x)-1,-1,-1):
        m += x[i]
    print(m)

def reverse2(a):
    m = ""
    for i in range(len(a)-1,-1,-1):
        m += a[i]
    print(m)

def prime():
    list = []
    list.append(2)
    for i in range(3,1000):
        isPrime = True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                isPrime = False
        if isPrime == True:
            list.append(i)

    # for i in range(len(list)):
    #    print(list[i])

    newlist = []
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if(list[i] != list[j] and list[i]+list[j] == 1000):
                newlist.append([list[i],list[j]])

    for i in range(len(newlist)):
        print(newlist[i])







def main():
    #rotate("joetomjob")
    reverse2("joetomjob")
    #rotateMul("joetomjob",2)
    prime()


if __name__ == '__main__':
    main()



