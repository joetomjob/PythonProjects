"""
@author = Joe Tom Job
Prof : zack butler
Program to write family name
"""
import math
import turtle

def main():

    #Move the cursor to left so that the family name will fit in the screen
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.left(180)
    turtle.down()

    #Start to write family name
    #Calling the function to write letter A
    A()
    #Calling the function to write letter R
    R()
    #Calling the function to write letter U
    U()
    #Calling the function to write letter P
    P()
    #Calling the function to write letter A
    A()
    #Calling the function to write letter R
    R()
    #Calling the function to write letter A
    A()

    turtle.mainloop()

#Function to write letter A
def A():
    turtle.up()
    turtle.forward(40)
    turtle.down()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.up()
    turtle.forward(50)
    turtle.down()

#Function to write letter R
def R():
    turtle.left(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.right(180)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(20)
    turtle.up()
    turtle.right(90)
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(50)
    turtle.down()

#Function to write letter U
def U():
    turtle.up()
    turtle.left(90)
    turtle.forward(10)
    turtle.down()

    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(60)

    turtle.right(180)
    turtle.forward(60)
    turtle.right(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.right(45)
    turtle.forward(20)
    turtle.up()
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(50)
    turtle.down()

#Function to write letter P
def P():
    turtle.left(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.right(45)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(10 * math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.up()
    turtle.forward(50)
    turtle.down()

if __name__ == "__main__":
   main()
