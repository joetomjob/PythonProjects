import turtle as t
import yard
import random
import math
from random import randint


def abc(x, y):
    t.speed(0)
    t.goto(x, y)
    if t.ycor() > 50:
        z = randint(1, 3)
        if z == 3:
            drawPine()
        elif z == 1:
            drawPine()
        else:
            drawPine()
        t.exitonclick()


def drawPine():
    t.speed(0)
    t.down()
    t.left(90)
    drawbark()
    t.left(90)
    t.fd(10)
    t.right(120)
    t.fd(20)
    t.right(120)
    t.fd(20)
    t.right(120)
    t.fd(10)
    t.right(180)
    t.up()


def drawbark():
    t.fd(50)


def lumber():
    t.screensize(800, 800)
    t.setworldcoordinates(0, 0, 800, 800)
    t.write('Harvest and Sort')
    t.up()
    t.fd(680)
    t.down()
    t.write('Harvest Unsorted')
    t.up()
    t.fd(120)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.down()
    t.fd(800)
    t.up()
    t.left(180)
    t.onscreenclick(abc)


def recTree(size, order):
    t.speed(0)
    if order == 0:
        return
    else:
        t.width(size / 12)
        t.fd(size)
        t.left(20)

        recTree(size / 1.25, order - 1)

        t.right(40)

        recTree(size / 1.25, order - 1)

        t.left(20)
        t.back(size)


def drawkoch(size, order):
    t.speed(0)
    if order == 0:
        t.fd(size)
    else:
        drawkoch(size / 2, order - 1)
        t.left(60)
        drawkoch(size / 2, order - 1)
        t.right(120)
        drawkoch(size / 2, order - 1)
        t.left(60)
        drawkoch(size / 2, order - 1)


def hanoi(source, destination, spare, n):
    if n == 0:
        return 0
    else:
        nsteps = hanoi(source, spare, destination, n - 1)
        print('moving disk ' + str(n) + ' from ' + source + ' to ' + destination)
        fsteps = hanoi(spare, destination, source, n - 1)
        steps = nsteps + fsteps + 1
        return steps


def GCD(a, b):
    if b == 0:
        return a, 1
    else:
        interim, steps = GCD(b, a % b)
        return interim, steps + 1


def fibonacci(n):
    if n == 0 or n == 1:
        return 1, 1
    else:
        x, steps1 = fibonacci(n - 1)
        y, steps2 = fibonacci(n - 2)

        return x + y, steps1 + steps2 + 1


def drawSquare(size):
    t.left(45)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.right(90)
    t.right(45)


def penupdown(n):
    if n == 1:
        t.down()
    else:
        t.up()


def drawfractal(size, order):
    t.speed(0)
    if order == 0:
        return
    else:
        for i in range(3):
            drawfractal(size / 3, order - 1)
            penupdown(order)
            drawSquare(size)
            t.up()
            t.fd(math.sqrt(2) * size)
            t.down()

        t.up()
        t.back(math.sqrt(2) * size * 2)
        t.left(90)
        t.fd(math.sqrt(2) * size)
        t.right(90)
        t.down()

        drawfractal(size / 3, order - 1)
        penupdown(order)
        drawSquare(size)

        t.up()
        t.right(90)
        t.fd(math.sqrt(2) * size * 2)
        t.left(90)
        t.down()

        drawfractal(size / 3, order - 1)
        penupdown(order)
        drawSquare(size)

        t.up()
        t.left(90)
        t.fd(math.sqrt(2) * size)
        t.right(90)
        t.back(math.sqrt(2) * size)
        t.down()


def drawfractal2(size, order):
    if order == 0:
        t.speed(0)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.left(90)

    else:

        drawfractal2(size, order - 1)
        drawfractal2(size, order - 1)

        t.right(180)
        drawfractal2(size, order - 1)

        t.right(180)
        drawfractal2(size, order - 1)
        drawfractal2(size, order - 1)

def listtest():
    mylist = [10, 3, 'joe', 45, 'tom']
    print(mylist)
    mylist.pop()
    print(mylist)
    mylist.append('tom')
    print(mylist)
    mylist.insert(2, 'job')
    print(mylist)
    mylist.pop(3)
    print(mylist)
    mylist.reverse()
    print(mylist)
    mylist.pop(0)
    mylist.pop(1)
    print(mylist)
    mylist.sort()
    print(mylist)
    mylist.reverse()
    print(mylist)

    x = mylist * 3
    print(x)
    mylist[0] = 'joe'
    print(mylist * 3)
    x.remove(45)
    print(x)
    print(x.count(45))
    print(x.index(45))

def stringandlisttest():
    print(1)

def main():
    # lumber()
    #t.left(90)
    #t.up()
    #t.back(300)
    #t.down()
    #t.right(90)
    # t.down()
    # recTree(150,7)
    # drawkoch(100, 4)
    # print(hanoi("Source", "destination", "spare", 3))
    # print(GCD(12,20))
    # print(fibonacci(6))
    # drawfractal(100,3)

    #t.left(45)
    #for i in range(4):
    #    drawfractal2(10, 2)

    #listtest()

    stringandlisttest()


if __name__ == "__main__":
    main()
    #t.mainloop()
