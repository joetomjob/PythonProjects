import turtle as t

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

if __name__ == '__main__':
    t.up()
    t.back(200)
    t.down()
    drawkoch(2,500)
    t.mainloop()