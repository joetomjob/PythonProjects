import turtle as t
def main():
    list = [1,2,3,4,5,6,7,8,9]
    print(list[1:3])
    print(list[5:8])
    x = "abcdefghij"

    print(chr(97))
    print(ord("b"))
    print(x[0:len(x):-1])
    print(x[::-1])
    print(x[len(x):0:-1])

    var = [42]
    print(var)
    funky(var)
    print(var)
    t.circle(30)

def funky(l):
    l.append([49])

def draw(number):
    for i in range(number):
        r = 50 + (i*50)
        t.up()
        t.right(90)
        t.fd(r)
        t.left(90)
        t.down()
        t.circle(r)
        t.left(90)
        t.up()
        t.fd(r)
        t.right(90)


if __name__ == '__main__':
    # main()
    draw(3)
    t.mainloop()