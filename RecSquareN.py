import math
import turtle as t
SIDELEN = 75

def penupdown(n):
    if n > 1:
        t.up()
    else:
        t.down()

def drawSquare(level,len):
    t.speed(0)
    if level == 0:
        return 0
    else:
        for i in range(4):
            drawSquare(level - 1, len / 3)
            penupdown(level)
            t.fd(3*len)
            t.left(90)
            t.fd(len)
            t.left(90)
            t.fd(len)
            t.left(90)

def main():
    t.up()
    t.back(200)
    t.down()
    t.left(45)
    drawSquare(3,SIDELEN)


if __name__ == '__main__':
    main()
    t.mainloop()