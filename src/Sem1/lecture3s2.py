import turtle

def drawFace():
    '''
    Draws a silly face.
    pre: origin, facing right, pendown
    post: origin, facing right, pendown
    :return:
    '''
    drawHead()
#    drawEyes()
#    drawNose()
    drawHair()



def drawHead():
    '''
    Draws a circle of fixed radius.

    pre: origin, right, down
    post: origin, right, down

    :return:
    '''

    radius = 140

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


def drawTriangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.right(360/3)

def drawPolygon(length, sides):
    # the usual pre/post conditions
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)


def drawShape(name, size):
    if name == "Triangle":
        drawPolygon(size, 3)
    elif  name == "Square":
        drawPolygon(size, 4)
    else:
        print("I don't know how to draw a " + name)

def drawSingleHair(hairlength):
    '''
    Draw a single hair.
    pre: origin, pendown, relative zero heading
    post: origin, pendown, relative zero heading
    param: hairlength -- length of hair to draw
    :return:
    '''
    radius = 140
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.forward(hairlength)
    turtle.penup()
    turtle.backward(hairlength + radius)

def hairLengthForAngle(angle):
    radius = 140
#    if (angle )

def drawHair():
    start_angle = 30
    stop_angle = 150
    short_start_angle = 70
    short_stop_angle = 110
    step = 5
    turtle.setheading(start_angle)
    while turtle.heading() < stop_angle:
        if (turtle.heading() > short_start_angle) and (turtle.heading() < short_stop_angle):
            drawSingleHair(10)
        else:
            drawSingleHair(30)
        turtle.left(step)



def main():
    '''
    Draws a silly face.
    pre: none
    post: origin, right, down.
    :return:
    '''
    drawFace()
    turtle.mainloop()

if __name__ == '__main__':
    main()