import turtle as tr
import numpy as np

tr.left(90)


def zero():
    for _ in range(2):
        tr.forward(50)
        tr.right(90)
        tr.forward(25)
        tr.right(90)
    tr.penup()
    tr.right(90)
    tr.forward(35)
    tr.left(90)
    tr.pendown()


def one():
    tr.penup()
    tr.forward(25)
    tr.right(45)
    tr.pendown()
    tr.forward(np.sqrt(2) * 25)
    tr.right(135)
    tr.forward(50)
    tr.left(90)
    tr.penup()
    tr.forward(10)
    tr.left(90)
    tr.pendown()


def four():
    tr.penup()
    tr.forward(50)
    tr.pendown()
    tr.backward(25)
    tr.right(90)
    tr.forward(25)
    tr.left(90)
    tr.forward(25)
    tr.backward(50)
    tr.right(90)
    tr.penup()
    tr.forward(10)
    tr.left(90)
    tr.pendown()


def seven():
    tr.penup()
    tr.forward(50)
    tr.right(90)
    tr.pendown()
    tr.forward(25)
    tr.right(135)
    tr.forward(np.sqrt(2) * 25)
    tr.left(45)
    tr.forward(25)
    tr.penup()
    tr.left(90)
    tr.forward(35)
    tr.left(90)
    tr.pendown()


def two():
    return None


def three():
    return None


def five():
    return None


def six():
    return None


def eight():
    return None


def nine():
    return None


draw = (zero, one, two, three, four, five, six, seven, eight)

b = '144701'
for i in b:
    draw[int(i)]()
