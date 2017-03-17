import turtle as t
def gcd(a,b):
    if b==0:
        return a,1
    else:
        interim,steps=(gcd(b,a%b))
        return interim,steps+1

def main():
    #x,y = gcd(132,20)
    #print(gcd(9,3))
    #print("Reuslt is : " + str(x))
    #print("No of steps are : " + str(y))
    draw_figure(-1,30,50,26)

def draw_figure(magnitude, weight, scalefactor,mass):
    t.speed(1)
    moving_distance = abs(magnitude) * scalefactor
    t.left(left_or_right(magnitude))
    t.fd(moving_distance)
    t.right(left_or_right(magnitude))
    t.fd(50)
    t.up()
    t.fd(15)
    t.down()
    t.write(mass)
    t.up()
    t.back(50+15)
    t.left(left_or_right(magnitude))
    t.back(moving_distance)
    t.right(left_or_right(magnitude))
    t.down()


def left_or_right(magnitude):
    if int(magnitude) < 0:
        return 90
    else:
        return -90
if __name__=='__main__':
    t.right(90)
    t.back(200)
    main()

    t.mainloop()