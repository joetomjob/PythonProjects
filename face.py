import turtle
import math
def main():
    MINLENGTH = 75
    MAXLENGTH = 750
    HAIRLEN = 20
    turtle.speed(0)
    facesize = int(input('What is the size of face?'))
    print(facesize)
    if facesize < MINLENGTH:
        print("We can't draw the circle")
    elif facesize > MAXLENGTH:
        print("We can't draw the circle")
    else:
        drawOutsideCircle(facesize)
        drawHair(facesize,HAIRLEN)
        drawEyes(facesize)
    turtle.mainloop()

def drawOutsideCircle(sz):
    turtle.up()
    turtle.forward(sz)
    turtle.down()
    turtle.left(90)
    turtle.circle(sz)
    turtle.right(90)
    turtle.up()
    turtle.back(sz)

def drawHair(sz,len):
    count = 0
    turtle.left(120)
 #   while(count<35):
 #       turtle.forward(sz)
 #      turtle.down()
 #      turtle.forward(len)
 #       turtle.up()
 #       turtle.back(len+sz)
 #       turtle.right(2)
 #       count = count+1
 #   turtle.right(120-(35*2))
    for hairnumber in range(35):
        turtle.forward(sz)
        turtle.down()
        turtle.forward(len)
        turtle.up()
        turtle.back(len + sz)
        turtle.right(2)
    turtle.right(120 - (35 * 2))

def drawEyes(sz):
    turtle.left(90)
    turtle.forward(sz/2)
    turtle.left(90)
    turtle.forward(sz/2)
    turtle.left(180)
    drawEye(sz)
    turtle.up()
    turtle.forward(sz / 2)
    turtle.right(90)
    turtle.forward(sz / 2)
    turtle.left(90)

    turtle.left(90)
    turtle.forward(sz/2)
    turtle.right(90)
    turtle.forward(sz / 2)
    turtle.back(sz / 8)
    drawEye(sz)
    turtle.up()
    turtle.back(sz / 2-sz/8)
    turtle.right(90)
    turtle.forward(sz / 2)
    turtle.left(90)


def drawEye(sz):
    turtle.down()
    turtle.forward(sz / 8)
    turtle.left(120)
    turtle.forward(sz / 8)
    turtle.left(120)
    turtle.forward(sz / 8)
    turtle.left(120)
main()
