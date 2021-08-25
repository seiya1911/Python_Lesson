from turtle import *


def tree(n):
    if n <= 1:
        forward(5)
    else:
        forward(5*(1.1**n))
        xx = pos()
        h = heading()
        left(30)
        tree(n - 2)
        up()
        setpos(xx)
        setheading(h)
        down()
        right(15)
        tree(n - 1)
        up()
        setpos(xx)
        setheading(h)
        down()


speed(0)

tree(12)
