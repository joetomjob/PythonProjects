import math
import turtle as t

def drawleft(len):
    t.fd(len)
    t.left(90)

def drawright(len):
    t.fd(len)
    t.right(90)

def penupdown(n):
    if n > 1:
        t.up()
    else:
        t.down()

def drawSquare(len):
    #t.speed(0)
    for i in range(4):
        t.fd(len)
        t.right(90)

def drawAntennaP1(n,len):
    #t.left(45)
    t.speed(0)
    if n==0:
        return 0;
    else:

        for i in range(3):
            drawAntennaP1(n - 1, len / 3)
            penupdown(n)
            t.left(45)
            drawSquare(len)
            t.right(45)
            t.up()
            t.fd(len*math.sqrt(2))
            t.down()

        t.up()
        t.back(2*len*math.sqrt(2))
        t.left(90)
        t.fd(len*math.sqrt(2))
        t.right(90)
        t.down()
        drawAntennaP1(n - 1, len / 3)
        penupdown(n)
        t.left(45)
        drawSquare(len)

        t.right(45)
        t.up()
        t.right(90)
        t.fd(2*len*math.sqrt(2))
        t.left(90)
        t.down()
        drawAntennaP1(n - 1, len / 3)
        penupdown(n)
        t.left(45)
        drawSquare(len)

        t.right(45)
        t.up()
        t.left(90)
        t.fd(len*math.sqrt(2))
        t.left(90)
        t.fd(len*math.sqrt(2))
        t.right(180)
        t.down()

def drawAntennaP2(s,depth):
    t.speed(0)
    if depth == 0:
        t.forward(s)
        t.left(90)
        t.forward(s-2)
        t.right(90)
        t.forward(s-4)
        t.right(90)
        t.forward(s-2)
        t.left(90)
        t.forward(s)
        t.left(90)
    else:
        drawAntennaP2(s,depth-1)
        drawAntennaP2(s,depth-1)
        t.right(180)
        drawAntennaP2(s,depth-1)
        t.right(180)
        drawAntennaP2(s,depth-1)
        drawAntennaP2(s,depth-1)

def drawAntennaP3(s,depth):
    t.speed(0)
    if depth == 0:
        t.forward(s)
        t.left(90)
        t.forward(s)
        t.right(90)
        t.forward(s)
        t.right(90)
        t.forward(s)
        t.left(90)
        t.forward(s)
        t.left(90)
    else:
        drawAntennaP3(s,depth-1)
        drawAntennaP3(s,depth-1)
        t.right(180)
        drawAntennaP3(s,depth-1)
        t.right(180)
        drawAntennaP3(s,depth-1)
        drawAntennaP3(s,depth-1)


def main():
    size = int(input('Enter the overall size of antenna : '))
    depth = int(input('Enter the depth of antenna : '))
    type = int(input('Do you need to draw it as a sequence of squares(1) or single line(2) : '))
    if type == 1 :
        t.up()
        t.back(200)
        t.down()
        drawAntennaP1(depth, size/5)
    elif type == 2:
        gap = input('Do you need gap(y) or not(n) (Enter y/n): ')
        t.up()
        t.left(90)
        t.back(200)
        t.right(90)
        t.down()
        t.left(45)
        if gap == 'y':
            for _ in range(4):
                drawAntennaP2(size/50,depth-1)
        elif gap == 'n':
            for _ in range(4):
                drawAntennaP3(size/50,depth-1)
        else:
            print("Invalid input")
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()
    t.mainloop()