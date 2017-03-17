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

def drawAntenna(order,size):
    #t.speed(0)
    if order == 0:
        return
    else:

        for i in range(2):
                drawAntenna(order - 1, size / 3)
                penupdown(order)
                drawright(size)
                drawleft(size)

                drawAntenna(order - 1, size / 3)
                penupdown(order)
                drawleft(size)
                drawright(size)

                drawAntenna(order - 1,size / 3)
                penupdown(order)
                drawright(size)
                drawright(size)

                drawleft(size)
                drawleft(size)

                drawright(size)
                drawright(size)

def main():
    #size = int(input('Enter the overall size of antenna : '))
    #depth= int(input('Enter the depth of antenna : '))
    t.up()
    t.back(300)
    t.down()
    t.left(45)
    drawAntenna(2,100)
    t.mainloop()

if __name__ == '__main__':
    main()
