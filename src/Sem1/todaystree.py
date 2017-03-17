__author__ = 'zjb'

import turtle as t

def tree1(height):
    '''
    pre: turtle pointing along the tree, at the "bottom"
    post: same
    :return:
    '''
    t.forward(height)
    t.back(height)

def tree2(height):
    t.forward(height)
    t.left(45)
    tree1(height/2)
    t.right(90)
    tree1(height/2)
    t.left(45)
    t.back(height)

def tree3(height):
    t.forward(height)
    t.left(45)
    tree2(height/2)
    t.right(90)
    tree2(height/4)
    t.left(45)
    t.back(height)

def tree4(height):
    t.forward(height)
    t.left(45)
    tree3(height/2)
    t.right(90)
    tree3(height/4)
    t.left(45)
    t.back(height)

def treeN(n,height):
    '''
    pre: turtle with pen down pointing along tree at "bottom"
    post: same
    :param n: depth of tree to draw - must be >= 0
    :param height: height of trunk
    :return: total ink in the tree
    '''
    if n <= 0:
        return 0
    t.width(2)
    t.forward(height)
    t.left(45)
    leftink = treeN(n-1,height/2)
    t.right(90)
    rightink = treeN(n-1,height/4)
    t.left(45)
    t.back(height)
    return height + leftink + rightink

def tests():
    t.speed(0)
    t.up()
    t.left(90)
    t.back(200)
    t.down()
    for depth in range(4):
        treeN(depth,200)
        input('press a key for next test')
        t.clear()
    for height in [0,10,-100,500]:
        treeN(3,height)
        input('press a key for next test')
        t.clear()

t.speed(0)
t.left(90)
print(treeN(3,205))