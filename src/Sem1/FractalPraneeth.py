import turtle as t

def drawAntenna(order,len):
    t.speed(0)
    if order==0:
        return
    else:
        for _ in range(4):
            drawAntenna(order-1, len/3)
            t.fd(len)
            t.left(90)
            t.fd(len)
            t.right(90)
            t.fd(len)
            t.right(90)
            t.fd(len)
            t.left(90)
            t.fd(len)
            t.left(90)
def main():
    drawAntenna(3, 100)


if __name__ == '__main__':
    t.left(45)
    main()
    t.mainloop()