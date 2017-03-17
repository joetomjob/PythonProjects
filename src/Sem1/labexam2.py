import turtle as t
import math


def triangle(size):
    for i in range(3):
        t.fd(size)
        t.left(120)


def drawTriangle(size, order):
    t.speed(0)
    if order == 0:
        triangle(size)
    else:

        drawTriangle(size / 2, order - 1)
        t.fd(size/2)
        drawTriangle(size / 2, order - 1)
        t.back(size/2)
        t.left(60)
        t.fd(size/2)
        t.right(60)
        drawTriangle(size / 2, order - 1)
        t.left(60)
        t.back(size/2)
        t.right(60)

def readdata():
    with open('data.txt') as data:
        print(data.readline())
        for d in data:
            print(str(d))

def shift(word,pos):
    i = len(word)
    print(word[(i-pos):]+word[:i-pos])

def ordinal(x,num):
    y = num%26
    r = ord(x)
    for i in range(y):
        if r == 90:
            r = 65
        else:
            r = r+1
    z = chr(r)
    print(z)

def circle(num):
    t.speed(0)
    for i in range(num):
        t.circle((i*50)+50)

        t.left(90)
        t.up()
        t.back(50)
        t.down()
        t.right(90)
    t.up()
    t.left(90)
    t.fd((num*50)+50)
    t.right(90)
    t.fd((num * 50))
    t.down()

def ack(m,n):
    if m==0:
        return n+1
    elif n==0 and m>0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

def rectree(l,n):
    if n==0:
        return 1
    else:
        t.speed(0)
        t.width(l/20)
        t.fd(l)
        t.left(30)
        s1 = rectree(l/2,n-1)
        t.right(60)
        s2 = rectree(l / 2, n - 1)
        t.left(30)
        t.back(l)
        return s1+s2+1

def x(a,b):
    return(max(a,b)+10)

def main():
    #drawTriangle(500, 6)
    #readdata()
    #shift('secret',2)
    #print(ord('A'))
    #print(ord('Z'))
    #print(chr(68))
    #circle(5)
    #ordinal('Z',2)
    #x = input("Enter the string: ")
    #parts = x.strip().split(',')
    #for i in parts:
    #    print(i)
    #l = (parts[0][1:])
    #m = (parts[1][:])
    #shift(l,m)
    #print(ack(1,2))

    #t.left(90)
    #print(rectree(150,6))

    #print(x(10,15))

    #print("Hello",'world')
    #help('')
    #s = "abcdefghi"
    #print(s[len(s)-2:0:-1])

    #r = [1,2,3,4,5,6,7,8,9]
    #print(r[len(r):-1:-1])

    #lists re mutable passed by reference

    s = 'abcde'
    #print(chr(99))
    #print(ord('G'))
    #print(s[::-1])
    #print(len(s))
    #print(s.find('s'))
    print(s[len(s):0:-1])
    print(s[-len(s):-1:-1])
    print(s.upper())
    print(s.lower())
    l = '         jjj,     kk,     ll       '
    print(l)
    print(l.strip())
    print(l.strip().split(','))
    x='joe,tom,job'
    print(x.split(',')[1:])
    lst = ['a','b','c','d','e','f']
    print(lst[-2])
    print(lst.index('f'))
    print('r' in lst)
    print(s[-4::])
    print('d' in s)
    print(lst.append('43'))
    print(lst)




    #var = []
    #lst = [var,var,var]
    #print(lst)
    #var.append('x')
    #print(lst)
    #lst.append('r')
    #print(lst)
if __name__ == '__main__':
    main()
    #t.mainloop()
