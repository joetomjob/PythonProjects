__author__='Pallavi chandanshive'

"""
This is my first program in python

"""


import  turtle

"""
 This function draws the plus sign
 :pre :  pos(0,0) ,heading east,up
 :post: pos(0,0) ,heading east,up
 return none
"""

def drawPlusSign(size):
    turtle.speed(0)
    for _ in range(4):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(90)

def recursivePlusSign(Level,size):
    if Level == 1:
        drawPlusSign(size)
    else:
        turtle.speed(0)
        for _ in range(4):
            turtle.forward(size)

            turtle.left(45)
            recursivePlusSign(Level-1, size/3)
            turtle.right(45)

            turtle.backward(size)
            turtle.left(90)




def main():
    turtle.speed(2)
    recursivePlusSign(3,40)
    turtle.mainloop()

if __name__ == '__main__':
    main()