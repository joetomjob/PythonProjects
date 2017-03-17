import turtle as t


def draw1(level,num):
    t.speed(0)
    t.width(level*3)
    if level==0:
        return
    t.forward(num)
    t.left(20)
    draw1(level-1,num/1.25)
    t.right(40)
    draw1(level-1,num/1.25)
    t.left(20)
    t.back(num)


def drawkoch(order,size):
    t.speed(0)
    print(order)

    if order==0:
        t.forward(size)
    else:
        drawkoch(order - 1, size / 3)
        t.left(60)
        drawkoch(order - 1, size / 3)
        t.right(120)
        drawkoch(order - 1, size / 3)
        t.left(60)
        drawkoch(order - 1, size / 3)

def drawTriangle(l,len):
    t.speed(0)
    while l>0:
        t.fd(len)
        t.left(120)
        t.fd(len)
        t.left(120)
        t.fd(len)
        t.left(120+60)
        t.fd(len/2)
        #new triangle
        t.right(60)
        t.fd(len / 2)
        t.right(120)
        t.fd(len / 2)
        t.right(120)
        t.fd(len / 2)
        t.right(60)
        t.back(len/2)
        t.right(60)
        drawTriangle(l-1,len/2)
        t.fd(len)
        drawTriangle(l - 1, len / 2)

if __name__ == '__main__':
    t.up()
    t.left(90)
    t.back(200)
    t.down()
    draw1(4,100)
    #drawkoch(2,500)
    #drawTriangle(3,300)
    t.mainloop()