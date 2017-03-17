#Shifts every characcter of the string k times
def NewEcrypt(x,k):
    r = ''
    for i in x:
        r = r+ShiftMul(i,0,k)
    x = r
    return(x)

def NewDecrypt(x, k):
    r = ''
    for i in x:
        r = r + ShiftMul(i, 0, k*-1)
    x = r
    return (x)

def Duplicate(x,b):
    a = int(b)
    l = x[:a]
    m = x[a+1:]
    x = str(x[a])
    r = l+x+x+m

    return r

def DuplicateMul(x,a,b):
    l = x[:a]
    m = x[a+1:]
    x = str(x[a])
    y = x
    for _ in range(b-1):
        x = x+y
    r = l+x+m

    return r

def Rotate(x):
    l = (x[len(x)-1:]+x[:len(x)-1])
    return l

def RotateMul(x,y):
    z = int(abs(y))%len(x)
    m = ""
    if y>=0:
        m = x[len(x) - z:] + x[:len(x) - z]
    else:
        m = x[z:] + x[:z]

    return m

def Shift(x,y):
    z = x[y]
    m = ord(z)
    if m == 90:
        m = 0
    else:
        m = m + 1
    c = chr(m)
    d = x[:y] + c + x[y + 1:]

    return d

def ShiftMul(x,a,b):
    l = x[a]
    m = ord(l)
    r=int(abs(b))%26
    n=0
    if b>=0:
        for _ in range(r):
            if m==90:
                m=65
            else:
                m=m+1
    else:
        for _ in range(r):
            if m==65:
                m=90
            else:
                m=m-1
    c= chr(m)
    d = x[:a]+c+x[a+1:]

    return d

def Swap(x,a,b):
    l = x[:a]
    m = x[a+1:b]
    n = x[b+1:]
    p = l+x[b]+m+x[a]+n

    return p

def SwapMul(x,a,b,c):
    l = int(len(x)/c)
    i = 0
    lst = []
    while(i<len(x)):
        lst.append(x[i:i+l])
        i=i+l
    m = lst[a]
    lst[a] = lst[b]
    lst[b] = m
    n = ""
    for i in lst:
        n = n+i

    return n

def Dupdecrypt(x,b):
    a = int(b)
    return x[:a]+x[a+1:]

def DupdecryptMul(x,a,b):
    return x[:a]+x[a+b-1:]

def main():
    f = input('Enter the message filename(with .txt): ')
    g = input('Enter the transform filename(with .txt): ')
    ende = input('Encryption or decryption to be performed (E/D): ')
    with open(f) as data:
        for x in data:
            x = x.strip()
            with open(g) as operations:
                if ende == 'E':
                    for op in operations:
                        op = op.strip()
                        partsop = op.strip().split(';')
                        for y in partsop:
                            if y[0]=='S':
                                if ',' in y:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = ShiftMul(x,a,b)
                                    #print(x)
                                else:
                                    x = Shift(x,int(y[1]))
                                    #print(x)
                            elif y[0]=='R':
                                if len(y)>1:
                                    a = int(y[1:])
                                    x = RotateMul(x,a)
                                    #print(x)
                                else:
                                    x = Rotate(x)
                                    #print(x)
                            elif y[0]=='D':
                                if ',' in y:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = DuplicateMul(x,a,b)
                                    #print(x)
                                else:
                                    x = Duplicate(x,y[1])
                                    #print(x)
                            elif y[0] == 'T':
                                if '(' in y:
                                    parts = y.strip().split(',')
                                    i=2
                                    c=''
                                    while(y[i]!=')'):
                                        c=c+y[i]
                                        i = i+1
                                    a = int(parts[0][int(i)+1:])
                                    b = int(parts[1])
                                    c = int(c)
                                    x = SwapMul(x, a, b, c)
                                    #print(x)

                                else:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = Swap(x,a,b)
                                    #print(x)
                            elif y[0] == 'J':
                                x = NewEcrypt(x, int(y[1:]))
                elif ende == 'D':
                    lst = operations.readlines()
                    oprev = lst[::-1]
                    for op in (oprev):
                        op = op.strip()
                        partsop = op.strip().split(';')
                        partsoprev = partsop[::-1]
                        for y in partsoprev:
                            if y[0]=='S':
                                if ',' in y:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = ShiftMul(x,a,b*-1)
                                    #print(x)
                                else:
                                    x = ShiftMul(x,int(y[1]),-1)
                                    #print(x)
                            elif y[0]=='R':
                                if len(y)>1:
                                    a = int(y[1:])
                                    x = RotateMul(x,a*-1)
                                    #print(x)
                                else:
                                    x = RotateMul(x,-1)
                                    #print(x)
                            elif y[0]=='D':
                                if ',' in y:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = DupdecryptMul(x, a, b)
                                    #print(x)
                                else:
                                    x = Dupdecrypt(x,y[1])
                                    #print(x)
                            elif y[0] == 'T':
                                if '(' in y:
                                    parts = y.strip().split(',')
                                    i=2
                                    c=''
                                    while(y[i]!=')'):
                                        c=c+y[i]
                                        i = i+1
                                    a = int(parts[0][int(i)+1:])
                                    b = int(parts[1])
                                    c = int(c)
                                    x = SwapMul(x, a, b, c)
                                    #print(x)
                                else:
                                    parts = y.strip().split(',')
                                    a = int(parts[0][1:])
                                    b = int(parts[1])
                                    x = Swap(x,a,b)
                                    #print(x)
                            elif y[0] == 'J':
                                x = NewDecrypt(x, int(y[1:]))
            print (x)

if __name__ =='__main__':
    main()