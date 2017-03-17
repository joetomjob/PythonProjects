import turtle as t

def drawleft(len):
    t.fd(len)
    t.left(90)

def drawright(len):
    t.fd(len)
    t.right(90)

def penupdown(n):
    if n > 1:
        t.up()
    else:
        t.down()

def drawAntennaP2(order,size):
    t.speed(0)
    print(order)
    if order == 0:
        return
    else:
        drawAntennaP2(order-1, size/3)
        penupdown(order)
        drawright(size)
        drawleft(size)
        drawleft(size)
        drawright(size)

        drawAntennaP2(order-1, size/3)
        penupdown(order)
        drawright(size)
        drawright(size)
        drawleft(size)
        drawleft(size)
        drawright(size)
        drawright(size)

        drawAntennaP2(order - 1, size / 3)
        penupdown(order)
        drawright(size)
        drawleft(size)

        drawAntennaP2(order - 1, size / 3)
        penupdown(order)
        drawleft(size)
        drawright(size)

        drawAntennaP2(order - 1, size / 3)
        penupdown(order)
        drawright(size)
        drawright(size)
        drawleft(size)
        drawleft(size)
        drawright(size)
        drawright(size)

if __name__ == '__main__':
    t.up()
    t.back(200)
    t.down()
    t.left(45)
    drawAntennaP2(3,100)
    t.mainloop()