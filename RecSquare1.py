import math
import turtle as t
SIDELEN = 50

def drawSquare(len):
    t.speed(0)
    for i in range(4):
        t.fd(len)
        t.right(90)

def drawfiveSquare(len):
    t.speed(0)
    for i in range(3):
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
    t.left(45)
    drawSquare(len)
    t.right(45)
    t.up()
    t.right(90)
    t.fd(2*len*math.sqrt(2))
    t.left(90)
    t.left(45)
    t.down()
    drawSquare(len)
    t.right(45)

def main():
    t.up()
    t.back(200)
    t.down()
    drawfiveSquare(SIDELEN)


if __name__ == '__main__':
    main()
    t.mainloop()