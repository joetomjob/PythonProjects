import math
import turtle as t

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

def drawfiveSquare(n,len):
    #t.left(45)
    t.speed(0)
    if n==0:
        return 0;
    else:

        for i in range(3):
            drawfiveSquare(n - 1, len / 3)
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
        drawfiveSquare(n - 1, len / 3)
        penupdown(n)
        t.left(45)
        drawSquare(len)

        t.right(45)
        t.up()
        t.right(90)
        t.fd(2*len*math.sqrt(2))
        t.left(90)
        t.down()
        drawfiveSquare(n - 1, len / 3)
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

def main():
    size = int(input('Enter the overall size of antenna : '))
    depth = int(input('Enter the depth of antenna : '))
    t.up()
    t.back(200)
    t.down()
    drawfiveSquare(depth,size)


if __name__ == '__main__':
    main()
    t.mainloop()