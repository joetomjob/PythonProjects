import turtle as t


def circle(num):
    '''
    pre:turtle facing east at centre
    post:turtle facing east at right end of outer circle
    :param num: the nymber of circles to be drawn
    '''
    for i in range(num):
        t.up()
        t.back(50 + ((i-1) * 50))
        t.left(90)
        t.back(50 + ((i) * 50))
        t.down()
        t.right(90)
        t.circle(50+(i*50))
        t.up()
        t.left(90)
        t.back(50)
        t.forward(50+((i+1)*50))
        t.right(90)
        t.forward(50 + ((i) * 50))

def circlenew(num):
    for i in range(num):
        t.down()
        t.circle(50+(i*50))
        t.up()
        t.left(90)
        t.back(50)
        t.right(90)
    t.left(90)
    t.forward(num*50+50)
    t.right(90)
    t.forward(num * 50)

if __name__ == '__main__':
    circlenew(2)
    t.mainloop()

