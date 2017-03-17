import turtle
import math
import yard
import math
import random
from random import randint

MAPLE_RADIUS = 50
PINE_LENGTH = 60
SQUARETREE_LENGTH = 50
SCREENX = 800
SCREENY = 800
BORDER = 30
LOGWIDTH = 10
fun = yard.LumberYard()

def onclickexit(x,y):
    turtle.bye()

def onclick(x,y):
    gotoresult = turtle.goto(x, y)
    print(x)
    print(y)
    if turtle.ycor()> BORDER :
        z = randint(1,3)
        if z==1:
            if turtle.xcor() > MAPLE_RADIUS and turtle.xcor() < SCREENX-MAPLE_RADIUS:
                Maple()
        elif z==2:
            if turtle.xcor() > PINE_LENGTH/2 and turtle.xcor() < SCREENX-PINE_LENGTH/2:
                Pine()
        elif z==3:
            if turtle.xcor() > SQUARETREE_LENGTH/2 and turtle.xcor() < SCREENX-SQUARETREE_LENGTH/2:
                Squaretree()
    if turtle.ycor() < BORDER and turtle.xcor() < SCREENX/2:
        turtle.clear()
        turtle.goto(SCREENX/2, SCREENY/2)
        turtle.right(90)
        sl = fun.allLogs()
        sl.sort(reverse=True)
        turtle.speed(0)
        for x in sl:
            drawlog(x)
        turtle.exitonclick()

    if turtle.ycor() < BORDER and turtle.xcor() > SCREENX/2:
        turtle.clear()
        turtle.goto(SCREENX/2, SCREENY/2)
        turtle.right(90)
        ul = fun.allLogs()
        turtle.speed(0)
        for y in ul:
            drawlog(y)
        turtle.exitonclick()

def drawlog(logsize):
    turtle.speed(0)
    turtle.speed(0)
    turtle.down()
    turtle.forward(logsize/2)
    turtle.left(90)
    turtle.forward(LOGWIDTH)
    turtle.left(90)
    turtle.forward(logsize)
    turtle.left(90)
    turtle.forward(LOGWIDTH)
    turtle.left(90)
    turtle.forward(logsize)
    turtle.up()
    turtle.back(logsize/2)
    turtle.left(90)
    turtle.forward(LOGWIDTH)
    turtle.right(90)


def drawbark(extra):
    turtle.speed(0)
    sz = randint(50,250)
    if SCREENY-turtle.ycor() > sz+extra:
        fun.addLog(sz)
        turtle.down()
        turtle.forward(sz)
        turtle.up()
        return 1
    else:
        return 0

def Maple():
    k = drawbark(2*MAPLE_RADIUS)
    if k == 1:
        turtle.speed(0)
        turtle.down()
        turtle.right(90)
        turtle.circle(MAPLE_RADIUS)
        turtle.left(90)
        turtle.up()

def Pine():
    k = drawbark(math.sqrt(math.pow(PINE_LENGTH,2)-math.pow(PINE_LENGTH/2,2)))
    if k == 1:
        turtle.speed(0)
        turtle.down()
        turtle.right(90)
        turtle.forward(PINE_LENGTH/2)
        turtle.left(120)
        turtle.forward(PINE_LENGTH)
        turtle.left(120)
        turtle.forward(PINE_LENGTH)
        turtle.left(120)
        turtle.forward(PINE_LENGTH/2)
        turtle.left(90)
        turtle.up()

def Squaretree():
    k = drawbark(SQUARETREE_LENGTH)
    if k == 1:
        turtle.speed(0)
        turtle.down()
        turtle.right(90)
        turtle.forward(SQUARETREE_LENGTH/2)
        turtle.left(90)
        turtle.forward(SQUARETREE_LENGTH )
        turtle.left(90)
        turtle.forward(SQUARETREE_LENGTH )
        turtle.left(90)
        turtle.forward(SQUARETREE_LENGTH )
        turtle.left(90)
        turtle.forward(SQUARETREE_LENGTH/2)
        turtle.left(90)
        turtle.up()

def main():
    #turtle.setup(800,800)
    turtle.screensize(SCREENX, SCREENY)
    turtle.setworldcoordinates(0,0,SCREENX,SCREENY)
    turtle.speed(0)
    turtle.write("Harvest and Sort")
    turtle.up()
    turtle.forward(680)
    turtle.down()
    turtle.write("Harvest Unsorted")

    turtle.up()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(BORDER)
    turtle.left(90)
    turtle.down()
    turtle.forward(800)
    turtle.up()
    turtle.left(90)
    turtle.forward(BORDER)
    turtle.left(180)
    turtle.onscreenclick(onclick)

if __name__ == '__main__':
    main()
    turtle.mainloop()
