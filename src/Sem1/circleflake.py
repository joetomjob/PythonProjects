import turtle as t

def drawcircleflake(size,order):
    '''
    pre: turtle facing east at centre of the circleflake
    post : turtle facing east at centre of the circleflake
    :param size: the size of the circleflake
    :param order: the level of the circleflake
    '''
    if order ==1:
        t.speed(0)

        for i in range(4):
            t.fd(size / 2)
            t.right(90)
            t.circle(size/6)
            t.left(90)
            t.back(size/2)
            t.left(90)
        return 4
    else:
        count1 = 0
        for i in range(4):
            t.fd(size/2)
            t.left(45)
            count1 = count1+drawcircleflake(size/3, order-1)
            t.right(45)
            t.back(size/2)
            t.left(90)

        return count1


def main():
    '''
    pre: turtle facing east at centre of the screen
    post: turtle facing east at centre of the screen
    '''
    size = int(input("Enter the size of the circleflake: "))
    level = int(input("Enter the level of the circleflake: "))
    print('The total number of circles are : '+ str(drawcircleflake(size,level)))

if __name__ == '__main__':
    main()
    t.mainloop()