import turtle as t
'''t.right(45)'''

def fractal(s,depth):
    t.speed(0)
    if depth == 0:
        t.forward(s)
        t.left(90)
        t.forward(s-2)
        t.right(90)
        t.forward(s-4)
        t.right(90)
        t.forward(s-2)
        t.left(90)
        t.forward(s)
        t.left(90)
    else:
        fractal(s,depth-1)
        fractal(s,depth-1)
        t.right(180)
        fractal(s,depth-1)
        t.right(180)
        fractal(s,depth-1)
        fractal(s,depth-1)


def main(s, depth):
    t.left(45)
    for _ in range(4):
        fractal(s,depth)

level = 1
size = 10

main(size,level-1)
t.mainloop()
