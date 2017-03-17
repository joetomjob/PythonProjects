import turtle as t

def drawsnowflake(size,order):
    '''
    pre: turtle facing east at centre of the snowflake
    post : turtle facing east at centre of the snowflake
    :param size: the size of the snowflake
    :param order: the level of the snowflake
    '''
    if order ==1:
        t.speed(0)
        t.fd(size / 2)
        t.back(size)
        t.fd(size / 2)
        t.left(90)
        t.fd(size / 2)
        t.back(size)
        t.fd(size / 2)
        t.right(90)
    else:
        t.fd(size/2)

        t.left(45)
        drawsnowflake(size/3, order-1)
        t.right(45)

        t.back(size)

        t.left(45)
        drawsnowflake(size / 3, order - 1)
        t.right(45)

        t.fd(size / 2)
        t.left(90)
        t.fd(size / 2)

        t.left(45)
        drawsnowflake(size / 3, order - 1)
        t.right(45)

        t.back(size)

        t.left(45)
        drawsnowflake(size / 3, order - 1)
        t.right(45)

        t.fd(size / 2)
        t.right(90)


def main():
    size = int(input("Enter the size of the snowflake: "))
    level = int(input("Enter the level of the snowflake: "))
    drawsnowflake(size,level)

if __name__ == '__main__':
    main()
    t.mainloop()