import turtle


def drawFace():
    '''
    Draw a silly face.

    pre: turtle at origin, pendown, facing right
    post: turtle at origin, pendown, facing right

    :return:
    '''
    drawHead()
    pass

def drawHead():
    '''

    Draws a head, centered at origin

    pre: at origin, pen down, facing right
    post: at origin, pen down, facing right

    :return:
    '''
    radius = 75
    turtle.right(90)
    turtle.penup()

    turtle.forward(radius)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(radius)
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.right(90)
    turtle.pendown()

def main():
    '''
    Draws a silly face.

    pre: none
    post: turtle at origin, facing right, pendown

    :return:
    '''

    drawFace()


def drawPolygon(size, sides):
    # the usual pre/post conditions.
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)

def drawTriangle(size):
    # the usual pre/post conditiions
    drawPolygon(size, 3)

def drawSquare(size):
    # the usual pre/post conditions
    drawPolygon(size, 4)


def drawShape(shape, size):
    '''

    Draw a triangle or a square.


    pre: origin, right, down
    post: origin, right, down
    :param size:  the length of each side of the shape
    :param shape:  the name of the shape to draw
    :return:
    '''

    if shape == "Triangle":
        drawTriangle(size)
    elif shape == "Square":
        drawSquare(size)
    else:
        print("I don't know how to draw a" + shape)




if __name__ == '__main__':
    main()
    turtle.mainloop()