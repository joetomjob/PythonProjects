import turtle
import math
"""pendown, pen up east"""

def square(side):
    turtle.penup()
    turtle.left(180)
    turtle.forward(math.sqrt(2)*side/2)
    turtle.right(135)
    turtle.pendown()
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.penup()
    turtle.right(45)
    turtle.forward(math.sqrt(2)*side/2)

    """penup east  """
def base(side):
    square(side)
    turtle.left(180)
    turtle.forward(math.sqrt(2)*side)
    turtle.right(180)
    square(side)
    turtle.forward(math.sqrt(2) * side*2)
    square(side)
    turtle.backward(math.sqrt(2) * side)
    turtle.left(90)
    turtle.forward(math.sqrt(2) * side)
    turtle.right(90)
    square(side)
    turtle.right(90)
    turtle.forward(math.sqrt(2) * side*2)
    turtle.left(90)
    square(side)
    turtle.left(90)
    turtle.forward(math.sqrt(2) * side)
    turtle.right(90)


def antenna(level,side):
    if level==1:
        base(side)
    elif level>0:
        turtle.penup()
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        #antenna(level-1,side)
        turtle.backward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.backward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        #antenna(level - 1, side)
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.left(90)
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.right(90)
        #antenna(level - 1, side)
        turtle.right(90)
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.left(90)
        #antenna(level - 1, side)
        turtle.left(90)
        turtle.forward((level-1) * math.pow(3, level-1) * math.sqrt(2) * side)
        turtle.right(90)
        #antenna(level - 1, side)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800





def base(side):
    turtle.pendown()
    turtle.forward(side)
    turtle.backward(side)
    turtle.backward(side)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.backward(side)
    turtle.backward(side)
    turtle.forward(side)
    turtle.right(90)


def func(side, level):
    turtle.speed(0)
    if level == 0:
        base(side)
    elif level > 0:
        turtle.forward(side)

        turtle.left(45)
        func(side / 3, level - 1)
        turtle.right(45)

        turtle.backward(side * 2)

        turtle.left(180)
        turtle.left(45)
        func(side / 3, level - 1)
        turtle.right(45)

        turtle.backward(side)
        turtle.right(90)
        turtle.forward(side)

        turtle.left(45)
        func(side / 3, level - 1)
        turtle.right(45)

        turtle.backward(side * 2)
        turtle.right(180)
        turtle.left(45)
        func(side / 3, level - 1)
        turtle.right(45)
        turtle.backward(side)
        turtle.left(90)

def main():
    #side=20
    #level=3
    #turtle.speed(0)
    #antenna(level,side)
    #turtle.mainloop()

    side = 80
    level = 4


    func(side, level)
    turtle.mainloop()


if __name__ == '__main__':
    main()
