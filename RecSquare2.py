import math
import turtle as t
SIDELEN = 50

def penupdown(n):
    if n > 1:
        t.up()
    else:
        t.down()

def drawSquare(len):
    t.left(45)
    for i in range(4):
        t.fd(3*len)
        t.left(90)
        t.fd(len)
        t.left(90)
        t.fd(len)
        t.left(90)


def drawSquare2(order,len):
    if order ==0:
        return
    else:
        for i in range(4):
            drawSquare2(order-1, len/3)
            penupdown(order)
            t.fd(len)
            t.left(90)
            t.fd(3*len)
            t.left(90)
            t.fd(len)
            t.left(90)


def main():
    t.up()
    t.back(200)
    t.down()

    t.right(45)
    #drawSquare(SIDELEN)
    drawSquare2(2,SIDELEN)


if __name__ == '__main__':
    main()
    t.mainloop()